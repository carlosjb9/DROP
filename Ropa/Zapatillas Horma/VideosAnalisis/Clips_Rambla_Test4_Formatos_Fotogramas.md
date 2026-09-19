# Rambla · test 4 «formatos» · versión por FOTOGRAMAS v2 (cara y zapatilla completas desde el frame inicial)

**Cómo funciona ahora:** cada clip arranca de un fotograma. Para cada clip te doy o bien el prompt de imagen del fotograma inicial (lo generas con Image 1 = hoja de personaje, Image 2 = foto del proveedor, Image 3 = placa de localización) o bien la indicación de reutilizar el último frame del clip anterior. Luego pegas el prompt de vídeo con ese fotograma como imagen de inicio. Cuando se reutiliza un frame, el vídeo empieza exactamente donde acabó el otro, así que el «Initial state» del prompt de vídeo describe ese frame y la acción empieza desde ahí.

**Cuándo hay fotograma nuevo:** primer clip de cada vídeo, cambio de plano (medio ↔ cerca ↔ cenital), aparición de los pies, cambio de qué hay en las manos o en el mostrador. Cuándo se reutiliza: mismo plano, mismo sitio, el personaje solo habla, gesticula o baja/sube la zapatilla.

**Modelo del vídeo de zapatería (F1):** Rambla Marrón (malla de pana marrón oscuro, ante marrón, raya y cordones crema, suela caramelo). Image 2 en F1 = la foto del proveedor del modelo marrón. En el resto de vídeos de Andrés se mantiene la gris; si prefieres que Andrés lleve siempre la marrón, cambio F4, F5, F6 y F7 en un minuto.

**Regla de cara:** en los planos medios la cara está entera en el fotograma inicial y se queda entera todo el clip; en los planos cerrados y cenitales no hay cara en el fotograma inicial y no entra ninguna cara en todo el clip. Nunca se pasa de una cosa a la otra dentro de un clip, para que no se invente la cara.

**Regla de zapatilla:** en todos los fotogramas iniciales hay al menos una Rambla completa a la vista, en tres cuartos (puntera ancha, lateral con la raya, cordones, cuello y toda la suela caramelo con su borde de tacos), sin recortar y sin que la mano la tape; se sujeta por el talón o por el cuello. Se han quitado los planos de «solo puntera» o «solo suela»: cuando se enseña la suela, la zapatilla se inclina de forma que el lateral siga a la vista. Así la IA no se inventa el diseño.

**Cierre fijo (sin precio):** «Tiene tallas de la 36 a la 49, el envío es gratis, y si no te van, las devuelves sin problemas.»

**Regla de simplicidad:** avatar quieto en su sitio, cámara fija, solo manos, cara y zapatilla. Con fotograma inicial además se gana consistencia: si un clip sale mal, se regenera solo ese.


---

## F1 · ZAPATERÍA · «Los de más de cincuenta no paran de hablar de estas» (Andrés, Rambla Marrón) · tienda · 5 clips · 36 s · réplica exacta del vídeo del tendero (Olyndra)

### Vídeo original, beat a beat

Tendero en su tienda con el par en la mano desde el segundo 0: «Los de más de 60 no paran de hablar de estas. Atiendo a 40 o 50 hombres a la semana y es la misma conversación: mi colega me ha dicho que me las coja, mi cuñado no para. Aquí va el porqué: puntera ancha, sitio de verdad para pies de verdad; soporte de arco que hace algo; te las llevas puestas desde el primer día, sin domar, sin ampollas, nada. Nueve colores, eran 40, ahora 24, envío gratis. Dile a tu colega que llegaste antes. Link abajo.»

### 1. Story Building

Réplica beat a beat con Andrés detrás del mostrador de su zapatería, el par gris en alto desde el primer fotograma: quién habla de ellas → la conversación que se repite → «aquí va el porqué» con tres cosas → colores → tallas, envío gratis, devolución → «dile a tu colega que llegaste antes» → link.

### 2. Character Building

Andrés, 54, vendedor de zapatería de toda la vida, cinta métrica al cuello. Habla como quien lo ve todos los días, sin vender: seco, seguro, media sonrisa. Rambla Marrón en este vídeo.
Localización fija de este vídeo (Zapatería): Zapatería pequeña: mostrador de madera en primer término, estanterías de roble claro con zapatos desenfocados detrás, cajas de zapatos apiladas al fondo, luz cálida de tienda, sin rótulos ni marcas.

### 3. Story Refining

Sin precio (no se dice). Sin cifras de clientes: «es la misma conversación cada semana» en lugar de «40 o 50 hombres»; si Carlos tiene un dato real de Navarros lo mete en esa frase. El soporte de arco no existe en la Rambla: se sustituye por suela plana y flexible.

Plan de fotogramas: F1.1 FOTOGRAMA NUEVO · F1.2 último frame de F1.1 · F1.3 FOTOGRAMA NUEVO · F1.4 último frame de F1.2 · F1.5 último frame de F1.4.

Clips: F1.1 Los de más de cincuenta no paran (7 s) · F1.2 Mi colega me ha dicho, mi cuñado no para (8 s) · F1.3 Aquí va el porqué (9 s) · F1.4 Colores y tallas (6 s) · F1.5 Dile a tu colega que llegaste antes (6 s). Total 36 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Andrés. Image 2 = foto del proveedor de Rambla Marrón. Image 3 = placa «Zapatería».


