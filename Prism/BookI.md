# I. Adventurer's Design

This book defines the adventurer's side of Prism: the character — their stats, their combat, their life, and their family line. Adventurer gameplay is a classic MMO. The Dungeon Maker population never interacts with adventurers directly; the coupling is asynchronous — dungeons are built, published, discovered, and run, never contested head-to-head (Book II; ledger C91261FB).

---

## The Seven Stats

The seven stats are canonical, one per color of magic (Book V, Canon Rulings 2026-07-02; ledger 2ABDD515, realigned by FF1F7955). Each stat is the capacity that its color's realm studies and reinforces, paired with that color's philosophy pair (Book V). Each color fields **two schools** — one per aspect, fourteen among the seven shard worlds — and the philosophy belongs to the color: followers of both poles study at both of its schools (ledger FF1F7955).

| Stat | Color | Schools | Philosophy (honorable vs dishonorable) |
|---|---|---|---|
| Wisdom | White | Light and Prophecy | Enlightenment vs Revelation |
| Dexterity | Yellow | Air and Lightning | Courage vs Audacity |
| Strength | Red | Fire and Blood | Valor vs Conquest |
| Luck | Orange | Chaos and Transformation | Diligence vs Cunning |
| Intelligence | Blue | Water and Illusion | Knowledge vs Truth |
| Endurance | Green | Earth and Life | Perseverance vs Hunger |
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

**Source material.** Ideation-only design notes from 2014 are archived at `sources/combat-systems-ideation-2014.md` (intake ruling: ledger 78C70439). They are twelve-year-old ideation, not canon, but carry the payload Elideus marked durable: a status-effect taxonomy treated as **direct game mechanics** — stun, snare, slow, root, poison, confound/distract, aphasia, fear, confuse, silence, expose, tashina, mesmerize — plus time/distance/movement constraints: attack property flags (physical/magic × melee/ranged/point-blank AE/targeted AE/cone/line), projectile travel, channeling as a self-root with tick-applied effects, displacement as velocity-on-hit, and cooldown discipline. The stat-to-mechanics coupling is design-and-build work still ahead (ledger 78C70439); the notes inform the [STUB] below without resolving it.

**The fairness law.** Canon, in Elideus's words (Half-Life 1998 design lineage; ledger 95EAF28D): *"If the player dies, they can only die because they missed something… The player cannot blame the designer for failure."* Combat is telegraph-and-dodge. Every threat carries two readable layers: a **spatial tell** — danger is a legible place, entered by choice — and a **temporal tell** — the attack telegraphs before it lands, and the counter-window keys to the tell. Lethality may be extreme (one-shot kills are permitted); legibility is non-negotiable. The canonical exemplar: shadow wisps that decapitate in one hit live only in mud, and the mud bubbles before they strike — avoid the mud and you are categorically safe; enter it, and the bubbles are the contract.

> **[STUB]** Everything beyond the facts above is undesigned or unrecorded: resource systems (stamina or its equivalent), poise and stagger, lock-on and targeting, block/parry/dodge specifics, damage typing, ranged and magical delivery, timing values, and how the seven stats parameterize the simulation.
> - **[OPEN QUESTION]** Is there an Endurance-governed action resource gating attacks and dodges, per the [PROPOSED] stat reading above?
> - **[OPEN QUESTION]** Spells are researched and memorized before casting (Book IV). Do spell casts occupy TAE-style combat timelines the same way weapon attacks do?
> - **[OPEN QUESTION]** Celestial events are global modifiers across all tiers and regions (ledger 8FB95281). How do they express in combat terms — damage, resources, timeline behavior?
> - **[OPEN QUESTION]** What does death in combat mean for the character and their family line? (Ledger D25A57E1.)

---

## Character Lifecycle and the Generational Dynasty System

An adventurer is one life in a family line. The character system is **generational**: a **family tapestry** records the line; characters leave active play through defined **retirement flows**; and the peoples of Prism trade lifespan against generational turnover — longer-lived races trade turnover for continuity, shorter-lived races cycle through the family tapestry faster. (Ledger 10A6150F, Seed canon 12; corroborated by Book V, Peoples of Prism.) The races themselves are Book V material and are currently a stub there.

