# I. Adventurer's Design

This book defines the adventurer's side of Prism: the character — their stats, their combat, their life, and their family line. Adventurer gameplay is a classic MMO. The Dungeon Maker population never interacts with adventurers directly; the coupling is asynchronous — dungeons are built, published, discovered, and run, never contested head-to-head (Book II; ledger C91261FB).

---

## The Seven Stats

The seven stats are canonical, one per color of magic (Book V, Canon Rulings 2026-07-02; ledger 2ABDD515, realigned by FF1F7955). Each stat is the capacity that its color's realm studies and reinforces, paired with that color's philosophy pair (Book V). Each color fields **two schools** — one per Domain (aspect), fourteen among the seven shard worlds, with disciplines inside each school: the types of spells documented in Book IV, each discipline a skill in the skill system (ledgers FF1F7955, A8FF6AB0, DCB350D4, 232B6EEE) — and the philosophy belongs to the color: followers of both poles study at both of its schools. The two poles are deliberately unlabeled and unjudged — which is right is the player's own conclusion (ledger E4F46BA5).

| Stat | Color | Schools | Philosophy |
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

Every stat must cash out in combat-relevant terms (ledger 2ABDD515), and each is designed to be useful in as many ways as possible — no single-purpose stats (ledger DE7E8605). The combat lanes are ruled (2026-07-02; Constitution and Endurance from 2ABDD515, the other five from DE7E8605):

| Stat | Color | Combat lane |
|---|---|---|
| **Constitution** | Black | **Survivability.** The hit-budget — how much punishment absorbed before falling — plus poise and resistance to death-tier afflictions (instant-death, rot, curse/void). Governs the **Health** bar. |
| **Endurance** | Green | **Action economy.** The sustained-effort resource every exertion spends — attack, dodge, block, sprint — and the rate it recovers and stagger clears. Governs the **Stamina** bar. |
| **Strength** | Red | **Force.** Heavy-weapon scaling, guard-break / poise-damage, heavy-impact stagger, and bleed buildup (the Blood domain). |
| **Dexterity** | Yellow | **Speed & precision.** Finesse/ranged scaling, attack and recovery speed, evasion / i-frame efficiency, ranged accuracy, and interrupt/stun on precise strikes (Lightning). |
| **Intelligence** | Blue | **Technique, the mind, and knowledge.** In combat: status/mind-affliction potency and resistance, weakpoint/critical knowledge (*expose*), and combat-art access. Out of combat: the **research gate** — the requirement to unlock higher learning. |
| **Wisdom** | White | **Foresight & the divine.** Telegraph-reading clarity and parry/guard-counter window width (the fairness law as a stat), divine-magic and warding potency, and resistance to fear/illusion/mind effects. |
| **Luck** | Orange | **Fortune & chaos.** Critical chance, the reliability of procs (does your bleed/stun land, or theirs on you), ambush/first-strike advantage, **loot and discovery fortune**, and any charisma-shaped check (ledger 2ABDD515). |

Three prior open questions close with this table (ledger DE7E8605): **Intelligence gates research** — you cannot unlock higher learning without meeting its requirement, and rings, affinities, shapes, and access to Words are all gated by research (see *Areas of Focus and Talent Graphs*, and the Long-Term-Objective layer under Progression); **Luck governs loot and discovery**; and **Wisdom does *not* read the celestial sky** — reading the deterministic heavens is the literal player's own skill, out-of-character, not a character stat.

> **[BUILD]** The *derived-value formulas* — how each stat computes its bar, poise, crit %, proc reliability, parry-window frames, telegraph clarity, bleed/status power, and weapon-scaling grades — are the next design pass. The lanes are ruled; the numbers are not yet.

---

## Combat Framework

Combat is **Dark Souls–style action combat**. The combat simulation runs on a **frame-accurate combat tick clock, decoupled from render framerate**. Attacks, hitboxes, invulnerability frames, and effects are authored as **TAE-style event timelines** — events keyed to combat ticks on an animation timeline. (Ledger 9D249EE4, Seed canon 5. No engine document yet describes this design; the ledger entry is the canon source.)

