# Rambla · primer test · 6 ángulos en 4 pasos (Story → Character → Refining → First Draft)

**Regla de continuidad:** entre vídeos no cambia nada de lo fijo. Marta siempre en su recibidor, con su bata, con la Rambla blanca/roja. Javi siempre en su portal, con su polo de trabajo, con la Rambla negra/blanca. Cada clip lleva tres referencias: Image 1 = hoja de personaje, Image 2 = foto del proveedor del color fijo de ese avatar, Image 3 = placa de localización (los prompts para generar las tres están al final del archivo).

**Regla de simplicidad (v2):** todo se rueda con el avatar sentado en su sitio de siempre y la cámara fija. Lo único que se mueve son las manos, la cara y la zapatilla que enseña a cámara. Nadie se pone ni se quita zapatillas, nadie ata cordones, nadie anda, ningún objeto entra ni sale de plano salvo que el prompt lo diga. Cuando la Rambla va puesta, ya está puesta desde el primer fotograma y los pies no se mueven; cuando va en la mano, no va puesta. Cada prompt lleva estas prohibiciones en [EXCLUSIONS].

**Cómo se usa:** cada bloque de código es un clip independiente de 10 s o menos. Lo copias entero, adjuntas Image 1, Image 2 e Image 3 y generas. Nada que rellenar. El diálogo va dentro en castellano de España; si prefieres ElevenLabs, generas igual y silencias la pista.


---

## Ángulo 1 · «Descálzate y mira» (Marta) · 5 clips · 38 s

### 1. Story Building

Marta llega a casa y hace lo de siempre: quitarse la zapatilla en la puerta. Esta vez se mira los dedos y ve que se le han quedado en punta. Lo que quiere es que no le duelan los pies; lo que descubre es que el culpable no era su pie sino la puntera de la zapatilla, que lleva años empujándole los dedos. Enseña a cámara la zapatilla de siempre al lado de la Rambla (puntera en punta contra puntera ancha, tacón contra suela plana) y cierra sentada con la Rambla puesta: por primera vez llega a casa y no se las quita. Arco: hábito → hallazgo → culpable → comparación en la mano → nuevo hábito. Una sola emoción: alivio con un poco de «ahora lo entiendo».

### 2. Character Building

Marta, 44, auxiliar de farmacia, pie ancho con juanete leve, lleva años con la costumbre de descalzarse en la puerta. Habla como quien deja un audio a una amiga, bajito y con muletillas. Nunca posa ni mira a cámara más de un segundo. Emociones que se ven en este ángulo: alivio (exhalación grande, hombros que caen, sonrisa temblorosa después) y realización (ojos que se abren, cejas que saltan, cabeceo lento). Ropa fija: bata blanca medio abierta sobre camiseta gris, vaqueros oscuros con una vuelta. Producto fijo: Rambla blanca/roja.

Localización fija de Marta: Recibidor de un piso español de los años 80: suelo de terrazo gris y crema, pared blanca con un interruptor beis, banco bajo de madera con asiento de rejilla contra la pared izquierda, zapatero de madera oscura con un cuenco de llaves encima contra la pared derecha, un espejo pequeño enmarcado sobre el zapatero, una ventana al fondo que da luz suave desde la izquierda, la puerta de la cocina visible al final del pasillo.

### 3. Story Refining

Se corta todo lo que no sea el pie o la zapatilla: sin planos de la farmacia, sin explicar barefoot. El gancho es la zapatilla en la mano con la puntera hacia cámara y los dedos en punta quietos en un plano cenital; nadie se descalza en cámara. La plantilla desaparece (demasiado objeto que mover): la prueba es sostener las dos zapatillas juntas, primero de puntera y luego de perfil. El cierre no es una promesa sino una consecuencia concreta: sentada con la Rambla puesta, sin habérsela quitado. Comprobaciones: Marta siempre sentada en el banco, cámara siempre en el zapatero de enfrente o cenital, la Rambla siempre blanca/roja, ninguna afirmación médica.

Clips: 1.1 El gancho: mira cómo se te quedan los dedos (7 s) · 1.2 Los dedos en punta (7 s) · 1.3 El culpable: la puntera en punta (8 s) · 1.4 La Rambla al lado: puntera ancha, suela plana (8 s) · 1.5 Llego a casa y no me las quito (8 s). Total 38 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa de localización de Marta.


#### Clip 1.1 · El gancho: mira cómo se te quedan los dedos · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Nothing else on the floor.

