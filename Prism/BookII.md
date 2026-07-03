# II. Dungeon Maker's Design

This book defines the Dungeon Maker's half of Prism: the modular template building system, the modular boss builder, and the item creation systems.

> **Provenance.** The primary source for this book is `sources/chatgpt-dm-system-notes.md` (early exploratory sessions — source material, not canon). Where that document conflicts with seed canon or Book V's Canon Rulings, the rulings win. Content below is Canon where backed by a ruling or ledger decision; everything else is marked **[PROPOSED]**, **[OPEN QUESTION]**, or **[STUB]**.

> **Terminology.** The source notes say "Dungeon Master"; the books say "Dungeon Maker". Which term wins platform-wide is an open glossary fork — do not treat either as ruled. This book uses **Dungeon Maker** (abbreviated **DM**) throughout pending that ruling. This is the book's single note on the fork. (Ledger 500F8438.)

---

## Design Philosophy

Canon (Seed canon 7, ledger C91261FB):

- Prism has two player populations that never directly interact: **Dungeon Makers** and **adventurers**.
- Dungeon Maker gameplay is an RTS/base-builder/tower-defense game. Adventurer gameplay is a classic MMO.
- The coupling between the two is **asynchronous**: dungeons are built, published, discovered, and run — never a live head-to-head.
- The point of the design is player-generated content at a scale no development team can match.

The Dungeon Maker path is not a housing system or an instanced dungeon generator. It is a full progression game with its own economy, advancement trees, resource requirements, and long-term goals: Dungeon Makers create the challenges, rewards, and destinations that drive adventurer activity, and a Dungeon Maker's success is measured by attracting repeated visitation, not by preventing completion. Players generate content for one another rather than relying exclusively on developer-authored experiences. *(Source framing, consistent with canon.)*

> **[OPEN QUESTION]** The source notes call the two loops "deeply interconnected" and the relationship "collaborative rather than adversarial", and describe adventurers discovering hidden dungeons by tracking imp resource routes. Read as world-mediated, this is consistent with asynchronous coupling — imps and expansion marks are world objects, and no player-to-player contact is required. But the live boundary is specified nowhere: can adventurers interfere with imps in real time; does a Dungeon Maker ever observe or respond during a run; and what does the tower-defense frame defend against, if never live adventurers? Options and implications are in the ledger; unresolved. (Ledger A2596715.)

---

## The Template System

Canon (Seed canon 8, ledger 49A3A9D6): dungeons are assembled from modular template pieces with **constrained connection points** — traps, rooms, and fills attach only at defined sockets, and fills are bounded. Fairness is enforced at the construction grammar, never policed after the fact.

Template pieces represent dungeon components. The source lists as examples: hallways, chambers, treasure rooms, boss arenas, trap complexes, secret passages, puzzle rooms, monster nests, ritual chambers, and environmental hazards. These pieces are the building blocks from which larger dungeons are assembled; as a Dungeon Maker advances, more sophisticated templates unlock, allowing more complex layouts, stronger encounters, and more specialized themes. The template system exists so that Dungeon Makers work at the level of design and progression rather than piece-by-piece sculpting. *(Source.)*

*[Fill and material pieces draw on Book III's material vocabulary; how materials are stored (voxel containers vs the engine's material ledger) is an open fork that touches Book II's fill pieces. Ledger 9C677816.]*

---

## Incentive Structure

Canon (Seed canon 8, ledger 49A3A9D6): uncompletable dungeons yield **no XP and no traffic**. Trolling is expected at the margins and starved economically, not moderated.

Dungeon Makers gain experience when their dungeons are completed; that experience funds advancement through tiers and technology trees. *(Source, consistent with canon.)* The source frames the resulting economy consistently: success is repeated visitation; reputation is a resource; better dungeons create better rewards, better rewards attract more adventurers, and more adventurers create more opportunities for Dungeon Maker progression.

---

## The Ten Tiers

Dungeon Makers advance through **ten tiers** of dungeon complexity, each a significant increase in capability, complexity, and influence. Early tiers focus on basic dungeon functionality and survival; by the highest tiers, a Dungeon Maker is operating an entire ecosystem rather than a single dungeon. Advancement unlocks, in aggregate: new construction templates, additional room types, larger dungeon sizes, stronger monsters, advanced traps, specialized themes, improved resource gathering, enhanced loot creation, and new technology branches. *(Source.)*

Canon constraint (Seed canon 6, ledger 8FB95281): celestial events are global modifiers across **all** tiers and regions — never tier-exclusive or endgame-only bonuses. Scarcity and abundance are deterministic and foretold in the sky.

**[STUB]** Per-tier unlock table. What each individual tier actually unlocks is specified in no source. Open questions: how the aggregate unlock list distributes across the ten tiers; whether tiers gate technology-tree depth or run parallel to it; whether tiers have names or thresholds.

---

## Technology Trees