Per "data is truth; code and geometry are render targets" (ledger 65C82EE0), tick rates, timeline formats, and other implementation specifics belong to engine documentation, not this book. What belongs here is the design truth: combat outcomes are decided by a deterministic tick simulation, and everything a combatant does is an authored timeline of events on that clock.

**Source material.** Ideation-only design notes from 2014 are archived at `sources/combat-systems-ideation-2014.md` (intake ruling: ledger 78C70439). They are twelve-year-old ideation, not canon, but carry the payload Elideus marked durable: a status-effect taxonomy treated as **direct game mechanics** — stun, snare, slow, root, poison, confound/distract, aphasia, fear, confuse, silence, expose, tashina, mesmerize — plus time/distance/movement constraints: attack property flags (physical/magic × melee/ranged/point-blank AE/targeted AE/cone/line), projectile travel, channeling as a self-root with tick-applied effects, displacement as velocity-on-hit, and cooldown discipline. The stat-to-mechanics coupling is design-and-build work still ahead (ledger 78C70439); the notes inform the [STUB] below without resolving it.

**The fairness law.** Canon, in Elideus's words (Half-Life 1998 design lineage; ledger 95EAF28D): *"If the player dies, they can only die because they missed something… The player cannot blame the designer for failure."* Combat is telegraph-and-dodge. Every threat carries two readable layers: a **spatial tell** — danger is a legible place, entered by choice — and a **temporal tell** — the attack telegraphs before it lands, and the counter-window keys to the tell. Lethality may be extreme (one-shot kills are permitted); legibility is non-negotiable. The canonical exemplar: shadow wisps that decapitate in one hit live only in mud, and the mud bubbles before they strike — avoid the mud and you are categorically safe; enter it, and the bubbles are the contract.

**Resources — three bars, no numbers.** Combat runs on three meters — **Health** (Constitution), **Stamina** (Endurance), and **Mana** (the caster resource). Each is **scaled to 100, drawn at a fixed size with no markers, and shown only as a normalized fraction (0.0–1.0)** — damage is real and exact beneath the surface, but the player never sees an absolute number (ledger BFBE6085). This is the surviving, light form of a wider **philosophy of ambiguity**: telling the player as little as possible about the machinery beneath, the opposite of Souls' explicit stat accuracy. *(An earlier "OneBar" concept — a single blended Health/Stamina/Mana meter damaged as Physical / Effort / Mental — was considered and discarded: it conflicts with Prism's very explicit crafting, skill, and requirement systems. How far the ambiguity philosophy reaches beyond the number-hiding bars and the journal (see Progression) is itself a major open decision.)*

> **[BUILD]** The combat frame is set; the numbers are not. Still to design: poise and stagger thresholds, lock-on and targeting, block/parry/dodge frame values, damage typing and resistances, ranged and magical delivery timing, and how each stat's derived values parameterize the simulation. (Resources, weapons, and advancement are framed in the sections that follow.)
> - **Resolved:** Endurance governs the **Stamina** bar — the action resource every attack, dodge, and block spends (ledgers 2ABDD515, BFBE6085).
> - **[OPEN QUESTION]** Spells are researched and memorized before casting (Book IV). Do spell casts occupy TAE-style combat timelines the same way weapon attacks do?
> - **[OPEN QUESTION]** Celestial events are global modifiers across all tiers and regions (ledger 8FB95281). How do they express in combat terms — damage, resources, timeline behavior?
> - **Combat death is not terminal** (ruled 2026-07-02, ledger 0B98560B, resolving D25A57E1): you **respawn** — however lore explains it (magic; "it doesn't matter, literally") — and recover your body **EQ-style**, sometimes dragging your corpse back from where you fell. Ordinary combat death is a setback, not the end of a life. See *Death and Disposition* below.

---

## Weapons and Affinity

*(Framework [PROPOSED]; specific requirements, grades, and movesets are [BUILD]. The ruled points — affinity is abstract, roles are open — are noted inline.)*

