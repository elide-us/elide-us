# Source: World-Sim Design — Coastline Morphology, Quench-Speed as a State Field, Biogenic Epochs

> **Provenance:** Recovered early-days conversation, pasted by Elideus into the recompile
> session on **2026-07-03**. Conversation partner is an **unidentified earlier assistant**
> (likely the same ChatGPT-style session as the world-modes excavation). No share link.
>
> **Status:** SOURCE MATERIAL, **live and relevant** — this concerns the surviving **Clay
> Engine / GM-mode / "epoch 7"** world-simulation layer (see
> `early-world-modes-godmode-and-realmwright.md`), not the retired social/role machinery.
> Still not formally canon (Elideus rules canon), but unlike the world-modes batch this is
> **not superseded** — Elideus actively endorsed and built on it (*"Yep — we're aligned then,"*
> *"that's the missing keystone,"* *"the one thing I was truly missing"*).
>
> **Canon-grade candidate (Elideus-sourced design realization):** promote **quench speed** to a
> **conserved, first-class hex state field** alongside composition, hardness, and stress
> history. It is the state variable that determines *how a hex breaks* (ductile vs brittle,
> fracture scale, failure mode) — the previously-missing keystone. If Elideus wants this as a
> binding decision, it can be promoted from this note.
>
> **Not previously recorded:** nothing in the ledger or in `chatgpt-dm-system-notes.md`
> (whose elemental section is high-level: periodic table, heat/pressure/chemistry, hardness→
> erosion) covers cooling/quench, coastline taxonomy, biogenic carbonate sediment, or hex
> failure modes. This file is the first capture of that material.

---

## 1. Coastline / beach morphology — ~8 emergent regimes (not labels)

The design goal: coastlines are **outputs of competing transport and production systems**, not
enumerated types. If the sim carries hardness, grain size, wave energy, sediment source
(rock vs biogenic), volcanism with verticality, and plant stabilization, then every real
coastline falls out of the phase space without special cases.

| # | Regime | Driver | Sim support |
|---|--------|--------|-------------|
| 1 | Rocky / cliffed (fjords, palisades) | hard lithology + high wave energy | ✔ hardness + uplift + erosion |
| 2 | Sandy siliciclastic | quartz from continental erosion + longshore drift | ✔ sediment transport |
| 3 | Mudflats / tidal flats | fine sediment, low energy, estuarine sinks | ✔ low-energy accumulation |
| 4 | **Biogenic carbonate** (white sand, chalk cliffs) | coral/shell/coccolith production over time | ⚠→✔ needs a carbonate sediment channel distinct from rock erosion; **already covered given biogenic epochs** |
| 5 | Volcanic (black sand) | basaltic glass, grain size from cooling | ✔ if volcanism + cooling-grain-size modeled |
| 6 | Columnar / pillar (basalt columns, sea stacks, hoodoos) | cooling fractures + differential erosion | ✔ if cooling gradients + vertical stress exist |
| 7 | Vegetation-dominated (mangrove, peat, jungle shore) | biology stabilizes/locks sediment | ✔ plant feedback suppresses erosion |
| 8 | Karst / limestone | chemical dissolution > mechanical erosion | ⚠ optional, cheap: add a slow chemical-erosion channel |

Plants **don't create** coasts — they **lock them in** (modulate failure rate, not kind).

---

## 2. The state triad → failure behavior

At the end of the molten / early-solid epochs, every hex carries:

- **Composition** (basaltic / siliciclastic / carbonate / mixed)
- **Quench speed** (slow ↔ fast cooling)  ← the keystone
- **Stress history** (compression / tension / shear)

From those, derive **brittleness vs ductility**, **fracture pattern scale**, and **failure mode
under erosion**. The sim never simulates cracks — it simulates **how the hex fails.**

One-line model:
> **Hardness** tells you *if* a hex resists. **Quench speed** tells you *how* it breaks.
> **Stress** tells you *when.*

Quench-speed → microstructure → downstream form:
- **Slow quench** → columnar basalt, large regular fracture planes → hex-scale chunk failure → cliffs, palisades, sea stacks.
- **Fast quench** → glassy/chaotic structure, fine fragmentation → grain liberation → black sand, scree, talus.
- **Intermediate** → mixed → stepwise retreat, shelves, benches.

