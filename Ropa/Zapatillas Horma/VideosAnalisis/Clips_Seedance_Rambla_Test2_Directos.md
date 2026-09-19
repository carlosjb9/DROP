# Rambla · test 2 «directos» · 6 formatos validados en 4 pasos

**Qué cambia respecto al test 1 (feedback del mentor):** los tres primeros anuncios tardaban casi diez segundos en enseñar el problema y no tenían hook visual. Aquí cada ángulo replica un formato que ya ha funcionado (Breeze, el tendero de Olyndra, las sandalias, el «esto o esto», el «ayúdame a elegir») sin copiarlo uno a uno: el problema o el producto están en el primer fotograma, la primera frase ya es el gancho, no hay presentaciones ni escenas de alivio, y a los 20 segundos ya está la oferta. Todo sigue siendo estático: avatar sentado, cámara fija, producto en la mano.

**Regla de honestidad:** no se inventan cifras de clientes ni reseñas («atiendo a cincuenta hombres al día», «20.000 opiniones»). Si Carlos tiene un dato real de Navarros, se puede meter en la primera frase de D2 o D6. Precio, envío y 30 días son los que están publicados en la tienda; si cambian, se cambian en los cuatro clips de cierre.

**Regla de continuidad (actualizada):** avatar y producto fijos entre vídeos (Marta con su bata y la Rambla blanca/roja; Javi con la Rambla negra/blanca). La localización es fija dentro de cada vídeo pero cambia de un vídeo a otro según el gancho: D1 recibidor, D2 portal, D3 salón, D4 gym (Javi con ropa de entrenar solo en este vídeo), D5 banco de la calle, D6 detrás del mostrador de la farmacia. Cada clip lleva tres referencias: Image 1 = hoja de personaje, Image 2 = foto del proveedor del color fijo de ese avatar, Image 3 = placa de la localización de ese vídeo (los seis prompts de placa están al final del archivo).

**Regla de simplicidad:** todo se rueda con el avatar sentado en su sitio de siempre y la cámara fija. Lo único que se mueve son las manos, la cara y la zapatilla que enseña a cámara. Nadie se pone ni se quita zapatillas, nadie ata cordones, nadie anda, ningún objeto entra ni sale de plano salvo que el prompt lo diga. Cuando la Rambla va puesta, ya está puesta desde el primer fotograma y los pies no se mueven; cuando va en la mano, no va puesta. Cada prompt lleva estas prohibiciones en [EXCLUSIONS].

**Cómo se usa:** cada bloque de código es un clip independiente de 10 s o menos. Lo copias entero, adjuntas Image 1, Image 2 e Image 3 y generas. Nada que rellenar. El diálogo va dentro en castellano de España; si prefieres ElevenLabs, generas igual y silencias la pista.


---

## D1 · «Si se te quedan los dedos así» (Marta) · 4 clips · 30 s · formato hook-visual de pie (Breeze)

### 1. Story Building

Formato replicado: el de Breeze (hook visual del pie en el segundo 0 y de ahí al producto sin rodeos). Marta no se presenta ni cuenta su día: el primer fotograma ya es el problema (dedos en punta con marcas) y la primera frase ya es el diagnóstico. Luego la solución en la mano, luego puestas con la prueba del turno, luego oferta. Arco: problema visible → solución en la mano → prueba de uso → oferta.

### 2. Character Building

Marta, 44, auxiliar de farmacia, pie ancho con juanete leve. Habla directa, como si no tuviera tiempo. Emociones: ninguna escena de alivio larga; solo una media sonrisa cerrada al hablar del turno. Ropa fija: bata blanca sobre camiseta gris, vaqueros, calcetines grises. Producto fijo: Rambla blanca/roja.

Localización fija de este vídeo (recibidor): Recibidor de un piso español de los años 80: suelo de terrazo gris y crema, pared blanca con un interruptor beis, banco bajo de madera con asiento de rejilla contra la pared izquierda, zapatero de madera oscura con un cuenco de llaves encima contra la pared derecha, un espejo pequeño enmarcado sobre el zapatero, una ventana al fondo que da luz suave desde la izquierda, la puerta de la cocina visible al final del pasillo.

### 3. Story Refining

Se quitan la exhalación, el «ahora lo entiendo» y cualquier frase de presentación: el mentor tiene razón en que el problema tardaba diez segundos en aparecer. Ahora aparece en el fotograma 1 y en la primera frase. Todo sentada o cenital fijo, producto en la mano, sin ponerse nada en cámara. Comprobaciones: la Rambla va en la mano en el clip 2 y puesta desde el primer fotograma en los clips 3 y 4; ninguna afirmación médica; el precio y los 30 días son los que Carlos tiene publicados.

Clips: D1.1 Hook visual: los dedos en punta, segundo 0 (6 s) · D1.2 La solución en la mano, las dos punteras (8 s) · D1.3 Puestas: ocho horas de pie (8 s) · D1.4 Oferta y cierre (8 s). Total 30 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa de localización «recibidor» (prompt al final del archivo).