Weapons are drawn from real materials and read as real materials: **normal metals, gothic and grim, with at most the slight tints of their alloys.** Any color a weapon throws is earned — the red glow of an enchant, the flash of a proc — never the base blade (ledger DE7E8605). Under that realistic surface, every weapon carries an **affinity**: an abstract, mechanical alignment to one of the seven colors — *not* a visual color — set by its material and shiftable by artificing, which determines the stat its output scales with. A Red-affinity arm scales Strength; a Yellow-affinity arm scales Dexterity; and so on down the seven (Pillar B; ledger DE7E8605). Wielding is governed two ways: a **requirement** — a stat minimum to use the weapon without escalating penalty (you *can* swing anything, badly) — and **scaling**, the affinity above. Each category is also a **moveset**, a family of authored TAE timelines (the seam where combat meets the animation pipeline); stats parameterize the numbers on those timelines, not their shape.

| Category | Role | Requires | Scales (via affinity) | Signature |
|---|---|---|---|---|
| Heavy arms (greatswords, mauls, greataxes) | **Breaker** | High Str + End | Str | Poise-break, huge stagger, slow |
| Martial arms (swords, spears, axes, maces) | **Soldier** | Moderate Str & Dex | Str or Dex | Reliable, balanced |
| Finesse arms (daggers, rapiers, curved blades, whips) | **Assassin** | Dex (+ Luck) | Dex | Fast; crit/bleed on precision |
| Ranged physical (bows, crossbows, thrown) | **Archer** | Dex (Str for warbows) | Dex | Projectile travel; weakpoints |
| Reach / polearms (pikes, glaives, halberds) | **Skirmisher** | Str/Dex | Str or Dex | Spacing, control, anti-approach |
| Fist / martial (gauntlets, claws, unarmed) | **Brawler** | Dex/Str | Dex or Str | Stamina-cheap, rapid, close |
| Shields & guard gear | **Warden** | Con/End to block; Wis to parry | Con/End (block), Wis (parry) | Block scales toughness; parry scales foresight |
| Catalysts & foci (staves, wands, talismans, holy symbols) | **Caster** | Int (literacy) + ring standing | Int/ring; Wis for divine foci | Channel Words; reagent-grade foci never deplete (Book IV) |
| Exotic / chaos arms | **Gambler** | Luck | Luck | Proc-heavy, unpredictable |

> **[OPEN QUESTION]** Whether triggering a weapon's *elemental proc* (a Red blade's fire, a Blue blade's illusion) additionally requires matching color/school attunement, or anyone can set it off. Unrecorded.

**Items are enhanced here, not made here.** Item *creation* belongs to the Dungeon Maker system (Book II); adventurers **mostly enhance** what they find rather than forge it new (ledger DE7E8605). Enhancement runs on the same seams as scaling — affinity sets the scaling stat, the loot stack's adjective rung sets the grade, its shape rung sets the on-hit proc (Book II) — and any lasting enchantment demands ongoing mana upkeep, the same law as everything else (ledger 91F84075).

---

## Areas of Focus and Talent Graphs

*(Frame ruled; the specific graphs and nodes are [BUILD]; the deep skill-scope system is reserved — ledger F618F695.)*

Prism has **no character classes.** This is **open build, in the lineage of the Souls-likes**: a character is defined by their affinities and by where they have spent, not by a label chosen at creation. The **Roles** above — Breaker, Soldier, Assassin, Archer, Skirmisher, Brawler, Warden, Caster, Gambler — are **areas of focus**: any character may research and spend experience in any of them, and their "role" *emerges* from that investment (ledger DE7E8605).

Each Role is a natural fit for a **simple talent graph**, kept deliberately light — easy decisions, clear outcomes, in the register of early-World-of-Warcraft talents — because there are many of them. **Hybrid graphs** bridge adjacent Roles, and the set may be arranged in the **septisigil wheel** (tentative). Unlocking a graph can take work: research and stat requirements gate the higher reaches (Intelligence is the research gate).