Beyond tier advancement, Dungeon Makers gain access to technology trees — specialized areas of expertise through which a Dungeon Maker develops a distinct identity. Different Dungeon Makers pursue different technological paths, producing varied dungeon experiences across the world. *(Source.)*

**[PROPOSED]** Example branches — source-work only; the source itself says "examples may include":

- **Monster Mastery** — monster quality, diversity, behavior, and specialization.
- **Trap Engineering** — advanced traps, environmental hazards, and defensive systems.
- **Arcane Research** — magical enhancements, enchantments, and unusual dungeon mechanics.
- **Resource Management** — efficiency of minions, logistics, harvesting, and material conversion.
- **Relic Crafting** — creation of rare equipment, magical artifacts, and unique rewards.

---

## Imps and Resource Logistics

Dungeon Makers maintain their dungeons through resource collection. Specialized servants — imps and other minions — gather materials from the surrounding world and haul them back to the dungeon. These resources are consumed by construction, expansion, maintenance, monster support, trap creation, and item production. *(Source.)*

The gathering process is not hidden from the world: observant adventurers may discover resource routes, track minion activity, or follow signs of dungeon expansion to uncover previously unknown dungeon locations. Visible logistics are the discovery mechanism that ties the Dungeon Maker ecosystem into the adventurer experience. *(Source.)* *[Whether adventurers can interfere with imps live is part of the open interaction-boundary question — ledger A2596715.]*

---

## Placement and Monster Recruitment

Canon (Elideus, 2026-07-02; ledger B4F9A3AC): specific biome types are **seeded with specific kinds of creatures**, and on the DM-vs-adventurer scale **certain monsters can only be recruited in certain areas**. **Picking where to place your dungeon matters** — siting is a strategic decision, because the biome decides the recruitable bench.

The bestiary itself — the fifteen Principality categories and the archetype matrix — lives in **Book VII: Bestiary** (ledger BEE2FC2D and companions). **[STUB]** remaining here: the biome→creature table (which of Book VII's creatures seed which biomes) and whether recruitment gating is exclusive or graded are still unbuilt; how placement interacts with discovery, imp logistics, and tier progression is likewise open (cross-reference Book IV's creature-noun dictionary and the Terradun peoples-vs-vocabulary fork, ledger EBA28F43).

---

## Discovery, Advertising, and Reputation

New dungeons begin hidden from the wider player population. As adventurers discover, explore, and report on dungeon locations, information spreads: locations become known destinations and may appear on regional information boards, guild records, and maps. Dungeon Makers advertise their creations on in-game boards and compete for attention — a poorly designed dungeon is ignored; a well-designed dungeon becomes a destination with a steady stream of visitors. Reputation is a resource. *(Source, consistent with the incentive canon above.)*

---

## Decay and Maintenance

The world is designed around continual change: resources shift, materials become depleted, monsters migrate, structures decay, environmental conditions change. Dungeon Makers must continually adapt to remain relevant and competitive; the pressure prevents long-term stagnation. *(Source.)*

Dungeons function as living systems rather than static structures: monsters occupy habitats, resources are consumed and replenished, bosses require support structures, and expansion creates new maintenance requirements. Over time a dungeon develops an identity from its creator's choices — a militarized fortress, a site of magical experimentation, a specialist in rare crafting materials or legendary equipment production. *(Source.)*

The same law governs the adventurer side: claims and settlements require ongoing upkeep even while actively played — maintenance costs, settlement NPCs doing repair work — and abandoned structures decay back into the world through the erosion system. Nothing persists that no one maintains. (Ruled; ledger 95EAF28D.)

---

## Story Content Packs

Canon (ruled 2026-07-01/02; ledger 95EAF28D; source archived at `sources/celestial-cosmology-session-2026-07-01.md`):

- Builders can unlock **specialized content trees** by invested points — explicitly **not by purchase** — granting curated sets of story content to deploy: webs of NPCs, quest parts, and items authored from the mythology (the scale of a self-contained storyline cluster with recurring NPCs across missions).
- Deployment is governed by **validation-as-authorship**: the content pack carries grammar constraints the builder must satisfy — in Elideus's words, rules like "if you [take] this particular content pack, you are not allowed to finish the ninth tier of a dungeon without having this kind of a room deployed that has this NPC sitting in it." The build validates only when the required interaction set is complete. This extends the fairness principle of Seed canon 8 — enforcement at the construction grammar — from spatial fairness to narrative completeness.
- The primitive set is **event-oriented discovery content, not fetch quests** ("I don't want to give people the ability to say, go collect ten seashells"): builders deploy opportunities players stumble upon, in the discovery-and-exploration register.
- Builders do not need to understand the story they deploy: they select storylines and enhancements that fit their theme, and **the lore rides the items and NPCs** — canonical mythology propagates through player-built dungeons by construction.

**[STUB]** The concrete toolkit — the quest-part building blocks, the constraint vocabulary, which storylines become packs — is undesigned. Open: how content-tree investment prices an authoring license; how packs interact with tiers (the tier-nine example implies gating); and where pack validation runs relative to the template grammar's socket validation.