#### Clip F1.1 · Los de más de cincuenta no paran · 7 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Andrés standing behind the wooden counter holding the brown Rambla pair up with both hands at chest height, one shoe in each hand, in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible, shelves of shoes out of focus behind him.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: the Rambla pair. Nothing else on the counter or table.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Los de más de cincuenta no paran]
Initial state: From the first frame: Andrés standing behind the wooden counter holding the brown Rambla pair up with both hands at chest height, one shoe in each hand, in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible, shelves of shoes out of focus behind him.
Primary event: He keeps the pair up, a knowing half-smile, one raised eyebrow, a small shake of the head as if amused.
End state: Andrés standing, pair held up.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés, dry, knowing: "Los de más de cincuenta no paran de hablar de estas. En la tienda es la misma conversación cada semana."}
<a shop door bell far away, a cardboard box set down>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F1.2 · Mi colega me ha dicho, mi cuñado no para · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F1.1** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Mi colega me ha dicho, mi cuñado no para]
Initial state: Starts exactly on the provided frame: Andrés standing behind the wooden counter holding the brown Rambla pair up at chest height, one shoe in each hand, in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible, shelves of shoes out of focus behind him.
Primary event: He lowers the pair onto the counter in front of him, in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge stay visible, one hand on each shoe. Then he lifts one hand as if quoting one customer, then the other hand as if quoting another, then shrugs.
End state: Andrés standing, hands back on the shoes.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "«Mi colega me ha dicho que me las coja.» «Mi cuñado no para con ellas.» Todos los días igual."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F1.3 · Aquí va el porqué · 9 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Close on Andrés's hands over the counter: one brown Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the tape measure end visible at the edge of frame.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: the Rambla pair. Nothing else on the counter or table.
Framing: Close shot at arm's length on the hands and the shoe, face out of frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 3 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | Aquí va el porqué]
Initial state: Close on Andrés's hands over the counter: one brown Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the tape measure end visible at the edge of frame.
Primary event: His finger draws the round outline of the toe box, then he turns the shoe to side profile, held by the heel so the whole shoe and the flat caramel sole line stay visible and runs the finger along the flat caramel sole, then taps the flat heel.
End state: The shoe in profile, finger on the heel.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at counter height, close on Andrés's hands and the shoes held over the wooden counter, shelves out of focus behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Aquí va el porqué. Puntera ancha: sitio de verdad para pies de verdad. Suela plana y flexible, que el pie apoya entero. Y te las llevas puestas desde el primer día: sin domar, sin ampollas, nada."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F1.4 · Colores y tallas · 6 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F1.2** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism. Part 4 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–6s | Colores y tallas]
Initial state: Starts exactly on the provided frame: Andrés behind the counter, the brown Rambla pair resting on the counter in front of him, in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge stay visible, one hand on each shoe.
Primary event: He opens one hand showing five fingers on «colores», then holds both hands wide apart on the sizes.
End state: Andrés standing, hands apart.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Varios colores. Tiene tallas de la treinta y seis a la cuarenta y nueve, el envío es gratis, y si no te van, las devuelves sin problemas."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F1.5 · Dile a tu colega que llegaste antes · 6 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F1.4** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism. Part 5 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: dark brown ribbed corduroy-look mesh, dark brown suede-look toe cap and side panels, one cream curved stripe on the lateral side, cream flat laces, cream padded collar and tongue lining, a small dark brown heel pull tab, caramel-amber gum lug sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–6s | Dile a tu colega que llegaste antes]
Initial state: Starts exactly on the provided frame: Andrés behind the counter, hands held wide apart, the brown Rambla pair on the counter in front of him.
Primary event: He rests one hand on the pair, a closed-lip smile, a slow nod, and points down at the bottom of the frame with the other hand.
End state: Andrés pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Dile a tu colega que llegaste tú antes. Link abajo."}
<a shop door bell far away, a cardboard box set down>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## F2 · TÍO PIE ANCHO · «¿Por qué los tíos con pies anchos están comprando estas?» (Javi) · portal · 7 clips · 56 s · réplica del vídeo de Breeze

### Vídeo original, beat a beat

«¿Por qué los hombres con pies anchos están comprando estos zapatos? Hola, soy Alejandro, fundador. Me encanta viajar pero encontrar zapatos cómodos siempre me ha resultado imposible, sobre todo con pies anchos. Así que creamos algo mejor.» → lanzamos en 2020, plantilla ortopédica, caminar horas sin dolor → puntera ancha, «como si anduvieras descalzo, sensación mágica» → transpirable, «el sudor es físicamente imposible» → versátiles: turismo de día y cena de noche, solo zapato que necesitas, espacio en la maleta → colores → «20.000 opiniones, 30 días de prueba, es hora de mejorar».

### 1. Story Building

Misma estructura y mismo orden: pregunta-gancho → «hola, soy Javi» + el problema (pie ancho, nada le valía) → «así que me pasé a estas» → puntera ancha «como ir descalzo» → malla, no sudas → versátiles (curro, calle, gym; unas para todo) → colores → devolución sin problemas → «es hora de cambiar». Javi en el portal con el par en la mano.

### 2. Character Building

Javi como el «fundador» del vídeo pero en versión usuario: presenta, cuenta su problema, enseña. Tono cercano, ilusionado sin gritar. Rambla Negro/Blanco.

Localización fija de este vídeo (Portal): Portal de un edificio español: tres escalones de piedra gris, puerta verde oscuro con el número 14, pared crema, acera de granito, bicicleta negra a la derecha, sombra abierta de mañana con luz desde la izquierda.

### 3. Story Refining

No se dice que es el fundador ni «20.000 opiniones» ni «plantilla ortopédica»: Javi se presenta por su nombre y cuenta su caso. Todo el B-roll de andar por la ciudad se sustituye por la zapatilla en la mano y planos cenitales de los pies quietos.

Plan de fotogramas: F2.1 FOTOGRAMA NUEVO · F2.2 FOTOGRAMA NUEVO · F2.3 FOTOGRAMA NUEVO · F2.4 último frame de F2.3 · F2.5 FOTOGRAMA NUEVO · F2.6 último frame de F2.5 · F2.7 último frame de F2.6.

Clips: F2.1 La pregunta (7 s) · F2.2 Hola, soy Javi (9 s) · F2.3 Puntera ancha: como ir descalzo (9 s) · F2.4 Malla: no sudas (8 s) · F2.5 Unas para todo (8 s) · F2.6 Colores (7 s) · F2.7 Es hora de cambiar (8 s). Total 56 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa «Portal».