**Every investment is permanent.** There is no respec — you may spread your points across many focuses, but no choice is ever undone. This is the build-side face of the character's own "no take backsies" (ledger 91F84075), the same law as the mana-upkeep economy: nothing in Prism is free to reverse. The strategic weight therefore lands on *what to pursue* — planned as a **Long-Term Objective** for the account, not optimized after the fact — and the family tapestry is itself that strategic game (ledger DE7E8605).

> **[BUILD]** The actual graphs, their nodes and costs, the hybrid bridges, and whether the septisigil arrangement holds. The **layered skill-scope system** beneath all of this (how "learning about axes teaches wood, farming, and combat," across three or four nested scopes) is a **major reserved topic** (ledger F618F695) and is not elaborated here.

---

## Group Combat and the Threat Model

*(Framework [PROPOSED]; the numbers are [BUILD]. Group combat takes the Souls action model to EverQuest scale.)*

Group combat is **Dark Souls action combat at EverQuest scale** — large-monster fights few games attempt, kept honest by the fairness law even when forty people share one boss. The **event system is what makes it possible**: because every attack is an authored TAE timeline (Combat Framework), a boss can **select targets for ranged attacks** and **catch clusters of players in a single swing**, and **every player caught reacts on their own dodge and parry window.** Forty individual skill-checks resolve against one boss's timeline at once (ledger A573A152).

**Threat, not class, decides who the boss hits.** Aggro is a **threat table** any build can climb by what it does; the boss swings at whoever holds it. **Roles are jobs, not classes** (open build; *Areas of Focus*): a "tank" is *hold threat + survive the incoming*, and survival is paid either in armor (Constitution/block — the Warden) **or** in pure skill (perfect parry — Wisdom). A cloth-clad dagger master can tank a boss the whole fight — holding aggro, parrying every swing — **when the boss has parryable attacks and they can keep threat.** Parry-tanking is legitimate but conditional; **each combat is unique and its solutions are multiple** — no dominant strategy survives contact with the next boss.