#### Clip D1.1 · Hook visual: los dedos en punta, segundo 0 · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | Hook visual: los dedos en punta, segundo 0]
Initial state: Overhead, from the very first frame: Marta's bare feet flat and completely still on the terrazzo in front of the bench, toes squeezed together into a point, the big toe angled inward, a mild natural bunion, faint red pressure marks on the sides of the toes, a faint sock line; the conventional white sneaker lying on its side beside the right foot with its pointed toe toward the foot.
Primary event: The feet do not move. Her right hand enters from the top of the frame and the index finger points at the squeezed toes, then at the pointed toe of the sneaker, then back at the toes. The hand stays there.
End state: Feet in the same place, the finger resting between the toes and the sneaker.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot directly overhead, looking straight down at the terrazzo; natural micro-sway only, no travel, no tilt. No face in frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta, direct, no intro: "Si al quitarte la zapatilla se te quedan los dedos así, en punta, escúchame, que a mí me pasaba y la culpa era de esta puntera."}
<a quiet flat>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D1.2 · La solución en la mano, las dos punteras · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | La solución en la mano, las dos punteras]
Initial state: Close on Marta's hands at chest height: the conventional white sneaker in her left hand and one white Rambla in her right hand, side by side at the same height, both toes toward the lens, the white wall behind.
Primary event: She holds them still for two seconds so the wider, rounder toe box of the Rambla reads. Her right thumb slides across the wide toe box once. Then she turns both to a strict side profile: flat caramel sole next to the raised heel wedge. She holds that.
End state: Both shoes in side profile side by side in her hands.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on her hands and the shoes she holds; natural micro-sway only, no travel, no tilt. Her face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<fabric brushing as the shoes turn>
{Marta: "Estas son las Rambla. Puntera con la forma del pie, los dedos van sueltos. Y suela plana, sin tacón. Mismo número, mira la diferencia."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D1.3 · Puestas: ocho horas de pie · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Puestas: ocho horas de pie]
Initial state: Marta seated on the low bench wearing the white Rambla pair, both feet flat and still on the terrazzo in the lower part of the frame, hands on her knees, looking at the lens.
Primary event: She points down at her feet once, then pinches the fabric of her tunic sleeve for a second as she mentions the shift, then opens one hand palm up. A closed-lip half-smile. Feet never move.
End state: Marta seated, Rambla on, feet in the same place, hand open palm up.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<the fridge humming far away>
{Marta: "Yo hago ocho horas de pie en la farmacia con ellas. Son de malla, no se te cuecen, y por fuera son una retro normal."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D1.4 · Oferta y cierre · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Oferta y cierre]
Initial state: Same framing: Marta seated on the bench wearing the white Rambla pair, feet flat and still, hands on her knees.
Primary event: She counts three things on her fingers, one at a time, then points down at the bottom of the frame and holds it with a small nod.
End state: Marta seated, pointing down at the bottom of the frame, nodding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Cuarenta y nueve con noventa y cinco, del treinta y seis al cuarenta y nueve, y si no te van, treinta días y te devuelven el dinero. Pruébalas, que no te las vas a querer quitar. Aquí abajo."}
<a bird outside the window>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## D2 · «Pie ancho y talla 46: estas» (Javi) · 4 clips · 30 s · formato «las que todos piden», con el producto en la mano desde el segundo 0

### 1. Story Building

Formato replicado: el del tendero de Olyndra («estas son las que todos piden», producto en alto desde el segundo 0, beneficios en tres frases, precio, envío, link), adaptado con honestidad: Javi no es tendero y no inventa cifras de clientes; lo que hace es abrir con su caso en una frase y el par en alto. Arco: par en alto + problema en una frase → ancho contra largo → suela plana + tallas grandes → oferta.

### 2. Character Building

Javi, 42, talla 46, pie ancho, práctico, habla seco y corto. Emociones: orgullo tranquilo (barbilla, sonrisa cerrada, parpadeo lento). Ropa fija: polo azul marino, pantalón gris oscuro, reloj digital, calcetines negros. Producto fijo: Rambla negra/blanca en talla grande.

Localización fija de este vídeo (portal): Portal de un edificio de viviendas español: tres escalones de piedra gris gastados, puerta de madera verde oscuro con el número 14 en latón, pared enfoscada color crema con zócalo de piedra gris, acera de granito delante, una bicicleta negra apoyada en la pared a la derecha, sombra abierta de mañana con luz suave desde la izquierda.

### 3. Story Refining

Se quitan la frustración larga y la explicación de «yo pedía una talla más» como escena: pasa a ser una frase del hook. El par aparece en alto en el primer fotograma para que el hook sea visual. Se evita cualquier cifra tipo «atiendo a cincuenta hombres al día» porque no es verdad; si Carlos tiene un dato real de Navarros (pedidos, tallas más vendidas) se puede sustituir la primera frase por él. Comprobaciones: mismo portal, Rambla en la mano en los clips 1 a 3 y puesta en el 4.

Clips: D2.1 Hook: el par en alto desde el primer fotograma (6 s) · D2.2 Ancho contra largo, mismo número (8 s) · D2.3 Suela plana y tallas grandes (8 s) · D2.4 Oferta y cierre (8 s). Total 30 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa de localización «portal» (prompt al final del archivo).


