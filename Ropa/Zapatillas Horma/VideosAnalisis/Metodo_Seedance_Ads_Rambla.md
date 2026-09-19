# Método Seedance 2.5 para los anuncios de Rambla (Navarros)

Fuentes que me has pasado: el prompt pack de Dan Kieft (Seedance 2.5 vía Higgsfield), la librería de emociones (seedance-emotion-direction.vercel.app, 25 performances) y la librería de movimientos de cámara (aicameramovements.com, 46 movimientos). Aquí está lo que vale de cada una, traducido a nuestro caso, y los prompts completos para los seis anuncios del primer test.

---

## 1. Lo que hace que sus vídeos parezcan reales (y lo que cambia para un anuncio)

1. **Hoja de personaje antes que nada.** Una imagen de referencia de tres paneles (cuerpo de frente sin cabeza · cuerpo de espaldas con cabeza · primer plano de la cara) sobre gris `B8B8B8`, misma ropa que la foto base. Luego, en cada vídeo: "@Image1 is used for the identity… Do not recast. Do not beautify. Do not use the image background." Así Marta y Javi son los mismos en 30 vídeos.
2. **Estructura por etapas con estados.** `[GOAL]` → `[CONTINUITY]` → `[STAGE n | 0–7s | título]` con *Initial state / Primary event / End state / Cut type* → `[VISUAL STYLE]` → `[CAMERA AND PERFORMANCE]` → `[AUDIO]` → `[EXCLUSIONS]` → `[MAINTAIN CONSISTENCY]`. El modelo no improvisa porque cada etapa empieza y acaba en una posición conocida.
3. **La emoción se escribe como comportamiento visible**, nunca como adjetivo: no "está aliviada", sino "una exhalación grande vacía el pecho, los ojos se cierran, las cejas bajan a neutro, los hombros caen; la sonrisa pequeña y temblorosa llega solo cuando termina la respiración". La librería de emociones está construida así y se pega **después** de la escena y del detonante.
4. **La cámara es una persona.** "Handheld, respira, se reajusta, nunca mecánicamente suave"; movimientos con nombre (de la librería de cámara) y un plano por intención. Para UGC: cámara en mano a altura humana, o teléfono apoyado (locked-off) cuando habla a cámara.
5. **Sonido por capas y por fuente.** Diálogo entre llaves `{…}`, efectos entre ángulos `<…>` que empiezan solo cuando su fuente se mueve, música no diegética entre paréntesis `(…)`. Tres distancias (cerca / media / lejos) y "no todos los sonidos igual de altos".
6. **Una línea de óptica y grado fija** en todos los vídeos de la campaña (la suya: "35mm lens, f/1.8, shallow depth of field, visible fine film grain, muted desaturated color grade, soft key from frame left, filmic contrast"). La nuestra está abajo.
7. **Exclusiones explícitas**: sin texto en pantalla, sin logos, sin gimbal suave, sin trípode inmóvil (salvo que lo pidamos), sin personas reales reconocibles.

**Lo que cambia para un anuncio de respuesta directa:** las etapas duran 5–8 s y coinciden con los clips del guion; una emoción por anuncio (no cinco); el producto es un objeto con continuidad ("exactly one pair of Rambla sneakers, white/red, the same pair throughout"); y el diálogo va en castellano de España, con muletillas, o se deja fuera y grabas la voz aparte (las dos versiones abajo). Sin música en frío.

---

## 2. Emociones útiles para Rambla (texto literal de la librería, para pegar tras la escena)

| Uso en nuestros anuncios | Emoción | Performance prompt (literal) |
|---|---|---|
| Al llegar a casa sin dolor (ángulos 1, 3) | **Relief** | A large visible exhale empties the chest, the eyes close, the raised eyebrows drop to neutral, and the shoulders collapse downward. One hand rises to the forehead. A small, shaky smile appears only after the breath finishes. |
| "Ahora lo entiendo" tras ver los dedos (1, 7) | **Realization** | A blank thinking expression breaks as the eyes widen, the eyebrows jump, the lips part on a silent breath, and focus snaps back. A slow nod follows while the knowing, slightly stunned look holds. |
| Final de turno, antes del producto (3) | **Exhaustion** | The eyelids drag downward, a long blink stays closed too long, the head drifts down and lifts again slowly, the jaw hangs slack, and one long breath empties out. The eyes reopen only halfway. |
| Pidiendo "una talla más" otra vez (4, 7) | **Frustration** | The eyes clamp shut, the jaw slides from side to side, a sharp breath pushes through the nose, and the head shakes once. The head tips back as one long defeated breath leaves the tension in the face. |
| "Sí, hay 49" (4) | **Pride** | The chin lifts, the chest expands, and a closed-lip smile spreads slowly and evenly. The shoulders roll back, followed by one slow, satisfied blink. The smile remains as the arms fold. |
| Decisión de probar (6, 10) | **Determination** | The eyes lift and lock forward, a deep breath expands the chest, the jaw sets visibly at the hinge, the eyes narrow, and the shoulders roll back. One sharp nod completes the change. |
| Viendo el precio de 150 € (6) | **Suspicion** | The chin drops while the eyes stay lifted. One eyebrow rises higher, the head turns slightly so the gaze lands sideways, and the mouth tightens at one corner. The stare holds without blinking. |
| Las barefoot "de dedos" (2) | **Disgust** (medio) | The nose wrinkles hard and pulls the upper lip upward, the eyes squint nearly shut, the chin draws in, and the head recoils and turns away. The revolted expression holds. |
| Sketch de las objeciones (9) | **Eye Roll** | The eyes roll in a full, slow arc while the head tilts with the movement. Air pushes out through the nose, the eyes return with lowered lids, and a flat stare holds before the gaze turns away. |
| "Me decían que parecían de bebé" (2, 16) | **Embarrassment** | Color rises in the cheeks, the eyes dart down and to the side, and an awkward pressed-lip half-smile appears. The head ducks and turns away while one hand rises near the mouth. The eyes stay lowered. |
| Remate con humor (9, 12) | **Smug / Gloating** | The eyelids lower, one corner of the mouth pulls into a slow smirk, the eyebrows rise once and settle, and the chin lifts slightly. The smirk holds through unbroken eye contact. |
| Risa al probarlas (8) | **Joy / Laughter** | The eyes squeeze into crinkled slits, the mouth opens wide showing teeth, the head drops forward and tips back, and the shoulders bounce with each breath. The laugh settles into a wide lingering grin. |
| Dedos apretados, roce (1, 15) | **Pain / Wince** (bajar intensidad) | The eyes clamp shut, the teeth bare in a hard grimace, the head snaps to one side, and one shoulder rises toward the ear. The face stays contracted before easing only slightly. |
| Sorpresa al ver que caben (2, 4) | **Awe / Wonder** (suave) | The eyes widen gradually without tension in the brow, the mouth opens little by little, the head tilts upward, and the body leans forward. The open, reverent expression never drops. |

