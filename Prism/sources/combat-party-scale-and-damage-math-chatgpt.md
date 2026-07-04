# Source: Combat Design — Party Scale, Difficulty Curve, and Damage Math (ChatGPT era)

> **Provenance:** A cluster of undated ChatGPT design conversations about combat — Elideus's
> estimate "at least three, probably closer to six" — pasted into the recompile session by
> Elideus on **2026-07-03**. Postdate the 2014 OneNote notes (they use the seven Prism colors,
> not the MTG-5) and predate current canon (Book I round-10 combat, Book IV magic).
> **Status: IDEATION / ARCHAEOLOGY** — "most of this lost and possibly superseded by newer
> designs, but there should be some degree of synergy between this and where we are now."
> Where this conflicts with Canon Rulings (Book V), seed canon, or ledger `decision` entries,
> the rulings win. Intake note: ledger (this session).
>
> **Reconciliation (what was already canon and is therefore NOT re-transcribed here):**
> - The **magic appendices** in these conversations — the combat-effect taxonomy (Counter
>   Physical / Magical / Player Control), the Magical/Specialty/Ancient Domains, the Types of
>   Casting, the Psionics section, and the expanded Cantrips list — are **already present,
>   nearly verbatim, in Book IV** (`BookIV.md` §Combat Mechanics, §Magical Domains, §Types of
>   Casting, §Psionics, §Cantrips). Those ChatGPT sessions are the direct ancestors of current
>   Book IV. Nothing new to archive.
> - The **caster archetypes** (Wizard–Fire, Necromancer–Death, Conjurer–Air, Shaman–Earth,
>   Priest–Life, Cleric–Water) and the **core casting mechanics / spell types** (Instant,
>   Normal, Channeled, Enchantment, Droppable) are **already archived** in
>   `sources/combat-systems-ideation-2014.md`. Known misalignment stands: those six archetypes
>   treat Life and Earth as separate schools; today they are merged in Green (seed canon 2).
>
> **What IS new and durable (transcribed below):** the party-size / raid-tier targets and the
> EverQuest-vs-WoW monster-scaling philosophy (Part 1); a worked stat-scaling damage formula
> with weapon-skill grade multipliers (Part 2); and the color counter/synergy web plus the
> "each effect in ≥3 schools" balancing principle from the enchantment-slotting exercise
> (Part 3).

---

## Part 1 — Party Scale and the Difficulty Curve

Elideus's stated design intent (voice-dictated; transcribed faithfully, artifacts noted):

**Fixed party-size content, no dynamic scaling.**
- **Dungeons: 5–7 players** (min 5, max 7). Dungeons and the clan dungeon framework are to be
  built so the challenge range of any given dungeon is 5–7.
- **Mid-tier low-level raids: 10–15** (stated once as "10 to 12").
- **Large raids: 25–35** (stated once as "25 to 30").
- **Mega-raids as an aspiration: 72 → 100.** Nostalgia for EverQuest 72-person raids; "Could
  you imagine a hundred person raid? In a modern MMO?" ("silly of me to say we couldn't go much
  beyond [25–35] when we used to run seventy-two person raids").
- Encounters are **tuned for a set size, not auto-scaled to the group** — "we're not going to go
  with dynamic scaling. A dungeon designed for 7 is for 7. Not 5. Not 3."
  - *Transcription artifact:* one garbled line reads "I'm definitely going to push for dynamic
    scaling… push in the direction of EverQuest." Read in context (immediately after "we're not
    going to go with dynamic scaling" and alongside "think EverQuest, not WoW"), the intent is
    **fixed encounter tuning + EverQuest-style punishing difficulty**, not party-size
    auto-scaling. **Confirm which he meant.**

**The EverQuest vs WoW monster-scaling philosophy (the mechanical heart of this session).**
- In EverQuest, **player power scaled on an exponent-of-2 curve; monster power for the same
  levels scaled on an exponent-of-3 curve** (squared vs cubed). Because monster power outran
  player power, **soloing was near-impossible** (class- and level-dependent; the "hell levels"
  came from the same exponential XP-requirement math). This is a large part of why party play
  was mandatory and why **pullers** mattered.
- **World of Warcraft made monster power scale the same as player power** → soloing became
  viable → a major factor (not the sole one) in the erosion of party-dependent design.
- **Design direction for Prism:** EverQuest + Dark Souls + roguelite pacing (Elden Ring
  Nightreign cited as a reference for the roguelite feel). **"Think Dark Souls, not World of
  Warcraft. Think EverQuest, not World of Warcraft."** Monsters are ridiculously hard; **a
  single monster can wipe a 5–7 party** without coordination. Positioning, coordination, and
  class synergy decide the fight; a poor pull ruins the run.

**The puller role.** Elideus played a **monk** and was a notorious puller (used ShowEQ). He
names **death knight** and **necromancer** as the other classic pullers, ranking them above
bard ("death knight before bard, bard before necromancer" — i.e. DK > bard > necro), and would
call death knight before the AI's suggestion of bard. The puller manages the feed of monsters
into the group — a tactical layer WoW largely dropped.