#### Clip D2.1 · Hook: el par en alto desde el primer fotograma · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | Hook: el par en alto desde el primer fotograma]
Initial state: From the very first frame: Javi seated on the top stone step holding the black Rambla pair up with both hands at chest height, one shoe in each hand, lateral sides to the lens, the shoes reading clearly big next to his hands, the green door behind him.
Primary event: He keeps the pair up and still. His chin lifts, a closed-lip smile spreads slowly, one slow blink. Then he tips both shoes so the wide toe boxes point straight at the lens and holds.
End state: The pair held up, toe boxes toward the lens.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi, direct, no intro: "Pie ancho, talla cuarenta y seis, y harto de pedir una talla más. Estas son las que me han quitado el problema."}
<a bicycle chain ticking>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D2.2 · Ancho contra largo, mismo número · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Ancho contra largo, mismo número]
Initial state: Close on Javi's hands at chest height: the conventional black sneaker in his left hand and the black Rambla in his right hand, side by side at the same height, both toes toward the lens, same nominal size, the green door behind.
Primary event: He holds them still: the difference in toe-box width reads without explanation. His thumb and index finger open a gap of about two centimetres in front of the conventional toe, then his thumb slides across the wide toe box of the Rambla. He holds them still again.
End state: Both shoes still side by side, toes to the lens.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a thumb brushing mesh>
{Javi: "Mismo número. Esta aprieta de ancho y sobra por delante. Esta tiene la puntera ancha de verdad y el pie va suelto."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D2.3 · Suela plana y tallas grandes · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Suela plana y tallas grandes]
Initial state: Close on Javi's hands: the same two shoes held in strict side profile side by side, soles toward the floor, the flat caramel sole of the Rambla next to the thick raised heel wedge of the conventional sneaker.
Primary event: His thumb taps the flat heel of the Rambla twice, then the tall heel of the other once. Then he lifts the Rambla alone closer to the lens and turns it slowly to show the toe box and the mesh, and holds.
End state: The Rambla alone close to the lens, the conventional sneaker lower in the other hand.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<three soft thumb taps on rubber>
{Javi: "Suela plana, sin tacón, de malla. Y hay cuarenta y siete, cuarenta y ocho y cuarenta y nueve, con esta misma horma."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D2.4 · Oferta y cierre · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Oferta y cierre]
Initial state: Javi seated on the top step wearing the black Rambla pair, both feet flat and still on the lower step in the lower part of the frame, hands on his knees, the green door behind him.
Primary event: He points down at his feet once, then holds up three fingers one after another, then points down at the bottom of the frame with the closed-lip smile.
End state: Javi seated, Rambla on, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Cuarenta y nueve con noventa y cinco, envío a casa y treinta días para devolverlas. Mide el pie en centímetros antes de pedir, que tallan pequeño. Aquí abajo."}
<a moped far away>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## D3 · «Os voy a ser sincera» (Marta) · 4 clips · 32 s · salón · formato escéptica-convencida, un solo plano con el producto en las manos

### 1. Story Building

Formato replicado: el de las sandalias del mentor (un solo plano, sentada, el producto en las manos los treinta segundos, escéptica que se convence, la amiga con las de marca, oferta, «no vas a querer quitártelas»). Es el formato que mejor encaja con la restricción de la IA: nada se mueve salvo las manos y la cara. Arco: escepticismo → lo que noté → la amiga de las de marca → oferta.

### 2. Character Building

Marta, la misma, hablando a cámara todo el rato como si dejara un vídeo a una amiga. Emociones: escepticismo (cejas, labios fruncidos, encogimiento), convencimiento (cabeceo lento), media risa cerrada. Ropa y producto fijos: bata, Rambla blanca/roja siempre en las manos, nunca en los pies.

Localización fija de este vídeo (salón): Salón de un piso español normal: sofá de tela gris claro contra una pared blanca lisa, un cojín beis, mesa baja de madera delante, ventana a la izquierda con luz suave, nada colgado en la pared de detrás.

### 3. Story Refining

Localización: el sofá del salón, como en el anuncio de las sandalias. Un solo encuadre en los cuatro clips: móvil apoyado en la mesa baja de enfrente, plano medio. El par no sale nunca de las manos, así no hay nada que aparezca o desaparezca. La «amiga con las de marca» sustituye a la opinión inventada: es una comparación, no una reseña. No se inventa un 2x1: la oferta es la real (precio, envío, 30 días). Comprobaciones: misma postura y mismo par en los cuatro clips.

Clips: D3.1 Hook: la sincera, con el par en las manos (8 s) · D3.2 Lo que noté el primer día (8 s) · D3.3 La amiga de las de marca (8 s) · D3.4 Oferta y cierre (8 s). Total 32 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa de localización «salón» (prompt al final del archivo).


#### Clip D3.1 · Hook: la sincera, con el par en las manos · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): the living room of an ordinary Spanish flat: a light grey fabric sofa against a plain white wall, one beige cushion, a low wooden coffee table in front, a window to the left giving soft daylight from frame left, nothing on the wall behind the sofa. Same layout in every frame.
Props: the Rambla pair only. Nothing else in frame.

[STAGE 1 | 0–8s | Hook: la sincera, con el par en las manos]
Initial state: From the very first frame: Marta seated on the sofa holding the white Rambla pair in her lap with both hands, one shoe in each hand, toe boxes toward the lens, feet in grey socks flat and still on the floor, looking straight at the lens.
Primary event: She lifts the pair a little toward the lens. Her eyebrows rise, her head tilts, a small skeptical purse of the lips, then a short honest shrug. She keeps the pair up.
End state: Marta seated, pair held up toward the lens.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta, straight to the lens: "Os voy a ser sincera. Cuando las vi pensé: otra zapatilla ancha que promete y luego aprieta igual. Y me he gastado un dineral en plantillas y separadores. Pues mira, me equivoqué."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one living room, one Rambla pair (white with red stripe) held in her hands in every clip, never on her feet; same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D3.2 · Lo que noté el primer día · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): the living room of an ordinary Spanish flat: a light grey fabric sofa against a plain white wall, one beige cushion, a low wooden coffee table in front, a window to the left giving soft daylight from frame left, nothing on the wall behind the sofa. Same layout in every frame.
Props: the Rambla pair only. Nothing else in frame.