Las otras once (Shock, Terror, Rage, Crying, Flirtation, Boredom, Confusion, Anxiety, Sadness, Guilt, Nervous Fake Smile) no las usamos: en un anuncio de zapatillas sobran. Regla: **una emoción dominante por anuncio y siempre en intensidad sutil o media**; lo explosivo parece anuncio.

---

## 3. Movimientos de cámara que usamos (texto literal de la librería)

| Plano de nuestros guiones | Movimiento | Prompt literal |
|---|---|---|
| Hablar a cámara con el móvil apoyado | Static shot | locked-off static shot. Movement: hold one fixed camera position for the full clip. |
| Selfie andando, coche, recibidor | Handheld shot | handheld shot. Movement: hold the camera at human operator height with natural body movement. |
| Pies andando por la calle | Low tracking | low tracking shot. Movement: move at ground or below-waist height alongside the subject's movement. |
| Zancada / paseo de lado | Side tracking | side tracking shot. Movement: move parallel beside the subject along their direction of travel. |
| Marta andando hacia cámara | Reverse tracking | reverse tracking shot. Movement: move backward in front of the walking subject. |
| Acercarse a los dedos / a la puntera | Dolly in | dolly in. Movement: move the camera physically forward in a straight line toward the main subject. |
| Énfasis suave en la suela doblada | Slow zoom in | slow zoom in. Movement: slowly increase lens focal length toward a tighter frame. |
| Del rostro a los pies | Tilt down | tilt down. Movement: rotate the camera downward from one fixed point. |
| De los pies al rostro (revelación) | Tilt up | tilt up. Movement: rotate the camera upward from one fixed point. |
| Mostrar la zapatilla en la mano por todos lados | Arc right | arc right. Movement: move on a shallow curved path around the main subject toward the right side. |
| Entrar por la puerta de casa | Push past | push past. Movement: move forward past a visible foreground object, edge or opening. |
| POV mirándose los pies | First-person view | first-person view. Movement: move forward at human eye height from the character's perspective. |
| Detalle de la puntera con la mano | Slider right | slider right. Movement: slide the camera a small distance to the right. |
| Reacción rápida (sketch) | Whip pan | whip pan right. Movement: rotate rapidly from the starting direction toward a new target on the right. |

Los que no usamos en UGC: órbitas, dron, crane, crash zoom, earth zoom, tilt-shift: gritan "IA".

---

## 4. Bloques fijos de la campaña (se pegan igual en todos los prompts)

**Óptica y grado (nuestra línea):**
> 26mm phone-style lens, f/2.0, moderate depth of field, visible fine grain, natural slightly warm color grade, soft window key from frame left, no HDR look, no digital-clean skin, filmic contrast but never cinematic-dark. Vertical 9:16.

**Producto con continuidad:**
> Exactly one pair of Rambla sneakers throughout: low-profile retro runner, wide rounded toe box visibly broader than the heel, completely flat caramel-amber rubber sole about 8 mm thick with a chunky lug tread, white ribbed air-mesh upper, light warm grey suede-look toe cap and panels, one red curved stripe on the lateral side, flat white laces, no logos. Do not slim the toe box, do not add a heel wedge, do not change the sole color.

**Exclusiones:**
> No on-screen text, subtitles, logos or watermarks (subtitles are added in the edit). No smooth gimbal or drone motion, no orbit, no crash zoom. No beautified or smoothed skin. No music. Keep the characters entirely original and non-representational of any real person. Do not show blood, injuries or medical imagery; the bunion is a mild natural shape of the foot, not a wound.

