# Source: Early World-Modes Discussion — God Mode ("Clay Engine"), Realmwright/DM Roles, Single-Shard Scale

> **Provenance:** Recovered raw text from the earliest days of the project, pasted by
> Elideus into the recompile session on **2026-07-03**. The conversation partner is an
> **unidentified earlier assistant** (the FDD format, `✔️`/`⭐` bullet styling, and tone are
> consistent with a ChatGPT session, but this is an inference, not a confirmed origin). Do
> not cite a share link; there isn't one.
>
> **Status:** SOURCE MATERIAL, **largely superseded.** This is early exploratory design, not
> canon. It predates the round 8/9/10 rulings and the current role structure. Capture-and-flag
> only — nothing here is written into any book, and where it conflicts with Canon Rulings or
> the `prism-bible-recompile` ledger, the rulings win.
>
> ### What survives (Elideus-sourced, carries forward)
> - **God Mode = the "Clay Engine":** an **offline, single-user, isolated** world-generation +
>   simulation toolset that exists **outside the multiplayer / social layer.** Players never
>   see, touch, or interact with it. It shapes terrain, biomes, erosion, weather, hydrology,
>   and mineral replenishment — the world's physical reality and self-healing integrity. This
>   is the **direct ancestor of what is now called "GM mode" / "epoch 7."** (Elideus confirmed
>   the framing: *"Eh, I suppose that is fair."*)
> - **Single-shard, full persistent-state, Earth-scale landmass world** — Elideus's explicit
>   architecture intent, **explicitly rejecting a multi-shard configuration.**
> - **A world decay system is assumed to exist** ("we already have a decay system in place");
>   abandoned/unvisited areas reverting is treated as fine ("no big deal in the grand scheme").
>   Consistent with the "Decay and World Evolution" material in `chatgpt-dm-system-notes.md`.
>
> ### What is DEAD / retired (do not re-propose)
> - **"Realmwright"** as a distinct **surface city-planner authority role** (paired with the
>   Dungeon Master as underworld builder). **RETIRED** — folded into GM mode / epoch 7
>   (Elideus, 2026-07-03). There is no surface-steward player authority role in current canon.
> - **Governance machinery:** quorum/soft-election stewardship, "flag an area = it's mine,"
>   hard caps ("1 Realmwright per 100–200 players"), approval-threshold voting, region
>   reclamation flows. **DEAD** — cuts directly against the current *"do not systematize
>   organic human consequences"* design ethos and the contested-world / pariah / **no
>   reputation system** rulings.
> - **Zoning-vs-building split** ("Realmwrights zone, adventurers physically build"). The
>   *Realmwright* half is gone; adventurer voxel town-building survives (see
>   `chatgpt-dm-system-notes.md`), but not under a zoning-authority role.
>
> ### Already captured elsewhere (not re-transcribed here)
> The DM system (ten tiers, tech-trees, template construction, minion resource-gathering,
> loot creation, dungeon ecology, discovery/reputation, decay) and the Adventurer loop,
> voxel town-building, and elemental/erosion/hydro systems are already captured in depth in
> **`chatgpt-dm-system-notes.md`.** Death-and-rebirth, the contested world, and no-reputation
> are settled in the round-10 rulings. This file preserves only what that file does not.
>
> ### Non-lore artifact preserved below
> The transcript also contains a proposed **FDD → TDD → Codex implementation pipeline** and a
> filled-in **Functional Design Document** for the (now-dead) Realmwright/DM/Adventurer system.
> That is a **build-process artifact, not Prism canon.** It is preserved verbatim at the foot
> of this file for provenance, but the *system it describes is superseded.*

---

## 1. God Mode framing (assistant restating Elideus's intent; Elideus confirmed)

> God Mode is offline, isolated, single-user, not social, not a game mode. It is your toolset
> for building and simulating worlds. It exists outside the multiplayer layer. Players never
> see it, touch it, or interact with it. It's basically the Clay Engine editor + world
> simulator.

The self-healing / world-integrity claim tied to it:

> Your offline God Mode ensures: erosion rebalances, weather cycles remain stable, element
> flows remain correct, atmosphere and hydrology stay coherent, biomes don't collapse,
> minerals replenish according to rules. No player can "break" the world. This preserves your
> engine integrity.

Early role picture (the surface/underworld split — **the Realmwright half is now dead**):

> - **God Mode (offline, admin):** world generation, simulation, terrain, biomes.
> - **Realmwrights (Surface):** manage settlements, zoning, economies. *[RETIRED]*
> - **Dungeon Masters (Underworld):** manage encounters and dungeons.
> - **Adventurers:** interact with both; only adventurers bridge the layers.

---

## 2. Elideus turn — single-shard scale + governance musings (verbatim)