[STAGE 1 | 0–8s | Lo que noté el primer día]
Initial state: Same framing: Marta seated on the sofa, the pair still in her hands, now one shoe lifted higher in her right hand with the toe box toward the lens.
Primary event: Her left index finger points inside the wide toe box, then traces the flat caramel sole along the side as she turns the shoe to profile. Her face softens: a slow nod, eyes on the shoe, then back to the lens.
End state: The shoe held in side profile, finger on the sole, Marta nodding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip on mesh, then on rubber>
{Marta: "Desde el primer día: los dedos sueltos aquí, sin tacón, la planta apoyada entera. Eso que las plantillas caras me prometían y nunca me dieron."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one living room, one Rambla pair (white with red stripe) held in her hands in every clip, never on her feet; same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D3.3 · La amiga de las de marca · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): the living room of an ordinary Spanish flat: a light grey fabric sofa against a plain white wall, one beige cushion, a low wooden coffee table in front, a window to the left giving soft daylight from frame left, nothing on the wall behind the sofa. Same layout in every frame.
Props: the Rambla pair only. Nothing else in frame.

[STAGE 1 | 0–8s | La amiga de las de marca]
Initial state: Same framing: Marta seated, the pair back in her lap, both toe boxes toward the lens, hands resting on the shoes.
Primary event: She leans a little toward the lens, one hand lifts palm up as if quoting a friend, then drops back onto the shoe. A half-laugh with closed lips, one slow blink.
End state: Marta seated, hands resting on the pair, half-smile holding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Una amiga que lleva unas barefoot de marca, de esas de ciento cincuenta euros, me las cogió y me dijo: pero si hacen lo mismo. Y yo, que he probado de todo, le doy la razón."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one living room, one Rambla pair (white with red stripe) held in her hands in every clip, never on her feet; same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D3.4 · Oferta y cierre · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): the living room of an ordinary Spanish flat: a light grey fabric sofa against a plain white wall, one beige cushion, a low wooden coffee table in front, a window to the left giving soft daylight from frame left, nothing on the wall behind the sofa. Same layout in every frame.
Props: the Rambla pair only. Nothing else in frame.

[STAGE 1 | 0–8s | Oferta y cierre]
Initial state: Same framing: Marta seated, the pair in her lap, toe boxes to the lens.
Primary event: She counts three things on her fingers, then points down at the bottom of the frame and holds it with a small nod and a closed-lip smile.
End state: Marta seated, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the coffee table at Marta's chest height, medium shot of Marta seated in the middle of the sofa, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Cuarenta y nueve con noventa y cinco, envío a casa, y si no te van las devuelves sin líos, treinta días. Hazme caso y pruébalas, que no te las vas a querer quitar. Aquí abajo."}
<a quiet flat, a television murmuring far away>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one living room, one Rambla pair (white with red stripe) held in her hands in every clip, never on her feet; same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## D4 · «Esto o esto» (Javi) · 4 clips · 30 s · gym · formato comparación en mano desde el segundo 0

### 1. Story Building

Formato replicado: comparación en mano desde el segundo 0 (la de dedos en una mano, la Rambla en la otra), como los hooks de «esto o esto» que abren con los dos objetos ya en plano. Arco: las dos en la mano → por dentro es barefoot → puestas → oferta.

### 2. Character Building

Javi, el mismo, humor seco. Emociones: asco leve a la de dedos, sonrisa cerrada a la Rambla, media sonrisa de lado al final. Ropa fija y Rambla negra/blanca.

Localización fija de este vídeo (gym): Rincón de un gimnasio de barrio: banco plano acolchado negro contra una pared gris clara lisa, suelo de losetas de caucho negro, un soporte de mancuernas desenfocado a la derecha, luz cenital uniforme con relleno de ventana desde la izquierda.

### 3. Story Refining

Localización: banco del gym, sentado, y es el único vídeo donde Javi va con camiseta y pantalón corto de entrenar (justifica el «voy al gym con ellas»). Desaparece la caja y la revelación: el mentor pide que el problema y el producto se entiendan en el primer segundo, así que las dos zapatillas están ya en las manos en el fotograma 1. Se quita andar por la acera. Comprobaciones: la de dedos nunca se suelta ni se tira, solo baja de altura; la Rambla en la mano en los clips 1 y 2 y puesta en los clips 3 y 4.

Clips: D4.1 Hook visual: la de dedos y la Rambla, una en cada mano (6 s) · D4.2 Por dentro es barefoot (8 s) · D4.3 Puestas (8 s) · D4.4 Oferta y cierre (8 s). Total 30 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa de localización «gym» (prompt al final del archivo).


