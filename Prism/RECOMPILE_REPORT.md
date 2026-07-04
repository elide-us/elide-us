# Prism Bible Recompile — Run Report

**Date:** 2026-07-02 · **Branch:** `bible-recompile` · **Oracle thread:** `prism-bible-recompile` (`CFD10EEB-682D-425B-995B-FF95FCED8B98`)

Six agents ran against a shared Oracle memory ledger under the four-class discipline (Canon / [PROPOSED] / [OPEN QUESTION] / [STUB]). Every change is a per-book commit reviewable as a diff:

| Commit | Book | Agent |
|---|---|---|
| `add63a4` | Baseline snapshot (all files, pre-recompile) | orchestrator |
| `bc820b5` | Book III — world-system alignment | C |
| `1e45401` | Book IV — canon audit | D |
| `d6e5057` | Book I — draft from seed canon | A |
| `f48abff` | Book II — draft from source notes | B |
| `b39c91a` | Book VI — mythology scaffold | F |
| `99f17d6` | Book V — guard pass | E |
| `57f89a2` | Book III — Elideus's mid-run rulings applied | orchestrator |

**Ledger state:** 12 seed-canon decisions, 4 mid-run rulings from Elideus, ~30 contradiction/question/glossary/note entries. All 38 ledger GUIDs cited inside the books were verified to exist in the thread.

---

## Findings that shaped the run

1. **Oracle memory contains no Prism lore.** Probed exhaustively (Muse, constellations, combat, dungeons, planets, races — ledger `7802053D`). The store holds engine canon (`flicker`) and backend canon only. Everything the briefs assumed was "retrievable from memory" — the Lonely Muse founding myth, constellation specifics, the seven-planet orbital order, race/lifespan data — **does not exist in memory and must come from Elideus.** Nothing was reconstructed; the absences are recorded in the books as [STUB]s with citations.
2. **The combat-clock design has no engine document.** Seed canon 5 (Souls-style, frame-accurate combat tick, TAE-style timelines) is canon by your statement alone; ledger `9D249EE4` is the citable source. Worth writing up as a flicker doc eventually.
3. **Agent E's pass ended early** (session limit) after completing its Book V edits and posting its four findings; its per-book verification of Books II/VI citations was finished by the orchestrator (GUID cross-check above).

## Mid-run rulings from Elideus (recorded and applied)

| Ruling | Ledger | Applied |
|---|---|---|
| Magnesium #12 is canon; table is 27 elements | `84E68FF7` | Mg row added to Book III's periodic table, mirrored verbatim from `periodic_table.json` |
| Epoch/crust-cycle timing unconfirmed; POCs non-canon | `65AE9274` | Book III Crust Clock reworded: concept canon, all durations working values (closes contradiction `53092068`) |
| Valence removal "probably fine" (hedged) | `217A3A9B` | Book III valence notes deprecation-flagged; column retained pending confirmation (item 10 below) |
| Book IV syllabus alignment deferred to engine effect-building | `33173716` | Agent D's audit flags stand as the engine-side worklist; no bulk book rewrite |

---

## Per-book summary

**Book I — Adventurer's Design** (3 lines → full classified draft). Canon: seven-stat table mirroring Book V; Charisma exclusion and Con/End non-collapse rationale; Souls-style combat framework; dynasty and endgame arc one-liners. [PROPOSED]: Con/End combat readings. [STUB] with sharp questions: the other five stats' combat readings, combat vitals, death rules, dynasty mechanics, ring progression, endgame resolution.

**Book II — Dungeon Maker's Design** (3 lines → full draft, 11 sections). Canon: two non-interacting populations, async coupling, template grammar fairness, economic starvation of trolling. Source-attributed: tiers, tech trees, imps, discovery/reputation, decay. [PROPOSED]: the loot stack (material → noun-residency → artificing → adjective-quality → shape-proc) with a per-rung basis map (`C1AF172E`) and deterministic legendary naming per the UUID5 principle. Uses "Dungeon Maker" throughout, fork flagged once.

**Book III — World System Design** (aligned, then rulings applied). New [PROPOSED] World-System Frame preamble (material ledger, nine-epoch bake, hex-sphere, Rivulets, crust clock); voxel-container passages flagged against fork `9C677816`, never rewritten; all source tables preserved; Mg added; timing softened; valence deprecation-flagged.

**Book IV — Magic System Design** (audited, not rewritten). Inline flags: dictionary slot collisions, creature-category collisions, Life/Light conflation in the White ring examples, synergy-vs-genealogy [OPEN QUESTION], rings and psionics tied to their forks, Necromancy annotated as the Black single-school exception. No words added or removed. Per ruling `33173716` these flags are now the engine effect-building worklist.

**Book V — Setting and Anthropy** (guarded). Two mechanical fixes ("Life and Earth" → "Earth and Life"; "Charism" → "Charisma"); editorial pointers at the cosmology fork and the moral/mortal wordplay; Peoples of Prism structured as a real [STUB] with five open questions. Canon Rulings ledger untouched — no ruling added without you.

**Book VI — Mythology** (scaffolded). Myth prose byte-identical (sha256-verified). Five saga stubs built only from Books V/VI's own text; Pantheon (god of the vine sole deity, structure posed as question); Constellations (canon counts only); Factions (four pure stubs from existing hooks); one editorial annotation for the pronoun fork.

---

## Contradiction ledger

**Resolved by ruling this run:**
- Crust-recycle period 500 My vs ~1.5 BY/6 recycles (`53092068`) → both are non-canon working values (`65AE9274`).
- Book III 26 vs engine 27 elements → Mg added (`84E68FF7`).

**Open contradictions (cited, not resolved):**
- `78524243` — Book III water-as-voxel-compound vs engine "water/ice/lava are effects, not layers".
- `44F17D1E` / `94774F28` — dictionary slot collisions (Umbra, Grav/Vis, Saxum/Terra, Altus/Altior, Infimus/Humilis, Durare/Longe/Longius, Breve/Brevis). ***RESOLVED round 15*** (`AA124D5D`) — see below; no longer deferred.
- `8E29A0D3` — creature-category collisions (liches ×2, phoenixes ×2, Aetheron gloss). ***RESOLVED round 15*** (`AA124D5D`) — see below.
- `62E81F6F` — "White (Life Magic)" ring examples conflate Life/Light (deprecated per Life-is-Green; flagged in place).
- `313123F1` — Book IV cites "Black combines with nothing" to Book V's rulings ledger, but the clause lives only in thread decision `442D03E8` (see item 11).
- `363D1BBA` — brief-vs-thread GUID transposition (bookkeeping; recorded, no action needed).

**Open questions:** all 20+ [QUESTION] entries feed the queue below.

---

## Adjudication queue

Numbered decisions for Elideus, ordered by how much content each ruling unblocks. *(cheap)* = a one-line ruling suffices.