**Audio (dos versiones):**
- *Versión A, voz aparte (tu flujo actual con ElevenLabs):* "No spoken dialogue. Diegetic sound only: <…>." Y luego montas la voz encima.
- *Versión B, diálogo en el modelo:* "Dialogue language: Spanish (Spain), casual, with natural fillers." y las frases entre llaves: `{Marta, tired but warm, half laughing: "…"}`. Pruébala con un clip corto antes: si la voz no suena de aquí, vuelve a la A.

---

## 5. Hojas de personaje (genera primero, adjunta siempre)

### Marta — prompt de hoja de referencia (Nano Banana o Higgsfield, con su retrato base como Image 1)
> Use the person from image 1. Keep their identity. Do not recast. Do not beautify. One image, three equal vertical panels, same width, same height, hard even splits, no decorative borders. Same background in every panel: flat seamless studio grey B8B8B8, even light, no gradient, no floor shadow color shift. Panel 1, left: front view, the head not visible, crop cleanly at the neck, body only, standing, feet in frame, wardrobe and hands readable: white pharmacy tunic half-zipped over a plain grey t-shirt, straight dark blue jeans rolled once at the ankle, white Rambla sneakers with the red stripe. Panel 2, middle: full body from the back, head included, same clothes, standing, feet in frame; bodies in panel 1 and 2 have the same height, neck to feet matches, same scale, feet on the same baseline. Panel 3, right: close-up of the face from the front on the same grey, shoulders in, face sharp, natural skin not smoothed: Spanish woman, 44, medium build, shoulder-length brown hair with a few greys tied back, minimal makeup, small silver hoop earrings. Photographed, not illustrated. No logos. No text. No grain overlay.

### Javi — prompt de hoja de referencia
> Use the person from image 1. Keep their identity. Do not recast. Do not beautify. One image, three equal vertical panels, same width, same height, hard even splits, no decorative borders. Same background in every panel: flat seamless studio grey B8B8B8, even light, no gradient. Panel 1, left: front view, the head not visible, crop cleanly at the neck, body only, standing, feet in frame: navy work polo, dark grey work trousers with the hem above the shoe collar, black Rambla sneakers with the white stripe, cheap digital watch. Panel 2, middle: full body from the back, head included, same clothes, same height and scale as panel 1, feet on the same baseline. Panel 3, right: close-up of the face from the front on the same grey, shoulders in, face sharp, natural skin not smoothed: Spanish man, 42, broad build, short dark beard with some grey, short hair. Photographed, not illustrated. No logos. No text. No grain overlay.

En cada vídeo: "@Image1 is used for Marta's identity, face, hair, build and wardrobe. Do not recast. Do not beautify. Do not use the image background. @Image2 is the Rambla sneaker reference; replicate it exactly."

---

## 6. Prompts completos · primer test (ángulos 1, 2, 3, 4, 6 y 11)

Cada uno está escrito como una pieza continua por etapas de 5–8 s. Si tu generador limita a 10–15 s por clip, genera etapa por etapa usando el "End state" de una como "Initial state" de la siguiente y la misma imagen de referencia. Diálogo en versión B; para la versión A borra las llaves y deja los `<sonidos>`.

### 6.1 · Ángulo 1 · "Descálzate y mira" (Marta) · 40 s