#### Clip D4.1 · Hook visual: la de dedos y la Rambla, una en cada mano · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing plain dark grey cotton t-shirt, black training shorts to the knee, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): a corner of a plain neighbourhood gym: a black padded flat bench against a plain light grey wall, black rubber floor tiles, one dumbbell rack out of focus far to the right, cool even overhead light with a soft window from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | Hook visual: la de dedos y la Rambla, una en cada mano]
Initial state: From the very first frame: Javi seated on the flat bench holding the dull-grey five-toe shoe in his left hand and the black Rambla in his right hand, side by side at chest height, both lateral sides to the lens, the plain grey wall behind him.
Primary event: He lifts the five-toe shoe a little: his nose wrinkles, his eyes squint, his head recoils. Then he lifts the Rambla a little higher: his eyebrows rise, a closed-lip smile. Both shoes stay in his hands the whole time.
End state: Both shoes still in his hands, the Rambla held a little higher.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the rubber floor at Javi's chest height, medium shot of Javi seated on the flat bench facing the lens, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi, deadpan, no intro: "Barefoot con dedos, o barefoot que parece una zapatilla normal. Las dos hacen lo mismo. Con una vas a por el pan, con la otra no."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one gym corner, one five-toe prop shoe, one Rambla pair (black with white stripe); same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D4.2 · Por dentro es barefoot · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing plain dark grey cotton t-shirt, black training shorts to the knee, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): a corner of a plain neighbourhood gym: a black padded flat bench against a plain light grey wall, black rubber floor tiles, one dumbbell rack out of focus far to the right, cool even overhead light with a soft window from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Por dentro es barefoot]
Initial state: Close on Javi's hands at chest height: the five-toe shoe lower in his left hand, the black Rambla in his right hand with the wide toe box toward the lens, the plain grey wall behind.
Primary event: His thumb slides across the wide rounded toe box of the Rambla, then he turns it to strict side profile so the flat caramel sole reads as one even line, taps the flat heel twice, and holds.
End state: The Rambla in side profile, thumb on the heel, the five-toe shoe lower in the other hand.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds, the plain grey wall behind; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a thumb brushing mesh, two soft taps on rubber>
{Javi: "Puntera ancha, suela plana, cero tacón, de malla. Lo mismo que la de dedos. Pero con vaqueros, con el pantalón del curro, con lo que sea."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one gym corner, one five-toe prop shoe, one Rambla pair (black with white stripe); same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D4.3 · Puestas · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing plain dark grey cotton t-shirt, black training shorts to the knee, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): a corner of a plain neighbourhood gym: a black padded flat bench against a plain light grey wall, black rubber floor tiles, one dumbbell rack out of focus far to the right, cool even overhead light with a soft window from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Puestas]
Initial state: Javi seated on the flat bench wearing the black Rambla pair, both feet flat and still on the rubber floor in the lower part of the frame, elbows on his knees, nothing in his hands, the plain grey wall behind him.
Primary event: He points down at his feet, holds it, then opens both hands palms up and looks at the lens with the slow smirk: eyelids lower, one corner of the mouth pulls up, one small nod.
End state: Javi seated, Rambla on, hands open palms up, smirk holding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the rubber floor at Javi's chest height, medium shot of Javi seated on the flat bench facing the lens, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a weight plate set down far away, the hum of a fan>
{Javi: "Las llevo al curro, a la calle y al gym. Y no parecen de viejo ni de friki."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one gym corner, one five-toe prop shoe, one Rambla pair (black with white stripe); same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D4.4 · Oferta y cierre · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing plain dark grey cotton t-shirt, black training shorts to the knee, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): a corner of a plain neighbourhood gym: a black padded flat bench against a plain light grey wall, black rubber floor tiles, one dumbbell rack out of focus far to the right, cool even overhead light with a soft window from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Oferta y cierre]
Initial state: Same framing: Javi seated, Rambla on, feet flat and still, hands on his knees.
Primary event: He holds up three fingers one after another as he counts, then points down at the bottom of the frame with the closed-lip smile.
End state: Javi seated, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the rubber floor at Javi's chest height, medium shot of Javi seated on the flat bench facing the lens, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Cuarenta y nueve con noventa y cinco, del treinta y seis al cuarenta y nueve, treinta días para devolverlas. Aquí abajo."}
<a distant treadmill, the hum of a fan>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one gym corner, one five-toe prop shoe, one Rambla pair (black with white stripe); same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## D5 · «Ayúdame a elegir» (Javi) · 2 clips · 14 s · calle · formato engagement con los colores en la mano

### 1. Story Building

Formato replicado: el de «ayúdame a elegir entre tres colores» (13 segundos, engagement, comentarios). Sirve para enseñar los pares/colores como Carlos quería, y para bajar el coste del anuncio con comentarios. Arco: tres colores en la mano → pregunta → link.

### 2. Character Building

Javi, el mismo, tono de pregunta abierta, cejas arriba, manos abiertas. Ropa fija. Aquí el producto fijo se rompe a propósito: tres colores, uno de cada, y se adjuntan tres fotos del proveedor (Image 2 negra, Image 4 blanca, Image 5 roja).

Localización fija de este vídeo (calle): Banco público de madera con patas de hierro verde oscuro en una acera de granito de un barrio español, pared enfoscada color crema detrás, tronco de plátano a la izquierda, sombra abierta de mañana con luz suave desde la izquierda.

### 3. Story Refining