**A codex / bestiary / party-logbook** was called for: tracking enemy types and behaviors
encountered, party configurations used, and notes left by prior runs — knowledge accrued over
time as part of the fun.

**AI-generated elaboration (Elideus did not author these; flagged where they conflict):**
- *Aligned with current canon:* no matchmaking; clan-based / recurring-group play; consumable
  scarcity and attrition (mana, cooldowns, health do not auto-refill without planning);
  meaningful downtime; tension curve over checkpoints; "trash" mobs as tactical puzzles rather
  than autofarm.
- *CONFLICTS with current canon:* the assistant framed dungeons as **"permadeath layers
  (roguelite): you fail = start over"** with **"no checkpoints."** This contradicts the ruled
  death model (Book I; ledger `0B98560B`): combat death is **respawn + EverQuest-style corpse
  recovery**, terminal exits are *additive* dispositions, and only **Burning** subtracts. The
  **difficulty philosophy** (hardcore, lethal, cooperation-mandatory) survives; the
  **roguelite-restart / permadeath-layer** elaboration does not.

---

## Part 2 — Stat-Scaling Damage Math (worked example)

A concrete damage formula developed with a Dexterity/katana example. Elideus corrected the
assistant's first (flat) reading into a **tiered diminishing-returns curve**, then applied a
**weapon-skill grade multiplier** (letter grades, Souls-style S/A/B/C/D). Base damage before any
deflection/absorption/other mitigation:

**Stat → base damage (tiered, diminishing returns):**

| Stat range | Per-point multiplier | Base damage at top of range |
|---|---|---|
| 10 (baseline) | ×2 | 20 |
| 11–20 | ×2 (+2 per point) | 40 |
| 21–40 | ×1.5 (+1.5 per point) | 70 |
| 41–45 | ×1 (+1 per point) | 75 |

**Worked example — 45 DEX, katana at "B" skill grade (×1.5):**
- Baseline (10 DEX): 20
- +11–20 (10 pts × 2): +20 → 40
- +21–40 (20 pts × 1.5): +30 → 70
- +41–45 (5 pts × 1): +5 → **75 base damage**
- Apply weapon-skill grade **B = ×1.5**: 75 × 1.5 = **112.5 final damage** (pre-mitigation)

Earlier in the session Elideus referenced pre-built tables of "stat scaling based on progression"
and "weapon scaling multipliers based on skill" — i.e. the letter-grade weapon-scaling column is
part of the original conception, not an ad-hoc number.

*Reconciliation:* this is a candidate for Book I's **`[BUILD]` derived-value formulas** (ledger
`DE7E8605`), specifically the weapon-scaling grades. Note current canon separates **affinity**
(the abstract color that sets *which stat* a weapon scales) from a possible **skill** grade;
the old "katana wielding skill" letter grade could map to the affinity-scaling grade, to the
reserved layered skill system (ledger `F618F695`), or to both. Integration is a design question,
not settled here. Damage staying "real and exact beneath the surface" while the player sees only
a normalized 0.0–1.0 bar (ledger `BFBE6085`) is consistent with hiding a formula like this.

---

## Part 3 — Color Counter/Synergy Web and the Enchantment-Slotting Exercise

An exercise slotting status-effect enchantments into the seven color schools across four "rings"
(Ring I–IV), with the constraint that **each effect appear in at least three schools** (themed
differently per school — e.g. root as White "Binding", Black "Grave", Green "Root", Blue
"Freeze"). The specific enchantment names are largely superseded by the current **Words of Power
grammar** (nouns/verbs/adjectives/shapes, Book IV) and the **ring** research track (ledger
`B92EE74A`). Two durable pieces:

**The color counter / synergy web (as stated in the exercise):**

| School | Counters | Synergy with |
|---|---|---|
| White | Black, Orange | Yellow, Green |
| Yellow | Black, Blue | White, Red |
| Red | Blue, Green | Yellow, Orange |
| Orange | Green, White | Red, Blue |
| Black | White | *(none listed)* |
| Blue | Yellow, Red | Green, Orange |
| Green | Red, Orange | Blue, White |

*Reconciliation:* Black counters/synergizes as an outlier (only "counters White," no synergy) —
consistent with current canon's **"Black combines with nothing"** (Book V; ledger `442D03E8`)
and Book IV's synergy-cycle bypass. The synergy pairings trace the same six-school loop Book IV
records. This web is provenance for Book IV's synergy/counter relationships; the
**synergy-cycle-vs-genealogy ordering fork** (ledger `244A27FF`) is still open and is NOT
resolved by this document.

**The balancing principle:** every status effect is distributed across **≥3 schools**, so no
single school monopolizes a control effect — an early expression of the effect-vocabulary
balance now handled by the Words-of-Power dictionaries.

The full effect list used (matches Book IV's Combat Mechanics taxonomy): root, snare, slow,
expose, poison, disease, stun, silence, distract/confound, sunder, fear, panic, charm.
