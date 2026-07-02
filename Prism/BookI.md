# I. Adventurer's Design

This book defines the adventurer's side of Prism: the character — their stats, their combat, their life, and their family line. Adventurer gameplay is a classic MMO. The Dungeon Maker population never interacts with adventurers directly; the coupling is asynchronous — dungeons are built, published, discovered, and run, never contested head-to-head (Book II; ledger C91261FB).

---

## The Seven Stats

The seven stats are canonical, one per school of magic (Book V, Canon Rulings 2026-07-02; ledger 2ABDD515). Each stat is the capacity that its school's realm studies and reinforces, paired with that school's philosophy (Book V).

| Stat | School | Domains | Philosophy |
|---|---|---|---|
| Wisdom | White | Light and Prophecy | Enlightenment vs Mendacity |
| Dexterity | Yellow | Air and Lightning | Courage vs Audacity |
| Strength | Red | Fire and Blood | Valor vs Wrath |
| Luck | Orange | Chaos and Transformation | Diligence vs Anarchy |
| Intelligence | Blue | Water and Illusion | Knowledge vs Truth |
| Endurance | Green | Earth and Life | Perseverance vs Relentlessness |
| Constitution | Black | Death and Void | Transcendence vs Ambition |

Stats measure **capacities, not actions**. Charisma is excluded on exactly this rule: charm is something a character *does*, not something a character *has* — and where a charisma-like check is required, it uses **Luck**. (Ledger 2ABDD515.)

Constitution and Endurance never collapse into one stat. **Constitution (Black) is the capacity to be hit. Endurance (Green) is the capacity for sustained effort.** One measures what the body withstands; the other measures what the body spends. (Ledger 2ABDD515.)

Every stat must cash out in combat-relevant terms (ledger 2ABDD515). How each one does so is only partly recorded:

> **[PROPOSED]** The two capacities canon defines translate directly into the combat framework below (basis: their canonical definitions in ledger 2ABDD515 plus the Souls-style combat frame, ledger 9D249EE4):
> - **Constitution** governs how much punishment a character absorbs before falling — the budget of hits a body can take.
> - **Endurance** governs the sustained-effort resource spent on continuous exertion in combat — the budget of actions a body can drive.

> **[STUB]** Combat readings for the remaining five stats — how Strength, Dexterity, Intelligence, Wisdom, and Luck cash out in combat is unrecorded.
> - **[OPEN QUESTION]** Does Intelligence gate spell learning? Book IV says cantrips can be cast "by anyone with sufficient intelligence and basic magical training" — whether that names the Intelligence stat or merely the word is unconfirmed.
> - **[OPEN QUESTION]** Does Luck's charisma-adjacent role extend to loot, discovery, or other fortune-shaped outcomes? Unrecorded.
> - **[OPEN QUESTION]** Celestial events are deterministic and foretold in the sky, readable by "players who learn the heavens" (ledger 8FB95281). Does Wisdom — the stat of Light and *Prophecy* — govern that reading, or is it pure player knowledge? Unrecorded.

---

## Combat Framework

Combat is **Dark Souls–style action combat**. The combat simulation runs on a **frame-accurate combat tick clock, decoupled from render framerate**. Attacks, hitboxes, invulnerability frames, and effects are authored as **TAE-style event timelines** — events keyed to combat ticks on an animation timeline. (Ledger 9D249EE4, Seed canon 5. No engine document yet describes this design; the ledger entry is the canon source.)

Per "data is truth; code and geometry are render targets" (ledger 65C82EE0), tick rates, timeline formats, and other implementation specifics belong to engine documentation, not this book. What belongs here is the design truth: combat outcomes are decided by a deterministic tick simulation, and everything a combatant does is an authored timeline of events on that clock.

> **[STUB]** Everything beyond the facts above is undesigned or unrecorded: resource systems (stamina or its equivalent), poise and stagger, lock-on and targeting, block/parry/dodge specifics, damage typing, ranged and magical delivery, timing values, and how the seven stats parameterize the simulation.
> - **[OPEN QUESTION]** Is there an Endurance-governed action resource gating attacks and dodges, per the [PROPOSED] stat reading above?
> - **[OPEN QUESTION]** Spells are researched and memorized before casting (Book IV). Do spell casts occupy TAE-style combat timelines the same way weapon attacks do?
> - **[OPEN QUESTION]** Celestial events are global modifiers across all tiers and regions (ledger 8FB95281). How do they express in combat terms — damage, resources, timeline behavior?
> - **[OPEN QUESTION]** What does death in combat mean for the character and their family line? (Ledger D25A57E1.)

---

## Character Lifecycle and the Generational Dynasty System