```
[GOAL]
A single, honest, phone-shot UGC piece, 40 seconds, in which a woman at home takes off a conventional sneaker, shows how her toes have been squeezed into a point, explains that the shoe's pointed toe box is the cause, and puts on a wide-toe retro sneaker where her toes spread. Calm, one-to-one tone, like a voice note to a friend. Vertical 9:16.

[CONTINUITY]
@Image1 is used for Marta's identity, face, hair, build and wardrobe (white pharmacy tunic half-zipped over a grey t-shirt, dark jeans rolled once). Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: [pega el bloque "Producto con continuidad"]. Exactly one pair, white/red, throughout.
Props: exactly one conventional white sneaker with a narrow pointed toe box, no logo, and one Rambla pair. Scene: the hallway of a 1980s Spanish flat: terrazzo floor, white wall, a low wooden bench, a wooden shoe cabinet, keys on top, late-afternoon window light from frame left. The layout stays consistent.

[STAGE 1 | 0–7s | The hook: shoe off, toes in a point]
Initial state: overhead phone shot, handheld, looking down at Marta's feet on the terrazzo as she sits on the bench; one foot still in the conventional sneaker, the other bare.
Primary event: she pulls the conventional sneaker off with one hand and sets it beside the foot. The bare foot rests on the floor with the toes squeezed together into a point, the big toe angled inward, a mild bunion, a faint sock line. She holds still so it reads.
End state: both bare feet on the floor next to the conventional sneaker, toes still in a point.
Cut type: NO CUT.

[STAGE 2 | 7–14s | Relief of taking it off, and the realization]
Initial state: the camera tilts up from the feet to Marta's face at the bench.
Primary event: [Relief] A large visible exhale empties the chest, the eyes close, the raised eyebrows drop to neutral, and the shoulders collapse downward. One hand rises to the forehead. A small, shaky smile appears only after the breath finishes. Then she looks down at her toes and [Realization] a blank thinking expression breaks as the eyes widen, the eyebrows jump, the lips part on a silent breath, and focus snaps back. A slow nod follows.
End state: Marta looking at her own feet, nodding once.
Cut type: NO CUT.

[STAGE 3 | 14–22s | The culprit: the pointed toe box]
Initial state: dolly in toward the conventional sneaker on the floor, overhead.
Primary event: her hand turns the sneaker toe-up and her index finger traces the narrow pointed toe box; then she places her bare foot on top of the sneaker's insole and the foot visibly overflows the insole on both sides while the insole's tip stays empty ahead of the toes.
End state: the foot resting on the insole, overflowing at the sides.
Cut type: NO CUT.

[STAGE 4 | 22–30s | The Rambla: toes spread]
Initial state: she reaches for the Rambla pair beside the bench.
Primary event: slider right to the Rambla; she slides her foot in without using her hands, standing; the camera comes back to overhead and the ribbed mesh shows the toes spreading inside the wide toe box. Then her hands lift the second shoe and fold the sole in half, caramel tread to camera, a clean natural bend at the forefoot.
End state: one Rambla on her foot, the other bent in her hands.
Cut type: NO CUT.

[STAGE 5 | 30–40s | Walking away, not taking them off]
Initial state: low tracking shot, ground height, behind her feet.
Primary event: she walks down the hallway toward the kitchen in the Rambla pair at a relaxed pace; the sole flexes at each step, heel landing flat. Near the end the camera tilts up as she looks back over her shoulder with the small shaky smile from Stage 2 still there.
End state: Marta in the kitchen doorway, shoes on, looking back once.
Cut type: NO CUT.

[VISUAL STYLE]
[pega la línea de óptica y grado]. Real 1980s Spanish flat, lived-in, nothing styled. Skin with pores and a faint sock mark; the bunion is a natural mild shape, not exaggerated.

[CAMERA AND PERFORMANCE]
Phone in hand throughout: handheld shot, natural body movement, small re-framings, never mechanically smooth. Stage 1 and 3 are overhead and close; Stage 2 is a tilt up to a medium close-up; Stage 4 uses one small slider right then returns overhead; Stage 5 is a low tracking shot from behind. Marta never looks into the lens for more than a beat; her performance is in the exhale, the nod and the way she stops holding her foot. No posing.

[AUDIO]
Dialogue language: Spanish (Spain), casual, with natural fillers, low volume, close to the phone microphone.
<the conventional sneaker pulled off the foot, a soft rubber scuff on terrazzo>
{Marta, tired, half to herself: "Oye, haz una cosa. Quítate la zapatilla y mira cómo se te quedan los dedos."}
<a long exhale close to the microphone>
{Marta, quieter: "¿Así, apretados, en punta? Pues escúchame un segundo."}
<the sneaker turned over on the floor, a small hollow knock>
{Marta: "Eso no es que tengas el pie raro. Es que la puntera acaba en punta y lleva años empujándote los dedos hacia dentro."}
<the foot sliding into the mesh shoe, fabric brushing skin>
{Marta, warmer: "Estas tienen la puntera con la forma del pie. Mira: los dedos van sueltos."}
<the rubber sole creaking softly as it bends>
{Marta: "Y la suela es plana y se dobla con el pie."}
<slow footsteps on terrazzo, receding>
{Marta, half laughing: "Es la primera vez en años que llego a casa y no me las quito en la puerta. Te las dejo aquí abajo."}
Far: faint street noise through the window. No music. No subtitles.

[EXCLUSIONS]
[pega el bloque de exclusiones]

[MAINTAIN CONSISTENCY]
Exactly one woman (Marta), one conventional sneaker, one Rambla pair, one hallway; same clothes and same light throughout; the conventional sneaker stays beside the bench after Stage 3; the Rambla toe box stays wide in every frame.
```

### 6.2 · Ángulo 2 · "Las barefoot que no parecen barefoot" (Javi) · 36 s