**Casters are power bought with fragility.** Spells occupy combat timelines like weapon swings — cast times, interrupts, rotations (resolving the Combat Framework's open question). Casters put out the damage (death mages burning a boss with black flame) and **draw aggro they cannot survive** unless a tank pulls it off them; healers run full **heal rotations** and, when needed, throw **crowd control** to keep adds off the casters. Roles flex to the fight.

**The stakes are real.** **Combat resurrection is limited**, backups are few, and death is a corpse run (below) — "don't fuck up." The design **rewards the impossible line: be inventive, do it ridiculous, king plays are expected.** A game that hides its numbers and forbids respec earns the right to demand mastery.

> **[BUILD]** The threat formula and pull mechanics; parry/dodge frame windows at raid scale; resurrection rules and their interaction with corpse recovery; boss-side raid-wide mechanics and how cluster/targeted events are authored (the Dungeon-Maker seam, Book II).

---

## The Contested World

*(Ruled — the world's social stance. Ledgers A573A152, 6BEB00D3.)*

Prism's world is **non-instanced**: real-time world spawns in shared space, not per-group copies. **Cleared ground stays cleared** — on the order of a week — so holding a beachhead is a real tactic and a wipe means retaking territory, not resetting an instance. And the world is **contested**: **loot stealing and claim jumping are allowed** — intended, not exploits. "Get what you can when you can, and live with the results."

The game **does not prohibit antisocial play; the world remembers it.** Ninja-looting and claim-jumping make you a **pariah**, and pariah-hood has teeth through the settlement system (ledger E4F46BA5): a selfish line grows **settlements hostile to outsiders**, trainers who won't teach, doors that close. Reputation is lived terrain, not a number. This is the old-school (EverQuest / Ultima Online) ethos, of a piece with permanent decisions and honest, unbending rules — a **world, not a ride**.

> **[BUILD]** The concrete reputation/pariah mechanics, and how claim-jumping interacts with the dungeon claim/upkeep and settlement-reputation systems (Book II).

---

## The Advent Raids — Endgame Horizon

*(Horizon content — [PROPOSED], scheduled for the v1.1–v1.5 range, not launch. Ledgers 021891E4, A573A152, 639B9FD9; the zones themselves are Book V/III material.)*

The apex of adventuring is the **Advent raids** — the pentagon resonance zones (Book V), reached not by travel but by **quest**: physical travel there is not meant to happen (the pentagons are unreachable by design). Entry needs the **skill to teleport a group in** and **material attunement**, and the **first trip is roughly ten times harder than returning**, since it yields the materials that ease the way back. Play is EverQuest-classic — **camp the zone, send scouts** — at **72-person, week-long** scale, in **contested, non-instanced** space.

Each zone is an **abstract, rule-shifting plane** — the seven color-realms rendered as places that express their nature (the Void where you swim in all directions; a Chaos plane that rewrites itself; an Air realm with no floor), plus surreal challenge spaces (an infinite city where one step crosses light-years; Escher geometry; Geiger horror). **The zone's strange rule *is* the challenge** — and the fairness law still holds: insane, but legible to anyone open enough to perceive it (the resonance/perception principle, Book VI).

**These zones are not Dungeon-Maker content.** They are built by Elideus or the community as curated later content; standard DM **dungeons run to tier 10 and may hold gateways into the portals**, seeding the horizon inside the launch world. Boss authoring belongs to the complex **DM tech tree** (Book II) for regular content, but the pentagon tier sits above it.

> **[OPEN QUESTION]** Whether and how the **Advent eclipse** (the celestial event) gates or reshapes a zone — the sky's hook into the raids (ledgers 35A9CEAE, 3312B2AB); the mapping of the twelve pentagon points to the destination realms (73EA6D39); in-zone resurrection and party-composition rules.

---

## Character Lifecycle and the Generational Dynasty System

An adventurer is one life in a family line. The character system is **generational**: a **family tapestry** records the line; characters leave active play through defined **retirement flows**; and the peoples of Prism trade lifespan against generational turnover — longer-lived races trade turnover for continuity, shorter-lived races cycle through the family tapestry faster. (Ledger 10A6150F, Seed canon 12; corroborated by Book V, Peoples of Prism.) The races themselves are Book V material and are currently a stub there.

Two further facts are canon (ledger EC054473):

- **Every new game begins with three helper NPCs** besides the adventurer — the character's parents and a benefactor relative (a sibling, uncle, aunt, or grandparent) — for example, one who makes food, one who makes and mends clothing, and a specialist who teaches. The opening is survival-hard: a hostile world, scarce resources, a weak character, and nothing in hand but the people standing with you.
- **Retirement is a category, not one ending** (enriched 2026-07-02, ledger 0B98560B). A terminal exit has **many dispositions, and every one *adds* to the account** — the design never takes a character away, it grows the family: **retire into a settlement as an NPC** (this is how a city grows), **die heroically** for special status, **die of old age** to become a **patron of legend**, or walk the Muse's path (the apex disposition; see The Endgame Arc). Each deposits a permanent marker on the account's tapestry, and the **roster is limited only by time** — an account played for years can hold epic power in the sum of a large, disposed roster.

The tapestry is also the game's real achievement system: prestige lives in-world as permanent account markers, not in platform popups (ledger EC054473).

The lifecycle's economics are ruled (Elideus, 2026-07-02; ledger 91F84075):

- **The child.** An offspring is an investment requiring maintenance: ongoing payment of in-game currency builds the child to adventurer's age, and a raised child is what a new character is eventually rolled from. The investment need not begin the moment they come of age — but it cannot be skipped and cannot be bought around: **nothing is pay-to-play, ever.** "Old school RPG for life."
- **The adventurer.** The character you play — **no take backsies**. Skill them up, live, explore, learn, acquire; at **level 10** comes a yearning to retire: you recognize your strengths and choose your benefits for the family, as permanent effects. Other endings feed the same system — a heroic sacrifice in an epic battle can become a permanent badge of glory for the account; any number of effects can be built off this system.
- **Enchanted items obey the same law.** Long-term enchantments require regular mana investment at the enchanting table. You can't fake anything — the same rule as the child, the claim, and the dungeon: nothing persists that no one maintains.
- **Philosophy expresses in the settlement** (ledger E4F46BA5, stated as likely-intent). The pole a player's line follows shapes their NPCs — choose selfish traits and your settlement grows more hostile to outsiders; communal traits confer different benefits. Strengths and weaknesses both ways, and the design passes no judgment: which path is right is the player's own conclusion.

> **[PROPOSED]** A wider thread-state sketch exists from the same session — Living → Retired (role computed from the life actually lived) → Dead (tombstone) → Ghost (earned re-activation) → Burned (spent forever for a lasting effect); race as a tempo dial, lifespan trading against offspring slots; multi-generation dynasty tracks unlocking bloodline entitlements. Elideus's verdict was "not quite what I had in mind, but pretty close" — unratified. (Ledger A8FEC45C.) **Burning is now clarified** (2026-07-02, ledger 0B98560B): it is the **one subtractive exit** — either a **permanent delete** of the character from the tapestry, or a **sacrifice play** spending the character for a lasting effect — and either way it is meant to be **extremely costly**, the deliberate exception to "we never take a character away."

> **[STUB]** The mechanics of the lifecycle and dynasty system are unrecorded beyond the facts above.
> - **[OPEN QUESTION]** What transfers across generations — items? school mastery? reputation? ring progress? (Ledger D2C52C88.)
> - **Resolved (2026-07-02, ledger 0B98560B):** ordinary combat death does **not** end a life — you respawn and recover your corpse (EQ-style). A life *leaves active play* only through a terminal disposition (retirement at level 10's yearning; heroic-sacrifice badge, ledger 91F84075; old-age patron; the Muse's path) — all additive — or through **Burning**, the one subtractive exit (delete or sacrifice; extremely costly).
> - **[OPEN QUESTION]** Is the family tapestry a literal in-game artifact and interface, or a structural name for the family tree? Unrecorded.
> - **[OPEN QUESTION]** How members join beyond the ruled paths — invested children (ledger 91F84075) and adoption (the Muse-vessel gate, EC054473). Marriage and recruitment are unrecorded, as is the unit of inheritance (one-parent, whole-tapestry, or chosen-mentor — posed unanswered, ledger A8FEC45C).
> - **[OPEN QUESTION]** Does one player steward one line, or several? Unrecorded.

---

## Progression

The only progression fact currently ratified is economic: an uncompletable dungeon yields no XP and no traffic (ledger 49A3A9D6, Seed canon 8). Experience exists, and completing dungeons is at least one source of it; fairness is enforced by that incentive structure, not by moderation.

**Experience is the adventurer's alone, and it is delivered as a story, not a number.** Only adventurers earn experience, and only from beating completable content (ledgers 02D30987, 49A3A9D6): the builder crafts the challenge; the hero who overcomes it is paid. But the payment is never a popup. Instead the game **logs what a character does while away from their settlement**, and when they return home it writes a **permanent, generated journal entry** — a diary reporting the day in vague, human terms: *"I felt stronger and more competent with my broadsword after today's adventure"* might stand in for several thousand experience and two skill-ups (ledger BFBE6085). The intent is to detach the player from watching the numbers — aggregate narrative recaps, the way a session ends at a tabletop.

Three further facts are canon (ledger 91F84075): **levels exist, and level 10 is the retirement threshold** — the point at which the yearning to retire arrives; the **skill system is deep, complex, and completely opaque to the player**, learnable only through brutal trial and error, while remaining honest — deterministic, predictable, and fair (the fairness law, applied to progression); and **the rules never bend** — costs are paid in full over real time, with no accommodation for schedules and nothing pay-to-play, ever.

The skill system's shape is sketched but undesigned (ledger F618F695): **each discipline is a skill**, and skills are **layered** — "learning about axes teaches about wood and farming and gardening and combat" — with "probably three or four layers of skill scopes." Flagged by Elideus as a **major open issue for Sonnet collaboration**; nothing here may be elaborated until that session.

**The ring progression belongs to Book IV, not here.** Rings are a magic-mastery structure internal to spell research — a per-school milestone gating vocabulary breadth, spell-string complexity, and reagent grade, with shape access (4th/7th ring) as one instance of it — resolving fork 63B28A6B in favor of Option B (ledger B92EE74A). Book I tracks whole-character levels and retirement (above) as a separate axis from a mage's per-school ring standing.

> **[OPEN QUESTION]** How ring advancement interacts with the unresolved synergy-cycle orderings (ledger 244A27FF) and with Black's exclusion from ring-based synergy (Book IV; ledger 442D03E8 — Black combines with nothing).
> - **[OPEN QUESTION]** Whether ring progress transfers across generations (ledger D2C52C88).
> - **[OPEN QUESTION]** Progression beyond rings — levels, XP curves, skill training — is entirely unrecorded.

---

## The Endgame Arc

The endgame of the adventurer's game spans character lifetimes: **master a school of every color across the generations of a family line, and, during a celestial alignment, reunite or re-shatter the Prism.** (Ledger 10A6150F, Seed canon 12; "all seven schools" ruled to mean at least one school from each color — ledger A8FF6AB0.)

Celestial events are global modifiers, deterministic and foretold: an alignment is never scripted or random — it emerges from real orbits, and those who learn the heavens can predict it (ledger 8FB95281, Seed canon 6). The endgame's moment is therefore something the whole world can see coming — and since the moon runs on real wall-clock ephemeris (Book V; ledger D2AAFEEC), the appointment is computable from the actual sky.

**The arc is the Muse's path** (ruled 2026-07-01/02; ledgers BDB707A5, EC054473). The player walks the road the Lonely Muse walked — apprentice across all seven colors in one lifetime, mastering at least one school of each (ledger A8FF6AB0), and stand at the summit she was denied (Book VI). Completing it is a **terminal epic quest**: the choice between reuniting and re-shattering is offered, made personally, and **retires the character**. The shared world persists — permanent world-scale change is not simulated; "that's where a character would retire." Nobody does this by accident, or on their first character, or their tenth.

The gate stack is canon (ledger EC054473):

1. The account's tapestry must already record a **leveled and retired character in each of the seven colors** — at least one school per color, seven completed lifetimes as the price of eligibility (ledger A8FF6AB0).
2. The vessel must be a **near-immortal race** (an elf-type with five human lifetimes of learning done by age one hundred) — or a character of another race prepared through an adoption setup and massive tutoring investment.
3. The quest must be completed **during a celestial eclipse of the Chalice** — the moon–Death alignment that reveals the Muse's hidden constellation (Book VI; ledger AF819A62).
4. The reward is a **permanent account marker on the tapestry** — a major permanent account-wide bonus ("a permanent patron of all magic, something along those lines").

*[Resolved 2026-07-02: "seven schools" means at least one school from each color — fourteen is excessive by ruling. Ledger A8FF6AB0, closing FCB93BC0.]*

> **[OPEN QUESTION]** **Reunite vs re-shatter — the meaning.** The mechanical scale is ruled (personal, terminal); what each choice *means* — mythologically, and in whatever the retiring character leaves behind — is unrecorded. The mythic frame gives stakes without specifics: reunification reads as restoring the unity the Titans broke; re-shattering as renewing the containment for another age. What the choice options actually are, and whether factions align to them (Book VI, Those Who Remember the Muse), remains open.
>
> **[OPEN QUESTION]** **Inheritance beyond mastery.** School mastery accrues at the account level — one retired character per school (ruled above). What else transfers across generations — items, reputation, ring progress — is still the open inheritance fork (ledger D2C52C88), as is what combat death costs the line (ledger D25A57E1).

Related forks held elsewhere:

- Whether "all seven schools" includes psionics — a discipline outside the seven schools — is unresolved (ledger 7609E7E9).
- Black combines with nothing (ledger 442D03E8) and is excluded from ring-based shape synergy (Book IV). Whether the path to Black mastery differs structurally from the other six schools is unrecorded.
