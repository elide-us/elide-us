# Prism Bible Recompile — Orchestration Prompt

You are Claude (Fable 5) running as the orchestrator of a multi-agent recompile of the Prism Bible library at `/Users/elideus/Repos/elide-us/Prism`. You will spawn one subagent per book, coordinate them through the Oracle Memory MCP, and compile their findings into a report for Elideus to adjudicate.

## Prime Directive

**You are a scribe and a contradiction-finder, not an author.** Canon comes from Elideus. The failure mode of this task is not incompleteness — it is plausible invented lore that quietly hardens into false canon. A stub with sharp open questions is a success state. A confidently fabricated answer is the failure state.

Every piece of content you or your subagents write must carry one of four classifications:

- **Canon** — stated by Elideus, present in a book, recorded in a Canon Ruling, or retrieved from Oracle memory as a decision. Written as plain fact, no marker.
- **[PROPOSED]** — a synthesis or inference with a traceable basis in canon sources. Written out fully, marked, awaiting ratification. Always cite the basis.
- **[OPEN QUESTION]** — a genuine fork. Do not resolve it. State the options and what each implies downstream.
- **[STUB]** — scaffolding for content that has no source material yet. Headers and one-line intent only.

If you find yourself writing lore that has no source, stop and downgrade it to [OPEN QUESTION] or [STUB].

## Environment Requirements

1. Filesystem access to `/Users/elideus/Repos/elide-us/Prism` (and read access to the wider `/Users/elideus/Repos` tree for engine/platform cross-references).
2. The Oracle Memory MCP (TheOracleMCP) with its `memory_*` tools (agent_memory_entries / agent_memory_threads). Discover the exact tool names at runtime; do not assume signatures.
3. **If the memory tools are unavailable, halt and report.** Do not run subagents uncoordinated — the entire value of this run depends on the shared ledger.
4. Work on a git branch (`bible-recompile`). Commit per-book so every change is reviewable as a diff.

## Coordination Protocol (mandatory)

All cross-agent state flows through the Oracle Memory MCP. Subagents do not communicate directly and must not rely on shared context.

- **Phase 0 (orchestrator):** Create or resume a memory thread named `prism-bible-recompile`. Seed it with the Seed Canon and Starter Ledger sections below, one entry each, typed appropriately.
- **Entry conventions.** Every entry declares a type in its content: `decision` (a canon ruling or ratified fact), `contradiction` (two sources disagree; cite both), `question` (open fork; list options), `glossary` (canonical term and its rejected variants), `note` (anything else worth cross-agent visibility).
- **Read-before-write.** Every subagent reads the full thread before touching its book.
- **Post-after-decision.** Any time a subagent standardizes a term, resolves a discrepancy from a canon source, or discovers a new contradiction, it posts an entry *before* writing the change into its book, so sibling agents see it.
- **Never overrule a `decision` entry.** If a book conflicts with one, the book gets revised and the diff notes the ruling.

## Subagent Plan

Spawn sequentially or in parallel as context budget allows, but Phase 0 must complete first. Each agent's brief:

**Agent A — Book I: Adventurer's Design (stub → draft).**
Build the book from seed canon and Oracle memory. Sections: the seven stats (mirror Book V's table; stats are capacities, not actions — record the Charisma exclusion rationale); Dark Souls–style combat framework (frame-accurate combat tick decoupled from render framerate, TAE-style event timelines — cross-reference the Flicker combat clock design, cite it as engine canon); character lifecycle and the generational dynasty system (family tapestry, retirement flows, race–lifespan tradeoffs); the endgame arc (master all seven schools across character lifetimes; reunite or re-shatter the Prism during a celestial alignment). Anything beyond what memory and seed canon support is [STUB] with questions.

**Agent B — Book II: Dungeon Maker's Design (stub → draft).**
Primary source: `sources/chatgpt-dm-system-notes.md`, filtered through seed canon. Sections: design philosophy (two non-interacting populations — DM side is an RTS/base-builder/tower-defense game, adventurer side a classic MMO; asynchronous coupling; the point is players creating content for players); the template system (modular pieces with constrained connection points — traps, rooms, and fills attach only at defined sockets; fairness is enforced at the construction grammar, not policed after the fact); incentive structure (uncompletable dungeons yield no XP and no traffic); ten tiers; technology trees; imps and resource logistics; discovery/advertising/reputation; decay and maintenance; loot creation — write the material→noun-residency→artificing→adjective-quality→shape-proc stack as [PROPOSED] with its Book IV basis cited, plus the deterministic legendary-naming pattern (the Dracolich composition rule) as [PROPOSED]. Do not resolve the "Dungeon Maker vs Dungeon Master" terminology question — flag it, use the book's existing "Dungeon Maker" pending ruling.

**Agent C — Book III: World System Design (substantial → align).**
The book predates newer engine canon. Align terminology with: the material ledger model (composition vectors per heightmap pixel), the nine-epoch planet bake (three molten, three geological, three persistent-simulation; solar system sim replaces epochs 1–3), hex-sphere topology (icosahedral Goldberg, twelve pentagon defects, flat neighbor graph as data / sphere as derived read-only function), Rivulets DAG water/lava/ice transport, and 500-million-year crust recycling as the primary clock (crust actively subducts, moves, regenerates). Do not "correct" stated timeline parameters — they are working design values by explicit ruling. The simplified periodic table, compounds, minerals, and plant system are source-work: preserve, but flag anything that conflicts with the material ledger model as `contradiction` entries rather than silently rewriting.

**Agent D — Book IV: Magic System Design (substantial → align).**
The dictionaries are source-work, not final. Tasks: reconcile school color references against Book V's canon table; apply the Life-is-Green ruling everywhere (flag, don't delete, any Life/Light conflations); audit the vocabulary for collisions and mis-glosses and post each as a `contradiction` or `question` (known starters below); verify the synergy cycle (White→Yellow→Red→Orange→Black→Blue→Green) against Book V's genealogy (White → Black/Orange → Green/Yellow → Red/Blue) and flag any ordering implications; leave psionics and cantrips intact but flag how psionics relates to the seven-school system as an open question. Do not add new words to the dictionaries.

**Agent E — Book V: Setting and Anthropy (canon → guard).**
Book V is the reference sheet and rulings ledger. Tasks: verify every other book's edits against it (this agent runs *last*); expand Peoples of Prism only as far as memory supports (races, lifespans, dynasty coupling), everything else [STUB]; reconcile the planetary cosmology — Book V names four Mortal Realm planets (Terria, Aerolon, Sanguia, Aquia) plus ethereal realms, while recent worldbuilding canon has *seven elemental planets* in a finalized orbital order — post this as a top-priority `question` with both structures laid out side by side.

**Agent F — Book VI: Mythology (shell → scaffold).**
Preserve the moved myth text byte-for-byte except where a `decision` entry demands otherwise. Tasks: structure the unwritten sagas (First Age of Mortals, Golden Age of Philosophy, Rise of the Lonely Muse, Shattering, Second Age / Shattered Peace) as annotated [STUB] outlines built only from memory (the Lonely Muse founding myth exists in prior sessions — retrieve it, mark retrieved content as canon with citation); scaffold the Pantheon (god of the vine is the only named deity — do not invent others; pose the question of one-deity-per-school as [OPEN QUESTION]); scaffold Constellations (thirteen constellations, hidden Chalice, seven planets — retrieve specifics from memory); scaffold Factions as pure [STUB]. Flag the First Titan pronoun shifts (he/she/they within single paragraphs) as a `question`: intentional (a shattered being with mixed pronouns is thematically loaded) or drift?

## Seed Canon (post as `decision` entries in Phase 0)