```
[GOAL]
A phone-shot UGC piece, 36 seconds, in which a man at the door of his building holds up a generic "toe-shoe" barefoot sneaker with mild disgust, drops it out of frame, then unboxes a retro-looking wide-toe sneaker and shows, with his own feet, that it is barefoot on the inside. Dry humor, one emotion: pleased surprise. Vertical 9:16.

[CONTINUITY]
@Image1 is used for Javi's identity, face, beard, build and wardrobe (navy work polo, dark grey work trousers hem above the shoe collar). Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: [bloque producto], colorway black upper with a white stripe, caramel sole. Exactly one pair throughout.
Props: one generic five-toe barefoot shoe in dull grey, no logo, and one plain cardboard box. Scene: the stone doorstep and wooden door of a Spanish apartment building, morning, open shade.

[STAGE 1 | 0–6s | The hook: the toe-shoe]
Initial state: locked-off phone at chest height on the doorstep, Javi seated on the step, medium shot.
Primary event: he lifts the five-toe shoe by the heel with two fingers. [Disgust, medium] The nose wrinkles hard and pulls the upper lip upward, the eyes squint nearly shut, the chin draws in, and the head recoils and turns away. He lets it drop out of frame.
End state: hands empty, the toe-shoe out of frame.
Cut type: NO CUT.

[STAGE 2 | 6–13s | The reveal]
Initial state: same framing; he pulls the cardboard box onto his knees.
Primary event: he opens it and lifts the black Rambla, turning it slowly; arc right of the phone around the shoe in his hand so the suede-look toe cap, the white stripe and the caramel sole read one after another. [Awe / Wonder, soft] The eyes widen gradually without tension in the brow, the mouth opens little by little, the head tilts, and the body leans forward.
End state: the shoe held up beside his face, lateral side to camera.
Cut type: NO CUT.

[STAGE 3 | 13–21s | Inside it is barefoot]
Initial state: tilt down to his feet on the stone step.
Primary event: he places the Rambla beside a conventional black sneaker of the same size; overhead, the Rambla's toe box is visibly wider. He slides his foot into the Rambla without hands; the mesh shows the toes spreading. Then he lifts the other shoe and folds the sole in half, tread to camera.
End state: one Rambla on, the other bent in his hands.
Cut type: NO CUT.

[STAGE 4 | 21–36s | Walking off to work]
Initial state: side tracking shot at ground height as he stands.
Primary event: he walks along the pavement in the Rambla pair, heel landing flat, sole flexing; the camera rises with a tilt up to his face as he glances at the lens once with [Smug / Gloating, light] the eyelids lower, one corner of the mouth pulls into a slow smirk, the eyebrows rise once and settle.
End state: Javi walking away, both shoes on, morning street.
Cut type: NO CUT.

[VISUAL STYLE]
[línea de óptica y grado]. Ordinary Spanish street, granite paving, no styling.

[CAMERA AND PERFORMANCE]
Stage 1 and 2 locked-off phone propped on the step; Stage 2 includes one slow arc right around the shoe in his hand; Stage 3 tilt down and overhead handheld; Stage 4 side tracking at ground height rising into a tilt up. Javi speaks to the lens only in Stage 1 and the last beat; the rest is hands and feet.

[AUDIO]
Dialogue language: Spanish (Spain), casual, dry.
{Javi, deadpan: "Yo quería probar las barefoot, en serio. Pero es que todas parecían esto."}
<a rubber shoe dropping onto stone, one dull bounce>
{Javi: "Y yo con esto no voy ni a por el pan."}
<cardboard box lid lifting, paper rustling>
{Javi, quieter, genuinely pleased: "Hasta que vi estas. Mira. Una retro de las de toda la vida."}
<the foot sliding into mesh; a soft creak as the sole bends>
{Javi: "Pero por dentro es barefoot de verdad: puntera ancha, suela plana, y se dobla así."}
<footsteps on granite paving, a distant moped>
{Javi, half smirk: "Las llevo al curro, a la calle y al gym. Y no parecen de viejo. Te las dejo aquí abajo."}
No music. No subtitles.

[EXCLUSIONS]
[bloque exclusiones] The five-toe shoe is a generic prop, no brand.

[MAINTAIN CONSISTENCY]
Exactly one man, one doorstep, one box, one Rambla pair (black/white) and one conventional black sneaker; same clothes and light throughout.
```

### 6.3 · Ángulo 3 · "Si llegas a casa deseando quitártelas" (Marta) · 45 s