#### Clip F2.1 · La pregunta · 7 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, black ribbed mesh, black suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Overhead: Javi's bare feet flat and completely still on the lower stone step, toes squeezed toward a point, a sock line, one black Rambla lying on its side beside them, medial side up, so the whole outline, the wide toe box and the full caramel sole edge read from above.
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks.
Props: the Rambla pair. Nothing else on the counter or table.
Framing: Straight-down overhead shot, no face in frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | La pregunta]
Initial state: Overhead from the first frame: Javi's bare feet flat and completely still on the lower stone step, toes squeezed toward a point, a sock line, one black Rambla lying on its side beside them, medial side up, so the whole outline, the wide toe box and the full caramel sole edge read from above.
Primary event: The feet do not move. His hand enters and points at the squeezed toes, then at the wide toe box of the Rambla.
End state: Feet in the same place, finger on the Rambla.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot directly overhead, looking straight down at the stone step; natural micro-sway only, no travel, no tilt. No face in frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi, voice-over: "¿Por qué los tíos con pies anchos se están comprando estas zapatillas?"}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F2.2 · Hola, soy Javi · 9 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, black ribbed mesh, black suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Javi seated on the top stone step holding one black Rambla in his right hand at chest height, in three-quarter view, lateral side with the stripe toward the lens and the full caramel sole edge visible, the green door behind him.
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks.
Props: the Rambla pair. Nothing else on the counter or table.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | Hola, soy Javi]
Initial state: From the first frame: Javi seated on the top stone step holding one black Rambla in his right hand at chest height, in three-quarter view, lateral side with the stripe toward the lens and the full caramel sole edge visible, the green door behind him.
Primary event: He raises his free hand in a small wave, then points at the shoe, then at his own feet below the frame.
End state: Javi seated, shoe held up.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Hola, soy Javi. Tengo el pie ancho, y encontrar una zapatilla cómoda siempre me ha parecido imposible. Todas apretaban. Así que me pasé a estas."}
<a moped far away, a bicycle chain ticking>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F2.3 · Puntera ancha: como ir descalzo · 9 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, black ribbed mesh, black suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Close on Javi's hands: the black Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the green door behind.
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks.
Props: the Rambla pair. Nothing else on the counter or table.
Framing: Close shot at arm's length on the hands and the shoe, face out of frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 3 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | Puntera ancha: como ir descalzo]
Initial state: Close on Javi's hands: the black Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the green door behind.
Primary event: His finger draws the round outline of the toe box, then he spreads the fingers of his free hand wide beside the shoe.
End state: The shoe in three-quarter view, toe box toward the lens, lateral side and full caramel sole edge visible, fingers spread beside it.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on the hands and the shoes held, the green door behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Puntera ancha: los dedos se mueven como cuando vas descalzo. Puedes estar horas de pie sin que te apriete nada. Es una sensación que hay que probar."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F2.4 · Malla: no sudas · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F2.3** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 4 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Malla: no sudas]
Initial state: Starts exactly on the provided frame: close on Javi's hands, the black Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the fingers of his free hand spread beside it, the green door behind.
Primary event: He turns the shoe slowly so the ribbed mesh upper faces the lens while the lateral side and the caramel sole edge stay visible, pinches the mesh between two fingers, then slides his thumb across it.
End state: The shoe turned so the ribbed mesh reads, the lateral side and the caramel sole edge still visible, thumb resting on the mesh.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on the hands and the shoes held, the green door behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<mesh pinched>
{Javi: "Todo esto es malla. Respira, el pie va fresco y seco, y en verano no se te cuece."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F2.5 · Unas para todo · 8 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, black ribbed mesh, black suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Medium framing: Javi seated on the step wearing the black Rambla pair, feet flat and still on the lower step in the lower frame, hands on his knees.
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks.
Props: the Rambla pair. Nothing else on the counter or table.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 5 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Unas para todo]
Initial state: Medium framing: Javi seated on the step wearing the black Rambla pair, feet flat and still on the lower step in the lower frame, hands on his knees.
Primary event: He points down at his feet, then counts three on his fingers, then opens both hands.
End state: Javi seated, hands open.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Y valen para todo: al curro, a la calle, al gym. Con vaqueros y con el pantalón del trabajo. Unas y ya está."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F2.6 · Colores · 7 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F2.5** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 6 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Colores]
Initial state: Starts exactly on the provided frame: Javi seated on the top step wearing the black Rambla pair, feet flat and still on the lower step, both hands open in front of him.
Primary event: He holds up fingers one by one as he names colours, with a closed-lip smile, feet never moving.
End state: Javi seated, fingers up.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Las hay en negro, blanco, gris, marrón, rojo. Con cualquier cosa que te pongas."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F2.7 · Es hora de cambiar · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F2.6** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 7 of 7 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Es hora de cambiar]
Initial state: Starts exactly on the provided frame: Javi seated on the step, Rambla on, feet flat and still, fingers held up.
Primary event: He lowers the hand, nods once, then points down at the bottom of the frame.
End state: Javi pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Tiene tallas de la treinta y seis a la cuarenta y nueve, el envío es gratis, y si no te van, las devuelves sin problemas. Es hora de cambiar de zapatillas. Aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## F3 · UNBOXING · «Me han llegado las Rambla» (Marta) · salón · 5 clips · 40 s · formato unboxing validado (caja en el regazo, tapa, papel, primera reacción, detalles, cierre)

### Vídeo original, beat a beat

Estructura clásica de unboxing que funciona en zapatillas: «me han llegado» con la caja en el regazo → abre la tapa (en nuestro caso ya abierta) → papel → primera reacción sincera → saca una y la gira → detalle que sorprende (puntera / suela) → la segunda para ver el par → tallas, envío, devolución → «os cuento cuando las lleve unos días».

### 1. Story Building

Marta en el sofá con la caja en el regazo desde el primer fotograma. Cada clip empieza con la caja en el estado que dejó el anterior (tapa apoyada, papel abierto, una zapatilla fuera). Nunca se prueba nada.

### 2. Character Building

Marta en casa, jersey, ilusión contenida y sincera, sin gritar. Rambla Blanco/Rojo.

Localización fija de este vídeo (Salón): Salón: sofá gris claro contra pared blanca lisa, cojín beis, mesa baja de madera, ventana a la izquierda.

### 3. Story Refining

La tapa no se abre en cámara (la IA la hace desaparecer): en el clip 1 ya está apoyada en el sofá. El papel solo se aparta con una mano. Sin precio.

Plan de fotogramas: F3.1 FOTOGRAMA NUEVO · F3.2 último frame de F3.1 · F3.3 FOTOGRAMA NUEVO · F3.4 último frame de F3.3 · F3.5 último frame de F3.2.

Clips: F3.1 Me han llegado (8 s) · F3.2 Primera reacción (8 s) · F3.3 La puntera (9 s) · F3.4 La suela y la malla (8 s) · F3.5 El par y cierre (7 s). Total 40 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa «Salón».