An adventurer is one life in a family line. The character system is **generational**: a **family tapestry** records the line; characters leave active play through defined **retirement flows**; and the peoples of Prism trade lifespan against generational turnover — longer-lived races trade turnover for continuity, shorter-lived races cycle through the family tapestry faster. (Ledger 10A6150F, Seed canon 12; corroborated by Book V, Peoples of Prism.) The races themselves are Book V material and are currently a stub there.

> **[STUB]** The mechanics of the lifecycle and dynasty system are unrecorded beyond the facts above.
> - **[OPEN QUESTION]** What transfers across generations — items? school mastery? reputation? ring progress? (Ledger D2C52C88.)
> - **[OPEN QUESTION]** What ends an active life: retirement only, or combat death too? (Ledger D25A57E1.)
> - **[OPEN QUESTION]** Is the family tapestry a literal in-game artifact and interface, or a structural name for the family tree? Unrecorded.
> - **[OPEN QUESTION]** How new members join the tapestry — birth, marriage, adoption, recruitment — is unrecorded.
> - **[OPEN QUESTION]** Does one player steward one line, or several? Unrecorded.

---

## Progression

The only progression fact currently ratified is economic: an uncompletable dungeon yields no XP and no traffic (ledger 49A3A9D6, Seed canon 8). Experience exists, and completing dungeons is at least one source of it; fairness is enforced by that incentive structure, not by moderation.

> **[STUB]** The ring progression. Book IV references a ring progression — mages gain their synergy schools' shapes at the **4th ring** and their secondary synergy shapes at the **7th ring**, and spells are "arranged by school and ring" — but no book defines what rings are. Ownership of the definition is an open fork (ledger 63B28A6B): **Option A**, rings are a character-progression tier system and belong here in Book I; **Option B**, rings are a magic-mastery structure internal to Book IV. This section anchors the Book I side of that fork without defining rings.
> - **[OPEN QUESTION]** Who owns rings — the fork itself (ledger 63B28A6B). Not resolved here.
> - **[OPEN QUESTION]** If Book I owns them: do rings measure per-school mastery or whole-character tier? Book IV's text implies at least seven rings exist; the actual count, and what advancement costs, are unrecorded.
> - **[OPEN QUESTION]** How ring advancement interacts with the unresolved synergy-cycle orderings (ledger 244A27FF) and with Black's exclusion from ring-based synergy (Book IV; ledger 442D03E8 — Black combines with nothing).
> - **[OPEN QUESTION]** Whether ring progress transfers across generations (ledger D2C52C88).
> - **[OPEN QUESTION]** Progression beyond rings — levels, XP curves, skill training — is entirely unrecorded.

---

## The Endgame Arc

The endgame of the adventurer's game spans character lifetimes: **master all seven schools across the generations of a family line, and, during a celestial alignment, reunite or re-shatter the Prism.** (Ledger 10A6150F, Seed canon 12.)

Celestial events are global modifiers, deterministic and foretold: an alignment is never scripted or random — it emerges from real orbits, and those who learn the heavens can predict it (ledger 8FB95281, Seed canon 6). The endgame's moment is therefore something the whole world can see coming.

> **[OPEN QUESTION]** **Reunite vs re-shatter.** What each choice means — mechanically for the world, mythologically for the story — is unrecorded. The mythic frame (Book V, Book VI) gives the stakes without the mechanics: the Prism was shattered to contain the Lonely Muse, so *reunification* reads as restoring the original unity and reopening whatever the Shattering closed, while *re-shattering* reads as renewing the containment for another age. Whether those readings hold, whether the choices oppose factions, and what either does to a live world: unresolved. (Ledger 10A6150F names the fork; do not resolve here.)
>
> **[OPEN QUESTION]** **How mastery accumulates across a dynasty.** Per-character mastery aggregated at the family level? A family ledger of schools mastered? Must a single line master all seven, one life per school, or may lives overlap? This is governed by the inheritance question (ledger D2C52C88).
>
> **[OPEN QUESTION]** **Scale of resolution.** Adventurer gameplay is a shared-world MMO (ledger C91261FB). Does one dynasty completing the arc change the world for everyone, resolve in an instanced or mythic frame, or recur cyclically with the celestial clock? (Ledger 432AAB1F.)

Related forks held elsewhere:

- Whether "all seven schools" includes psionics — a discipline outside the seven schools — is unresolved (ledger 7609E7E9).
- Which celestial bodies participate in the alignment turns on the cosmology fork: four Mortal Realm planets plus ethereal realms (Book V) vs seven elemental planets in orbital order (ledger 973162E7).
- Black combines with nothing (ledger 442D03E8) and is excluded from ring-based shape synergy (Book IV). Whether the path to Black mastery differs structurally from the other six schools is unrecorded.