**1. Cosmology — four Mortal Realm planets vs seven elemental planets** (`973162E7`) — **RESOLVED (rounds 1–3 + 9).** Body order recorded (`8543A752`), slot-5 = Light (`D30A32BF`), and the final piece — the seven realm names ARE the seven bodies and their Titans — ruled round 9 (`2FCEB0B3`, closing `7BC8E9B6`).
Options: (a) same objects at different altitudes — the mythic/structural view (4 mortal planets + Realm of Light + 2 ethereal realms) and the astronomical view (7 planets, one per school) coexist; (b) genuine conflict — Book V's roster predates the celestial model and gets revised. Also needed regardless: **the seven-planet orbital order recorded somewhere durable** — it exists only in your head; no book or memory holds it.
Unblocks: Book V realm roster, Book VI Constellations and celestial mythology, which peoples live where, the celestial sim's body roster and alignment patterns.

**2. Rings — who owns the progression** (`63B28A6B`) — **RESOLVED round 8** (`B92EE74A`): Option (b), Book IV magic-mastery structure. Remaining sub-items (exact ring count/table, reagent-grade curve, Black's ring mechanic) are new small forks, not this queue item.

**3. Death rules — what ends an active life** (`D25A57E1`) — **RESOLVED round 10** (`0B98560B`): Option (a) — combat death is a setback (respawn + EQ-style corpse recovery). Terminal exits are a category of *additive* dispositions (settlement NPC / heroic status / old-age patron / the Muse's path); only **Burning** subtracts — permanent delete or a sacrifice play — at extreme cost. Roster is limited only by time. Inheritance (`D2C52C88`) stays separate/open.
Options: (a) retirement only, combat death is a setback; (b) combat death can end a life (permadeath tier); (c) something between (age + circumstance). Agent A called this the single highest-leverage unknown: it decides whether the dynasty system is load-bearing or flavor.
Unblocks: Book I lifecycle, dynasty stakes, and most of the combat stub's tone.

**4. Combat vitals and the five unruled stats** — **RESOLVED round 10** (`DE7E8605`, `BFBE6085`): Con → Health (survivability), End → Stamina (action economy); the five lanes ruled — Str force, Dex speed/precision, Int technique + the research gate, Wis foresight/parry/divine, Luck fortune/crit/loot. The derived-value *formulas* remain `[BUILD]`.

**5. Dynasty inheritance — what transfers across generations** (`D2C52C88`, with `432AAB1F`)
Options per fork: items / school mastery / reputation / ring progress / stat predispositions by bloodline — any subset. Plus the endgame corollary: how "master all seven schools across lifetimes" accumulates, and whether reunite-vs-re-shatter resolves world-globally, per-dynasty, or cyclically.
Unblocks: Book I dynasty mechanics and the endgame arc.

**6. "Dungeon Maker" vs "Dungeon Master"** (`500F8438`) *(cheap)* — **RESOLVED round 13** (`C6E42EE8`): Dungeon Maker wins platform-wide; Dungeon Master dropped as a likely TSR/WotC trademark risk.
Unblocks: Book II terminology finalization, the "DM" gloss, UI copy.

**7. The DM–adventurer interaction boundary** (`A2596715`)
The source says loops are "deeply interconnected" and adventurers can track imp routes; seed canon says populations never directly interact. What happens live: can adventurers fight imps in the world? Can a Maker watch a run in progress? What does the tower-defense actually defend against?
Unblocks: Book II's imps/logistics and discovery sections at mechanical depth.

**8. Boss builder mechanism** (`EBF514AA`)
Options: word-grammar composition (like spells), socketed templates (like rooms), or both. **Illuminated, not resolved, round 8** (`563804ED`): a Vetala-riding-a-Dracolich boss concept demonstrates "archetype + word-grammar composition, stacked" as one candidate direction — a worked example, not a ruling.
Unblocks: Book II's boss builder section (currently four source lines + stub).

**9. Loot stack ratification** (`C1AF172E`, dependency `67DB3F76`)
The material → noun-residency → artificing → adjective-quality → shape-proc stack is [PROPOSED]; rungs 4–5 (adjectives as quality grades, shapes as procs) rest on your brief alone. Legendary naming additionally needs Draco/Mortuus to exist in the dictionaries (engine-side per `33173716`).
Unblocks: Book II loot creation as canon; the item-creation design doc the source session already identified as next.

**10. Valence removal — final confirmation** (`217A3A9B`) *(cheap, near-ratified)*
You said "probably fine". On confirmation: strip the VEs column from Book III and `periodic_table.json` in one pass, delete the valence notes.

**11. The Black clause's citation home** (`313123F1`) *(cheap)* — **RESOLVED round 13** (`5936222F`): Option (b) — "Black combines with nothing" ratified straight into Book V's Canon Rulings ledger.
Options: (a) fix Book IV's two citations to point at thread decision `442D03E8`; (b) ratify "Black combines with nothing" into Book V's Canon Rulings ledger, which makes Book IV's citation valid. (b) also settles where future books point.

**12. "Moral realms" vs "mortal realms"** (`89D9BC90`) *(cheap)* — **RESOLVED round 13** (`2EE825B7`): "mortal" is correct; "moral" was a voice-transcription artifact, not wordplay. Books V and VI corrected.
Typo or deliberate wordplay. Book VI already quotes the phrasing; both books follow the ruling.

**13. Pantheon structure** (`69E6E8E7`) — **RESOLVED round 9** (`2FCEB0B3`): Option (c), the gods ARE the Titans. Five count — the Two-Faced God + Terria/the Vine, Aerolon/the Bird, Sanguia/the Mountain, Aquia/the Serpent; White is the formless Principality (no figure); the Divine Vine = god of the vine = Terria; mortal Principality-holders stay human (`24054B89`), the magics passing Titan → ancient immortals (original patrons, names lost) → humans (`12411325`).
One god per school / multiple per virtue-vice pair / no gods, only remembered Titans. Unblocks Book VI Pantheon and Factions (religious orders).

**14. Who are the Second Age immortals?** (`BB152B09`)
The heading "The Second Age of the Immortals" frames the present, mortal game age. Unblocks the Shattered Peace saga framing.

**15. Peoples roster** (`EBA28F43`)
Which races exist, lifespans, playability — plus the interface question: does Book IV's Terradun entry (dwarves, kobolds, gnomes) attest peoples or only targeting vocabulary? This is an authoring session more than a ruling.
Unblocks: Book V Peoples of Prism, Book I race–lifespan values.

**16. Psionics' seat** (`7609E7E9`) — **Illuminated round 9** (`BC54B7D7`): Chaos (Orange) is the magic side of psionics and the First Titan's hidden other face; Psionics keeps its own Principality (Inverted, Book VII) as the willed/power side. **Further clarified 2026-07-03** (`CC7C057B`): psionics is one unified discipline, not two systems needing reconciliation — Magic, Cantrips, and Psionics are three parallel paths to the same underlying power, and Inverted's Lovecraftian bestiary entries are simply the extreme/monstrous end of the same psionics spectrum that also holds the mundane 16-ability roster (telepathy, technopathy, etc.) already in Book IV. Not fully resolved — the exact seat and the hidden-Titan link (`57960182`) stay open.
Outside the Prism by design / a casting style of an existing school / legacy pending redesign. Unblocks Book IV psionics framing and whether "master all seven schools" has an eighth asterisk.

**17. Synergy cycle vs school genealogy** (`244A27FF`)
Book IV's cycle (White→Yellow→Red→Orange→Black→Blue→Green) vs Book V's genealogy (White → Black/Orange → Green/Yellow → Red/Blue), and Black's seat in a loop when Black combines with nothing. Vocabulary side is deferred to engine work; the *ordering* question is book-side.

**18. First Titan pronouns** (`5E9DB061`) *(cheap)* — **RESOLVED round 9** (`5E2FB886`): intentional, the expression of chaos; pronouns rotate they/him/her/them/us/hers/his/she/we. Prose preserved; Book VI editorial converted to canon.
Intentional shattered-being pronoun mixing, or drift. Book VI annotates but does not touch the text.

**19. Voxel model fork** (`9C677816`, with `78524243`)
Same model at two resolutions, or Book III revision. Low urgency — Book III is fully flagged and readable either way.

**20. Authoring sessions wanted** (not rulings)
The Lonely Muse founding myth (exists nowhere; Book VI stub is ready to receive it) · constellation names and stories (**8 of 13 named as of round 9, `25699317`; 5 slots open**) · the **"story of the mountain and the plow"** (Sanguia↔Terria — earth, life, growth, blood; remembered but unrecovered, round 9) · Book II per-tier unlock table · the flicker combat-clock engine doc.

---

## Addendum — adjudication round 1 (2026-07-02, post-report)

Elideus reviewed the report and ruled on the first batch. Recorded in the ledger and applied:

- **Item 1, Cosmology — structurally RULED** (`05840ADF`). The realms are distilled into the celestial system: seven instances of the world, each a different body, one shared universe and celestial simulation; hex-planet pentagon zones are gateways into the other realms. Book V's editorial updated. **Still pending:** the body order values (a strong decision, recorded nowhere — needs Elideus), ratification of the realm↔body mapping ([PROPOSED]: Book V's seven realm names are the seven bodies), and a new question — pentagon zones were previously "beyond player reach"; as gateways, what condition opens them?
- **Item 2, Rings — under review** (`2A2A5A97`). Elideus leans magic-system origin; fuzzy old idea, needs further review. Archaeology flagged for that review: the 2014 notes' "three ranked spheres of power in each school" is a plausible ancestor.
- **Items 3/5, Death rules and dynasty — confirmed authoring work** (`07B563B1`). Real mechanics to be written down; forks stay open until that session.
- **Item 4, Stats/combat — stats LOCKED; coupling is design-and-build work** (`78C70439`). 2014-06-27 design notes archived at `sources/combat-systems-ideation-2014.md` as **IDEATION ONLY**; the durable payload is the status-effect taxonomy (stun, snare, slow, root, poison, confound, aphasia, fear, confuse, silence, expose, tashina, mesmerize) as direct game mechanics plus time/distance/movement constraints. Book I's combat section now points at it.
- **Memory policy** (`3107D080`, project `general`): durable memory lives in the Oracle MCP; local MEMORY.md/CLAUDE.md files are pointers only. Repo CLAUDE.md created accordingly.

## Addendum — adjudication round 2 (2026-07-02): the celestial session intake

Elideus surfaced the 2026-07-01 claude.ai session ("Celestial system with elemental planets") and pasted the majority of it into the recompile; it is archived verbatim at `sources/celestial-cosmology-session-2026-07-01.md`. It closed the queue's top item and several others:

- **Item 1, Cosmology — CLOSED (body order recorded).** Final orbital order (ledger `8543A752`), inner → outer: Chaos, Fire, **Home** (carries the moon), Earth, Life/Light (white gas giant), Air (the ringed one), Water, Death (occulted; shadow-transits). Palettes, equal apparent sizes (~¼ sun/moon disc), rings on Air, Death's occultation event — all ruled and written into Book V. Remaining: the **slot-5 naming fork** ("Life/Light" predates Life-is-Green — ledger `7BC8E9B6`) and ratification of the realm↔body mapping.
- **Time and the moon — RULED** (`D2AAFEEC`): 1 in-game minute = 5 real seconds (2-hour day); the moon is the real Moon, 1:1, ephemeris-driven, with Elideus's acceptance test recorded. Open declarations needed: latitude mapping, reference longitude; the 13-period civil-calendar alignment stays open.
- **Item 20, the Lonely Muse myth — RECOVERED** (`BDB707A5`). The founding myth's canonical beats, in Elideus's own telling, are archived and written into Book VI's saga stub. PRISM = the crystal. Her post-sundering fate remains the load-bearing open question. The prose is still Elideus's to write.
- **Constellations — RULED** (`AF819A62`): thirteen; the hidden **Chalice** (the Muse's, revealed on moon–Death alignment) plus Beltan the Bear, the Two-Faced God, the Touching of God, the Night of the Daggers; mixed registers; eight slots open. New question: is the Two-Faced God the First Titan?
- **Items 3/5 partially, endgame scale — CLOSED** (`EC054473`): the reunite/re-shatter choice is personal and **terminal** — the character retires; the world persists; retirement is a category of terminal quests; the Muse's Ascension gate stack (seven prior retirements, near-immortal vessel, Chalice-eclipse timing, permanent tapestry marker) is canon. Three starting NPCs and the non-instanced quest-NPC presence system are canon. Death rules (`D25A57E1`) and non-mastery inheritance (`D2C52C88`) remain open.
- **Stratigraphy — RULED** (`66541B83`): Titans are non-humanoid cosmic forms (the Divine Vine); Beltan is near-immortal into the modern era (spelling **Beltan**); the Veiled Veil / Empire of the Steel Crown human-era material is canon-pending-refit, inventoried in Book VI. New questions: Divine Vine vs god of the vine; Dragan/Bloodfangs appearing in two eras; the unrecovered "vines of early creation" document.
- **Design canon batch** (`95EAF28D`): the combat fairness law (Half-Life lineage, telegraph-and-dodge, spatial+temporal tells) into Book I; story content packs with validation-as-authorship into Book II; claims upkeep/decay; the "Welcome, dreamer…" boot sequence; the one-consciousness metaphysical frame.

**Queue effect:** item 1 closed (naming fork `7BC8E9B6` replaces it, much smaller); item 20's Muse and constellation sub-items largely resolved (prose authoring remains); new items: slot-5 naming *(cheap)*, Two-Faced God ↔ First Titan *(cheap)*, Divine Vine ↔ god of the vine *(cheap)*, Muse's post-sundering fate, moon latitude/longitude declarations *(cheap)*, human-era refit *(authoring)*, financial-calendar structure confirmation *(cheap)*.

**Round 3 (2026-07-02, same day):** slot-5 naming RESOLVED (`D30A32BF`) — the planet is **Light**; "Life/Light" was Elideus's misremembering, the color/philosophy canon stands. The seven sky-planets now map one per school (Chaos→Orange, Fire→Red, Earth→Green, Light→White, Air→Yellow, Water→Blue, Death→Black). Books V and VI corrected. Fork `7BC8E9B6` narrows to its part (b): whether Book V's seven realm names name the seven bodies.

Also round 3: **pentagon gateways refined** (`73EA6D39`) — twelve points per world; idea-grade split of six above the survivable line (mountains) and six below (deep ocean); zones "weird" in the Bermuda-Triangle register; portals surround the points. Supersedes the archived session's 7-gates/5-reserved proposal. Still open: transit mechanics, and how twelve points serve six destination realms.

And: **Advent locations ruled** (`35A9CEAE`) — the pentagons are unreachable BY DESIGN: the player-centered hex-cluster renderer breaks on pentagons, so pentagon spaces sit outside the standard world and entering one removes you from it; world-gen enforces the unreachability. The elsewhere is hand-crafted, rule-shifting content ("a void where you can swim in all directions, distant glows of massive titans faces"); fog-wall teleport is idea-grade. Named **Advent locations** with the full Berserk meaning. New question: are the Advent eclipse (event) and Advent locations (places) mechanically coupled?

And: **celestial primacy ruled** (`3312B2AB`) — celestial events drive ALL possibilities; design-side, events are conceived only as the sky's schedule, never as dates (players resolve the sky to calendars, the design never runs the other way). Answers the Advent coupling question at the principle level: the doors answer to the sky; mechanics still open. The unification principle recorded verbatim: "colors, stats, events, people, bodies, magic, titans, all reflections of the same Prism."

**Round 4 (2026-07-02): the colors/schools/philosophies REALIGNMENT** (`FF1F7955`). Schools are not schools of colors — each color's two aspects are themselves two schools, each pair on its color's shard world: **fourteen schools among the seven worlds**. Philosophies belong to the **color** (followers of both at both schools), each pair an honorable-vs-dishonorable approach to the color's virtue, all running off one axiom (collective/impersonal vs self/claimed). **Four pairs revised:** Enlightenment vs **Revelation**, Valor vs **Conquest**, Diligence vs **Cunning**, Perseverance vs **Hunger**. Applied: Book V table + new Canon Rulings entry (old two-domain ruling annotated), Book I stat table, Book VI (Golden Age, sects, institutions, Muse flag), Book IV editorial; seed canon entries 442D03E8/2ABDD515 updated in place. **New forks:** what "the seven schools" means under fourteen — the Muse's arc and the endgame gate (`FCB93BC0`); whether the honorable/dishonorable axiom gets a player-facing name (`0E5DA637`).

**Round 5 (2026-07-02): lifecycle economics and the bestiary** (source archived: `sources/animation-lifecycle-session-2026-07.md`). **Lifecycle ruled** (`91F84075`): children are invested to adventurer's age with ongoing in-game currency and are what new characters roll from (nothing pay-to-play, ever); the adventurer is no-take-backsies; **level 10 is the retirement threshold** (a yearning; benefits chosen for the family); heroic-sacrifice deaths become permanent account badges; enchanted items require regular mana upkeep; the skill system is deep, opaque, and deterministic-fair; the rules never bend. Narrows `D25A57E1` (ordinary combat death still open) and `D2C52C88` (items/reputation still open). The five-state thread sketch (Ghost/Burned), race-as-tempo, and dynasty tracks are held at [PROPOSED] — Elideus's verdict was "pretty close," not ratification (`A8FEC45C`); the inheritance-unit fork (one-parent / whole-tapestry / chosen-mentor) is posed unanswered. **Bestiary ruled** (`B4F9A3AC`): biomes seed specific creatures, monster recruitment is region-gated, dungeon placement matters — Book II gains a Placement and Monster Recruitment section; the bestiary is a named buildout need (home undecided). Engine-side (flicker ledger `386AC689`): sol2 largely discarded for the disk-first rebuild; the celestial system is a game-event calendar; a granny-tier animation system is a named need.

**Round 6 (2026-07-02): mastery and the unnamed split.** Seven-vs-fourteen RESOLVED (`A8FF6AB0`, closing `FCB93BC0`): mastery means **at least one school from each color** — fourteen is excessive; the Muse's seventh was Light, White's school of Light; schools additionally contain **further disciplines** (new tier, specifics unrecorded). Axiom naming RESOLVED as deliberate absence (`E4F46BA5`, closing `0E5DA637`): the split is never named or judged by the design — "we do not preach, we reveal" — and the **"Honorable vs Dishonorable" header is struck as misspeak** across Books V/I/VI and the realignment entry. New canon: **the Muse took the self-aligned philosophy in all schools** (Book VI), and player-chosen philosophy expresses in NPC settlements (selfish → hostile to outsiders; communal → different benefits; no judgment). Books I, V, VI corrected.

Round 6 follow-up: **disciplines are not new** (`DCB350D4`) — they are Book IV's documented domain layer (Magical/Specialty/Ancient Domains: Pyromancy, Divination, Thaumaturgy, …); each spell belongs to a discipline. This also RESOLVES Agent D's "domain double-duty" fork (`9D85D076`, Option A): color aspects are **schools**, spell categories are **disciplines**; Book IV's "Domain" headings stay as legacy labels pending the deferred reconciliation. Full ruled structure: **color → school → discipline → spell**. Still open from that fork: one-vs-many discipline membership (Elideus's phrasing leans singular).

**Round 7 (2026-07-02): Domains, Principalities, and the skill flag** (`232B6EEE`). Refinement: **Domains ≠ Disciplines** — "Domain" properly names the fourteen school-aspects (each of the 14 schools aligned with a Domain); disciplines are the spell types, and **each discipline is a skill in the skill system**. Full structure: **color → Domain → aligned school → discipline (a skill) → spell**. Major mythology canon: **the Principalities** — the superhuman tier is ownership, not permission; White's magic belongs to the **Principality of White** ("the source, the one, the pure, the origin of eternity"), and the four Black/Orange schools belong to the **First Titan — confirmed as the Two-Faced God** (closing that constellation fork). New sharper question: the mortal colors' principalities (is the Divine Vine Green's?). And per Elideus's explicit instruction, **the skill system (3–4 layered skill scopes, cross-scope learning) is flagged as a MAJOR open issue for Sonnet collaboration** (`F618F695`).

**Round 8 (2026-07-02): rings and reagents — and, in a separate planning thread the same day, the bestiary** (`B92EE74A`). **Queue item 2 RESOLVED in favor of Option (b)**: rings are a magic-mastery structure internal to Book IV, not a Book I character-progression tier. A ring is a per-school milestone in the Words of Power research track; ranking up grants vocabulary breadth, spell-string complexity headroom, and reagent grade — shape access at the 4th/7th ring (unchanged, confirmed as correct original intent) is one instance of this, not the whole of it. New canon: **reagents come in three kinds** — consumable (burned per cast), charge-limited talismans, and permanent foci (equipped, never depletes) — and higher ring is intended to let a mage satisfy a spell with a cheaper-grade reagent. Book IV gained a **Reagent Grades** subsection; Book I's ring stub trimmed to a cross-reference; Book II's shape-proc open question citation updated. Still open: exact ring count/table, the reagent-grade curve, Black's "other means" ring mechanic, ring inheritance (`D2C52C88`), and the synergy-cycle-vs-genealogy conflict (`244A27FF`) — none of those were adjudicated here.

The same day, a separate planning session built **Book VII: Bestiary** from scratch (`CBCADC66`, resolving the document-placement half of `B4F9A3AC`). Elideus rejected a first-pass draft as "too tame... too World of Warcraft," setting a standing **tonal ruling** (`C3D46D10`): the bestiary is gothic horror, Dark Souls–style, across every category without exception. Structural canon that followed: the bestiary's **fifteen categories** are the fourteen Domains plus a new 15th, **Inverted** (`C3D46D10`, `B9276D17`) — Psionics' own Principality, standing entirely outside the color system, register explicitly Lovecraftian (screen-scrambling perception effects, forced-panic fear, screeching). The four mortal colors' Principality-holders were ruled **human**, gifted the magics by the ancient immortals near the end of the Age of Immortals (`24054B89` — later folded into round 9's pantheon work below). **Black/Void was given a governing definition** (`D0BE40E5`): "the absence of" — it cannot invent or create, only reflect/reanimate what already lived, with a canon lich definition ("a skeleton of, reanimated from, but not living"). A **hidden Titan behind the Two-Faced God** was flagged (`57960182`, illuminated but not resolved by round 9's `BC54B7D7` below). The session's biggest structural move was the **archetype matrix** (`BEE2FC2D`): creature archetypes (goblins, wisps, hounds, corvids, serpents, and more, drawn deliberately from Middle Eastern, Far Eastern/Japanese, South American, Pacific Islander, and Sanskrit-rooted mythology, not just Western default) recur across multiple Domain categories in different dress; Death is near-universal (almost anything can have a reanimated variant); decay and poison are cross-cutting modifiers, not their own category. A seed roster was written up as [PROPOSED] and explicitly flagged by Elideus as "probably a bit too ambitious... but that's a scope question for much later" — the tone and structure are ratified, the specific roster is not. One boss idea (a Vetala riding a Dracolich, `563804ED`) came out of the session and doubles as a candidate answer to queue item 8 (boss composition), not a resolution of it.

**Round 9 (2026-07-02): the Pantheon, the constellations, and the alignment system.** Elideus closed the cosmology's last piece and built the pantheon and the sky end to end.

- **The Pantheon = the Titans** (`2FCEB0B3`, closing `69E6E8E7` → Option C). Five Titans count: the **Two-Faced God** (First Titan, Orange+Black) and four elementals, each naming a Mortal Realm, its planet, and its Titan at once — **Terria/the Vine** (Green), **Aerolon/the Bird** (Yellow), **Sanguia/the Mountain** (Red), **Aquia/the Serpent** (Blue). Titans are non-humanoid cosmic forms. **White** stands apart — "other, formless, eternity," the Principality of White, with no form and no constellation. **The Divine Vine = the god of the vine = Terria** (closes the Green fork of `66541B83`). The realm↔body↔Titan identity closes **`7BC8E9B6`**. The four mortal-color Principality-*holders* remain **human** (`24054B89` preserved); the mortal magics descend Titan (source) → **ancient immortals** (original patrons, names lost to the centuries) → human holders (`12411325`).
- **The constellations** (`25699317`, amending `AF819A62`). Eight of thirteen now named: the **Chalice** (Muse, galactic heart), the **Faces** (Two-Faced God, "> <"), the **Vine** (Terria), the **Anvil** (Sanguia — the Mountain's forge), the **Spiral** (Aquia, the coiled Serpent), the **Bird** (Aerolon), **Beltan the Bear**, and the **Scar** (the Touching of God, drawn as a wound). **The Night of the Daggers is retired** as derivative; **White casts no constellation.** Five slots open.
- **The alignment-event system** (`25699317`): the constellation field rotates while the seven planets each move at their own rate; planet↔constellation alignments are bonus events, they stack, counter-alignments are their own class, and self-alignment (a planet over its own constellation) is peak resonance. The Chalice/moon–Death reveal is the marquee instance. Mechanism is canon; the specific effect of any given alignment is downstream design (celestial primacy `3312B2AB`).
- **First Titan pronouns — RULED intentional** (`5E2FB886`, closing `5E9DB061`): the expression of chaos, rotating they/him/her/them/us/hers/his/she/we; the myth prose is preserved, future First-Titan text follows the rotation.
- **The metaphysics of the three magics** (`BC54B7D7`): holy magic is divine invocation, elemental magic is element-channelling. **White** channels *eternity* (divination + divine invocation, "words of divine power") — direct and uncreated. **Black/Orange** are the First Titan's own two faces (Black = *not-life*; **Orange/Chaos = the magic side of psionics and the Titan's hidden other face**). Only the **elemental colors** were *created for mortals and taught*, which is why they alone carry the intermediary chain; the "ancient immortals" are long-lived *mortals*, and Titans, as concepts, are neither mortal nor immortal. Illuminates item 16 / `7609E7E9` (psionics seat) and `57960182` (hidden Titan) without resolving them.

**Queue effect:** items 1 (final piece), 13, and 18 close. Item 20's constellation want is now 8/13 named. New authoring/recovery need logged: the **"story of the mountain and the plow"** (Sanguia↔Terria — earth, life, growth, blood). New small opens: the five remaining constellation slots; the four human mortal-Principality-holders' identities (`24054B89`); the specific bonus each named alignment confers; whether Chaos-as-psionics'-magic-side subsumes the hidden-Titan flag (`57960182`) or is distinct.

---

**Round 10 (2026-07-02): the combat system opens.** Elideus set the authoring format and the design identity, then worked the combat frame; Book I gains ruled stat lanes, a resource model, and two new sections.

- **The two games** (`02D30987`): Prism builds both tabletop roles into one MMO — the **Game Master's game** (build challenges, Book II) and the **Player's game** (EQ/WoW adventuring, Book I). Everyone can do both; **only adventurers earn XP**; design outputs are shaped like a **GM guide** (tables of stats, weapons, costs, advancement).
- **Death — RESOLVED** (`0B98560B`, closing `D25A57E1`): combat death is **respawn + EQ corpse recovery**; terminal exits are a category of *additive* dispositions (settlement-NPC grows your city, heroic status, old-age patron, the Muse's path); only **Burning** subtracts (permanent delete *or* a sacrifice play), at extreme cost; the roster is limited only by time.
- **The seven stats' combat lanes — RULED** (`DE7E8605`): Con→survivability/Health, End→action-economy/Stamina, Str→force, Dex→speed/precision, Int→technique **+ the research gate**, Wis→foresight/parry/divine, Luck→fortune/crit/loot — closing the five-stat combat stub and three open questions (Int gates research = yes; Luck owns loot/discovery = yes; **Wisdom does *not* read the sky** — that's the player's own realm).
- **Resources** (`BFBE6085`): OneBar discarded; three bars (Health/Stamina/Mana) scaled to 100, no markers, shown as normalized 0.0–1.0 with **no absolute numbers**; the **Journal / adventure-summary system** replaces XP popups with a home-written narrative diary; the wider **philosophy of ambiguity** is a major open decision.
- **Weapons & build** (`DE7E8605`): scaling flows from an **abstract material affinity, not literal color** (blades stay realistic gothic metal; glow comes from enchants); **no classes** — open Souls-like build where the Roles are investable **talent graphs** (early-WoW-light, hybrids, maybe the septisigil wheel), and **every investment is permanent (no respec)**; **item creation is Dungeon-Maker-side**, adventurers enhance.

- **Group & raid combat, the contested world, the Advent-raid horizon** (`A573A152`, `6BEB00D3`, `021891E4`, `639B9FD9`): group combat is Souls action at EverQuest scale, made possible by the event system (targeted/cluster attacks; per-player parry/dodge windows); a **threat table** any build can climb, with **conditional parry-tanking** (roles are jobs, not classes — a cloth dagger-master can tank); combat-res limited; **non-instanced real-time world spawns** (cleared ground holds ~weekly, beachheads legit). The world is **contested** — loot-stealing and claim-jumping allowed; antisocial play makes you a **pariah** (teeth via hostile settlements, `E4F46BA5`). The **Advent raids** (pentagon zones) are **horizon content (v1.1–1.5)**, quest-gated, Elideus/community-built, seeded by tier-10 dungeon gateways; **boss authoring lives in the complex DM tech tree** (`639B9FD9`) — the deep counterpart to the simple adventurer graphs. Book I gains *Group Combat and the Threat Model*, *The Contested World*, and *The Advent Raids* sections; the immortals'-return "Second Age" is scoped as future expansion (`7D0C59F3`, closing `BB152B09`).

**Queue effect:** items 3 and 4 close; combat is now framed in Book I with derived-value formulas, status tables, and the talent graphs flagged `[BUILD]`. The **layered skill-scope system stays reserved** (`F618F695`).

**Round 11 (2026-07-03): the excavation adjudication.** Five recovered ChatGPT-era sources were captured to `sources/` (origin myth, Blue Realm/Caeloreth, party-scale combat, world-modes/Realmwright, world-sim/quench — intake notes `52C549CC`, `59DF9DD6`, `D834A6A3`, `A40C5CC7` + six myth decisions), then adjudicated:

- **The prison frame is canon** (`69412269`): the Shattering built a prison; the Titans locked the rebellious scholars in — **the Muse was one of them** (`41729188`); the Titans guard the **gateways**, and the **Advent locations are the guarded gates**. Books V/VI updated. **Narrowed, round 14** (see below): the prison mythology stands; only the "PRISM pun carries both meanings *by intent*" claim — that the name was deliberately chosen to pun on "prison" — does not.
- **Era-specific philosophies** (`CDE8479D`): an era of conflated, hidden philosophies precedes the Golden Age — Caeloreth (Blue's High Seer, castle-root name `F7EFAD30`) sold curated Truth as Knowledge; **the Muse's de-conflation is the transition** to today's public, unjudged pairs. Blue-realm beats canon (Caeloreth, Belmar, the Mirror Lake; prose held as draft); her Lake visions feed the open constellation slots. Answers the old "Knowledge vs Truth — two goods?" question and places the Muse in the Blue school.
- **Architecture** (`DC66A0FB`): the excavated single-shard directive is **overridden** — one universe instance, **seven literal playable worlds, "the seven prisms"**; Death Gate Cycle noted as loose inspiration. "Shard" in books = world-shard only. **Realmwright stays dead**; Clay Engine/GM-mode/epoch-7 and its isolation principle stand (`59DF9DD6`).
- **Quench speed promoted to canon** (`41EB4B47`): a conserved, first-class hex state field (hardness = *if*, quench = *how*, stress = *when* a hex fails); coastline morphology and biogenic epochs ride with it; Book III integration pending a world-sim pass.
- **Party scales canon, fixed tuning** (`CA50B875`): dungeons **5–7**, mid raids **10–15**, large **25–35**, mega **72→100**; no dynamic scaling. EQ's player-x²/monster-x³ asymmetry, the **puller** role, and the **party logbook** ride as [PROPOSED] (`A40C5CC7`). **Top-tier DMs can unlock raid-zone construction** (deep tech tree + high rating; refines `639B9FD9`) — the community path to Advent-tier content.
- **Deferred to sessions** (`1E5C0E3C`): the **color counter-web** design (old permadeath model confirmed dead); the **item-creation + enchantment system** (DM-side) — with the explicit constraint that items, combat, and stats interdepend and must land together with the derived-value formulas pass.
- **The Advent gate chain** (`8E571A6E`, closing the CA50B875 boundary question): **top-tier DM dungeons must be defeated to unlock the Advents** — an advanced Maker earns the capability to place an Advent gateway at the end of a dungeon; clear the dungeon, the gate opens. The Advent zones themselves are future design: **carefully curated puzzle zones, essentially the game's only designed fixed content**, community-built or Elideus's "personal imaginarium of advent insanity projects."

---

**Round 12 (2026-07-03): bestiary depth — factions, the psionics spectrum, and the biome table.** A follow-on planning pass deepened Book VII and touched Book VI, largely superseding its own earlier steps same-day; final state only is now in the books.

- **New present-age factions and two deep-past epochs, placed on Home** (`D593CB3C`, note, [PROPOSED]). Four factions recovered from outside inspiration — **Crescent Empire** (Middle Eastern/Ottoman/Mughal, ley-line mage-aristocracy), **Silver Sultanate** (Persian/Central Asian, magic+alchemy+enchanted-technology trade kingdom), **Jade Dominion** (Indian/SE Asian/Far Eastern syncretic magical-scholarship coalition), **Iron Republic** (early-20th-century-European-coded industrializing power) — plus two archaeological-history layers: a **Hunter-Gatherer Epoch** (~20,000–15,000 years before present, animist/shamanist, leaves megalithic standing-stones aligned to celestial bodies) and an **Ancient Civilization Era** (~10,000–6,000 years before present, magic-technology fusion, ends in an unexplained collapse, leaves ruin-fields). An original nine-continent-globe framing was self-flagged by Elideus as conflicting with locked cosmology (`DC66A0FB`) and dropped; everything sits on **Home**, the third orbital body, distinct from the seven Domain worlds. Sits alongside Book VI's existing Human-Era Stratum stub as a sibling faction set, not yet reconciled to the same timeline — an open question in the same shape as the Dragan/Bloodfangs cross-era fork (`66541B83`).
- **Psionics unified into one discipline, not two systems** (`CC7C057B`, decision). Magic (word-grammar), Cantrips, and Psionics are three parallel paths to the same power. Psionics itself is **one** discipline, not split mundane-vs-cosmic-horror: Book IV's existing 16-ability roster (Telepathy, Telekinesis, Pyro/Cryokinesis, Hydrokinesis, Eidetic Projection, Geokinesis, Aerokinesis, Chronokinesis, Bio/Hemokinesis, Photo/Umbrakinesis, Technopathy, Metakinesis, Morphokinesis, Necropathy) and Inverted's Lovecraftian bestiary entries are the ordinary and extreme ends of the same spectrum, not two things to reconcile. Feeds queue item 16.
- **Biome seeding table drafted, then corrected twice, same day.** First pass (`14DFFA2E`, note, [PROPOSED]): nine *named* biomes (Sundered Desert, Ashlands, the Underland, Foxfire Wood, the Drowned Moor, Monsoon Delta, the Reefless Coast, High Steppe, the Smoke-Wastes) each anchored to a Continental Powers/Human-Era-Stratum faction, plus two new archetype families to carry the deep-past flavor: **Golems/Constructs** (Ancient Civilization; unaffected by the Black/Void constraint since nothing died to make them) and **Megalith Guardians/the Standing Ones** (Hunter-Gatherer; wake on celestial triggers, `3312B2AB`, not on sight or sound). **Corrected same day** (`45DC8EA4`, decision): the named-zone framing was wrong — Home is procedurally generated (hex-sphere heightmap, quench-speed hardness/quench/stress field `41EB4B47`, crust recycling, coastline morphology, biogenic epochs — Book III), so a biome must be a **recurring conceptual-dominance category**, not a fixed named place with a faction owner. Book VII's table was rewritten to nine generic categories — Desert, Volcanic, Mountain/Highland, Underland (shared subsurface layer, not its own surface biome), Temperate Forest, Tropical/Jungle, Wetland, Coastal/Ocean, Tundra/Polar — carrying the same Domain-mix/creature-bench content, minus all faction-anchor language; Grassland was cut as redundant default fill, "industrial blight" was cut as a faction effect (Iron Republic) rather than a terrain type. **Ruins/starter-town model also corrected** (`35D58182`, then narrowed further by `D932B78D`): the world has **no fixed authored elements** at all — what looks like a ruin anywhere is ordinary erosion-system output (`95EAF28D`); Ancient Civilization/Hunter-Gatherer *flavor* specifically (Wardens, Broken Wardens, Cinder-Forms, the Standing Ones) rides in only via builder-deployed **Story Content Packs**, never as baked-in world-gen dressing. The only fixed place at all is a production-practical one: Elideus's own player-built settlement (built with ordinary Dungeon Maker tools, no special lore status), kept fully serviced so early players have somewhere to go — explicitly *not* the same thing as the still-unwritten three-starting-NPCs ruling (`EC054473`) unless Elideus later confirms they're identical.

**Queue effect:** item 16 gains the `CC7C057B` clarification (above). New open items, not yet numbered into the formal queue: whether the new faction set and Book VI's existing Human-Era Stratum are the same era/region; whether the central player-built town is the same thing as `EC054473`'s three starting NPCs; DM tier gating and exclusive-vs-graded recruitment per biome (`B4F9A3AC`, unchanged); whether the nine Home biomes relate at all to the seven Domain worlds' own endgame bestiary (flagged, unaddressed). None of this round's biome/faction/ruin content is ratified as hard canon — all written up as [PROPOSED] pending Elideus's confirmation.

---

**Round 13 (2026-07-04): working the contradiction ledger.** Elideus went through the standing queue's cheap items in order and ruled four of them; the fifth is a full retraction, not a resolution.

- **Dungeon Maker wins** (`C6E42EE8`, closing queue item 6 / `500F8438`): "Dungeon Master" is dropped platform-wide — "that is likely copyrighted by TSR/WotC." Books II and IV corrected; Book II's glossary note now reads resolved instead of pending.
- **Black combines with nothing — ratified** (`5936222F`, closing queue item 11 / `313123F1`, Option b): the fact is now a dated entry in Book V's own Canon Rulings ledger rather than a thread-only decision, so Book IV's existing citations resolve to something real. Cross-referenced against this session's own Black/Void "absence of" ruling (`D0BE40E5`, Book VII), which supplies the mythological reason.
- **"Mortal," not "moral"** (`2EE825B7`, closing queue item 12 / `89D9BC90`): a voice-transcription artifact, not deliberate wordplay. Books V and VI corrected; the editorial flag removed.
- **Valance removal** — still deferred; no action taken, no change to Book III or `periodic_table.json`.
- **RETRACTION, then corrected same day** (`AB7749F0`, corrected by `B3DE987E`). First pass overruled round 11's prison mythology (`69412269`, `41729188`, `FF4D0EF0`) in full — wrong scope. Elideus's actual point: "I didn't say get rid of all of the prison stuff, I said the PUN association between prison and prism is not cannon." **Final state:** the Shattering-built-a-prison mythology stands, unretracted — the Titans as wardens, the rebellious scholars (the Muse among them) locked into magicked shards, all canon per round 11. Only the claim that "Prism" was *deliberately named* to pun on "prison" is struck; that resemblance is acknowledged wordplay, not intentional design. Books V and VI reverted to the round-11 text with only that narrow correction applied. **Craft lesson:** confirm the scope of a correction before rewriting — a narrow note ("the pun isn't canon") is not the same as "retract the whole mythology."

**Queue effect:** items 6, 11, and 12 close. No new forks opened by this round — it's pure cleanup, one full retraction included.

---

**Round 15 (2026-07-04): the Book IV dictionary collisions.** Elideus pulled the vocabulary and creature-noun collisions out of their "deferred to engine effect-building" limbo and ruled them directly (`AA124D5D`, closing `44F17D1E`, `94774F28`, `8E29A0D3`), with a standing principle for future word disputes: words should read as Latin-esque words of power, and where two collide, keep the more grammatically correct one rather than picking arbitrarily.

- **Nouns:** Grav re-glossed Energy → **Gravity**; Vis narrowed to exclude gravity specifically. Terra narrowed to soil/ground, dropping "stone" to Saxum. Ferrum's gloss broadened Iron → **Metal**.
- **Adjectives:** Umbra keeps the noun slot; the adjective "Dark" becomes **Ater**. Altior and Humilis removed as redundant comparative duplicates of Altus/Infimus — degree now stacks via Vas/Bet instead.
- **Adverbs:** "Durare" (actually a verb infinitive) replaced by **Diu** (true duration adverb); "Breve" replaced by **Breviter**, matching the dictionary's own -iter pattern (Fortiter, Debiliter); "Brevis" removed as redundant. "Longe" re-glossed to its correct classical meaning, **Distant**, absorbing "Longius" — this was the root of the whole Durare/Longe/Longius tangle: "longe" was mislabeled as a duration word when it's actually the standard distance adverb.
- **Creatures:** liches settle under Mortivus only (undead, not merely cursed); Maleforix swaps in "gorgons." Phoenixes settle under Pyrravus only; Mystivora swaps in "pegasi." Aetheron narrowed to **Heavenly Hierarchies** — infernal beings are Inferaxis's alone.

Book II's two citations of these collisions (adjective-quality, noun-residency) updated to reflect the resolution.

**Queue effect:** the dictionary/creature-noun half of the contradiction ledger closes entirely. No new forks opened.

---

**Round 16 (2026-07-04): the bestiary converges — seven colors, a creature template, and White's roster.** Elideus scoped the bestiary down hard: the earlier global-mythology archetype pass and 15-category/9-biome sprawl give way to **seven color-based sets, ~20 creatures each, ~140 total**, explicitly traditional Forgotten Realms-coded — undead, liches, dragons, headless, goblins, kobolds, hobgoblins, ogres, giants, cyclopes, Diablo/Ultima-tier classics — gothic-horror-coded but not overt. A curated handful of the earlier global-mythology survivors converge into whichever color fits (Ifrit→Red, Naga/Encantado→Blue, Rakshasa→Orange, Vetala/Jiangshi/Pisacha→Black, Thunderbird→Yellow); the rest are cut. One dragon per color anchors each set's apex terror. Critters/animals are a smaller, shared pool rather than 20 unique-per-color. Inverted stays separate, outside the 140.

**Creature entry template and power tiers ruled** (`24DD9710`): every entry gets Name / Type / Color / Description / Behaviors / Threats & Defenses (using Book IV's existing status-effect taxonomy) / Statistics (the same seven player stat lanes, Normal-tier baseline, Health/Stamina/Mana left `[BUILD]`). Four power bands — Weak (~60%), Normal, Strong (~175%), Boss (multiples of Normal, always ≥1 signature mechanic) — gated by *existing* systems, not a new one: Weak/Normal default-available, Strong gated by Book II's Monster Mastery tech tree, Boss gated by the same top-tier/deep-tech-tree wall as raid-zone/Advent construction (`639B9FD9`, `CA50B875`, `8E571A6E`).

**White (Light/Prophecy)'s full 20-entry roster written** — White Hart, Doves of Dawn, Augur-Cat, Radiant Moth-Swarm, Sunhawk, Pegasus, Unicorn, Sphinx, Lightbound Hound, Dawnwisp, Radiant Sentinel, Scorched Faithful, Unmade Seer, Choir of the Hollow Bell, Herald of Judgment, The Blinding, Sentinel of the Sun (Boss), The Weeping Oracle (Boss), White Dragon (Boss/apex), The First Witness (Boss/unique). Book VII's existing 9-biome Bench table is flagged **pending revision** — it still fills its benches from the cut mythology pass and needs a rewrite once all seven color rosters exist.

**Queue effect:** no formal queue items close (this was bestiary content, not ledger contradictions), but it sets the template the remaining six color rosters (Yellow, Red, Orange, Blue, Green, Black) will follow.

---

**Round 17 (2026-07-04): White's roster corrected; Book VII cleaned up.** Elideus rejected the first White roster as "too ham, too campy... angelic tier stuff... critters and animals is way too extra" (`E8323659`). Replaced with 18 plainer entries: 7 ordinary-wildlife critters (Mountain Goat, Snow Hare, Highland Eagle, Pale Wolf, White Owl, Snow Leopard, Mountain Ram), 8 classic monsters (Pegasus, Unicorn, Sphinx, Couatl, Will-o-Wisp, Radiant Guardian, Cursed Oracle, Hollow Zealot), 3 boss/terror (Temple Sentinel, Mad Prophet, White Dragon) — locked in.

**Standing cleanup instruction:** once a section's actual content demonstrates the pattern, drop the decision/guidance detail from the book itself (it stays here and in Oracle memory) and keep only generic theme/intent prose. Applied this pass: the "Fifteen Categories" section trimmed to a short Color Ownership table; the global-mythology Archetype Matrix list cut to three generic Cross-Cutting Rules plus the still-load-bearing Golems/Megalith Guardians mechanic; the Biome Seeding Table's multi-correction history collapsed to a short stub. Apply the same trim to each remaining color as it's written.

**Queue effect:** none (bestiary content, not ledger contradictions). Sets the cleaned-up baseline the remaining six color rosters (Yellow, Red, Orange, Blue, Green, Black) build from.

---

**Round 18 (2026-07-04): the creature template gets real depth.** Elideus corrected a scope miss directly in Book VII (editing the Mountain Goat entry as the reference example): round 17's cleanup instruction applied to the surrounding process/decision text only, not the creature entries — those had wrongly been compressed to single-sentence fields (`5F5BF70D`).

**Template expansion, applies to every future entry:** Statistics is now a table — Base/Weak(×0.6)/Strong(×1.75)/Boss(×4, a floor). Two new sections: **Attack Patterns** (named Souls-like moves, base + signature, stationary-vs-motion variants) and **Materials** (harvestable drops). **Weapons/Armor** tables are conditional, only where a creature would plausibly carry them. All 18 White entries rewritten to this shape; named Boss-tier creatures (Temple Sentinel, Mad Prophet) are now explicitly their base creature's own Boss row rather than a separately hand-tuned line. White Dragon uses age tiers (Young/Adult/Elder/Ancient) mapped onto Weak/Normal/Strong/Boss — a pattern worth reusing for other colors' dragons.

**Queue effect:** none (bestiary content). Sets the final template shape the remaining six color rosters follow.

---

**Round 19 (2026-07-04): Orange (Chaos/Transformation) roster.** The second color set, 20 entries in the full expanded template (`C9C4CD10`). Theme: aberration, mutation, body horror — the First Titan's Laboratory — on a broken badlands biome. Animals stay mundane biome fauna per the White precedent (Elideus again rejected a campy mutated-animals first draft): Vulture, Jackal, Hyena, Monitor Lizard, Desert Scorpion, Carrion Beetle Swarm, Jerboa. Monsters: Gray Ooze, Mimic, Owlbear, Chimera, Basilisk, Gibbering Mouther, Rakshasa (the global-mythology survivor that converged here; carries the Weapons/Armor tables), Otyugh, Flesh-Stitched Abomination. Terrors: Beholder (signature — eye-barrage stacking Root/Slow/Sunder/Fear/Confound plus a central-eye Silence field), Hydra (severed-head regrowth), The Fleshwright (named boss, maker of the abominations), Orange Dragon (apex, age tiers). Five colors left: Yellow, Red, Blue, Green, Black.

**Queue effect:** none (bestiary content).

**Round 20 (2026-07-04): Yellow (Air/Lightning) roster.** Third color set, 19 entries in the full template (`8B5930F9`). Theme: storm and sky, on a windswept storm-steppe biome. Animals: Falcon, Wild Horse, Pronghorn, Crane, Grouse, Marmot, Cheetah. Monsters: Harpy, Griffin, Hippogriff, Wyvern, Cockatrice (petrifying peck via Root→Stun, distinct from Orange's gaze-based Basilisk), Storm Elemental, Cloud Giant (Weapons/Armor), Skyborn Marauder (armed winged humanoids, Weapons/Armor). Terrors: Roc, Storm Giant, Thunderbird (the global-mythology survivor converging here), Yellow Dragon (apex, age tiers, chain lightning). Elideus flagged a developing biome-coverage gap across the sets but chose to fill it later with additional sets. Remaining: Red, Blue, Green, Black.

---

*Ledger conventions, all entry GUIDs, and full finding bodies live in the Oracle thread `prism-bible-recompile`. Books remain internally honest: every unsourced claim is marked, every fork is cited, nothing was invented.*