```
[GOAL]
A phone-shot UGC piece, 45 seconds, following a pharmacy worker from the last hour of her shift to her own front door: the moment she used to take her shoes off in pain, and the day she does not need to. One dominant emotion: recognition turning into relief. Vertical 9:16.

[CONTINUITY]
@Image1 is Marta (white pharmacy tunic, grey t-shirt, dark jeans rolled once). Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: [bloque producto], colorway pale sky-blue upper with a white stripe, caramel sole. Exactly one pair.
Scenes: (a) the staff side of a Spanish pharmacy counter: glossy white floor tiles, the base of a white counter, an anti-fatigue mat pushed aside, white medicine boxes on a low shelf out of focus, a faint green cross reflection on the tiles; (b) the hallway of her 1980s flat: terrazzo, white wall, low wooden bench, shoe cabinet. Both consistent.

[STAGE 1 | 0–7s | Hook: the door, the old habit]
Initial state: push past the half-open front door into the hallway, handheld, following Marta from behind as she comes home with a supermarket bag.
Primary event: she drops the bag, sits on the bench and reaches for her conventional sneaker with the old urgency; the camera tilts down to her hands on the laces, then back to her face: [Exhaustion] the eyelids drag downward, a long blink stays closed too long, the head drifts down and lifts again slowly, the jaw hangs slack, and one long breath empties out.
End state: Marta on the bench, hands on the laces, not yet untied.
Cut type: HARD CUT to Stage 2 (a memory of the shift).

[STAGE 2 | 7–15s | Behind the counter, hour six]
Initial state: low handheld shot at floor level behind the pharmacy counter, white tiles, Marta's feet in the conventional sneakers.
Primary event: her weight shifts from one foot to the other, one heel lifts, the toes visibly press against the narrow toe box through the fabric; a hand comes down briefly to rub the outside of the big toe joint through the shoe.
End state: feet still, weight on one leg.
Cut type: HARD CUT.

[STAGE 3 | 15–23s | The cause, at the bench]
Initial state: back in the hallway, overhead, she has taken the conventional sneaker off.
Primary event: her bare foot on the terrazzo with the toes in a point and a mild bunion; then the foot placed on the sneaker's insole, overflowing the sides while the tip stays empty. [Realization] a blank thinking expression breaks as the eyes widen, the eyebrows jump, the lips part on a silent breath, and focus snaps back; a slow nod.
End state: foot on the insole, Marta nodding.
Cut type: NO CUT.

[STAGE 4 | 23–33s | Rambla on]
Initial state: she lifts the sky-blue Rambla from beside the bench.
Primary event: foot in without hands, standing; overhead, the toes spread inside the mesh; she folds the other sole in half, tread to camera; a small slider right along the flat sole profile.
End state: both Rambla on, Marta standing.
Cut type: NO CUT.

[STAGE 5 | 33–45s | Same door, new habit]
Initial state: reverse tracking shot in the hallway, the phone moving backward in front of her.
Primary event: she walks toward the kitchen in the Rambla pair, unhurried, then sits at the kitchen table with the shoes still on, scrolling her phone; [Relief] a large visible exhale empties the chest, the eyes close, the eyebrows drop to neutral, the shoulders collapse downward; a small shaky smile appears only after the breath finishes.
End state: Marta at the table, shoes on, smiling slightly.
Cut type: NO CUT, end on this image.

[VISUAL STYLE]
[línea de óptica y grado]. The pharmacy is warm, not clinical; the flat is lived-in.

[CAMERA AND PERFORMANCE]
Handheld phone throughout; Stage 1 push past the door and tilt down/up; Stage 2 low handheld at floor level; Stage 3 and 4 overhead and close; Stage 5 reverse tracking then a locked beat at the table. Marta never performs to the lens; the story is in her feet and her breathing.

[AUDIO]
Dialogue language: Spanish (Spain), casual, tired-warm.
<keys on wood, a supermarket bag set down on terrazzo>
{Marta, low: "Si llegas a casa y lo primero que haces es quitarte las zapatillas en la puerta, escúchame un segundo, que a mí me pasaba igual."}
<pharmacy: a till drawer closing, a soft beep, shoes shifting on tile>
{Marta, voice over the memory: "Ocho horas de pie. Y a las cuatro ya notas los dedos apretados de aquí, el gordo rozando, las plantas ardiendo."}
<the sneaker turned over on the floor>
{Marta: "Yo pensaba que era de tener el pie ancho. Pero es que la puntera acababa en punta y el pie no cabía. Ocho horas apretando. Claro que duele."}
<the foot sliding into mesh; the sole creaking as it bends>
{Marta, warmer: "Con estas los dedos van sueltos, la suela es plana y se dobla. Y son de malla, así que en el turno no se te cuecen."}
<a chair pulled out on tile; a long exhale>
{Marta, half laughing: "Llevo unas semanas con ellas en el turno entero. Y sí, llego a casa y ni me acuerdo de quitármelas. Te las dejo aquí abajo."}
No music. No subtitles.

[EXCLUSIONS]
[bloque exclusiones] No visible medicine brand names on the boxes.

[MAINTAIN CONSISTENCY]
One woman, two locations (pharmacy, flat), one conventional sneaker pair and one Rambla pair (sky-blue); same tunic in both locations; the green cross reflection only in the pharmacy.
```

### 6.4 · Ángulo 4 · "Sí, hay 47, 48 y 49" (Javi) · 40 s

```
[GOAL]
A phone-shot UGC piece, 40 seconds, at the open side door of a delivery van at dawn: a broad man with size-47 feet explains that he was never short of length, he was short of width, and shows it with a normal sneaker's insole and the wide-toe sneaker. One emotion: quiet pride. Vertical 9:16.

[CONTINUITY]
@Image1 is Javi (navy work polo, dark grey work trousers, cheap digital watch). Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: [bloque producto], colorway black upper with a white stripe, caramel sole, a visibly large size. Exactly one pair.
Props: one conventional black sneaker pair of the same nominal size, no logo; a paper coffee cup; a folded newspaper for scale. Scene: a white delivery van with the side door open in an industrial estate outside a Spanish city, dry tarmac, a pallet, morning haze, low sun from frame left.

[STAGE 1 | 0–6s | Hook: sizes]
Initial state: locked-off phone at shin height on the tarmac, Javi seated on the van's floor edge, feet planted wide, coffee in hand.
Primary event: he lifts one black Rambla beside the folded newspaper so the size reads huge; [Pride] the chin lifts, the chest expands, and a closed-lip smile spreads slowly and evenly; the shoulders roll back, one slow satisfied blink.
End state: shoe held up, smile holding.
Cut type: NO CUT.

[STAGE 2 | 6–14s | The old trick]
Initial state: overhead handheld on his feet.
Primary event: his bare foot on the insole of the conventional sneaker: the foot overflows both sides while a finger's width of insole stays empty at the tip. Then he pulls on the conventional sneaker one size up: the toe box creases, the laces pulled to the last eyelet. [Frustration, light] the eyes clamp shut, the jaw slides side to side, a sharp breath through the nose, one head shake.
End state: the conventional sneaker on, creased at the toe.
Cut type: NO CUT.

[STAGE 3 | 14–22s | Width, not length]
Initial state: overhead, two toe boxes side by side on the tarmac: the conventional sneaker and the Rambla, same nominal size.
Primary event: the difference in toe-box width reads without explanation; a slider right along the two toes. Then his foot slides into the Rambla without hands and the mesh shows the toes spreading.
End state: Rambla on one foot, the conventional sneaker beside.
Cut type: NO CUT.

[STAGE 4 | 22–30s | Demo]
Initial state: medium shot, Javi holding the second Rambla.
Primary event: he folds the sole in half, caramel tread to camera; sets it down flat and the camera slides along the flat profile from heel to toe.
End state: both Rambla on the tarmac, flat.
Cut type: NO CUT.

[STAGE 5 | 30–40s | Off to work]
Initial state: low tracking shot from behind as he stands and closes the van door.
Primary event: he walks across the yard in the Rambla pair, flat heel landings, sole flexing; the camera tilts up as he glances back once with the closed-lip smile from Stage 1.
End state: Javi walking away between pallets, morning haze.
Cut type: NO CUT.

[VISUAL STYLE]
[línea de óptica y grado], but the key is low sun from frame left at 4800 K with long shadows; cool open-sky fill on the shadow side.

[CAMERA AND PERFORMANCE]
Locked-off at shin height for Stage 1; overhead handheld for 2 and 3 with one small slider right; medium handheld for 4; low tracking from behind for 5. Javi talks to the lens only in Stage 1; his pride is in the chin and the slow blink, not in words.

[AUDIO]
Dialogue language: Spanish (Spain), casual.
<a van door sliding, a paper cup set on metal>
{Javi, calm: "Sí. Hay 47, hay 48 y hay 49. Y no, no es una talla grande con la horma de siempre."}
<laces pulled tight, fabric creasing>
{Javi: "Yo llevaba años pidiendo una talla más para que no me apretaran de ancho. Y me sobraba medio dedo por delante."}
<a shoe set down on tarmac>
{Javi: "El problema no era el largo. Era el ancho. Mira la puntera de una y la de otra, mismo número."}
<the sole creaking as it bends>
{Javi: "Puntera ancha de verdad, suela plana y que se dobla. Y una retro normal, que te la pones con vaqueros y ya."}
<footsteps on tarmac, a forklift far away>
{Javi: "Eso sí: en estas se elige por centímetros, no por tu número. Mide el pie, mira la tabla, y si no aciertas te la cambian gratis. Aquí abajo."}
No music. No subtitles.

[EXCLUSIONS]
[bloque exclusiones] No company name on the van.

[MAINTAIN CONSISTENCY]
One man, one van, one conventional sneaker pair, one Rambla pair (black/white); the newspaper stays on the van floor; same low sun throughout.
```

