# Source: Legacy "Book II — Dungeon Maker's Design" (recovered generated draft)

> **Provenance:** An older, generated draft of Book II, pasted into the recompile session by
> Elideus on **2026-07-13** for concept recovery ("may contain some useful concepts, some
> guidelines for templates and traps and advancement").
> **Status: RECOVERED DRAFT, partially adjudicated.** Much is already canon in the current
> Book II (absorbed from the earlier `chatgpt-dm-system-notes.md` intake and the 2026-07-02→04
> rounds); some is genuinely new and recovered as [PROPOSED]; some is superseded. Where it
> conflicts with ledger `decision` entries, the rulings win.
>
> **Intake mapping (2026-07-13):**
> - **Already canon (confirmed, not re-added):** RTS/base-builder frame; challenge-not-punishment;
>   XP *only* on completion; the tier system (T1 = Door·Hall·Heart with one trap and a
>   Normal-scale boss; prior boss room → loot camp as the Heart migrates; max tier 10 —
>   ledger 66083A94); designer-authored modular templates + **voxelmancy** with fillable/locked
>   regions and collision-driven construction-grammar fairness (Seed canon 8, 66083A94); minion
>   labor and open-world gathering; discovery by following minions; decay/maintenance; reputation.
> - **Recovered as [PROPOSED]** (added to Book II): the **trap system** — trap **nodes/sockets**
>   (attachment type, allowed trap class, trigger compatibility; count scales with tier),
>   **triggering** (1:1 → one-to-many / delay chains / randomized, all pre-authored, no player
>   scripting), the five **trap archetypes** (projectile, impact, environmental, movement,
>   psychological), and **trap progression** by tier with fair-interaction validation; **bounded
>   editable-region** examples; the **deformable-voxel ("ClayEngine") geometry** note; **external
>   community tools** (out-of-game map/board/ratings/screenshots) alongside in-game hidden stats;
>   **theme-expansion** tech branches.
> - **SUPERSEDED:** the **Monster Ecosystem & Attraction System** (attract factions by
>   environmental theming) → replaced by **recruitment-by-siting** + the Book VII bestiary
>   ("the monster manual") + biome-of-the-entrance gating (B1472A6A) + the emergent ecological
>   sim (10B27578) — *Elideus flagged this on intake.* The **free-form boss builder**
>   (archetype + traits + affinity + loot table, a player-composed creature) → replaced by the
>   **recruited-creature boss** model (66083A94 / EBF514AA); its trait/archetype vocabulary is
>   kept only as a [PROPOSED] candidate for Boss-tier **signature mechanics** (Book VII). The
>   **40³–160³ template-size ladder** → superseded by the canon **16→64** dungeon scale (66083A94).
>
> Applied to Book II; recorded in Oracle thread `prism-bible-recompile` (note) and
> RECOMPILE_REPORT.md (2026-07-13). Source text preserved verbatim below.

---

## II. Dungeon Maker's Design

### Overview

The Dungeon Maker gameplay mode provides an RTS-style experience where players construct and evolve fully customizable dungeons. These builders do not win by defeating adventurers, but by challenging them. Success for the Dungeon Maker is achieved **when players complete the dungeon**, making it an experience of **asymmetrical design, reward through creativity, and emergent narrative.**

The Dungeon Builder gains experience and prestige by crafting dungeons that are **difficult yet beatable**, encouraging thoughtful challenge rather than brute-force punishment. Every dungeon is a stage; every adventurer, a participant.

---

### Core Gameplay Loop

* Players build dungeons from modular components using unlockable templates.
* Control is RTS-style: players manage minions and environmental elements.
* Attract various monster factions based on dungeon environment and upgrades.
* As adventurers challenge the dungeon, Builders earn XP **only when the dungeon is completed**.
* Builders use XP to unlock tech trees, new dungeon pieces, monsters, traps, and ultimately massive, cinematic boss arenas.

---

### Dungeon Tiers & Progression

#### Tier 1 (Beginner Tier)

* **Component Limit**: 3
  * Entrance
  * Hallway (with 1 trap)
  * Boss Room (Dungeon Heart)
* **Purpose**: Introduce core mechanics and provide a compact but functional encounter.

#### Tier 2+

* **Expanded Component Limit** (e.g., 10 rooms)
* Unlocks:
  * Branching layouts (T-halls, loops, dead-ends)
  * Multiple Dungeon Hearts (prior ones become Treasure Rooms)
  * Greater variety of templates
  * Access to new trap types, puzzle rooms, and monster factions

#### Tier Advancement

* Tiers serve as a cap on dungeon complexity.
* Final boss room is unlocked at high tiers with access to large arena layouts and advanced mechanics.
* Maximum dungeon tier is **10**.

---

### Modular Templates

Dungeon construction is modular, with snap-grid architecture akin to building systems in modern survival/builders (e.g., Ark, Valheim).

The engine underpinning this system—**ClayEngine**, inspired by VoxelFarm—enables advanced template design using voxel manipulation. Templates are essentially blueprints, extracted as defined regions (e.g., 40x40x40 voxel cubes) within the voxel world. Minions perform the actual build process by physically digging and sculpting these templates into the world.

#### Template Behavior:

* **Players do not create templates**—they select from a curated and expanding library.
* Templates are categorized by **voxel complexity tiers**:
  * Tier 1: 40x40x40
  * Tier 2: 64x64x64
  * Tier 3: 80x80x80
  * Tier 4: 128x128x128
  * Tier 5: 160x160x160
* Higher tier templates allow for:
  * More elaborate rooms and traps
  * Puzzle mechanics
  * Boss arena construction (only available at top tiers)

#### Template Mechanics:

* Editable voxel zones governed by strict rulesets.
* Only certain regions (e.g., bottom/top 4 layers, 4x4 corners) are editable within a template.
* Prevents invalid layouts (e.g., blocked hallways, unreachable exits).
* Voxels are sculpted, not placed as simple blocks—using **vector-defined deformable geometry**.

#### Advanced Voxel Features:

* Voxels have shape data defined by a center point and a vector to the top-right-forward (TRF) corner.
* One voxel + its neighbors defines a full 3D shape, enabling:
  * Curves
  * Slants
  * Rounded geometry
* Templates appear block-based but allow for organic, sculptural design—hence the "ClayEngine" name.

---

### Monster Ecosystem & Attraction System

> *(Intake 2026-07-13: SUPERSEDED — Elideus: "way out of line with the monster manual which
> already supersedes that." Replaced by recruitment-by-siting: Book VII bestiary + biome-of-the-
> entrance gating B1472A6A + emergent ecological sim 10B27578.)*

Rather than purchasing monsters, Builders attract monster factions by shaping the dungeon environment and investing in Tech Tree upgrades.

#### Examples:

* **Dark Dwarves**: Prefer industrial/fire themes. Unlock fire traps, mechanical hazards.
* **Fungal Beasts**: Prefer moist, dark, decaying chambers. Unlock spore clouds, bio-hazards.

Attraction based on:

* Environmental cues
* Room types
* Trap types and themes
* Biome (connected to voxel world data)

Each faction brings specific strengths, weaknesses, and synergy with certain dungeon types.

---

### Builder Experience & Tech Tree

Builders earn XP **only when players reach and defeat the Dungeon Heart**.

* Easy dungeons = less XP.
* Challenging but fair dungeons = higher XP.
* XP is spent on:
  * Unlocking new room templates
  * Access to higher tiers
  * New monster factions and upgrades
  * Boss design and mechanics
  * Dungeon theme expansions (e.g., Fae, Undead, Clockwork, Eldritch)

---

### Final Boss Room

> *(Intake 2026-07-13: the free-form boss-composition model is SUPERSEDED by the recruited-
> creature boss — a Book VII creature at an elevated power tier in a designer-made, tier-scaled
> boss-room template, 66083A94/EBF514AA. The trait/archetype vocabulary below is retained only
> as a candidate for Boss-tier signature mechanics, Book VII.)*

* Unlocked at high tier.
* Designed as the capstone to a full dungeon arc.
* Large arena-style template.
* Fully customizable boss:
  * Base Archetype (Brute, Mage, Trickster, Summoner)
  * Traits (Teleport, Enrage, Phases, Summons)
  * Elemental affinity
  * Loot Table Design

Bosses function as mechanical showcases, combining learned dungeon elements into climactic encounters.

---

### Resource Gathering & Dungeon Discovery

Dungeon Minions are more than builders—they're gatherers.

* Minions mine for resources in the open world, extracting materials for dungeon construction.
* Resources are finite and scattered, requiring minions to travel far.
* Adventurers may **follow minions** back to your dungeon, which becomes the primary dungeon discovery method.

#### Importance of Location:

* Dungeon visibility is tied to activity.
* **Location matters**: proximity to adventurer routes, biome rarity, and strategic placement all influence discoverability.

#### Decay & Maintenance:

* Dungeons degrade over time—walls crumble, traps break.
* Active maintenance is needed to preserve functionality and aesthetic.
* Logging in doesn't reset decay.
* Adventurer interactions contribute to damage.
* Automation exists, but players must **engage regularly** to thrive.

This system supports a **Dark Souls-like sense of mystery and exploration**—no glowing markers or map exclamations. Discovery is earned.

---

### Surfaces Beyond the Game

While dungeon visibility in-game is built on mystery and indirect discovery, **external systems** support community knowledge-sharing and social features.

* A dedicated **online map and message board** displays discovered dungeons, completion rates, average clear times, and social metrics.
* Players can post **screenshots, leave reviews, share strategies**, and participate in rankings.
* Builders may earn prestige and reputation outside the game based on dungeon performance and player interactions.

In-game, dungeon stats are largely hidden to preserve immersion. However, as players return to town, they receive narrative feedback—like "Your journey sharpened your senses"—representing character growth without overt numerical displays.

---

### Design Philosophy

* **Challenge, not punishment**
* **Reward comes from being defeated well**
* **Players want glory**; Builders give them legends
* Dungeons are surfaced in game via:
  * Completion Rate (internal stat)
  * Time to Clear (internal stat)
  * Adventurer Ratings (Fun/Challenge)

But these are surfaced externally, through community tools—not through in-game UI.

---

### Traps System

#### Modular Trap Integration

Traps are not built freeform by players. Each room template includes designated Trap Nodes, predefined points where modular traps can be slotted in. These nodes determine:

* Attachment Type (floor, ceiling, wall, hidden)
* Allowed Trap Classes (e.g., projectiles only, no liquids)
* Trigger Compatibility (step plates, line-of-sight, proximity)

The number and complexity of these trap nodes scale with template tier, ensuring that only advanced builders can access the most complex traps.

#### Triggering System

Basic triggering operates on a one-to-one linkage: a specific trigger activates a specific trap. Higher tech unlocks allow:

* One-to-many triggering (one trigger, multiple traps)
* Delay chains
* Randomized activation

Triggers are template-governed. Players select from pre-authored behaviors as part of their build, but cannot script new logic.

#### Trap Archetypes

Trap categories are designed to remain broadly defined for scalability:

##### 1. Projectile Traps

* Examples: Arrows, darts, spears, flames
* Directionality: Single, burst, cone, fan
* Upgrades: Homing, elemental, volley effects

##### 2. Impact Traps

* Examples: Spikes, hammers, crushers
* Delivery methods: Drop-from-above, rise-from-below
* Can be combined with bait triggers (e.g., false doors, loot chests)

##### 3. Environmental Hazards

* Liquids: Acid, lava, slime, oil
* Solids: Sand floods, boulder drops
* Gases: Poison, hallucinogen, sleep mist

##### 4. Movement Traps

* Mechanisms: Pusher plates, moving walls, gusts of wind
* Layout effects: Platform removal, collapsing pits
* Useful for puzzle integration

##### 5. Psychological Traps

* Examples: Misdirection through layout, lighting, sound
* Includes false triggers or aesthetic cues to instill caution or fear

#### Trap Progression & Tech Unlocks

Trap classes are gated behind XP-based progression linked to successful dungeon completions:

* Tier 1: Basic spikes and projectile traps
* Tier 2: Hidden traps, delayed triggers, pitfall combinations
* Tier 3: Liquids, corrosives, chain reactions
* Tier 4+: Elemental traps, puzzle-linked mechanisms, multi-room effects
* Tier 8+: Rolling boulders, dungeon resets, boss arena modifiers

Each unlocked trap module includes:

* A visual preview in the ClayEngine UI
* Collision and timing validations to ensure fair interaction
* Balance constraints to prevent unintended or overpowered trap behavior