#### Clip F3.1 · Me han llegado · 8 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Marta seated in the middle of the sofa with the open kraft shoe box on her lap, the lid resting beside her on the sofa, white tissue paper still covering the contents, both hands on the box edges.
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing plain oatmeal knit jumper, straight dark blue jeans rolled once at the ankle, plain grey socks.
Props: one plain kraft-brown shoe box with no logo, white tissue paper inside, and the white Rambla pair. Nothing else on the sofa.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Me han llegado]
Initial state: From the first frame: Marta seated in the middle of the sofa with the open kraft shoe box on her lap, the lid resting beside her on the sofa, white tissue paper still covering the contents, both hands on the box edges.
Primary event: She looks at the lens with raised eyebrows and a small excited smile, then looks down into the box and folds the tissue paper back with one hand.
End state: Marta looking into the box, tissue folded back, the white Rambla visible inside.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Vale, me han llegado las Rambla. Os lo enseño porque llevo una semana esperándolas. A ver."}
<tissue paper rustling>
<a quiet flat, a television murmuring far away>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one sofa, one box, one Rambla pair (white with red stripe). The box stays on her lap in every clip; nothing else appears. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F3.2 · Primera reacción · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F3.1** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Primera reacción]
Initial state: Starts exactly on the provided frame: Marta seated in the middle of the sofa, the open kraft box on her lap, the lid beside her, the tissue folded back and the white Rambla visible inside, her eyes on the box.
Primary event: She lifts one white Rambla out of the box with her right hand and holds it up at chest height, in three-quarter view, lateral side with the stripe toward the lens and the full caramel sole edge visible. Her mouth opens a little, eyebrows up, then a wide honest smile; she turns the shoe slowly so the red stripe and caramel sole catch the light.
End state: Marta holding the shoe up, smiling.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta, honest: "Ay. Vale. Son más bonitas en persona. La suela caramelo… y no parecen barefoot para nada, parecen una retro normal."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one sofa, one box, one Rambla pair (white with red stripe). The box stays on her lap in every clip; nothing else appears. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F3.3 · La puntera · 9 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Close on Marta's hands: the white Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the plain white wall behind.
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing plain oatmeal knit jumper, straight dark blue jeans rolled once at the ankle, plain grey socks.
Props: one plain kraft-brown shoe box with no logo, white tissue paper inside, and the white Rambla pair. Nothing else on the sofa.
Framing: Close shot at arm's length on the hands and the shoe, face out of frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 3 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | La puntera]
Initial state: Close on Marta's hands: the white Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the plain white wall behind.
Primary event: Her finger draws the round outline of the toe box, then points inside it, then she spreads the fingers of her free hand beside it.
End state: The shoe in three-quarter view, toe box toward the lens, lateral side and full caramel sole edge visible, fingers spread beside it.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on the hands and the shoes held, the plain white wall behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Mirad la puntera. Es ancha de verdad, redonda, con la forma del pie. Aquí los dedos van sueltos, no en punta."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one sofa, one box, one Rambla pair (white with red stripe). The box stays on her lap in every clip; nothing else appears. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F3.4 · La suela y la malla · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F3.3** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 4 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | La suela y la malla]
Initial state: Starts exactly on the provided frame: close on Marta's hands, the white Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the fingers of her free hand spread beside it, the plain white wall behind.
Primary event: She tilts the shoe so the caramel lug tread reads while the lateral side stays visible, presses the sole once with her thumb, taps the tread twice, then turns it to side profile, held by the heel so the whole shoe and the flat caramel sole line stay visible so the flat line reads.
End state: The shoe in profile.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on the hands and the shoes held, the plain white wall behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<two taps on rubber>
{Marta: "Suela plana, sin tacón, y fina. Y la parte de arriba es malla, así que pesan nada."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one sofa, one box, one Rambla pair (white with red stripe). The box stays on her lap in every clip; nothing else appears. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F3.5 · El par y cierre · 7 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F3.2** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 5 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | El par y cierre]
Initial state: Starts exactly on the provided frame: Marta seated on the sofa, the open box on her lap, one white Rambla held up in her right hand, in three-quarter view, lateral side with the stripe toward the lens and the full caramel sole edge visible, smiling.
Primary event: She lifts the second white Rambla out of the box with her left hand and holds the pair up, one in each hand, in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible; a happy nod, then she points down at the bottom of the frame with the right hand still holding its shoe.
End state: Marta holding the pair, pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Tiene tallas de la treinta y seis a la cuarenta y nueve, el envío es gratis, y si no te van, las devuelves sin problemas. Os cuento cuando las lleve unos días. Aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one sofa, one box, one Rambla pair (white with red stripe). The box stays on her lap in every clip; nothing else appears. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## F4 · AUTORIDAD · «Tres cosas que miro antes de vender una zapatilla» (Andrés) · tienda · 5 clips · 42 s · formato experto (tres innegociables) en boca del profesional de la zapatería

### Vídeo original, beat a beat

Formato experto: «innegociable número uno: puntera ancha, los dedos tienen que abrirse; número dos: talón y punta en el mismo plano; número tres: suela fina y flexible. Es una zapatilla de trabajo, el pie se hace más fuerte.» Luego el creador confirma que la zapatilla lo cumple.

### 1. Story Building

Andrés, detrás del mostrador, con la zapatilla normal y la Rambla: «llevo treinta años vendiendo zapatos y miro tres cosas» → una, dos y tres enseñándolas en la mano y comparando con la normal → «con esto el pie trabaja» → «esta las cumple las tres» → tallas, envío, devolución.

### 2. Character Building

Andrés como autoridad de mostrador: didáctico, tranquilo, cuenta con los dedos, gafas en la cabeza. Rambla Gris/Blanco.

Localización fija de este vídeo (Zapatería): Zapatería pequeña: mostrador de madera en primer término, estanterías de roble claro con zapatos desenfocados detrás, cajas de zapatos apiladas al fondo, luz cálida de tienda, sin rótulos ni marcas.

### 3. Story Refining

La autoridad es de oficio (vendedor de zapatería), no médica: no se dice «podólogo», «estudios» ni «cura». Comparación siempre en la mano.

Plan de fotogramas: F4.1 FOTOGRAMA NUEVO · F4.2 FOTOGRAMA NUEVO · F4.3 último frame de F4.2 · F4.4 último frame de F4.1 · F4.5 último frame de F4.4.

Clips: F4.1 Tres cosas que miro (8 s) · F4.2 Uno: puntera ancha (9 s) · F4.3 Dos: sin tacón. Tres: fina y flexible (9 s) · F4.4 El pie se hace más fuerte (8 s) · F4.5 Cierre (8 s). Total 42 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Andrés. Image 2 = foto del proveedor de Rambla Gris/Blanco. Image 3 = placa «Zapatería».