### 6.5 · Ángulo 6 · "150 € por unas barefoot. Ya." (Javi) · 38 s

```
[GOAL]
A phone-shot UGC piece, 38 seconds, in a neighbourhood gym: a man shows a phone screen with a 149,95 € barefoot shoe listing, explains in one breath what actually makes a shoe barefoot, and shows that his 49,95 € pair does exactly that. One emotion: "I'm not stupid" — suspicion turning into determination. Vertical 9:16.

[CONTINUITY]
@Image1 is Javi (plain white t-shirt, black training shorts, black socks). Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: [bloque producto], colorway black upper with white stripe, caramel sole. Exactly one pair.
Props: his phone showing a generic shoe listing with the price "149,95 €" and no brand name. Scene: a municipal gym, black rubber floor with white speckle, a dumbbell rack, a high side window, cool ceiling LEDs.

[STAGE 1 | 0–6s | Hook: the price]
Initial state: locked-off phone at chest height on a bench, Javi seated, holding his phone toward the lens.
Primary event: the listing with "149,95 €" fills part of the frame; he lowers the phone and [Suspicion] the chin drops while the eyes stay lifted, one eyebrow rises higher, the head turns slightly so the gaze lands sideways, and the mouth tightens at one corner.
End state: Javi looking sideways at the lens, phone lowered.
Cut type: NO CUT.

[STAGE 2 | 6–14s | What barefoot actually is]
Initial state: he picks up the black Rambla from the bench.
Primary event: he counts on the shoe with his fingers: taps the wide toe box, runs a finger along the flat sole profile, then folds the sole in half, tread to camera. Slow zoom in on the bending sole.
End state: the shoe bent in his hands.
Cut type: NO CUT.

[STAGE 3 | 14–22s | Same thing, no logo]
Initial state: tilt down to his feet.
Primary event: foot into the Rambla without hands; overhead, toes spreading in the mesh; then a close pass along the plain lateral side with no logo.
End state: both Rambla on.
Cut type: NO CUT.

[STAGE 4 | 22–30s | Honest limits]
Initial state: medium shot, Javi standing.
Primary event: he pinches the mesh between two fingers and taps the thin sole with his knuckle while shaking his head slightly: a small honest concession.
End state: Javi standing, shoe on, hands open.
Cut type: NO CUT.

[STAGE 5 | 30–38s | Squat, decision]
Initial state: low handheld at floor level, side-on.
Primary event: a bodyweight squat with feet planted flat, toes spread, heels down; then he stands and [Determination] the eyes lift and lock forward, a deep breath expands the chest, the jaw sets visibly, the shoulders roll back; one sharp nod.
End state: Javi standing, nod completed.
Cut type: NO CUT.

[VISUAL STYLE]
[línea de óptica y grado], key from the high side window, cool LED fill.

[CAMERA AND PERFORMANCE]
Locked-off on the bench for Stage 1 and 2 with one slow zoom in on the bending sole; tilt down and overhead handheld for 3; medium handheld for 4; low handheld side-on for 5. He talks to the lens in Stages 1, 2 and 4.

[AUDIO]
Dialogue language: Spanish (Spain), casual, dry.
<gym ambience: a plate set down far away, a fan>
{Javi: "Unas barefoot de marca: ciento cincuenta euros. Por una zapatilla de malla con suela plana. Ya."}
<fingers tapping the shoe; the sole creaking as it bends>
{Javi: "Lo que hace que una barefoot sea barefoot son tres cosas: puntera ancha, suela plana y suela que se dobla. Esto. Lo demás es el logo."}
<foot sliding into mesh>
{Javi: "Estas hacen lo mismo. Y no te cobran la marca. Cuarenta y nueve con noventa y cinco, del 36 al 49."}
<mesh pinched, a knuckle tapping rubber>
{Javi: "¿Son de piel? No, son de malla, y en invierno pides la bota. ¿Para la obra? Tampoco. Para el día a día, van de sobra."}
<a breath in, rubber floor creaking under the squat>
{Javi: "Yo entreno con ellas y voy al curro con ellas. Y si no te convencen, treinta días y te devuelven el dinero. Aquí abajo."}
No music. No subtitles.

[EXCLUSIONS]
[bloque exclusiones] The listing on the phone shows no brand name or logo; no gym brand visible.

[MAINTAIN CONSISTENCY]
One man, one bench, one phone, one Rambla pair; same gym light; the phone stays on the bench after Stage 1.
```

