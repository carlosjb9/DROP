# -*- coding: utf-8 -*-
"""
Generador de fotogramas para los creativos de Navarros.
Lee prompts.json, sube las referencias a APIMart, lanza las tareas de
Nano Banana Pro, espera el resultado y guarda cada PNG en su carpeta.

USO:   python generar.py            -> genera lo que falte
       python generar.py --force    -> vuelve a generar todo
       python generar.py G2         -> solo los prompts cuyo id empiece por G2
       python generar.py --modelo nano   -> cambia a Nano Banana Pro en vez de ChatGPT 2

Solo usa la libreria estandar de Python. No hay que instalar nada.
"""
import json, os, sys, time, uuid, mimetypes
import urllib.request, urllib.error

BASE = "https://api.apimart.ai"
# Modelo por defecto. Se puede cambiar al vuelo:  python generar.py --modelo nano
MODELOS = {
    "chatgpt": ("gpt-image-2", "2k"),                    # ChatGPT 2  (por defecto)
    "chatgpt4k": ("gpt-image-2", "4k"),
    "nano": ("gemini-3-pro-image-preview", "2K"),        # Nano Banana Pro
}
MODEL, RESOLUTION = MODELOS["chatgpt"]
SIZE = "9:16"

AQUI = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(AQUI, "referencias")
CACHE = os.path.join(AQUI, ".refs-subidas.json")

def clave():
    k = os.environ.get("APIMART_KEY")
    if k: return k.strip()
    p = os.path.join(AQUI, "clave.txt")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip()
    sys.exit("No encuentro la API key. Ponla en clave.txt o en la variable APIMART_KEY.")

KEY = clave()
H = {"Authorization": "Bearer " + KEY}

def pedir(url, data=None, headers=None, metodo=None, intentos=3):
    hh = dict(H); hh.update(headers or {})
    for i in range(intentos):
        try:
            req = urllib.request.Request(url, data=data, headers=hh, method=metodo)
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            cuerpo = e.read().decode("utf-8", "replace")[:400]
            if e.code in (429, 500, 502, 503) and i < intentos - 1:
                time.sleep(5 * (i + 1)); continue
            raise SystemExit("HTTP %s en %s\n%s" % (e.code, url, cuerpo))
        except Exception as e:
            if i < intentos - 1:
                time.sleep(5 * (i + 1)); continue
            raise SystemExit("Fallo de red en %s: %s" % (url, e))

def subir(ruta):
    """POST multipart /v1/uploads/images -> devuelve la URL publica (72 h)."""
    lim = "----navarros" + uuid.uuid4().hex
    tipo = mimetypes.guess_type(ruta)[0] or "image/png"
    cuerpo = b"".join([
        ("--%s\r\n" % lim).encode(),
        ('Content-Disposition: form-data; name="file"; filename="%s"\r\n'
         % os.path.basename(ruta)).encode(),
        ("Content-Type: %s\r\n\r\n" % tipo).encode(),
        open(ruta, "rb").read(),
        ("\r\n--%s--\r\n" % lim).encode(),
    ])
    r = pedir(BASE + "/v1/uploads/images", cuerpo,
              {"Content-Type": "multipart/form-data; boundary=" + lim})
    u = r.get("url") or (r.get("data") or {}).get("url")
    if not u: raise SystemExit("Subida sin URL: %s" % r)
    return u

def refs_subidas(nombres):
    cache = {}
    if os.path.exists(CACHE):
        try: cache = json.load(open(CACHE, encoding="utf-8"))
        except Exception: cache = {}
    ahora = time.time()
    for n in nombres:
        e = cache.get(n)
        if e and ahora - e.get("t", 0) < 60 * 60 * 60:   # 60 h de margen sobre las 72
            continue
        ruta = os.path.join(REFS, n) if os.sep not in n and "/" not in n else os.path.join(AQUI, n)
        if not os.path.exists(ruta):
            raise SystemExit("Falta la referencia: %s" % ruta)
        print("  subiendo referencia %s ..." % n)
        cache[n] = {"url": subir(ruta), "t": ahora}
    json.dump(cache, open(CACHE, "w", encoding="utf-8"))
    return {n: cache[n]["url"] for n in nombres}