#### Clip F4.1 · Tres cosas que miro · 8 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Andrés standing behind the counter, the conventional black sneaker and one grey Rambla lying on the counter in front of him in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge stay visible, his hands resting on the counter.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: one conventional black sneaker with a narrow pointed toe box and no logo, and the grey Rambla pair. Only the props named in each clip are on the counter.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Tres cosas que miro]
Initial state: From the first frame: Andrés standing behind the counter, the conventional black sneaker and one grey Rambla lying on the counter in front of him in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge stay visible, his hands resting on the counter.
Primary event: He looks at the lens, holds up three fingers, then rests the hand on the Rambla.
End state: Andrés standing, hand on the Rambla.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés, calm: "Llevo treinta años vendiendo zapatos, y antes de vender una zapatilla miro tres cosas. Solo tres."}
<a shop door bell far away, a cardboard box set down>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F4.2 · Uno: puntera ancha · 9 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Close on Andrés's hands over the counter: the conventional black sneaker in his left hand and the grey Rambla in his right, side by side, both in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge of each shoe stay visible.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: one conventional black sneaker with a narrow pointed toe box and no logo, and the grey Rambla pair. Only the props named in each clip are on the counter.
Framing: Close shot at arm's length on the hands and the shoe, face out of frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | Uno: puntera ancha]
Initial state: Close on Andrés's hands over the counter: the conventional black sneaker in his left hand and the grey Rambla in his right, side by side, both in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge of each shoe stay visible.
Primary event: One finger up. Then his thumb squeezes the pointed toe of the conventional sneaker, then slides across the wide round toe box of the Rambla.
End state: Both shoes in three-quarter view, toe boxes toward the lens, lateral sides and full caramel sole edges visible.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at counter height, close on Andrés's hands and the shoes held over the wooden counter, shelves out of focus behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Una: puntera ancha. Los dedos tienen que poder abrirse. Esta acaba en punta y te los junta. Esta tiene la forma del pie."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F4.3 · Dos: sin tacón. Tres: fina y flexible · 9 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F4.2** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 3 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | Dos: sin tacón. Tres: fina y flexible]
Initial state: Starts exactly on the provided frame: close on Andrés's hands over the counter, the conventional black sneaker in his left hand and the grey Rambla in his right, side by side, both in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge of each shoe stay visible.
Primary event: He turns both shoes at the same time to side profile, held by the heel so the whole shoe and the flat caramel sole line stay visible side by side, the flat caramel sole of the Rambla next to the raised heel wedge of the conventional sneaker. Two fingers up, then he taps the raised heel of the conventional shoe and the flat heel of the Rambla. Three fingers up, then his thumb presses the thin Rambla sole.
End state: Both shoes in profile, thumb on the Rambla sole.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at counter height, close on Andrés's hands and the shoes held over the wooden counter, shelves out of focus behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Dos: talón y punta a la misma altura, sin tacón. Mira esta, y mira esta. Tres: suela fina y flexible, que el pie trabaje y no vaya en una caja."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F4.4 · El pie se hace más fuerte · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F4.1** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 4 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | El pie se hace más fuerte]
Initial state: Starts exactly on the provided frame: Andrés standing behind the counter, the conventional black sneaker and one grey Rambla lying on the counter in front of him in three-quarter view, in three-quarter view, toe boxes toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible but angled so the lateral side with the stripe and the full caramel sole edge stay visible, his hand resting on the Rambla.
Primary event: He lifts the Rambla up beside his face, in three-quarter view, lateral side with the stripe toward the lens and the full caramel sole edge visible. He flexes his free hand open and closed twice, then taps the shoe.
End state: Andrés holding the Rambla up.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Con esto el pie trabaja y se hace más fuerte. Con tacón y mucha amortiguación, el pie va dormido, y luego vienen los dolores. Esta las cumple las tres."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F4.5 · Cierre · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F4.4** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 5 of 5 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Cierre]
Initial state: Starts exactly on the provided frame: Andrés behind the counter holding the grey Rambla up beside his face, the conventional sneaker on the counter.
Primary event: He sets the Rambla down on the counter under his hand, a slow nod, then points down at the bottom of the frame.
End state: Andrés pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Se llama Rambla. Tiene tallas de la treinta y seis a la cuarenta y nueve, el envío es gratis, y si no te van, las devuelves sin problemas. Aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## F5 · RESPUESTA A COMENTARIO · «¿Sirven para un pie muy ancho, talla 47?» (Andrés) · tienda · 4 clips · 30 s · formato respuesta a comentario (sticker del comentario arriba, respuesta directa)

### Vídeo original, beat a beat

Formato «respondiendo a un comentario»: sticker con el comentario en la parte alta de la pantalla los primeros segundos (lo pones tú en CapCut), el creador lo lee o lo resume, responde directo con el producto en la mano, y cierra con link. En los vídeos de referencia es uno de los formatos con mejor retención.

### 1. Story Building

Andrés lee el comentario («¿sirven para un pie muy ancho, talla 47?»), responde con el par grande en la mano: sí, por qué, cómo elegir talla, y cierra. Texto del sticker: «¿Sirven para pie muy ancho? Uso una 47 y todo me aprieta».

### 2. Character Building

Andrés respondiendo a un cliente, cercano y concreto. Rambla Gris/Blanco en talla grande.

Localización fija de este vídeo (Zapatería): Zapatería pequeña: mostrador de madera en primer término, estanterías de roble claro con zapatos desenfocados detrás, cajas de zapatos apiladas al fondo, luz cálida de tienda, sin rótulos ni marcas.

### 3. Story Refining

El comentario se pone en postproducción, no se pide a la IA. La respuesta de talla es por centímetros, sin prometer nada.

Plan de fotogramas: F5.1 FOTOGRAMA NUEVO · F5.2 FOTOGRAMA NUEVO · F5.3 último frame de F5.1 · F5.4 último frame de F5.3.

Clips: F5.1 Leo el comentario (7 s) · F5.2 Sí, y por esto (8 s) · F5.3 Cómo elegir la talla (8 s) · F5.4 Cierre (7 s). Total 30 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Andrés. Image 2 = foto del proveedor de Rambla Gris/Blanco. Image 3 = placa «Zapatería».


