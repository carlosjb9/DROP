# Cómo generar los 12 fotogramas

## Una sola vez

Comprueba que tienes Python. Abre una ventana de comandos (tecla Windows → escribe `cmd`) y escribe:

```
python --version
```

Si te contesta con un número de versión, estás listo. Si dice que no lo encuentra, instálalo desde python.org marcando la casilla **"Add Python to PATH"** — o dímelo y te preparo la misma herramienta en PowerShell, que ya viene con Windows.

## Cada vez que quieras generar

Doble clic en **`ejecutar.bat`**. Eso es todo.

O, desde la ventana de comandos, dentro de esta carpeta:

```
python generar.py            genera lo que falte
python generar.py --force    vuelve a generar todo, pisando lo que haya
python generar.py G2         solo los fotogramas del guion 2
python generar.py --modelo nano      lo mismo pero con Nano Banana Pro
python generar.py --modelo chatgpt4k ChatGPT 2 a 4K
```

El script sube las referencias a APIMart, lanza las 12 tareas con **ChatGPT 2** (`gpt-image-2`) en 9:16 a 2K, espera a cada una y deja el PNG en la carpeta de su guion. Si una falla, sigue con las demás y te dice al final cuáles han fallado: vuelves a lanzarlo y solo reintenta esas, porque las que ya están hechas se las salta.

## Qué hay en cada archivo

| | |
|---|---|
| `prompts.json` | Los 12 prompts. Si quieres retocar una escena, la editas aquí y lanzas `--force`. |
| `generar.py` | El motor. No hace falta tocarlo. |
| `clave.txt` | Tu API key de APIMart. |
| `referencias\` | Las 4 fotos del producto, una por color. |
| `.refs-subidas.json` | Caché de las referencias ya subidas. Se regenera solo cada 60 horas. |

## Si una imagen falla por moderación

ChatGPT 2 pasa el prompt por un filtro de contenido **antes** de generar. Dos de las escenas hablan de pies descalzos (`G1-02-mecanismo` y `G1-03-prueba`) y es posible que alguna se rechace. Si pasa, el script te lo dirá por su nombre. Dos salidas: lanzas solo esas con `python generar.py --modelo nano G1`, o me lo dices y reescribo el prompt evitando la palabra que lo dispara.

## Dos avisos

**Tu API key ha pasado por el chat.** Cuando termines la tanda, entra en apimart.ai/keys y genera una nueva; pegas la nueva en `clave.txt` y listo. Cuesta treinta segundos y te ahorra un disgusto.

**Esta carpeta está dentro de OneDrive**, así que `clave.txt` se sincroniza a la nube. Si prefieres que no, borra el archivo y define la variable de entorno `APIMART_KEY` en su lugar: el script la busca ahí primero.