def refs_de(t):
    """Devuelve la lista de referencias de un trabajo (acepta 'ref' o 'refs')."""
    r = t.get("refs") or ([t["ref"]] if t.get("ref") else [])
    return [x for x in r if x]

def lanzar(prompt, ref_urls):
    cuerpo = {"model": MODEL, "prompt": prompt, "size": SIZE,
              "n": 1, "resolution": RESOLUTION}
    if ref_urls:
        cuerpo["image_urls"] = list(ref_urls)
    r = pedir(BASE + "/v1/images/generations",
              json.dumps(cuerpo).encode("utf-8"),
              {"Content-Type": "application/json"})
    d = r.get("data")
    if isinstance(d, list) and d:
        return d[0].get("task_id") or d[0].get("id")
    if isinstance(d, dict):
        return d.get("task_id") or d.get("id")
    return r.get("task_id") or r.get("id")

def esperar(task_id, limite=600):
    t0 = time.time()
    while time.time() - t0 < limite:
        r = pedir(BASE + "/v1/tasks/%s?language=es" % task_id)
        d = r.get("data", r)
        est = d.get("status")
        if est == "completed":
            ims = (d.get("result") or {}).get("images") or []
            if ims:
                u = ims[0].get("url")
                return u[0] if isinstance(u, list) else u
            return d.get("url")
        if est in ("failed", "cancelled"):
            raise SystemExit("Tarea %s: %s" % (est, (d.get("error") or {}).get("message", "")))
        time.sleep(6)
    raise SystemExit("Tiempo agotado esperando la tarea %s" % task_id)

def bajar(url, destino):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=180) as r, open(destino, "wb") as f:
        f.write(r.read())

def main():
    args = [a for a in sys.argv[1:]]
    forzar = "--force" in args

    global MODEL, RESOLUTION
    if "--modelo" in args:
        clave_m = args[args.index("--modelo") + 1].lower()
        if clave_m not in MODELOS:
            sys.exit("Modelos disponibles: " + ", ".join(MODELOS))
        MODEL, RESOLUTION = MODELOS[clave_m]
        args = [a for a in args if a != clave_m]

    filtro = next((a for a in args if not a.startswith("--")), None)
    print("Modelo: %s  ·  resolucion: %s  ·  formato: %s\n" % (MODEL, RESOLUTION, SIZE))

    trabajos = json.load(open(os.path.join(AQUI, "prompts.json"), encoding="utf-8"))
    if filtro:
        trabajos = [t for t in trabajos if t["id"].upper().startswith(filtro.upper())]
    if not trabajos:
        sys.exit("Ningun prompt coincide con ese filtro.")

    necesarias = sorted({r for t in trabajos for r in refs_de(t)})
    urls = refs_subidas(necesarias) if necesarias else {}

    hechos, fallos = 0, []
    for i, t in enumerate(trabajos, 1):
        carpeta = os.path.join(AQUI, t["carpeta"])
        os.makedirs(carpeta, exist_ok=True)
        destino = os.path.join(carpeta, t["id"] + ".png")
        if os.path.exists(destino) and not forzar:
            print("[%02d/%02d] %s  ya existe, lo salto" % (i, len(trabajos), t["id"]))
            continue
        print("[%02d/%02d] %s  generando ..." % (i, len(trabajos), t["id"]))
        try:
            tid = lanzar(t["prompt"], [urls[r] for r in refs_de(t)])
            if not tid: raise SystemExit("no me han devuelto task_id")
            url = esperar(tid)
            bajar(url, destino)
            print("           guardado en %s" % os.path.relpath(destino, AQUI))
            hechos += 1
        except SystemExit as e:
            print("           ERROR: %s" % e)
            fallos.append(t["id"])

    print("\nListo. %d imagenes nuevas." % hechos)
    if fallos:
        print("Han fallado: %s  (vuelve a lanzar el script y solo reintentara esas)" % ", ".join(fallos))

if __name__ == "__main__":
    main()