> "Eh, I suppose that is fair, I think. Well, hmm. So, that in one way implies the need for a
> multi-shard configuration for the game, and that actually wasn't my intent. I had planned a
> full single-shard persistent state world. Um, since the scale of the worlds that I'm making
> was large enough that it... I mean, I'm talking, like, like no fire scale here. Like, I kind
> of want to be at that level. Like, earth scale. Landmass. So, with the character death and
> rebirth system and all of that kind of stuff, it kind of feels like maybe there could be a
> system for more promotion to city builder or city planner. Like, either through a
> quorum-style election, which may or may not actually need a large number of players.
> Basically, you could format it in such a way if, like, there aren't any players around, you
> can just flag an area and say, this is mine now. And if it never goes anywhere, that's
> probably no big deal in the grand scheme of things. If nobody ever goes there, then great. If
> somebody does go there and there's nothing happening because the player stopped playing, we
> already have a decay system in place. So, that's all jelly. All Gucci."

**Reconciliation:** The *single-shard / persistent / Earth-scale* commitment and the *decay
system* survive. The *promotion-to-city-planner / quorum-election / flag-an-area* governance is
the seed of the Realmwright idea and is **retired** — see the header.

---

## 3. Elideus turn — the Codex documentation-pipeline request (verbatim)

> "I've started a new project on Codex, and unfortunately, one of the challenges that we run
> into is transitioning information and discussions that are found over here over to Codex so
> that the engine that's building the engine can actually understand what it is that we're
> trying to do. So I kind of need to develop a bit of a framework for taking concepts here,
> turning them into functional documents that can then be turned into technical documents that
> can then be implemented by Codex. But of course, we need each of those steps to be performed
> by Codex, so it's a little chicken-before-the-egg type thing. What I'd like is maybe a
> proposal, a format, functional design document-style document here that kind of outlines this
> larger concept that we discussed here so that it could be then interpreted into a technical
> design and then implemented with the data layer, which is what we're working on right now."

**Reconciliation:** This is a **build-process** need (concept → FDD → TDD → Codex data-layer
implementation), not Prism lore. Recorded here for provenance. The FDD the assistant produced in
response is preserved verbatim in the appendix below; note that its *subject matter* (the
Realmwright/DM/Adventurer governance system) is superseded, so the appendix is an example of the
*format*, not a live spec.

---

## 4. Elideus closing notes (this session, 2026-07-03)

> "The above design was very early and the Realmwright idea is gone, that's just GM mode in
> current thinking (in some places referred to as 'epoch 7')."

> "Some additional thoughts and ideas were here, again, this is all old recovered conversations
> from the earliest days of the project."

---

## Appendix A — Superseded FDD (format artifact; subject matter is dead)

Preserved for provenance as an example of the assistant's proposed Functional Design Document
format. **The system it describes (Realmwright surface stewards, quorum governance, region
decay/reassignment) is retired.** Reproduced in condensed form.

- **Title:** PRISM WORLD MODES — Functional Design Document (FDD), v0.1.
- **Intent:** a functional (non-technical) description that Codex converts to a TDD, then to
  schema/services. No schema, code, or engine internals in the FDD itself.
- **Core concepts:** single-shard planet (Earth-scale, space not limited); **God Mode**
  (offline, single-user world-gen/simulation, never interacts with players); three player
  modes — **Adventurer** (~85%, the core loop), **Realmwright** *(retired)*, **Dungeon Master**.
- **Governance (all dead):** region partitioning; Realmwright claim via quorum approvals
  (3 / 10–20 / 100+ by density); DM claim permissive; inactivity → decay → reclaim.
- **Zoning/construction:** Realmwrights place non-destructive plan objects; adventurers build
  in zoned plots with voxel tools. *(Realmwright zoning-authority half is dead; adventurer
  voxel building survives.)*
- **Contracts:** Realmwrights/DMs post tasks (terrain, roads, deliveries, public works);
  adventurers complete for currency/XP/plot rights.
- **Lifecycle:** creation → maintenance (activity keeps regions/dungeons alive) → decay
  (inactivity removes authorities; dungeons collapse; regions reopen).
- **Out of scope for the FDD:** voxel sim internals, chemistry, AI routines, economy balancing,
  rendering, networking, DB schema, auth, access control — all deferred to the TDD.
- **Proposed pipeline:** FDD → (Codex) TDD → entities/tables/enums/relations/events → backend
  modules per project standards.

---

## Reconciliation notes (editorial)

- **God Mode / Clay Engine → "epoch 7 / GM mode":** the offline single-user world-builder is the
  through-line that survives intact. The *name "Clay Engine"* and the "outside the social
  equation" isolation principle are captured here because they are not recorded in the
  `prism-bible-recompile` ledger.
- **Realmwright:** the one genuinely new-and-then-discarded concept. It briefly split the
  "builder" side into surface (Realmwright) and underworld (Dungeon Master). Current canon keeps
  a single builder axis (the **DM tech-tree** — see round-10 rulings, boss authoring / "the
  game's building tools") plus **GM mode** for world authoring, and has **no** surface-steward
  player-authority role.
- **Governance/quorum/caps:** superseded by design ethos. Prism deliberately does **not**
  systematize social/organic consequences; scarcity is handled by geography and by the
  contested-world / pariah dynamic, not by voting thresholds or hard role caps.
- **Cross-refs:** `chatgpt-dm-system-notes.md` (DM + adventurer + elemental systems, in depth);
  round 8/9/10 rulings in the `prism-bible-recompile` ledger (roles, combat, death, contested
  world, no reputation); this session's Realmwright-retirement note.