Localización: un banco de la calle, con los tres colores alineados en el asiento. Es el único ángulo donde hay objetos que se cogen y se dejan: se limita a tres zapatillas alineadas en el escalón, se cogen de una en una y se dejan exactamente donde estaban, y todo está en plano desde el primer fotograma. Si aun así la IA falla, versión de respaldo: las tres siempre en el escalón y Javi solo señala cada una con el dedo. Comprobaciones: exactamente tres zapatillas, mismo sitio en los dos clips.

Clips: D5.1 Hook: los tres colores en la mano (7 s) · D5.2 Pregunta y cierre (7 s). Total 14 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa de localización «calle» (prompt al final del archivo). Image 4 = foto del proveedor Blanco/Rojo. Image 5 = foto del proveedor Rojo.


#### Clip D5.1 · Hook: los tres colores en la mano · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 2 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image4 is the same Rambla sneaker in the white colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Replicate it exactly.
@Image5 is the same Rambla sneaker in the red colorway: red ribbed mesh, red suede-look panels, white stripe, caramel sole. Replicate it exactly.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): a wooden public bench with dark green cast-iron legs on a granite pavement in a Spanish neighbourhood street, a plain cream rendered wall behind it, a plane tree trunk to the left, morning open shade with soft light from frame left. Same layout in every frame.
Props: three Rambla shoes, one of each colorway, all with the same caramel sole: black with white stripe (@Image2), white with red stripe (@Image4), red mesh with white stripe (@Image5). Only these three shoes and Javi are in frame.

[STAGE 1 | 0–7s | Hook: los tres colores en la mano]
Initial state: From the very first frame: Javi seated on the public bench, the three Rambla shoes lined up on the bench seat beside him lateral sides to the lens, black, white and red, and he is already holding the black one up in his right hand at chest height, the cream wall behind him.
Primary event: He shows the black one, sets it back exactly where it was, lifts the white one, shows it, sets it back, lifts the red one, shows it, and keeps it up. Eyebrows up, an open, asking expression.
End state: Javi holding the red shoe up, the black and white ones back on the bench beside him.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the pavement at Javi's chest height, medium shot of Javi seated in the middle of the public bench facing the lens, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi, direct: "Ayúdame a elegir. Misma zapatilla, puntera ancha, tres colores: negra, blanca o roja. ¿Tú cuál cogerías?"}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one public bench, exactly three shoes of three colors, the same three in both clips; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D5.2 · Pregunta y cierre · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 2 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image4 is the same Rambla sneaker in the white colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Replicate it exactly.
@Image5 is the same Rambla sneaker in the red colorway: red ribbed mesh, red suede-look panels, white stripe, caramel sole. Replicate it exactly.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): a wooden public bench with dark green cast-iron legs on a granite pavement in a Spanish neighbourhood street, a plain cream rendered wall behind it, a plane tree trunk to the left, morning open shade with soft light from frame left. Same layout in every frame.
Props: three Rambla shoes, one of each colorway, all with the same caramel sole: black with white stripe (@Image2), white with red stripe (@Image4), red mesh with white stripe (@Image5). Only these three shoes and Javi are in frame.

[STAGE 1 | 0–7s | Pregunta y cierre]
Initial state: Same framing: Javi seated with the red shoe still in his right hand, the black and white ones on the bench beside him.
Primary event: He sets the red one back beside the others, opens both hands palms up toward the lens, and points down at the bottom of the frame with a half-smile.
End state: The three shoes lined up on the bench, Javi pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the pavement at Javi's chest height, medium shot of Javi seated in the middle of the public bench facing the lens, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi: "Y si te gustan las tres, también me vale. Dímelo en los comentarios. Las tallas y los colores están aquí abajo."}
<a bird, a moped far away>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one public bench, exactly three shoes of three colors, the same three in both clips; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## D6 · «Me paso el día vendiendo plantillas» (Marta) · 4 clips · 30 s · farmacia · formato proximidad al problema (variante del formato tendero)

### 1. Story Building

Formato replicado: el del tendero, pero con la proximidad al problema que Marta sí tiene de verdad: en la farmacia vende plantillas y separadores a diario. Es la versión honesta de «atiendo a cincuenta al día»: no da cifras, enseña los productos que vende. Arco: los parches en la mano → el problema no es el pie → puestas en el turno → oferta.

### 2. Character Building

Marta, la misma, con la bata; aquí habla como profesional cercana, no como paciente. Emociones: cansancio leve con media sonrisa al principio, cabeceo lento después. Ropa fija y Rambla blanca/roja.

Localización fija de este vídeo (farmacia): Detrás del mostrador de una farmacia pequeña: mostrador blanco limpio en primer término, estanterías blancas con pocas cajas blancas ordenadas y desenfocadas detrás, reflejo tenue de la cruz verde en la pared izquierda, luz blanca uniforme con relleno de día desde la izquierda.

### 3. Story Refining

Localización: detrás del mostrador de la farmacia, de pie, con la bata por fin en su sitio; el mostrador limpio y las estanterías desenfocadas para que la IA no cambie las cajas entre clips. Aquí la Rambla no se ve puesta (el mostrador tapa los pies): va en la mano en los clips 2, 3 y 4. Los apósitos y la plantilla son genéricos y sin marca, y aparecen en el fotograma 1 para que el hook sea visual. Se evita decir «cura» o «corrige»: se dice «la mayoría de eso sobra», que es opinión. Comprobaciones: la plantilla y la caja se quedan en el regazo o en el banco, nunca desaparecen; Rambla en la mano en el clip 2 y puesta en los clips 3 y 4.