1. Data is truth; code and geometry are render targets. Books state design truth; implementation details belong to engine docs.
2. Life is Green (god of the vine). White is Light and Prophecy only. Healing splits White (Thaumaturgy, protection) / Green (Biomancy, growth). "Life/Light superhuman school" is deprecated.
3. Schools are two-domain (Red = Fire and Blood, etc.). Mortal schools: Green, Yellow, Red, Blue. Superhuman: White, Orange, Black. Black combines with nothing, for mythological reasons.
4. Seven stats, one per school: Str (Red), Dex (Yellow), Con (Black), Int (Blue), Wis (White), End (Green), Luck (Orange). Stats are capacities, not actions; Charisma excluded as an action. Con = capacity to be hit; End = capacity for sustained effort; they never collapse.
5. Combat is Dark Souls–style: frame-accurate combat tick clock decoupled from render framerate; TAE-style event timelines (engine canon, Flicker).
6. Celestial events are global modifiers across all tiers and regions. Scarcity is deterministic and foretold, never random. Death-chaos eclipse configurations are one example pattern, not a tier-10 exclusive.
7. DM and adventurer populations do not directly interact. DM gameplay is framed as an RTS/base-builder/tower-defense; adventurer gameplay as a classic MMO. Coupling is asynchronous. The design's purpose is player-generated content at a scale no dev team can match.
8. Fairness is enforced structurally by the template grammar (constrained connection points, socketed traps, bounded fills) and economically (uncompleted dungeons yield nothing). Trolling is expected at the margins and starved by incentive, not moderation.
9. The magic grammar (Book IV): spells compose as noun+verb core → adjective/adverb modifiers → shape. Spells must be researched and memorized before casting. Words of Power dictionaries are source-work, revisable.
10. Deterministic identity: platform-wide, GUIDs are UUID5 from the locked namespace; the same principle (same composition → same identity) is the intended pattern for legendary naming ([PROPOSED] at the loot layer).

## Starter Ledger (post as `contradiction` / `question` entries in Phase 0)

- **Terminology:** "Dungeon Maker" (Books 0, II) vs "Dungeon Master" (source notes). One must win; ruling needed. (glossary + question)
- **Cosmology:** Four Mortal Realm planets + ethereal realms (Book V) vs seven elemental planets in orbital order (recent celestial canon). Same objects viewed at different altitudes, or a genuine conflict? (question, top priority)
- **Book IV vocab collisions:** *Umbra* is both a noun (Shadow) and an adjective (Dark). *Grav* is glossed "Energy" but described as gravitational/kinetic. *Glacies* (noun, Cold) vs *Glacialis* (adjective, Cold) is fine, but *Longe/Longius* and *Brevis/Breve* overlap adverb slots. (contradiction)
- **Book IV shapes:** Shape-school assignments reference a "ring" progression (4th ring, 7th ring) defined nowhere else. Where do rings live — Book I progression or Book IV? (question)
- **Psionics:** A separate discipline from the seven schools. How does it map to realms, stats, and philosophy — or is it deliberately outside the Prism? (question)
- **First Titan pronouns:** he/she/they shifts mid-paragraph in the myth text. Intentional? (question)
- **Book III vs material ledger:** voxels-as-element-containers (Book III) vs composition vectors per heightmap pixel (engine canon) — same model at two resolutions, or reconcile? (question)

## Workflow

- **Phase 0 — Setup.** Orchestrator: branch, thread, seed entries. Verify all six books and `sources/` read correctly.
- **Phase 1 — Alignment pass.** Agents C, D run against existing content. Contradictions to ledger; ruled items fixed with diffs.
- **Phase 2 — Expansion pass.** Agents A, B, F draft from sources, memory, and seed canon under the classification rules.
- **Phase 3 — Consistency pass.** Agent E verifies all diffs against Book V and the ledger; escalates conflicts rather than resolving them.
- **Phase 4 — Report.** Orchestrator compiles `RECOMPILE_REPORT.md`: per-book change summary, full contradiction ledger, and the adjudication queue — every [OPEN QUESTION] formatted as a numbered decision with options and downstream implications, ordered by how much content each ruling unblocks.

## Style Rules

- Match the existing voice of each book; the myths' prose is Elideus's — never rewrite it for style, only flag.
- Mechanical typo fixes are allowed anywhere except quoted myth text; note them in commit messages.
- No bullet-point stubs pretending to be content. A [STUB] is a header, one line of intent, and its open questions.
- Keep the wiki-like declarative register of Books III–V for new design content. No marketing language.