So when erosion/wave energy exceeds a threshold, the question isn't "does it erode?" but "does
this hex **shed grains, spall slabs, or fail catastrophically?**"

---

## 3. Hex-scale failure model (no mesh cracking, no voxel micro-management)

At hex resolution a hex can:
- **Lose mass** (sediment export)
- **Lose faces** (chunk collapse into neighboring hexes)
- **Transfer fracture bias** into adjacent hexes

That alone yields undercut cliffs, bowl-shaped coves, pillar remnants, and jagged-vs-smooth
coastlines. Same fields explain inland geology (hoodoos, desert pillars, Appalachians vs
Cascades, why some mountains crumble and others stand); plant life modulates *how fast* failure
happens, not *what kind.*

---

## 4. Cooling rate as a conserved "memory field" from the Navier–Stokes epochs

Treat temperature gradient / cooling velocity as a **continuous scalar carried forward from the
molten (Navier–Stokes) epochs.** It automatically produces columnar basalt (slow uniform
cooling), chaotic fracture (fast quench), grain-size/beach-color/texture variation, and
brittle-vs-ductile failure during later uplift. It **persists as a memory field into later
epochs and biases erosion** — no separate system needed.

**Verticality principle:** do **not** flatten vertical motion into a heightmap too early. Kept
vertical, it yields plumes → islands, cooling columns → fracture memory, later erosion → sea
stacks / pillars / archipelagos.

---

## 5. Biogenic epochs — already in the design (Elideus)

Elideus confirms several epochs were already implied/categorized as **biogenic epochs**. Given
biogenic production epochs + carbonate-vs-siliciclastic differentiation + warm/shallow/clear-
water constraints, coral sand, chalk cliffs, reef-locked coastlines, and atoll logic are
**inevitable outcomes** — from **production rates + deposition persistence**, with no organism
simulation required. Life is abstracted as an **environmental modifier.** This upgrades the
carbonate coastline (#4 above) from "needs support" to "already accounted for."

---

## Elideus turns (verbatim)

> "Yeah, and I think the the cooling columns Yeah, cooling rates might actually be an
> interesting factor Because I think that would actually be important probably at the
> Navier-Stokes level as well the early epochs I think that I had implied if not explicitly
> categorized several epochs as biogenic epochs So that also was already in the design and may
> not necessarily have been in your context though"

> "Oh, that's right. The quench speed matters. Oh, shit. So... Brittleness and hardness and
> quench speed actually are all extremely important. Because that does make all of those
> determinants. Okay. I think that was perhaps the one thing that I was truly missing there.
> Was really just the concept of quench speed determining a certain kind of ductile versus
> brittle... Yeah, fracture, hardness, and other kinds of things like that. Because... Yeah,
> remember that the scale that we're doing this at is like the sum of an entire hex. And its
> impact on the hexes next to it and other kinds of things like that. Yeah, chunking off an
> entire hex based on it being a certain level of ductile... Or on a certain level of
> ductivity, I guess, would be the conjugation, right? Does make sense."

---

## Reconciliation notes (editorial)

- **Belongs to the Clay Engine / GM-mode / epoch-7 layer** — the offline world-gen + simulation
  toolset (see `early-world-modes-godmode-and-realmwright.md`). This is the physics that makes
  "no player can break the world" true.
- **Hex is the simulation unit.** Erosion/failure operate on whole hexes and their neighbors —
  consistent with the hex-tiled planet in `chatgpt-dm-system-notes.md` and the hex-cluster /
  Advent-zone geometry in the round rulings.
- **New state variable, not a new system.** The whole insight is additive: quench speed +
  cooling-rate memory field slot alongside existing composition/hardness/stress; no new
  subsystem required.
- **Open/underspecified (not resolved here):** karst chemical-erosion channel (#8) is optional;
  exact hex-neighbor fracture-bias propagation rules; how quench-speed and grain-size map to the
  "simplified periodic table" material model in `chatgpt-dm-system-notes.md`.
- **Cross-refs:** `early-world-modes-godmode-and-realmwright.md` (God Mode / Clay Engine /
  epoch 7); `chatgpt-dm-system-notes.md` (elemental/erosion/hydro systems).