Clips: D6.1 Hook visual: la plantilla y el separador en la mano (7 s) · D6.2 El problema no es el pie (8 s) · D6.3 Puestas en el turno (8 s) · D6.4 Oferta y cierre (7 s). Total 30 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa de localización «farmacia» (prompt al final del archivo).


#### Clip D6.1 · Hook visual: la plantilla y el separador en la mano · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): behind the counter of a small Spanish pharmacy: a clean white counter in the foreground, plain white shelves with a few tidy white boxes out of focus behind, a green cross glow reflected faintly on the left wall, even cool white light with a soft daylight fill from frame left. Same layout in every frame.
Props: one plain white cardboard box of gel toe separators with no brand, one plain unbranded gel insole, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–7s | Hook visual: la plantilla y el separador en la mano]
Initial state: From the very first frame: Marta standing behind the pharmacy counter in her tunic holding an unbranded gel insole in her left hand and a small plain white box of toe separators in her right hand, both toward the lens, the white counter edge in the lower frame.
Primary event: She lifts both a little, then sets them down on the counter in front of her with a small tired shake of the head and a closed-lip half-smile.
End state: Marta standing, insole and box resting on the counter in front of her.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the counter at Marta's chest height, medium shot of Marta standing behind the counter facing the lens, the counter edge in the lower frame, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta, direct: "En la farmacia me paso el día vendiendo esto. Plantillas, separadores, parches. A gente con el mismo problema que yo tenía: los dedos apretados."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one pharmacy counter, one insole, one small box, one Rambla pair (white with red stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D6.2 · El problema no es el pie · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): behind the counter of a small Spanish pharmacy: a clean white counter in the foreground, plain white shelves with a few tidy white boxes out of focus behind, a green cross glow reflected faintly on the left wall, even cool white light with a soft daylight fill from frame left. Same layout in every frame.
Props: one plain white cardboard box of gel toe separators with no brand, one plain unbranded gel insole, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | El problema no es el pie]
Initial state: Close on Marta's hands at chest height: one white Rambla in her right hand with the wide toe box toward the lens, the insole and the box resting on the counter below, shelves out of focus behind.
Primary event: Her left index finger points inside the wide toe box, then she turns the shoe to strict side profile and runs the finger along the flat caramel sole, taps the flat heel, and holds.
End state: The Rambla in side profile, finger on the heel.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at counter height, close on Marta's hands and the shoe she holds over the white counter, shelves out of focus behind; natural micro-sway only, no travel, no tilt. Her face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip on mesh, then on rubber>
{Marta: "Y casi nunca es el pie. Es la puntera en punta. Con la puntera con la forma del pie y la suela plana, la mayoría de eso sobra."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one pharmacy counter, one insole, one small box, one Rambla pair (white with red stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D6.3 · Puestas en el turno · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): behind the counter of a small Spanish pharmacy: a clean white counter in the foreground, plain white shelves with a few tidy white boxes out of focus behind, a green cross glow reflected faintly on the left wall, even cool white light with a soft daylight fill from frame left. Same layout in every frame.
Props: one plain white cardboard box of gel toe separators with no brand, one plain unbranded gel insole, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Puestas en el turno]
Initial state: Marta standing behind the counter holding one white Rambla up in her right hand at chest height, lateral side to the lens, the insole and the box on the counter in front of her, her other hand resting on the counter.
Primary event: She taps the shoe in her hand once, then points at the insole and box on the counter with a small dismissive wave, then looks back at the lens with a slow nod.
End state: Marta standing, shoe held up, nodding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the counter at Marta's chest height, medium shot of Marta standing behind the counter facing the lens, the counter edge in the lower frame, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a pharmacy door chime far away>
{Marta: "Yo llevo estas en el turno, ocho horas de pie, sin plantilla y sin separadores. Y por fuera, una retro normal."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one pharmacy counter, one insole, one small box, one Rambla pair (white with red stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip D6.4 · Oferta y cierre · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every clip of this video, matches @Image3): behind the counter of a small Spanish pharmacy: a clean white counter in the foreground, plain white shelves with a few tidy white boxes out of focus behind, a green cross glow reflected faintly on the left wall, even cool white light with a soft daylight fill from frame left. Same layout in every frame.
Props: one plain white cardboard box of gel toe separators with no brand, one plain unbranded gel insole, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–7s | Oferta y cierre]
Initial state: Same framing: Marta standing behind the counter, the white Rambla still held up in her right hand, the insole and box on the counter.
Primary event: She counts three things on her fingers, then points down at the bottom of the frame with a closed-lip smile.
End state: Marta standing, shoe in hand, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the customer side of the counter at Marta's chest height, medium shot of Marta standing behind the counter facing the lens, the counter edge in the lower frame, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta: "Cuarenta y nueve con noventa y cinco, del treinta y seis al cuarenta y nueve, treinta días para devolverlas. Aquí abajo."}
<a pharmacy door chime far away>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one pharmacy counter, one insole, one small box, one Rambla pair (white with red stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Referencias fijas (se generan una vez y se reutilizan en todos los vídeos)

### Image 3 · Placa de localización · Recibidor (D1)
```
Photorealistic phone photo, vertical 9:16, of an empty entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Camera at chest height looking down the hallway, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Lived-in and clean, nothing styled.
```
### Image 3 · Placa de localización · Portal (D2)
```
Photorealistic phone photo, vertical 9:16, of the empty entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Camera at chest height from the pavement facing the door, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Ordinary and real, nothing styled.
```
### Image 3 · Placa de localización · Salón (D3)
```
Photorealistic phone photo, vertical 9:16, of an empty living room of an ordinary Spanish flat: a light grey fabric sofa against a plain white wall, one beige cushion, a low wooden coffee table in front, a window to the left giving soft daylight from frame left, nothing on the wall behind the sofa. Camera at chest height facing the sofa from the coffee table, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Lived-in and clean, nothing styled.
```
### Image 3 · Placa de localización · Gym (D4)
```
Photorealistic phone photo, vertical 9:16, of an empty corner of a plain neighbourhood gym: a black padded flat bench against a plain light grey wall, black rubber floor tiles, one dumbbell rack out of focus far to the right, cool even overhead light with a soft window from frame left. Camera at chest height facing the bench from the floor, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Ordinary and real, nothing styled.
```
### Image 3 · Placa de localización · Calle (D5)
```
Photorealistic phone photo, vertical 9:16, of an empty wooden public bench with dark green cast-iron legs on a granite pavement in a Spanish neighbourhood street, a plain cream rendered wall behind it, a plane tree trunk to the left, morning open shade with soft light from frame left. Camera at chest height facing the bench from the pavement, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Ordinary and real, nothing styled.
```
### Image 3 · Placa de localización · Farmacia (D6)
```
Photorealistic phone photo, vertical 9:16, from the customer side of the counter of a small empty Spanish pharmacy: a clean white counter in the foreground, plain white shelves with a few tidy white boxes out of focus behind, a green cross glow reflected faintly on the left wall, even cool white light with a soft daylight fill from frame left. Camera at chest height facing the counter, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no brand names, no logos, no readable packaging. Ordinary and real, nothing styled.
```
### Retrato base · Marta
```
Photorealistic phone photo, vertical 4:5, of a Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings, realistic skin with pores, sitting on a low wooden bench with a woven seat in the entrance hallway of a 1980s Spanish flat with speckled grey-and-cream terrazzo floor and a white wall, wearing a white pharmacy tunic half-zipped over a plain grey t-shirt and straight dark blue jeans rolled once at the ankle, white retro sneakers with a red stripe and a caramel sole. Soft window light from frame left, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no retouching. She looks slightly off camera with a tired, warm half-smile. No text, no logos. Original person, not a real individual.
```
### Retrato base · Javi
```
Photorealistic phone photo, vertical 4:5, of a Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands, realistic skin, sitting on the top worn grey stone step of a Spanish apartment building entrance with a dark green wooden door behind him, wearing a navy work polo, dark grey work trousers with the hem above the shoe collar, a cheap digital watch, and black retro sneakers with a white stripe and a caramel sole. Morning open shade with soft light from frame left, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no retouching. He looks slightly off camera, calm, closed-lip half-smile. No text, no logos. Original person, not a real individual.
```
### Image 1 · Hoja de personaje · Marta (adjunta el retrato base como image 1)
```
Use the person from image 1. Keep their identity. Do not recast. Do not beautify. One image, three equal vertical panels, same width, same height, hard even splits, no decorative borders. Same background in every panel: flat seamless studio grey B8B8B8, even light, no gradient, no floor shadow color shift. Panel 1, left: front view, the head is not visible, crop cleanly at the neck, no head, no face, no hair, no neck stump cheat, body only, standing, feet in frame, wardrobe and hands readable: white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, white retro sneakers with a red stripe and caramel sole, same clothes as image 1. Panel 2, middle: full body from the back, head included, same clothes, standing, feet in frame; the bodies in panel 1 and panel 2 have the same height, neck to feet matches, same scale, feet on the same baseline, do not scale one body up or down to fill the panel. Panel 3, right: close-up of the face from the front on the same grey B8B8B8, shoulders in, face sharp, natural skin, not smoothed: Spanish woman, 44, shoulder-length brown hair with a few greys tied back, small silver hoop earrings. Photographed, not illustrated. No logos. No text. No grain overlay.
```
### Image 1 · Hoja de personaje · Javi (adjunta el retrato base como image 1)
```
Use the person from image 1. Keep their identity. Do not recast. Do not beautify. One image, three equal vertical panels, same width, same height, hard even splits, no decorative borders. Same background in every panel: flat seamless studio grey B8B8B8, even light, no gradient, no floor shadow color shift. Panel 1, left: front view, the head is not visible, crop cleanly at the neck, no head, no face, no hair, no neck stump cheat, body only, standing, feet in frame, wardrobe and hands readable: navy work polo, dark grey work trousers with the hem above the shoe collar, cheap digital watch, black retro sneakers with a white stripe and caramel sole, same clothes as image 1. Panel 2, middle: full body from the back, head included, same clothes, standing, feet in frame; the bodies in panel 1 and panel 2 have the same height, neck to feet matches, same scale, feet on the same baseline, do not scale one body up or down to fill the panel. Panel 3, right: close-up of the face from the front on the same grey B8B8B8, shoulders in, face sharp, natural skin, not smoothed: Spanish man, 42, broad build, short dark beard with some grey, short hair. Photographed, not illustrated. No logos. No text. No grain overlay.
```

Image 2 es la foto del proveedor tal cual: Blanco/Rojo para todos los vídeos de Marta, Negro/Blanco para todos los de Javi.