[STAGE 1 | 0–7s | El gancho: mira cómo se te quedan los dedos]
Initial state: Marta seated on the low bench, feet in grey socks flat on the terrazzo, holding the conventional white sneaker in her right hand at chest height with its pointed toe toward the lens. Nothing else in her hands.
Primary event: She keeps the sneaker still and looks at the lens, tired. Her free hand comes up and her index finger taps the pointed tip of the toe box twice, then points down toward her own feet. Her eyebrows lift slowly and her mouth stays closed.
End state: Marta seated, sneaker still held up toe to the lens, finger pointing down at her socked feet.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a quiet flat, the fridge humming far away>
{Marta, tired, half to herself: "Oye, haz una cosa. Cuando llegues a casa, quítate la zapatilla y mira cómo se te quedan los dedos."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 1.2 · Los dedos en punta · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Nothing else on the floor.

[STAGE 1 | 0–7s | Los dedos en punta]
Initial state: Overhead: Marta's bare feet flat and completely still on the terrazzo in front of the bench, toes squeezed together into a point, the big toe angled inward, a mild natural bunion at the joint, a faint sock line; the conventional white sneaker lying beside the right foot.
Primary event: The feet do not move. Her right hand enters from the top of the frame and her index finger slowly traces the outline of the squeezed toes from the little toe to the big toe, then rests on the bunion. The hand stays there.
End state: Both feet still in the same place, the finger resting on the big-toe joint, the sneaker beside the foot.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot directly overhead, looking straight down at the terrazzo; natural micro-sway only, no travel, no tilt. No face in frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip brushing skin, the tunic sleeve shifting>
{Marta, quieter: "¿Así, apretados, en punta? Pues escúchame un segundo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 1.3 · El culpable: la puntera en punta · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Nothing else on the floor.

[STAGE 1 | 0–8s | El culpable: la puntera en punta]
Initial state: Close on Marta's hands at chest height: she holds the conventional white sneaker with both hands, toe toward the lens, the pointed narrow toe box filling the lower half of the frame; the white hallway wall behind.
Primary event: Her index finger traces the narrow pointed toe box from the laces to the tip, slowly, twice. Then she turns the sneaker so the lens looks straight into the opening and her finger points at how the inside narrows to a point.
End state: The sneaker held with its opening to the lens, finger pointing inside.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on her hands and the shoes she holds; natural micro-sway only, no travel, no tilt. Her face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip sliding along stiff fabric>
{Marta: "Eso no es que tengas el pie raro. Es que la puntera acaba en punta y lleva años empujándote los dedos hacia dentro."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 1.4 · La Rambla al lado: puntera ancha, suela plana · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Nothing else on the floor.

[STAGE 1 | 0–8s | La Rambla al lado: puntera ancha, suela plana]
Initial state: Close on Marta's hands at chest height: the conventional white sneaker in her left hand and one white Rambla in her right hand, held side by side at the same height, both toes toward the lens, the white wall behind.
Primary event: She holds them still for two seconds so the difference reads: the Rambla's toe box is visibly wider and rounder. Then she turns both shoes at the same time to a strict side profile, soles toward the floor: the Rambla's caramel sole is one flat, even line from heel to toe while the conventional sneaker sits on a thick raised heel wedge. She holds that.
End state: Both shoes in side profile, side by side in her hands, flat caramel sole next to the raised heel.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on her hands and the shoes she holds; natural micro-sway only, no travel, no tilt. Her face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<fabric brushing as the shoes turn>
{Marta, warmer: "Estas tienen la puntera con la forma del pie. Los dedos van sueltos. Y la suela es plana, sin tacón. Mira la diferencia."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 1.5 · Llego a casa y no me las quito · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 5 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: exactly one conventional white sneaker with a narrow pointed toe box and no logo, and the Rambla pair. Nothing else on the floor.

[STAGE 1 | 0–8s | Llego a casa y no me las quito]
Initial state: Marta seated on the low bench wearing the white Rambla pair, both feet flat and still on the terrazzo in the lower part of the frame, hands resting on her knees, the conventional sneaker on the floor to her left.
Primary event: A large visible exhale empties her chest, her eyes close, her raised eyebrows drop to neutral, her shoulders collapse downward; a small, shaky smile appears only after the breath finishes. She glances down at her feet once, then back at the lens.
End state: Marta seated, Rambla on, feet in the same place, small smile holding, hands on her knees.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a long exhale close to the microphone, a kitchen tap dripping once far away>
{Marta, half laughing: "Es la primera vez en años que llego a casa y no me las quito en la puerta. Te las dejo aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one woman, one conventional sneaker, one Rambla pair, one hallway; same clothes and same light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Ángulo 2 · «Las barefoot que no parecen barefoot» (Javi) · 5 clips · 35 s

### 1. Story Building

Javi quería probar barefoot y no lo hizo porque todas parecían zapatillas de dedos. En el portal de su casa enseña esa zapatilla con asco, la suelta, y saca de la caja una Rambla negra que parece una retro de siempre. Con las dos zapatillas en la mano demuestra que por dentro es barefoot (puntera ancha, suela plana sin tacón) y cierra sentado con ellas puestas. Arco: rechazo → sorpresa → comparación en la mano → puestas. Una emoción: sorpresa agradable con humor seco.

### 2. Character Building

Javi, 42, talla 46, pie ancho, práctico, habla poco y con ironía. Se ríe de sí mismo. Emociones visibles en este ángulo: asco medio (nariz arrugada, cabeza que se aparta), asombro suave (ojos que se abren sin tensión, cuerpo que se inclina) y una media sonrisa de satisfacción al final (párpados bajos, comisura). Ropa fija: polo azul marino de trabajo, pantalón gris oscuro con el bajo por encima de la zapatilla, reloj digital barato. Producto fijo: Rambla negra/blanca.

Localización fija de Javi: Portal de un edificio de viviendas español: tres escalones de piedra gris gastados, puerta de madera verde oscuro con el número 14 en latón, pared enfoscada color crema con zócalo de piedra gris, acera de granito delante, una bicicleta negra apoyada en la pared a la derecha, sombra abierta de mañana con luz suave desde la izquierda.

### 3. Story Refining

La zapatilla de dedos es un atrezo genérico sin marca y aparece solo dos segundos: lo justo para el gancho. La comparación con la zapatilla normal del mismo número se hace en la mano, sin pies, en el clip 3. Se quita andar por la acera: los dos últimos clips son Javi sentado con la Rambla ya puesta, pies quietos, y la venta la hacen la cara y la frase. No hay precio ni oferta en este ángulo; vende estética y mecanismo. Comprobaciones: Javi siempre sentado en el escalón de arriba, cámara siempre en la acera a la altura del pecho o en la mano a un palmo de las zapatillas, la bici a la derecha, la puerta verde con el 14 detrás, Rambla negra/blanca en todos.

Clips: 2.1 El gancho: la zapatilla de dedos (6 s) · 2.2 La revelación (7 s) · 2.3 Por dentro es barefoot (8 s) · 2.4 Puestas (7 s) · 2.5 Media sonrisa y cierre (7 s). Total 35 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa de localización de Javi.


#### Clip 2.1 · El gancho: la zapatilla de dedos · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, one plain brown cardboard box, one conventional black sneaker with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | El gancho: la zapatilla de dedos]
Initial state: Javi seated on the top stone step, the closed cardboard box beside him on the step, the five-toe shoe in his right hand held by the heel with two fingers at chest height, the green door behind him.
Primary event: He lifts the five-toe shoe a little toward the lens. His nose wrinkles hard and pulls the upper lip upward, his eyes squint nearly shut, his chin draws in, and his head recoils and turns away. He lowers the shoe slowly onto the step beside him and leaves it there.
End state: Javi seated, hands empty, the five-toe shoe resting on the step beside him, the closed box on his other side.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi, deadpan: "Yo quería probar las barefoot, en serio. Pero es que todas parecían esto."}
<a rubber shoe set down on stone>
{Javi: "Y yo con esto no voy ni a por el pan."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one man, one doorstep, one box, one five-toe prop shoe, one conventional black sneaker and one Rambla pair (black with white stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 2.2 · La revelación · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, one plain brown cardboard box, one conventional black sneaker with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–7s | La revelación]
Initial state: Same framing: Javi seated on the top step with the cardboard box on his knees, lid already open, one black Rambla lifted out and held in both hands at chest height, lateral side to the lens, the five-toe shoe resting on the step beside him.
Primary event: He turns the shoe slowly in his hands so the suede-look toe cap, the white stripe and then the caramel sole read one after another, and holds it lateral side to the lens again. His eyes widen gradually without tension in the brow, his mouth opens little by little, his head tilts, and his body leans forward.
End state: The black Rambla held beside his face, lateral side to the lens, box open on his knees.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<tissue paper rustling in the box>
{Javi, quieter, genuinely pleased: "Hasta que vi estas. Mira. Una retro de las de toda la vida."}
<a distant moped passing on the street>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one man, one doorstep, one box, one five-toe prop shoe, one conventional black sneaker and one Rambla pair (black with white stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 2.3 · Por dentro es barefoot · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, one plain brown cardboard box, one conventional black sneaker with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Por dentro es barefoot]
Initial state: Close on Javi's hands at chest height: the conventional black sneaker in his left hand and the black Rambla in his right hand, side by side at the same height, both toes toward the lens, the green door behind.
Primary event: He holds them still for two seconds: the Rambla's toe box is visibly wider and rounder. Then he turns both shoes at the same time to a strict side profile: the Rambla's caramel sole is one flat, even line from heel to toe; the conventional sneaker sits on a thick raised heel wedge. His thumb taps the flat heel of the Rambla twice.
End state: Both shoes in side profile side by side in his hands, thumb resting on the Rambla's flat heel.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<fabric brushing, two soft thumb taps on rubber>
{Javi: "Pero por dentro es barefoot de verdad: puntera ancha y suela plana, sin tacón. Mira."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one man, one doorstep, one box, one five-toe prop shoe, one conventional black sneaker and one Rambla pair (black with white stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 2.4 · Puestas · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, one plain brown cardboard box, one conventional black sneaker with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–7s | Puestas]
Initial state: Javi seated on the top step wearing the black Rambla pair, both feet flat and still on the lower step in the lower part of the frame, elbows on his knees, hands loose, nothing in his hands, the green door behind him.
Primary event: He points down at his own feet with one hand, holds the point for a second, then opens both hands palms up in a small 'that's it' gesture and looks at the lens.
End state: Javi seated, Rambla on, feet in the same place, hands open palms up.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<keys shifting in a pocket, a shop shutter rolling up somewhere down the street>
{Javi: "Las llevo al curro, a la calle y al gym. Con vaqueros, con el pantalón del trabajo, con lo que sea."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one man, one doorstep, one box, one five-toe prop shoe, one conventional black sneaker and one Rambla pair (black with white stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 2.5 · Media sonrisa y cierre · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 5 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one generic dull-grey five-toe barefoot shoe with no logo, one plain brown cardboard box, one conventional black sneaker with a narrow toe box and no logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–7s | Media sonrisa y cierre]
Initial state: Same framing: Javi seated on the top step wearing the black Rambla pair, feet flat on the lower step, hands on his knees.
Primary event: He glances at the lens: his eyelids lower, one corner of his mouth pulls into a slow smirk, his eyebrows rise once and settle, his chin lifts slightly. He gives one small nod and holds.
End state: Javi seated, smirk holding, feet in the same place.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Javi, half smirk: "Y no parecen de viejo. Te las dejo aquí abajo."}
<a bird, the moped far away>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
Exactly one man, one doorstep, one box, one five-toe prop shoe, one conventional black sneaker and one Rambla pair (black with white stripe); same clothes and light as the reference. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Ángulo 3 · «Si llegas a casa deseando quitártelas» (Marta) · 6 clips · 44 s

### 1. Story Building

Marta entra en casa deseando quitarse las zapatillas, como cada día. En el banco del recibidor cuenta las ocho horas de pie y enseña que el problema no era su pie ancho sino la puntera en punta. Enseña la Rambla al lado de la de siempre y cierra sentada en el mismo banco con la Rambla puesta, sin haberse descalzado. Arco: costumbre → dolor contado → causa en la mano → comparación → puestas → nueva costumbre. Una emoción: reconocimiento que se convierte en alivio.

### 2. Character Building

La misma Marta del ángulo 1, con su bata de farmacia, contando su turno desde casa. Emociones visibles: agotamiento (párpados que caen, parpadeo largo, mandíbula floja), realización (ojos que se abren, cabeceo) y alivio (exhalación, hombros que caen, sonrisa después). Ropa y producto fijos: bata blanca, camiseta gris, vaqueros; Rambla blanca/roja.

Localización fija de Marta: Recibidor de un piso español de los años 80: suelo de terrazo gris y crema, pared blanca con un interruptor beis, banco bajo de madera con asiento de rejilla contra la pared izquierda, zapatero de madera oscura con un cuenco de llaves encima contra la pared derecha, un espejo pequeño enmarcado sobre el zapatero, una ventana al fondo que da luz suave desde la izquierda, la puerta de la cocina visible al final del pasillo.

### 3. Story Refining

La farmacia no se ve: se cuenta desde el banco. Se quitan la entrada por la puerta, la plantilla, ponerse la zapatilla y el paseo hasta la cocina; todo ocurre sentada, y la Rambla va en la mano en el clip 4 y ya puesta desde el primer fotograma en los clips 5 y 6. Se mantiene el pellizco a la malla porque responde a la objeción de sudar en el turno. Comprobaciones: la bolsa del súper está de pie junto a la puerta en todos los planos medios, misma luz de ventana, Rambla blanca/roja.

Clips: 3.1 El gancho: la costumbre de siempre (7 s) · 3.2 Ocho horas de pie (8 s) · 3.3 La causa, en la mano (8 s) · 3.4 La Rambla al lado (9 s) · 3.5 Unas semanas en el turno entero (6 s) · 3.6 Misma puerta, nueva costumbre (6 s). Total 44 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa de localización de Marta.


#### Clip 3.1 · El gancho: la costumbre de siempre · 7 s

```
[GOAL]
One continuous 7-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 6 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one conventional white sneaker pair with a narrow pointed toe box and no logo, a reusable supermarket bag standing on the floor by the front door, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–7s | El gancho: la costumbre de siempre]
Initial state: Marta seated on the low bench just after arriving, wearing the conventional white sneakers, both feet flat and still on the terrazzo, the reusable supermarket bag standing on the floor by the door, her hands resting on her thighs, looking down at her feet.
Primary event: Her eyelids drag downward, a long blink stays closed too long, her head drifts down and lifts again slowly, her jaw hangs slack, and one long breath empties out. She lifts her eyes to the lens without moving anything else.
End state: Marta seated, sneakers still on, feet in the same place, eyes on the lens, the bag by the door.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a quiet flat, the window open at the far end>
{Marta, low: "Si llegas a casa y lo primero que haces es quitarte las zapatillas en la puerta, escúchame un segundo, que a mí me pasaba igual."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, the same tunic in every clip, one conventional sneaker pair and one Rambla pair (white with red stripe); the supermarket bag stays by the door in every clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 3.2 · Ocho horas de pie · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 6 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one conventional white sneaker pair with a narrow pointed toe box and no logo, a reusable supermarket bag standing on the floor by the front door, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Ocho horas de pie]
Initial state: Overhead: Marta's feet in the conventional white sneakers flat and still on the terrazzo in front of the bench, the tunic hem visible at the top of the frame.
Primary event: The feet do not move. Her right hand comes down into frame and rubs the outside of the big-toe joint through the shoe slowly, three times, then the fingertips press the narrow tip of the toe box once. The hand stays resting on the shoe.
End state: Feet in the same place, the hand resting on the right shoe.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot directly overhead, looking straight down at the terrazzo; natural micro-sway only, no travel, no tilt. No face in frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<the tunic fabric rustling, a hand rubbing canvas>
{Marta: "Ocho horas de pie. Y a las cuatro ya notas los dedos apretados de aquí, el gordo rozando, las plantas ardiendo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, the same tunic in every clip, one conventional sneaker pair and one Rambla pair (white with red stripe); the supermarket bag stays by the door in every clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 3.3 · La causa, en la mano · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 6 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one conventional white sneaker pair with a narrow pointed toe box and no logo, a reusable supermarket bag standing on the floor by the front door, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | La causa, en la mano]
Initial state: Close on Marta's hands at chest height: she holds one conventional white sneaker with both hands, toe toward the lens, the pointed narrow toe box filling the lower half of the frame, the white wall behind.
Primary event: Her index finger traces the narrow pointed toe box from the laces to the tip, slowly. Then she turns the sneaker so the lens looks straight into the opening and her finger points at how the inside narrows to a point. She holds it there.
End state: The sneaker held with its opening to the lens, finger pointing inside.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on her hands and the shoes she holds; natural micro-sway only, no travel, no tilt. Her face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip sliding along stiff fabric>
{Marta: "Yo pensaba que era de tener el pie ancho. Pero es que la puntera acababa en punta y el pie no cabía. Ocho horas apretando. Claro que duele."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, the same tunic in every clip, one conventional sneaker pair and one Rambla pair (white with red stripe); the supermarket bag stays by the door in every clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 3.4 · La Rambla al lado · 9 s

```
[GOAL]
One continuous 9-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 6 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one conventional white sneaker pair with a narrow pointed toe box and no logo, a reusable supermarket bag standing on the floor by the front door, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–9s | La Rambla al lado]
Initial state: Close on Marta's hands at chest height: the conventional white sneaker in her left hand and one white Rambla in her right hand, side by side at the same height, both toes toward the lens, the white wall behind.
Primary event: She holds them still for two seconds so the wider, rounder toe box of the Rambla reads. She turns both to a strict side profile: flat caramel sole next to the raised heel wedge. Then she brings the Rambla closer to the lens and pinches the ribbed mesh of the upper between two fingers so it reads as thin and airy.
End state: The Rambla close to the lens, mesh pinched between her fingers, the conventional sneaker still in the other hand.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Marta's chest height, close on her hands and the shoes she holds; natural micro-sway only, no travel, no tilt. Her face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<fabric brushing, mesh pinched>
{Marta, warmer: "Con estas los dedos van sueltos, la suela es plana, sin tacón. Y son de malla, así que en el turno no se te cuecen."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, the same tunic in every clip, one conventional sneaker pair and one Rambla pair (white with red stripe); the supermarket bag stays by the door in every clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 3.5 · Unas semanas en el turno entero · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 5 of 6 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one conventional white sneaker pair with a narrow pointed toe box and no logo, a reusable supermarket bag standing on the floor by the front door, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | Unas semanas en el turno entero]
Initial state: Marta seated on the low bench wearing the white Rambla pair, both feet flat and still on the terrazzo in the lower part of the frame, hands on her knees, the supermarket bag by the door.
Primary event: She looks down at her feet, then at the lens, and gives one slow nod with a closed-lip half-smile. Nothing else moves.
End state: Marta seated, Rambla on, feet in the same place, half-smile holding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<the fridge humming from the kitchen>
{Marta: "Llevo unas semanas con ellas en el turno entero."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, the same tunic in every clip, one conventional sneaker pair and one Rambla pair (white with red stripe); the supermarket bag stays by the door in every clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 3.6 · Misma puerta, nueva costumbre · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 6 of 6 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one conventional white sneaker pair with a narrow pointed toe box and no logo, a reusable supermarket bag standing on the floor by the front door, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | Misma puerta, nueva costumbre]
Initial state: Same framing: Marta seated on the bench wearing the white Rambla pair, feet flat and still, hands on her knees, the bag by the door.
Primary event: A large visible exhale empties her chest, her eyes close, her eyebrows drop to neutral, her shoulders collapse downward; a small, shaky smile appears only after the breath finishes.
End state: Marta seated, shoes on, smiling slightly, still.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a long exhale>
{Marta, half laughing: "Y sí, llego a casa y ni me acuerdo de quitármelas. Te las dejo aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, the same tunic in every clip, one conventional sneaker pair and one Rambla pair (white with red stripe); the supermarket bag stays by the door in every clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Ángulo 4 · «Sí, hay 47, 48 y 49» (Javi) · 5 clips · 38 s

### 1. Story Building

Javi, sentado en el escalón de su portal antes de ir a trabajar, dice que sí hay 47, 48 y 49, y enseña por qué siempre pedía una talla más: no le faltaba largo, le faltaba ancho. Con la zapatilla normal y la Rambla del mismo número en las manos lo demuestra, y cierra sentado con la Rambla puesta y la regla de la talla en centímetros. Arco: afirmación → truco de siempre → ancho contra largo en la mano → suela plana → regla de talla. Una emoción: orgullo tranquilo.

### 2. Character Building

El mismo Javi, con su polo de trabajo y su café. Emociones visibles: orgullo (barbilla arriba, pecho, sonrisa cerrada, parpadeo lento) y una frustración breve al contar lo de la talla de más (ojos cerrados, mandíbula, cabeceo). Ropa fija y Rambla negra/blanca, en una talla que se vea grande.

Localización fija de Javi: Portal de un edificio de viviendas español: tres escalones de piedra gris gastados, puerta de madera verde oscuro con el número 14 en latón, pared enfoscada color crema con zócalo de piedra gris, acera de granito delante, una bicicleta negra apoyada en la pared a la derecha, sombra abierta de mañana con luz suave desde la izquierda.

### 3. Story Refining

La furgoneta y el periódico desaparecen: la escala la dan la mano y la cara de Javi al lado de la zapatilla. La plantilla y ponerse la talla grande se sustituyen por un gesto de dedos (el hueco de medio dedo por delante). Andar al trabajo se quita: el último clip es Javi sentado con la Rambla puesta contando con los dedos. El clip de talla en centímetros va al final porque es la instrucción que evita devoluciones, no el gancho. Comprobaciones: el vaso de café se queda de pie en el escalón, la bici a la derecha, mismo portal, misma luz, ninguna marca en la zapatilla normal.

Clips: 4.1 El gancho: tallas (6 s) · 4.2 El truco de siempre: una talla más (8 s) · 4.3 Era el ancho, no el largo (8 s) · 4.4 Suela plana, sin tacón (8 s) · 4.5 Se elige por centímetros (8 s). Total 38 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa de localización de Javi.


#### Clip 4.1 · El gancho: tallas · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, a paper coffee cup standing on the top step, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | El gancho: tallas]
Initial state: Javi seated on the top stone step, feet planted wide on the lower step, the paper coffee cup standing on the step beside him, one black Rambla held up in his right hand at chest height, lateral side to the lens, so the shoe reads clearly big next to his hand and face, the green door behind him.
Primary event: He keeps the shoe still. His chin lifts, his chest expands, and a closed-lip smile spreads slowly and evenly; his shoulders roll back, followed by one slow, satisfied blink.
End state: The shoe held up beside his face, the closed-lip smile holding.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a bicycle chain ticking as the wheel settles>
{Javi, calm: "Sí. Hay 47, hay 48 y hay 49. Y no, no es una talla grande con la horma de siempre."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the coffee cup stays on the top step; the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 4.2 · El truco de siempre: una talla más · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, a paper coffee cup standing on the top step, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | El truco de siempre: una talla más]
Initial state: Same framing: Javi seated on the top step holding the conventional black sneaker in his left hand at chest height, toe toward the lens, the coffee cup on the step beside him.
Primary event: His right index finger taps the narrow toe box of the conventional sneaker, then his thumb and index finger open a gap of about two centimetres in front of the toe to show the wasted length. His eyes clamp shut, his jaw slides from side to side, a sharp breath pushes through his nose, and his head shakes once.
End state: The conventional sneaker still held up, the finger gap held in front of its toe, Javi's head just after the shake.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip tapping stiff fabric>
{Javi: "Yo llevaba años pidiendo una talla más para que no me apretaran de ancho. Y me sobraba medio dedo por delante."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the coffee cup stays on the top step; the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 4.3 · Era el ancho, no el largo · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, a paper coffee cup standing on the top step, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Era el ancho, no el largo]
Initial state: Close on Javi's hands at chest height: the conventional black sneaker in his left hand and the black Rambla in his right hand, side by side at the same height, both toes toward the lens, same nominal size, the green door behind.
Primary event: He holds them still: the difference in toe-box width reads without explanation. His right thumb slides across the wide rounded toe box of the Rambla once, then his left thumb across the narrow one. He holds them still again.
End state: Both shoes still side by side, toes to the lens.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a thumb brushing mesh, then stiff fabric>
{Javi: "El problema no era el largo. Era el ancho. Mira la puntera de una y la de otra, mismo número."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the coffee cup stays on the top step; the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 4.4 · Suela plana, sin tacón · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, a paper coffee cup standing on the top step, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Suela plana, sin tacón]
Initial state: Close on Javi's hands at chest height: the same two shoes now held in strict side profile side by side, soles toward the floor, the caramel sole of the Rambla one flat, even line while the conventional sneaker sits on a thick raised heel wedge.
Primary event: He holds them still for two seconds. His thumb taps the flat heel of the Rambla twice, then taps the tall heel wedge of the conventional sneaker once. He holds them still again.
End state: Both shoes still in side profile, thumb resting on the conventional heel wedge.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<three soft thumb taps on rubber>
{Javi: "Puntera ancha de verdad y suela plana, sin tacón. Y una retro normal, que te la pones con vaqueros y ya."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the coffee cup stays on the top step; the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 4.5 · Se elige por centímetros · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 5 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole, a visibly large size. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: one conventional black sneaker of the same nominal size with a narrow toe box and no logo, a paper coffee cup standing on the top step, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Se elige por centímetros]
Initial state: Javi seated on the top step wearing the black Rambla pair, both feet flat and still on the lower step in the lower part of the frame, the coffee cup on the step beside him, hands loose on his knees, the green door behind him.
Primary event: He points down at his feet once, then holds up three fingers one after another as he counts, then looks at the lens with the closed-lip smile and points down at the bottom of the frame.
End state: Javi seated, Rambla on, feet in the same place, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a moped far away>
{Javi: "Eso sí: en estas se elige por centímetros, no por tu número. Mide el pie, mira la tabla, y si no aciertas te la cambian gratis. Aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one conventional black sneaker, one Rambla pair (black with white stripe); the coffee cup stays on the top step; the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Ángulo 6 · «150 € por unas barefoot. Ya.» (Javi) · 5 clips · 38 s

### 1. Story Building

Javi enseña en el móvil unas barefoot de marca a 149,95 € y explica, contando con los dedos sobre la Rambla, las tres cosas que hacen barefoot a una zapatilla. Las suyas hacen lo mismo sin cobrar el logo. Reconoce lo que no son (de piel, para la obra) y cierra sentado con la Rambla puesta, la cara de decisión y la garantía de 30 días. Arco: precio → mecanismo → igualdad → honestidad → decisión. Una emoción: «no soy tonto».

### 2. Character Building

El mismo Javi, mismo polo de trabajo, en el portal. Emociones visibles: sospecha (barbilla baja, ceja alta, mirada de lado), concesión honesta (cabeza que niega suave, manos abiertas) y determinación (respiración, mandíbula, hombros atrás, un cabeceo). Ropa fija y Rambla negra/blanca.

Localización fija de Javi: Portal de un edificio de viviendas español: tres escalones de piedra gris gastados, puerta de madera verde oscuro con el número 14 en latón, pared enfoscada color crema con zócalo de piedra gris, acera de granito delante, una bicicleta negra apoyada en la pared a la derecha, sombra abierta de mañana con luz suave desde la izquierda.

### 3. Story Refining

El gimnasio y la sentadilla desaparecen: la decisión se ve en la cara (respiración, mandíbula, hombros, un cabeceo), sentado. El listado del móvil no tiene marca y el móvil se queda boca abajo en el escalón después del clip 1. El anclaje es contra 150 €, nunca contra las de 40 €. La concesión de la malla y de la obra se queda porque es lo que sube la credibilidad. Comprobaciones: la Rambla va en la mano en los clips 2, 3 y 4 y puesta desde el primer fotograma en el clip 5, mismo portal, misma bici, misma luz.

Clips: 6.1 El gancho: el precio (6 s) · 6.2 Qué es barefoot de verdad (8 s) · 6.3 Lo mismo, sin logo (8 s) · 6.4 Lo que no son (8 s) · 6.5 Decisión (8 s). Total 38 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Javi. Image 2 = foto del proveedor de Rambla Negro/Blanco. Image 3 = placa de localización de Javi.


#### Clip 6.1 · El gancho: el precio · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 1 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: Javi's own phone showing a generic online shoe listing with the price 149,95 € and no brand name or logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | El gancho: el precio]
Initial state: Javi seated on the top stone step holding his own phone toward the lens at chest height, the screen showing a shoe listing with the price 149,95 € and no brand, the green door behind him.
Primary event: The listing fills part of the frame for two seconds. He lowers the phone onto his knee, screen down: his chin drops while his eyes stay lifted, one eyebrow rises higher, his head turns slightly so the gaze lands sideways, and his mouth tightens at one corner. The stare holds.
End state: Javi looking sideways at the lens, the phone resting screen down on his knee.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a moped passing, a bicycle bell far away>
{Javi: "Unas barefoot de marca: ciento cincuenta euros. Por una zapatilla de malla con suela plana. Ya."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one phone, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 6.2 · Qué es barefoot de verdad · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: Javi's own phone showing a generic online shoe listing with the price 149,95 € and no brand name or logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Qué es barefoot de verdad]
Initial state: Same framing: Javi seated on the top step holding the black Rambla in his left hand at chest height, lateral side to the lens, his right hand free, the phone resting screen down on the step beside him.
Primary event: He counts on the shoe with his right hand: taps the wide toe box once, then turns the shoe to a strict side profile and runs his finger along the flat caramel sole from heel to toe, then taps the flat heel. He holds the profile still to the lens.
End state: The shoe held still in flat side profile, finger on the heel.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<fingers tapping the shoe>
{Javi: "Lo que hace que una barefoot sea barefoot son tres cosas: puntera ancha, suela plana y cero tacón. Esto. Lo demás es el logo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one phone, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 6.3 · Lo mismo, sin logo · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 3 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: Javi's own phone showing a generic online shoe listing with the price 149,95 € and no brand name or logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Lo mismo, sin logo]
Initial state: Close on Javi's hands at chest height: the black Rambla held in both hands, lateral side square to the lens, the white stripe and the plain panel with no logo filling the frame, the green door behind.
Primary event: His index finger slides slowly across the plain lateral panel where a logo would be, then taps the white stripe once. He turns the shoe slightly toward the lens so the wide toe box reads, and holds it still.
End state: The shoe held still, toe box angled to the lens.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot, at arm's length, at Javi's chest height, close on his hands and the shoes he holds; natural micro-sway only, no travel, no tilt. His face stays out of frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip sliding on suede-look fabric>
{Javi: "Estas hacen lo mismo. Y no te cobran la marca. Cuarenta y nueve con noventa y cinco, del 36 al 49."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one phone, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 6.4 · Lo que no son · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: Javi's own phone showing a generic online shoe listing with the price 149,95 € and no brand name or logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Lo que no son]
Initial state: Same medium framing: Javi seated on the top step holding the black Rambla in his left hand at chest height, the phone on the step beside him.
Primary event: He pinches the ribbed mesh of the upper between two fingers, then taps the thin sole with his knuckle, shaking his head slightly and opening his free hand palm up: a small honest concession, no drama.
End state: Javi seated, shoe held up, free hand open palm up.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<mesh pinched, a knuckle tapping rubber>
{Javi: "¿Son de piel? No, son de malla, y en invierno pides la bota. ¿Para la obra? Tampoco. Para el día a día, van de sobra."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one phone, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 6.5 · Decisión · 8 s

```
[GOAL]
One continuous 8-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 5 of 5 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Javi's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: black ribbed mesh, black suede-look panels, white stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Javi: Spanish man, 42, broad build, short dark beard with some grey, short hair, big hands; wearing navy work polo, dark grey work trousers with the hem sitting above the shoe collar, a cheap digital watch, plain black socks. Appearance and clothing never change between clips.
Location (fixed for every Javi video, matches @Image3): the entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Same layout in every frame.
Props: Javi's own phone showing a generic online shoe listing with the price 149,95 € and no brand name or logo, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Decisión]
Initial state: Javi seated on the top step wearing the black Rambla pair, both feet flat and still on the lower step in the lower part of the frame, hands on his knees, the phone on the step beside him, the green door behind him.
Primary event: His eyes lift and lock on the lens, a deep breath expands his chest, his jaw sets visibly at the hinge, his shoulders roll back, and one sharp nod completes the change. He points down at the bottom of the frame.
End state: Javi seated, Rambla on, feet in the same place, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the granite pavement at Javi's chest height, medium shot of Javi seated on the top stone step, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a breath in>
{Javi: "Yo entreno con ellas y voy al curro con ellas. Y si no te convencen, treinta días y te devuelven el dinero. Aquí abajo."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One man, one building entrance, one phone, one Rambla pair (black with white stripe); the bicycle stays against the wall; same light throughout. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Ángulo 11 · «Mide el pie» (Marta) · 4 clips · 30 s

### 1. Story Building

Marta, en el suelo del recibidor junto al banco, enseña cómo medir el pie con un folio contra la pared y cómo elegir la talla en una zapatilla que talla pequeño: 27 cm es una 44. Explica el método con el folio en la mano, enseña la cinta en el suelo, y si no aciertas te la cambian. Arco: dato → método → regla → red. Sin emoción dramática: tranquilidad y un encogimiento de hombros al final.

### 2. Character Building

La misma Marta, misma bata, en calcetines en el recibidor. Una sola expresión: sonrisa cerrada y parpadeo lento al final. Ropa fija y Rambla blanca/roja.

Localización fija de Marta: Recibidor de un piso español de los años 80: suelo de terrazo gris y crema, pared blanca con un interruptor beis, banco bajo de madera con asiento de rejilla contra la pared izquierda, zapatero de madera oscura con un cuenco de llaves encima contra la pared derecha, un espejo pequeño enmarcado sobre el zapatero, una ventana al fondo que da luz suave desde la izquierda, la puerta de la cocina visible al final del pasillo.

### 3. Story Refining

No vende: quita la duda de talla y evita devoluciones, por eso no lleva mecanismo ni promesa. No se mide el pie en cámara (demasiada acción de pie y de objetos): el folio ya tiene la marca hecha y la cinta ya está puesta marcando 27 cm; Marta solo señala y lo explica con el folio en la mano. Un único número en toda la pieza (27 cm = 44) para que la cinta no cambie entre clips. Comprobaciones: folio, boli y cinta en el mismo sitio en los dos planos cenitales, misma luz, Rambla blanca/roja.

Clips: 11.1 El gancho: 27 cm es una 44 (6 s) · 11.2 Cómo medir (10 s) · 11.3 Entre dos, la grande (8 s) · 11.4 Si no aciertas, te la cambian (6 s). Total 30 s.

### 4. First Draft (prompts listos)

Image 1 = hoja de personaje de Marta. Image 2 = foto del proveedor de Rambla Blanco/Rojo. Image 3 = placa de localización de Marta.


#### Clip 11.1 · El gancho: 27 cm es una 44 · 6 s

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
Props: one white A4 sheet of paper with a single short blue pen mark on it, one blue pen, one yellow tape measure, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | El gancho: 27 cm es una 44]
Initial state: Overhead on the terrazzo next to the bench: the white A4 sheet lying with one short edge against the white wall, a short blue pen mark near the far edge, the yellow tape measure lying flat on the sheet from the wall to the mark reading 27 cm, the blue pen beside the sheet, one white Rambla lying beside it. Nothing moves.
Primary event: Marta's right hand enters from the bottom of the frame and her index finger taps the tape at the 27 mark twice, then taps the toe of the shoe once. The hand stays resting on the shoe.
End state: Everything in the same place, the finger resting on the shoe.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot directly overhead, looking straight down at the terrazzo; natural micro-sway only, no travel, no tilt. No face in frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip tapping paper, then tapping mesh>
{Marta: "Antes de pedirlas, esto: en estas un pie de veintisiete centímetros es una cuarenta y cuatro. No una cuarenta y dos."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, one sheet, one pen, one tape measure, one Rambla pair (white with red stripe); the sheet, pen and tape keep their exact place on the terrazzo in every overhead clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 11.2 · Cómo medir · 10 s

```
[GOAL]
One continuous 10-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 2 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one white A4 sheet of paper with a single short blue pen mark on it, one blue pen, one yellow tape measure, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–10s | Cómo medir]
Initial state: Marta seated on the low bench, feet in grey socks flat and still on the terrazzo, holding the white A4 sheet up with both hands at chest height, the blue pen mark visible, the white wall behind her.
Primary event: She explains with the sheet: taps the short edge of the sheet with one finger, then taps the pen mark, then draws her finger slowly from the edge to the mark. She lowers the sheet to her lap and looks at the lens with a small nod.
End state: Marta seated, the sheet flat on her lap, looking at the lens.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<paper flexing in her hands>
{Marta: "Folio contra la pared. Talón pegado a la pared. Marcas donde acaba el dedo más largo. Y mides desde el borde hasta la marca. Ya está, ese es tu pie."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, one sheet, one pen, one tape measure, one Rambla pair (white with red stripe); the sheet, pen and tape keep their exact place on the terrazzo in every overhead clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 11.3 · Entre dos, la grande · 8 s

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
Props: one white A4 sheet of paper with a single short blue pen mark on it, one blue pen, one yellow tape measure, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–8s | Entre dos, la grande]
Initial state: Overhead on the terrazzo next to the bench: the same A4 sheet against the wall, the tape reading 27 cm from the wall to the mark, the pen beside the sheet, the white Rambla lying beside it. Nothing moves.
Primary event: Marta's hand enters from the bottom and her thumb and index finger open a gap of about one centimetre just past the tip of the shoe's toe box, hold it, then the finger taps the toe box once.
End state: Everything in the same place, the finger resting on the toe box.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Handheld from one fixed spot directly overhead, looking straight down at the terrazzo; natural micro-sway only, no travel, no tilt. No face in frame. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
<a fingertip tapping mesh>
{Marta: "Y si te sale entre dos tallas, la grande. Siempre. Que el dedo tenga un poco de sitio por delante."}
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, one sheet, one pen, one tape measure, one Rambla pair (white with red stripe); the sheet, pen and tape keep their exact place on the terrazzo in every overhead clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

#### Clip 11.4 · Si no aciertas, te la cambian · 6 s

```
[GOAL]
One continuous 6-second clip, vertical 9:16, phone-shot UGC realism, a real Spanish setting, nothing styled. Part 4 of 4 of one short ad for a wide-toe retro sneaker; the clip must start exactly in the initial state and end exactly in the end state described below.

[REFERENCES]
@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker. Replicate it exactly: a low-profile retro running sneaker with a deliberately wide, rounded toe box visibly broader than the heel, a completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, a lightweight ribbed air-mesh upper, suede-look toe cap and side panels, one curved stripe on the lateral side, flat laces, no logos. Colorway: white ribbed mesh, light warm grey suede-look panels, red stripe, caramel sole. Exactly one pair, the same pair in every frame. Do not slim the toe box, do not add a heel wedge, do not change the sole color.
@Image3 is the location. Use this exact place, layout, materials and light in every frame. Do not redesign the location, do not add furniture, do not change the wall color or the floor.

[CONTINUITY]
Marta: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings; wearing white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, plain grey socks. Appearance and clothing never change between clips.
Location (fixed for every Marta video, matches @Image3): the entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Same layout in every frame.
Props: one white A4 sheet of paper with a single short blue pen mark on it, one blue pen, one yellow tape measure, and the Rambla pair. Only the props named in each clip are in frame.

[STAGE 1 | 0–6s | Si no aciertas, te la cambian]
Initial state: Marta seated on the low bench wearing the white Rambla pair, both feet flat and still on the terrazzo in the lower part of the frame, hands on her knees, the white wall behind her.
Primary event: She shrugs once, small, with a closed-lip smile and one slow blink, looking at the lens, then points down at the bottom of the frame.
End state: Marta seated, Rambla on, feet in the same place, pointing down at the bottom of the frame.
Cut type: NO CUT — one continuous take.

[VISUAL STYLE]
26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

[CAMERA AND PERFORMANCE]
Locked-off static shot: the phone propped on the shoe cabinet across the hallway at Marta's chest height, medium shot of Marta seated on the bench, one fixed position for the full clip, only slight natural exposure breathing. The performance is only what is described in the primary event: no extra gestures, no posing, no looking for the lens unless stated.

[AUDIO]
Dialogue language: Spanish from Spain, casual, with natural fillers, recorded close to the phone microphone.
{Marta, lighter: "Y si aun así no aciertas, te la cambian gratis. La tabla está en la ficha, aquí abajo."}
<a quiet hallway, a bird outside the window>
No music. No subtitles. Every sound starts only when its visible source moves.

[EXCLUSIONS]
No on-screen text, subtitles, logos or watermarks. No camera travel: no tracking, no dolly, no orbit, no drone, no crash zoom. No walking. Nobody puts a shoe on or takes a shoe off, nobody touches laces. No object enters or leaves the frame unless the primary event says so; every prop listed is present from the first frame to the last and keeps its place. No extra shoes, no extra hands, no extra people. No beautified or smoothed skin. No music. Keep the characters original and non-representational of any real person. No blood, injuries or medical imagery.

[MAINTAIN CONSISTENCY]
One woman, one hallway, one sheet, one pen, one tape measure, one Rambla pair (white with red stripe); the sheet, pen and tape keep their exact place on the terrazzo in every overhead clip. Everything stays where the initial state puts it. The location matches @Image3 exactly.
```

---

## Referencias fijas (se generan una vez y se reutilizan en todos los vídeos)

### Image 3 · Placa de localización · Marta (recibidor)
```
Photorealistic phone photo, vertical 9:16, of an empty entrance hallway of a 1980s Spanish flat: speckled grey-and-cream terrazzo floor, white painted wall with a single beige light switch, a low wooden bench with a woven seat against the left wall, a dark wooden shoe cabinet with a bowl of keys on top against the right wall, a small framed mirror above the cabinet, a window at the far end giving soft daylight from frame left, the kitchen doorway visible at the end of the hallway. Camera at chest height looking down the hallway, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Lived-in and clean, nothing styled.
```
### Image 3 · Placa de localización · Javi (portal)
```
Photorealistic phone photo, vertical 9:16, of the empty entrance of a Spanish apartment building: three worn grey stone steps, a dark green wooden door with a brass number 14, cream rendered wall with a grey stone base, granite pavement in front, a black bicycle leaning on the wall to the right, morning open shade with soft light from frame left. Camera at chest height from the pavement facing the door, 26mm phone-style lens, natural slightly warm color grade, visible fine grain, no HDR, no people, no text, no logos. Ordinary and real, nothing styled.
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