Two further facts are canon (ledger EC054473):

- **Every new game begins with three helper NPCs** besides the adventurer — the character's parents and a benefactor relative (a sibling, uncle, aunt, or grandparent) — for example, one who makes food, one who makes and mends clothing, and a specialist who teaches. The opening is survival-hard: a hostile world, scarce resources, a weak character, and nothing in hand but the people standing with you.
- **Retirement is a category, not one ending.** Many terminal quest lines end a character — evolving them into certain kinds of powered creatures or enabling permanent effects — and each retirement deposits a permanent marker on the account's tapestry. The Muse's path (see The Endgame Arc) is the apex member of the category.

The tapestry is also the game's real achievement system: prestige lives in-world as permanent account markers, not in platform popups (ledger EC054473).

The lifecycle's economics are ruled (Elideus, 2026-07-02; ledger 91F84075):

- **The child.** An offspring is an investment requiring maintenance: ongoing payment of in-game currency builds the child to adventurer's age, and a raised child is what a new character is eventually rolled from. The investment need not begin the moment they come of age — but it cannot be skipped and cannot be bought around: **nothing is pay-to-play, ever.** "Old school RPG for life."
- **The adventurer.** The character you play — **no take backsies**. Skill them up, live, explore, learn, acquire; at **level 10** comes a yearning to retire: you recognize your strengths and choose your benefits for the family, as permanent effects. Other endings feed the same system — a heroic sacrifice in an epic battle can become a permanent badge of glory for the account; any number of effects can be built off this system.
- **Enchanted items obey the same law.** Long-term enchantments require regular mana investment at the enchanting table. You can't fake anything — the same rule as the child, the claim, and the dungeon: nothing persists that no one maintains.

> **[PROPOSED]** A wider thread-state sketch exists from the same session — Living → Retired (role computed from the life actually lived) → Dead (tombstone) → Ghost (earned re-activation) → Burned (spent forever for a lasting effect); race as a tempo dial, lifespan trading against offspring slots; multi-generation dynasty tracks unlocking bloodline entitlements. Elideus's verdict was "not quite what I had in mind, but pretty close" — unratified. (Ledger A8FEC45C.)

> **[STUB]** The mechanics of the lifecycle and dynasty system are unrecorded beyond the facts above.
> - **[OPEN QUESTION]** What transfers across generations — items? school mastery? reputation? ring progress? (Ledger D2C52C88.)
> - **[OPEN QUESTION]** What ends an active life beyond the ruled endings — retirement at level 10 (chosen, "a yearning") and heroic-sacrifice deaths that become account badges (ledger 91F84075)? Whether ordinary combat death ends a life is still open. (Ledger D25A57E1.)
> - **[OPEN QUESTION]** Is the family tapestry a literal in-game artifact and interface, or a structural name for the family tree? Unrecorded.
> - **[OPEN QUESTION]** How members join beyond the ruled paths — invested children (ledger 91F84075) and adoption (the Muse-vessel gate, EC054473). Marriage and recruitment are unrecorded, as is the unit of inheritance (one-parent, whole-tapestry, or chosen-mentor — posed unanswered, ledger A8FEC45C).
> - **[OPEN QUESTION]** Does one player steward one line, or several? Unrecorded.

---

## Progression

The only progression fact currently ratified is economic: an uncompletable dungeon yields no XP and no traffic (ledger 49A3A9D6, Seed canon 8). Experience exists, and completing dungeons is at least one source of it; fairness is enforced by that incentive structure, not by moderation.

Three further facts are canon (ledger 91F84075): **levels exist, and level 10 is the retirement threshold** — the point at which the yearning to retire arrives; the **skill system is deep, complex, and completely opaque to the player**, learnable only through brutal trial and error, while remaining honest — deterministic, predictable, and fair (the fairness law, applied to progression); and **the rules never bend** — costs are paid in full over real time, with no accommodation for schedules and nothing pay-to-play, ever.