### 6.6 · Ángulo 11 · "Mide el pie" (Marta) · 30 s

```
[GOAL]
A phone-shot how-to, 30 seconds, overhead on a home floor: how to measure your foot with a sheet of paper against the wall and pick the right size of a wide-toe sneaker that runs small. Calm, practical, no selling. Vertical 9:16.

[CONTINUITY]
@Image1 is Marta (grey t-shirt, dark jeans rolled once, bare feet). Do not recast. Do not beautify. Do not use the image background.
@Image2 is the Rambla sneaker: [bloque producto], colorway white/red. Exactly one pair.
Props: one white A4 sheet, one pen, one tape measure, a white wall meeting a wooden floor. Scene: a corner of a Spanish flat, window light from frame left.

[STAGE 1 | 0–6s | Hook: 27 cm is a 44]
Initial state: overhead handheld on the floor: a bare foot on the A4 sheet, heel against the wall, the tape measure lying beside reading 27 cm, one Rambla beside it.
Primary event: a finger taps the tape at 27, then taps the shoe.
End state: finger resting on the shoe.
Cut type: NO CUT.

[STAGE 2 | 6–16s | How to measure]
Initial state: overhead, the sheet empty on the floor against the wall.
Primary event: Marta places her heel against the wall on the sheet, marks the tip of the longest toe with the pen, lifts the foot, and measures from the sheet's edge to the mark with the tape; the camera dollies in on the number.
End state: tape reading in frame.
Cut type: NO CUT.

[STAGE 3 | 16–24s | Between two sizes, take the larger]
Initial state: overhead, the tape reads 26,3 cm.
Primary event: her hand brings the Rambla in and slides her foot in; the toes have a finger of room at the tip; she wiggles the toes inside the mesh.
End state: foot in the shoe, toes spread.
Cut type: NO CUT.

[STAGE 4 | 24–30s | If it's wrong, free swap]
Initial state: tilt up from the floor to Marta sitting back on her heels.
Primary event: she shrugs once, small, with a closed-lip smile and one slow blink.
End state: Marta looking at the lens, relaxed.
Cut type: NO CUT.

[VISUAL STYLE]
[línea de óptica y grado].

[CAMERA AND PERFORMANCE]
Overhead handheld for Stages 1–3 with one dolly in on the tape; tilt up for Stage 4. No performance beyond the shrug.

[AUDIO]
Dialogue language: Spanish (Spain), calm.
<paper set on wood, a tape measure unspooling>
{Marta: "Antes de pedirlas, esto: en estas un pie de veintisiete centímetros es una cuarenta y cuatro. No una cuarenta y dos."}
<pen on paper, one short mark>
{Marta: "Folio contra la pared. Talón pegado. Marca donde acaba el dedo más largo. Mide. Ya está."}
<foot sliding into mesh>
{Marta: "Y si estás entre dos, la grande. Con veintiséis con tres, la cuarenta y tres, aunque uses la cuarenta y uno."}
{Marta, lighter: "Y si aun así no aciertas, te la cambian gratis. La tabla está en la ficha, aquí abajo."}
No music. No subtitles.

[EXCLUSIONS]
[bloque exclusiones]

[MAINTAIN CONSISTENCY]
One woman, one sheet, one pen, one tape, one Rambla pair; the sheet stays against the wall throughout.
```

---

## 7. Cómo iterar con esto
- Genera la hoja de Marta y la de Javi una vez; guarda las dos imágenes como @Image1 fijas de la campaña.
- Prueba primero el ángulo 11 (30 s, sin emoción compleja) para calibrar voz, grano y tallaje del producto; luego el 1.
- Si la voz del modelo no suena de aquí, pasa a la versión A (sin llaves) y monta ElevenLabs: los `<sonidos>` se quedan.
- Si el producto cambia entre etapas, sube la referencia @Image2 a la primera posición y repite en cada etapa "the same pair as @Image2".
- Los hooks alternativos del documento de guiones se meten cambiando solo la STAGE 1 y la primera línea de diálogo; el resto del prompt no se toca.