#### Clip F5.1 · Leo el comentario · 7 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole, a visibly large size. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Andrés standing behind the counter looking slightly above the lens as if reading a comment on screen, the grey Rambla pair on the counter in front of him under his hands.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: the grey Rambla pair in a visibly large size. Nothing else on the counter.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Leo el comentario]
Initial state: From the first frame: Andrés standing behind the counter looking slightly above the lens as if reading a comment on screen, the grey Rambla pair on the counter in front of him under his hands.
Primary event: He reads, nods twice, then looks straight into the lens and lifts one shoe.
End state: Andrés holding one shoe up.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Me preguntan: «¿sirven para un pie muy ancho? Uso una cuarenta y siete y todo me aprieta.» Pues mira."}
<a shop door bell far away, a cardboard box set down>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F5.2 · Sí, y por esto · 8 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole, a visibly large size. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Close on Andrés's hands over the counter: the grey Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the shoe reading clearly large next to his hands.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: the grey Rambla pair in a visibly large size. Nothing else on the counter.
Framing: Close shot at arm's length on the hands and the shoe, face out of frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Sí, y por esto]
Initial state: Close on Andrés's hands over the counter: the grey Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, the shoe reading clearly large next to his hands.
Primary event: His finger draws the round outline of the toe box, then he lays his open hand flat inside the opening to show the width.
End state: The shoe in three-quarter view, toe box toward the lens, lateral side and full caramel sole edge visible, his open hand laid flat inside the opening.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at counter height, close on Andrés's hands and the shoes held over the wooden counter, shelves out of focus behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Sí. Y no porque sean grandes de largo: la puntera es ancha de verdad, con la forma del pie. Aquí cabe la mano entera."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F5.3 · Cómo elegir la talla · 8 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F5.1** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 3 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Cómo elegir la talla]
Initial state: Starts exactly on the provided frame: Andrés standing behind the counter holding one large grey Rambla up in his right hand, the other shoe on the counter.
Primary event: He sets the shoe down on the counter beside the other one, takes the end of the tape measure hanging around his neck and holds it out toward the lens, taps it, then draws a short line on the counter with his finger as if measuring a foot.
End state: Andrés holding the tape measure out.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Solo una cosa: tallan pequeño. Mide el pie en centímetros, folio contra la pared, y mira la tabla. Y si estás entre dos, la grande."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F5.4 · Cierre · 7 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F5.3** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 4 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Cierre]
Initial state: Starts exactly on the provided frame: Andrés behind the counter holding the end of the tape measure out toward the lens, the grey Rambla pair on the counter.
Primary event: He lets the tape drop back against his chest, rests both hands on the pair, a closed-lip smile, and points down at the bottom of the frame.
End state: Andrés pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Tiene tallas de la treinta y seis a la cuarenta y nueve, el envío es gratis, y si no te van, las devuelves sin problemas. Pregúntame lo que quieras en los comentarios."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one person, one Rambla pair, one location; same clothes and light as the reference. Everything stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## F6 · ALMACÉN · «Estamos preparando los pedidos de hoy» (Andrés) · almacén · 4 clips · 31 s · formato almacén (detrás de las cajas, la que más sale, se empaqueta a cámara)

### Vídeo original, beat a beat

Formato almacén: el vendedor entre estanterías de cajas, «estamos preparando los pedidos de hoy», enseña la que más sale, la mete en la caja y cierra con envío gratis y link. Transmite que se vende de verdad y que hay stock.

### 1. Story Building

Andrés en la trastienda con la mesa de embalar: pedidos de hoy → «esta es la que más sale» con la zapatilla en la mano → por qué (puntera y suela) → la deja en la caja abierta (un solo gesto) → tallas, envío gratis, devolución.

### 2. Character Building

Andrés con las mangas remangadas, ritmo de trabajo, sin vender. Rambla Gris/Blanco.

Localización fija de este vídeo (Almacén): Trastienda/almacén de zapatería: estanterías metálicas grises con cajas de zapatos marrones, mesa de embalar de madera con un rollo de cinta y una caja de envío abierta, luz fluorescente fría con relleno de día.

### 3. Story Refining

Sin cifras de pedidos. Solo un movimiento de objeto en todo el vídeo: dejar la zapatilla dentro de la caja abierta en el clip 3, y la caja ya está abierta desde el primer fotograma. Nadie precinta nada.

Plan de fotogramas: F6.1 FOTOGRAMA NUEVO · F6.2 FOTOGRAMA NUEVO · F6.3 último frame de F6.1 · F6.4 último frame de F6.3.

Clips: F6.1 Los pedidos de hoy (8 s) · F6.2 La que más sale (9 s) · F6.3 A la caja (7 s) · F6.4 Cierre (7 s). Total 31 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Andrés. Image 2 = foto del proveedor de Rambla Gris/Blanco. Image 3 = placa «Almacén».


