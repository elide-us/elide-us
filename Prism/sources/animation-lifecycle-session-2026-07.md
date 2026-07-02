# Source: Animation System → Character Lifecycle → Celestial Rebuild (early July 2026)

> **Provenance:** A recent wide-ranging conversation between Elideus and Claude (the thread's
> nominal topic was building a "granny-tier animation system" for the engine; it leeched into
> character lifecycle and the celestial sim). The majority was pasted into the recompile session
> by Elideus on 2026-07-02, together with a framing note (below). Transcribed with speaker labels.
> **Status:** SOURCE MATERIAL. Elideus's turns are canon-grade; the assistant's proposals are
> **[PROPOSED] at best** — Elideus's explicit verdict on the lifecycle sketch was "That wasn't
> quite what I had in mind, but pretty close," followed by his own statement, which is the canon.
> Rulings extracted to ledger entries recorded 2026-07-02 (see RECOMPILE_REPORT addendum round 5).
> **Framing note from Elideus at paste time (canon-grade):** "there is a need to build out a
> bestiary. There are some specific biome types that we're going to seed with certain kinds of
> creatures, on the larger DM vs Adventurer scale, certain monsters can only be recruited in
> certain areas, picking where to place your dungeon matters."

---

**Elideus:** We spent a good amount of time working on defining the world shape and other kinds of things, um, in order to actually have a game engine. Obviously, we need, you know, more than just something that draws triangles on the screen. I also need an animation system. Now I had purchased a model from the marketplace in Unreal Engine for an older version of the game, and, uh, it comes with a model that has some, I would describe, inappropriate animations. Um, but what I'm thinking is that there's probably a way that we can convert the model that is in the project into something, um, you know, that that I can do something with from an animation perspective. I don't know how those things are packaged, like, from a binary perspective or if they come with... yeah. I don't know how animation hooks work and things like that. But, basically, we need to at least duplicate something of the class of, like, granny for animation. I know that... I had actually planned on buying granny, but Microsoft bought granny and then just kinda made it disappear. So I don't know exactly what they did with it. But either way, we need to create a granny tier animation system for our engine.

**Claude:** [The conversation developed the animation architecture and, via the question of how characters live and die, the lineage system. The assistant's synthesis — quoted below because Elideus's correction responds to it:]

Before we play with it — say what just happened, because it's the capstone of this whole conversation. The protagonist was never a character. It's the lineage. Individual characters are generations of one long protagonist that does have interiority, pacing, and an arc — the authored personal story a soulslike wants — except it's told entirely through systemic play and never scripted once. [...] The tapestry is the narrative. No two are alike, and nobody had to write them.

The engine that makes the lifecycle generative instead of a menu: a character's history is the spec for their afterlife. The warrior retires into a dark-steel blacksmith because the role is computed from what they actually did — the sword they carried, the aspect they ran, the eclipse drop they were holding — not picked from a list. You can't farm a retirement build. You have to live it. Every retired NPC is unique because every life was.

Staged, roughly:

- Living — your active main.
- Retired — leaves play, joins the settlement; role and bonus derived from the life. This is where a whole character cashes out into permanent infrastructure.
- Dead — tombstone. Passive memorial, maybe a quiet standing bonus. The thread at rest.
- Ghost — the earned tier. A "stick around" quest converts a dead thread back into an active one. Permanence you pass a test for.
- Burned — the sacrifice. Spend a thread forever to fire a long-term effect. The destructive lever.

Five states, and every transition is earned or paid for. Nothing good is free — which has been the spine of this entire world.

Race is the part I want to push on, because it's secretly a tempo-and-variance dial, not a stat block. Lifespan trades against offspring slots, and the same total throughput feels completely different:

- Long-lived — few, deep, slow. Each character is a major investment; losing one to retirement hurts; the dynasty advances in big careful steps. Low variance, high commitment.
- Human — many, fast, wide. Churn and resilience-through-numbers, more rolls at the dynasty project, cheaper mistakes.
- Lizard / brood — burst clutches, the gambler's race. Some broods are duds, some are gold. Lottery dynamics.

So race isn't power — it's how your family experiences time. [...]