> **[STUB]** The ring progression. Book IV references a ring progression — mages gain their synergy schools' shapes at the **4th ring** and their secondary synergy shapes at the **7th ring**, and spells are "arranged by school and ring" — but no book defines what rings are. Ownership of the definition is an open fork (ledger 63B28A6B): **Option A**, rings are a character-progression tier system and belong here in Book I; **Option B**, rings are a magic-mastery structure internal to Book IV. This section anchors the Book I side of that fork without defining rings.
> - **[OPEN QUESTION]** Who owns rings — the fork itself (ledger 63B28A6B). Not resolved here.
> - **[OPEN QUESTION]** If Book I owns them: do rings measure per-school mastery or whole-character tier? Book IV's text implies at least seven rings exist; the actual count, and what advancement costs, are unrecorded.
> - **[OPEN QUESTION]** How ring advancement interacts with the unresolved synergy-cycle orderings (ledger 244A27FF) and with Black's exclusion from ring-based synergy (Book IV; ledger 442D03E8 — Black combines with nothing).
> - **[OPEN QUESTION]** Whether ring progress transfers across generations (ledger D2C52C88).
> - **[OPEN QUESTION]** Progression beyond rings — levels, XP curves, skill training — is entirely unrecorded.

---

## The Endgame Arc

The endgame of the adventurer's game spans character lifetimes: **master all seven schools across the generations of a family line, and, during a celestial alignment, reunite or re-shatter the Prism.** (Ledger 10A6150F, Seed canon 12.)

Celestial events are global modifiers, deterministic and foretold: an alignment is never scripted or random — it emerges from real orbits, and those who learn the heavens can predict it (ledger 8FB95281, Seed canon 6). The endgame's moment is therefore something the whole world can see coming — and since the moon runs on real wall-clock ephemeris (Book V; ledger D2AAFEEC), the appointment is computable from the actual sky.

**The arc is the Muse's path** (ruled 2026-07-01/02; ledgers BDB707A5, EC054473). The player walks the road the Lonely Muse walked — apprentice at all seven schools in one lifetime, master them all, and stand at the summit she was denied (Book VI). Completing it is a **terminal epic quest**: the choice between reuniting and re-shattering is offered, made personally, and **retires the character**. The shared world persists — permanent world-scale change is not simulated; "that's where a character would retire." Nobody does this by accident, or on their first character, or their tenth.

The gate stack is canon (ledger EC054473):

1. The account's tapestry must already record a **leveled and retired character in each of the seven schools** — seven completed lifetimes as the price of eligibility.
2. The vessel must be a **near-immortal race** (an elf-type with five human lifetimes of learning done by age one hundred) — or a character of another race prepared through an adoption setup and massive tutoring investment.
3. The quest must be completed **during a celestial eclipse of the Chalice** — the moon–Death alignment that reveals the Muse's hidden constellation (Book VI; ledger AF819A62).
4. The reward is a **permanent account marker on the tapestry** — a major permanent account-wide bonus ("a permanent patron of all magic, something along those lines").

*[OPEN QUESTION — the arc and the gate say "seven schools", phrasing recorded before the 2026-07-02 realignment (two schools per color, fourteen among the seven worlds — ledger FF1F7955). Whether eligibility means one school per color, all fourteen, or seven-for-the-gate and fourteen-for-the-vessel is an open re-reading — ledger FCB93BC0. Do not resolve here.]*

> **[OPEN QUESTION]** **Reunite vs re-shatter — the meaning.** The mechanical scale is ruled (personal, terminal); what each choice *means* — mythologically, and in whatever the retiring character leaves behind — is unrecorded. The mythic frame gives stakes without specifics: reunification reads as restoring the unity the Titans broke; re-shattering as renewing the containment for another age. What the choice options actually are, and whether factions align to them (Book VI, Those Who Remember the Muse), remains open.
>
> **[OPEN QUESTION]** **Inheritance beyond mastery.** School mastery accrues at the account level — one retired character per school (ruled above). What else transfers across generations — items, reputation, ring progress — is still the open inheritance fork (ledger D2C52C88), as is what combat death costs the line (ledger D25A57E1).

Related forks held elsewhere:

- Whether "all seven schools" includes psionics — a discipline outside the seven schools — is unresolved (ledger 7609E7E9).
- Black combines with nothing (ledger 442D03E8) and is excluded from ring-based shape synergy (Book IV). Whether the path to Black mastery differs structurally from the other six schools is unrecorded.