#### Clip F6.1 · Los pedidos de hoy · 8 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Andrés standing behind the packing table, the open brown shipping box and the tape roll in front of him, the grey Rambla pair beside the box, metal shelving with boxes behind him.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: the grey Rambla pair, one plain kraft shoe box with no logo, one open brown shipping box and a roll of brown tape on the packing table. Nothing else on the table.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–8s | Los pedidos de hoy]
Initial state: From the first frame: Andrés standing behind the packing table, the open brown shipping box and the tape roll in front of him, the grey Rambla pair beside the box, metal shelving with boxes behind him.
Primary event: He looks at the lens, gestures at the shelving behind him with a thumb, then rests both hands on the table.
End state: Andrés standing, hands on the table.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the far end of the packing table at Andrés's chest height, medium shot of Andrés standing behind the packing table facing the lens, the open shipping box and the tape roll on the table in the lower frame, metal shelving with boxes behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Estamos preparando los pedidos de hoy. Y os enseño la que más sale, porque no es casualidad."}
<a tape roll tearing somewhere, a box slid on a shelf>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one stockroom, one Rambla pair, one shoe box, one shipping box, one tape roll; everything on the table stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F6.2 · La que más sale · 9 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
Scene: Close on Andrés's hands over the packing table: one grey Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, then turned to side profile, held by the heel so the whole shoe and the flat caramel sole line stay visible.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: the grey Rambla pair, one plain kraft shoe box with no logo, one open brown shipping box and a roll of brown tape on the packing table. Nothing else on the table.
Framing: Close shot at arm's length on the hands and the shoe, face out of frame. Eye level with the subject, no wide-angle distortion.
Face rule: no face in the frame, only hands and the shoe; the crop is clean at the chest, no chin, no hair.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–9s | La que más sale]
Initial state: Close on Andrés's hands over the packing table: one grey Rambla held in three-quarter view, the wide toe box toward the lens but angled so the lateral side with the stripe and the full caramel sole edge stay visible, then turned to side profile, held by the heel so the whole shoe and the flat caramel sole line stay visible.
Primary event: His finger draws the toe box outline, then runs along the flat caramel sole in profile, then taps the flat heel.
End state: The shoe in profile, finger on the heel.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at table height, close on Andrés's hands and the shoes held over the packing table, shelving out of focus behind; natural micro-sway only, no travel, no tilt. The face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "La Rambla. Puntera ancha para pies anchos, suela plana sin tacón, y por fuera una retro normal. Por eso se la llevan los que ya lo han probado todo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one stockroom, one Rambla pair, one shoe box, one shipping box, one tape roll; everything on the table stays where the initial state puts it. The face, clothes and location match the start frame exactly. No face ever enters the frame: the shot stays on the hands and the shoe from the first frame to the last. The whole shoe stays inside the frame, never cropped, never hidden by the hands: it is held by the heel or the collar so the toe box, the lateral side with the stripe and the caramel sole stay in view. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F6.3 · A la caja · 7 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F6.1** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 3 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | A la caja]
Initial state: Starts exactly on the provided frame: Andrés standing behind the packing table, both hands on the table, the open brown shipping box and the tape roll in front of him, the grey Rambla pair beside the box.
Primary event: He picks up one grey Rambla and lowers it into the open box in one slow movement, leaves it there, then pats the box once.
End state: The shoe inside the open box, Andrés's hand on the box.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the far end of the packing table at Andrés's chest height, medium shot of Andrés standing behind the packing table facing the lens, the open shipping box and the tape roll on the table in the lower frame, metal shelving with boxes behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a shoe set down in cardboard>
{Andrés: "Esta sale hoy. Envío gratis."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one stockroom, one Rambla pair, one shoe box, one shipping box, one tape roll; everything on the table stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F6.4 · Cierre · 7 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F6.3** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 4 of 4 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Cierre]
Initial state: Starts exactly on the provided frame: Andrés behind the table, one grey Rambla inside the open box, the other beside it, his hand on the box.
Primary event: He rests both hands on the table, a nod, then points down at the bottom of the frame.
End state: Andrés pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the far end of the packing table at Andrés's chest height, medium shot of Andrés standing behind the packing table facing the lens, the open shipping box and the tape roll on the table in the lower frame, metal shelving with boxes behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Tiene tallas de la treinta y seis a la cuarenta y nueve, el envío es gratis, y si no te van, las devuelves sin problemas. Aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one stockroom, one Rambla pair, one shoe box, one shipping box, one tape roll; everything on the table stays where the initial state puts it. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## F7 · ELEGIR COLOR · «Ayúdame a elegir entre estos tres» (Andrés) · tienda · 2 clips · 14 s · réplica exacta del vídeo de «elegimos entre 3 modelos: miel, black cherry o negro»

### Vídeo original, beat a beat

Vendedor en su tienda con tres zapatos sobre el mostrador: «Elegimos entre tres modelos. Un miel, black cherry o negro. ¿Tú cuál prefieres? Y si te gustan los tres también, dame tu comentario.» 13 s, coge cada uno al nombrarlo.

### 1. Story Building

Igual: Andrés con las tres Rambla en el mostrador, las nombra levantando cada una y devolviéndola a su sitio, pregunta y pide comentario.

### 2. Character Building

Andrés preguntando de verdad, cejas arriba, manos abiertas. Tres colores: gris, blanca, negra.

Localización fija de este vídeo (Zapatería): Zapatería pequeña: mostrador de madera en primer término, estanterías de roble claro con zapatos desenfocados detrás, cajas de zapatos apiladas al fondo, luz cálida de tienda, sin rótulos ni marcas.

### 3. Story Refining

Es el único vídeo con objetos que se levantan: cada zapatilla vuelve exactamente a su sitio. Versión de respaldo si falla: solo señalar con el dedo.

Plan de fotogramas: F7.1 FOTOGRAMA NUEVO · F7.2 último frame de F7.1.

Clips: F7.1 Elegimos entre tres (7 s) · F7.2 Y si te gustan las tres (7 s). Total 14 s.

### 4. First Draft (fotograma + vídeo, listos)

Image 1 = hoja de personaje de Andrés. Image 2 = foto del proveedor de Rambla Gris/Blanco. Image 3 = placa «Zapatería».


#### Clip F7.1 · Elegimos entre tres · 7 s

**Fotograma inicial: NUEVO.** Genera esta imagen con Image 1, Image 2 e Image 3 y úsala como imagen de inicio del vídeo.

```
Photorealistic phone photo, vertical 9:16, a real Spanish setting, nothing styled. This image is the first frame of a short UGC video, so it must be a natural mid-action still, not a posed catalogue shot.
@Image1 is the person: keep their identity, face, hair, build and clothes exactly. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: replicate it exactly, grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Do not slim the toe box, do not add a heel wedge, do not change the sole colour.
@Image3 is the location: use this exact place, layout, materials and light. Do not add furniture, do not change the wall or the floor.
@Image4 is the same Rambla sneaker in the white colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Replicate it exactly.
@Image5 is the same Rambla sneaker in the black colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Replicate it exactly.
Scene: Andrés standing behind the counter with the three Rambla shoes lined up on the counter, grey, white and black, in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible, both hands resting on the counter.
Andrés: Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, calm shopkeeper's face; wearing light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, a yellow shoemaker's tape measure hanging around his neck.
Props: three Rambla shoes, one of each colorway, lined up on the counter in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible: grey with white stripe (@Image2), white with red stripe (@Image4), black with white stripe (@Image5). Nothing else on the counter.
Framing: Medium shot, phone propped at chest height, subject centred facing the lens. Eye level with the subject, no wide-angle distortion.
Face rule: the face is fully visible in the frame, looking at the lens, not cropped.
Product rule: at least one Rambla sneaker is completely visible in this frame, in three-quarter view, so its whole design reads at once: the wide round toe box, the lateral side with the stripe, the laces, the collar and the full caramel gum sole with its lug edge. Not cropped, not hidden by the hands, not seen only from the toe or only from the sole.
Light: soft daylight from frame left, 26mm phone-style lens, f/2.0, natural slightly warm colour grade, visible fine grain, no HDR, no retouching, realistic skin with pores.
No on-screen text, no subtitles, no logos, no watermarks, no extra people, no extra shoes. Original person, not a real individual.
```

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 1 of 2 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Elegimos entre tres]
Initial state: From the first frame: Andrés standing behind the counter with the three Rambla shoes lined up on the counter, grey, white and black, in three-quarter view, lateral sides with the stripe toward the lens and the full caramel sole edge visible, both hands resting on the counter.
Primary event: He lifts the grey one, shows it, sets it back exactly in place; lifts the white one, shows it, sets it back; lifts the black one, shows it, and keeps it up.
End state: Andrés holding the black one, the grey and white back in place.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Elegimos entre tres. Una gris, una blanca con la raya roja, o negra. ¿Tú cuál prefieres?"}
<a shop door bell far away, a cardboard box set down>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one counter, exactly three shoes of three colors in the same order in both clips. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