The Targaryen thing — the ten-generation build — is a tech tree at the dynasty scale [...]: each generation that commits to dragons installs another node; ten of them unlock an entitlement — ride dragons — that belongs to the bloodline, not any character who could ever earn it alone. Which opens the real strategic axis [...]: depth versus breadth. Specialize into an apex dynasty, narrow and terrifying. Or run a broad house — a smith, a mage, a rider, no apex but no gaps. Burning a thread is how you prune a diversified house back toward a thesis. [...]

The starting tapestry is a tutorial you don't notice. The ghost, the patron, the rich uncle — they aren't just a head start, they're worked examples of a system you haven't been shown. [...]

And the question I'd most want settled: what's the unit of inheritance? When a child is born into the tapestry, what carries — one parent, the whole accumulated dynasty, or a chosen mentor-thread? One-parent makes lineages branch and diverge [...]. Whole-tapestry makes every newborn heir to everything [...]. Chosen-mentor lets the player direct propagation [...]. Three different games. [...] Is the unit of inheritance one-parent, whole-tapestry, or chosen-mentor — and is retirement forced by the lifespan clock or chosen as a disposition?

**Elideus:** That wasn't quite what I had in mind, but pretty close.

Child - something you have to invest in, if you choose to have an offspring it requires maintenance, this is required to roll a new character eventually, you don't have to do it when they are of age, but you do need to build the child to adventurer's age and that requires ongoing payment of in game currency, nothing is pay to play ever, old school RPG for life. This is also how you make long term enchanted items, you have to invest mana in them regularly at the enchanting table, you can't fake anything, and I won't hear anyone's complaints about casual schedules or anything else, the game rules are the rules, live with it.

Adventurer - The character you play, no take backsies. Skill them up, do what you like, live, explore, learn, acquire, eventually, you'll reach level 10 and you'll have a yearning to retire, you'll recognize your strengths and you'll chose your benefits for the family. Permanent effects, you could sacrifice yourself heorically in an epic battle and become a permanent badge of glory for your account, any number of effects can be built off this system for any number of reasons.

The skill system we built is deep and complex and completely opaque to the player except through brutal trial and error that I know a few absolute psychos out there will work out becaues people always do, but the system will be honest, it will be, as you said, dterminitistic predictable and fair. I want you to play the game and enjoy the persistence, build and grow and adventure, find the world. find a rare spot, build a castle, make the world your own. Paint a picture, tell your own story.

**Claude:** [Reflected the philosophy back: everything costs its real cost, paid over real time, the rules never bend; determinism is the fairness; opacity plus determinism protects the existence of discovery; the persistent world as canvas. Suggested the character lifecycle spec as the first artifact.]

**Elideus:** Think I already wrote all that, was just filling you in and fleshing out the ideas one more time, probably the third time I've voiced it, and that's the point, the vision becomes clearer each time I repeat it. This thread, btw, was about how to build a granny-tier animation system for our game. Leeched into a discussion on how characters live because it is, in some interesting ways, related to how characters live and die.

**Claude:** [Noted the animation/lineage rhyme — durable rig vs disposable surface — and the three-iteration rule. Named the animation architecture as settled: TAE-style event timeline as authority, logical pose on CPU for hitboxes, bake-once volumetric bind, palette skinning on the immutable buffer, glTF in.]

**Elideus:** Funny story about the cosmology, I've basically decided to throw away almost all of sol2 and just go back to the disk simulation and work from there again because I think I've finally figured out how to do this HAHAHAHA

**Claude:** [Endorsed the disk-first direction: simulate the field, let the planets condense out.]

**Elideus:** Sol2 did everything right, and it's just too much, the flicker-world system for building planets is actually all we need for the initial sim there and just expanding how it starts is all we need to do. As for the system, it always going to be the same system since that's actually a specific calendar for the game events, and the simulation we built back in voxel-cluster is still the best iteration of that we've done, so again, a lot of interesting work proving a lot of the systems roots and improving major parts of the generation. We now have Mg in our periodic table, didn't even have that before, for example. Huge. So, anyway. No need to detail it, but yes, the celestial sim will be rebuilt one last time ;)

**Claude:** [Closed the thread: subtraction that increases fidelity; the celestial system's calendar role; the rebuild reuses machinery already proven — flicker-world with a wider intake, the voxel-cluster sim as the best evolution pass.]