---

## The Boss Builder

Book 0 names a **modular boss builder** as one of this book's three systems. The source supports: boss arenas and boss rooms as template pieces; stronger bosses unlocked by tier; "unique boss experiences" at the high tiers; and bosses requiring support structures within the dungeon's ecology.

**[STUB]** The builder's mechanism is specified in no source. Open questions: whether bosses compose via Book IV's creature-word grammar (the Dracolich pattern — itself resting on words defined in no dictionary, ledger 67DB3F76), assemble from socketed templates the way rooms do (Seed canon 8's grammar extended to creatures), or both — a template-built body with a word-composed identity. Do not elaborate past this line without a ruling. (Ledger EBF514AA.)

---

## Loot Creation

Reward generation is a core Dungeon Maker responsibility. Rewards are tied to the progression and capabilities of the Dungeon Maker who created them rather than to static loot tables; as a Dungeon Maker unlocks new technologies, materials, enchantments, and techniques, the ceiling of producible rewards rises. *(Source.)*

The source session ended with exactly this item open: "How magical item creation actually works: crafted directly, procedurally generated from components, assembled from Words of Power, derived from materials, or some combination" — identified as the next major design document. The stack below is a candidate answer, not a ruling.

### The Artificing Stack **[PROPOSED]**

Source of the stack: Elideus, recompile brief 2026-07-02. Each rung cites its Book IV basis; rungs whose application to items appears nowhere in Book IV are flagged as such. (Basis map in ledger C1AF172E.)

1. **Material.** An item begins as materials — Book III's element, compound, and mineral tables; the source notes' elemental system generates what the world offers.

2. **Noun-residency.** Book IV: "Every interactive object in the game world is assigned a magical name (**noun**)" — and material nouns exist in its dictionaries: **Ferrum** (Iron — described as covering metals generally; gloss flag, ledger 44F17D1E), **Saxum** (Stone — coverage overlaps Terra, ledger 44F17D1E), **Lignum** (Wood), **Crystallum** (Crystal — "often used in enchanting, crafting, or reinforcing magical objects"). **[PROPOSED]**: the nouns resident in an item's materials determine what magic the item can carry. Book IV grounds the residency; the consequence is brief-sourced.

3. **Artificing.** Book IV's Magical Domains include **Artificing** — "Imbuement of items with magical properties." **[PROPOSED]**: artificing is the act that binds words to the item.

4. **Adjective-quality.** Book IV's adjectives grade intensity and scale — **Vas** (Greater) / **Bet** (Lesser), **Fortis** (Strong) / **Debilis** (Weak), **Magna** (Large) / **Parva** (Small). **[PROPOSED]**: adjectives serve as quality grades on an imbued property. Basis gap: Book IV applies adjectives to spells, never to item grades — the application is brief-sourced only. The adjective slot's collisions (Altus/Altior and Infimus/Humilis duplicates, ledger 44F17D1E; Umbra in two grammar slots, ledger 94774F28) must resolve before grades can be unambiguous.

5. **Shape-proc.** Book IV's shapes — **Orbis**, **Serratus**, **Rectus**, **Chevronis**, **Lunaris**, **Undula**, **Spiralis**, one per school — define how magic interacts with space. **[PROPOSED]**: a shape gives an item its triggered (proc) effect form. **[OPEN QUESTION]** — basis gap: Book IV never attaches shapes to items. It ties shape access to school synergy through a ring progression, now defined as a per-school mastery structure (ledger B92EE74A, resolving 63B28A6B) — but whether an item's shape-proc is constrained by its maker's ring standing, and whether a shape-proc marks the item with a school identity, remains unresolved. (Ring-gated **reagent grade**, same ledger, is a plausible second constraint on artificed items — a focus or talisman is itself a candidate reagent-substitute, per Book IV's Reagent Grades — but this is not ruled here.)

### Deterministic Legendary Naming **[PROPOSED]**

Basis: Seed canon 10 (ledger C936766F) — platform-wide, the same composition yields the same identity (UUID5 from a locked namespace); the same principle is the intended pattern at the loot layer, where it is [PROPOSED], not ratified.

The pattern is the **Dracolich composition rule**: as Book IV composes **Vas** + **Draco** + **Mortuus** into a Dracolich, a legendary item's name derives deterministically from what it is made of. Two items of identical composition are the same legendary — same name, same identity, everywhere, always.

Unresolved dependency (ledger 67DB3F76): the exemplar's constituent words — **Draco** and **Mortuus** — are defined in no Book IV dictionary, and their grammar slots are unassigned. The identity math requires ratified constituent words; until the dictionaries close that gap (and the slot collisions noted above), deterministic naming has a canon-grade principle and source-work vocabulary.

> **[OPEN QUESTION]** Whether the artificing stack is the whole answer to the source's open item or one component of "some combination" (crafted directly / procedurally generated from components / assembled from Words of Power / derived from materials) remains the fork the source itself left open.