#### Clip F7.2 · Y si te gustan las tres · 7 s

**Fotograma inicial: reutiliza el ÚLTIMO FRAME del clip F7.1** (exporta el último fotograma de ese vídeo y úsalo como imagen de inicio). No hay que generar imagen.

**Prompt de vídeo (image-to-video, con el fotograma como imagen de inicio):**

```
[START FRAME]
The provided image is frame 0 of this clip. Keep everything in it unchanged for the whole clip: same person, same face, same clothes, same shoes, same place, same framing, same light. Nothing new enters the frame and nothing in it disappears.

[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism. Part 2 of 2 of one short ad for a wide-toe retro sneaker. The clip starts exactly on the provided frame and ends exactly in the end state described below.

[PRODUCT]
The sneaker in the frame is the Rambla: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: grey ribbed mesh, light grey suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

[STAGE 1 | 0–7s | Y si te gustan las tres]
Initial state: Starts exactly on the provided frame: Andrés behind the counter holding the black Rambla up in his right hand, the grey and the white ones lined up on the counter.
Primary event: He sets the black one back in its place beside the others, opens both hands toward the lens, eyebrows up, then points down at the bottom of the frame with a smile.
End state: The three shoes in place, Andrés pointing down.
Cut type: NO CUT — one continuous take.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the wooden counter at Andrés's chest height, medium shot of Andrés standing behind the counter facing the lens, the counter edge in the lower frame, shelves of shoes out of focus behind, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Andrés: "Y si te gustan las tres, también me vale. Déjamelo en un comentario. Tallas de la treinta y seis a la cuarenta y nueve, aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one counter, exactly three shoes of three colors in the same order in both clips. The face, clothes and location match the start frame exactly. The face stays fully visible inside the frame for the whole clip, never cropped, never turned away from the lens for more than a moment. The Rambla keeps exactly the design visible in the start frame: same toe box shape, same stripe, same laces, same caramel sole; at least one shoe stays completely visible in every frame.
```

---

## Placas de localización (Image 3) · se generan una vez

### Image 3 · Zapatería
```
Photorealistic phone photo, vertical 9:16, of the inside of a small empty Spanish shoe shop from the customer side of a wooden counter: the counter in the foreground, behind it light oak wall shelving with rows of shoes out of focus, a few plain shoe boxes stacked at the end of the shelves, warm even shop light with a soft daylight fill from frame left, no signage, no brand names, no readable labels. Camera at chest height facing the counter, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Real and ordinary, nothing styled.
```
### Image 3 · Almacén
```
Photorealistic phone photo, vertical 9:16, of a small empty stockroom behind a shoe shop: grey metal shelving on both sides stacked with plain brown shoe boxes, a wooden packing table in the foreground with a roll of brown tape and one open brown shipping box, cool fluorescent light with a soft daylight fill from frame left, no labels or logos readable. Camera at chest height facing the table, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Real and ordinary, nothing styled.
```
### Image 3 · Portal
```
Photorealistic phone photo, vertical 9:16, of the empty entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Camera at chest height from the pavement facing the door, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Ordinary and real, nothing styled.
```
### Image 3 · Salón
```
Photorealistic phone photo, vertical 9:16, of an empty living room of an ordinary Spanish flat: a light grey fabric sofa against a plain white wall, one beige cushion, a low wooden coffee table in front, a window to the left giving soft daylight from frame left, nothing on the wall behind the sofa. Camera at chest height facing the sofa from the coffee table, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Lived-in and clean, nothing styled.
```

## Retrato base · Andrés
```
Photorealistic phone photo, vertical 4:5, of a Spanish man, 54, lean build, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head, realistic skin with pores, standing behind the wooden counter of a small shoe shop with light oak shelving of shoes out of focus behind him, wearing a light blue Oxford shirt with the sleeves rolled twice, a navy V-neck knitted vest over it, dark chinos, and a yellow shoemaker's tape measure hanging around his neck. Warm even shop light with a soft daylight fill from frame left, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no retouching. He looks slightly off camera with a calm, knowing half-smile. No text, no logos. Original person, not a real individual.
```
## Image 1 · Hoja de personaje · Andrés (adjunta el retrato base como image 1)
```
Use the person from image 1. Keep their identity. Do not recast. Do not beautify. One image, three equal vertical panels, same width, same height, hard even splits, no decorative borders. Same background in every panel: flat seamless studio grey B8B8B8, even light, no gradient, no floor shadow color shift. Panel 1, left: front view, the head is not visible, crop cleanly at the neck, no head, no face, no hair, no neck stump cheat, body only, standing, feet in frame, wardrobe and hands readable: light blue Oxford shirt with the sleeves rolled twice, navy V-neck knitted vest, dark chinos, a yellow shoemaker's tape measure around the neck, grey retro sneakers with a white stripe and caramel sole, same clothes as image 1. Panel 2, middle: full body from the back, head included, same clothes, standing, feet in frame; the bodies in panel 1 and panel 2 have the same height, neck to feet matches, same scale, feet on the same baseline, do not scale one body up or down to fill the panel. Panel 3, right: close-up of the face from the front on the same grey B8B8B8, shoulders in, face sharp, natural skin, not smoothed: Spanish man, 54, short grey hair combed back, neat grey stubble, reading glasses pushed up on his head. Photographed, not illustrated. No logos. No text. No grain overlay.
```

Marta y Javi: retratos y hojas de personaje del test 1 (Clips_Seedance_Rambla_Test1.md, sección final).
