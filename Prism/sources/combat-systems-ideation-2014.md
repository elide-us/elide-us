# Source: Combat Systems — Design Notes (2014)

> **Provenance:** Personal design notes dated **Friday, June 27, 2014, 2:32 AM** (OneNote),
> pasted into the recompile session by Elideus on 2026-07-02.
> **Status: IDEATION ONLY** — over twelve years old; treat it as such. Some of this does not
> align with current designs. Where this document conflicts with Canon Rulings (Book V), the
> seed canon, or ledger `decision` entries, the rulings win.
> **The durable payload** (Elideus, 2026-07-02): the combat mechanics and effects — particularly
> how effects like stun, silence, fear, and snare are *direct game mechanics* — and the
> time/distance/movement constraints. Intake ruling: ledger 78C70439.
>
> **Known misalignments, flagged not corrected:**
> - Five-school magic list (protection/life/death/cold/fire, MTG-styled) vs the seven schools of
>   Prism (Book V). Six caster archetypes treat **Life and Earth as separate schools**
>   (Priest–Life, Shaman–Earth) — today they are merged in Green (Seed canon 2, Life is Green).
> - MOBA-era vocabulary (Champions, Minions, Avatars, pre-defined kits) predates the
>   research-and-memorize magic grammar (Seed canon 9) and the Souls-style combat canon
>   (Seed canon 5, ledger 9D249EE4).
> - The 10-cantrip list overlaps but does not match Book IV's cantrips.
> - "Three ranked spheres of power in each school" is a possible ancestor of the undefined
>   **ring** progression (fork 63B28A6B; observation ledgered in 2A2A5A97).
>
> Transcribed with wording verbatim (including artifacts); tables reformatted to markdown.

---

## Combat Systems

Friday, June 27, 2014
2:32 AM

| Archetype | Movement | Damage | Durability |
|---|---|---|---|
| Brawler | Low | High | Medium |
| Tank | Low | Medium | High |
| Hoplite | Medium | Low | High |
| Archer | Medium | High | Low |
| Cavalry | High | Low | Medium |
| Assassin | High | Medium | Low |

Defining various objects:
Avatars - Champions, have abilities, player controlled
Minions - Basic creatures, have basic abilities, system controlled

### Combat basic concepts

   There are many properties to attacks, the following combinations of traits are allowed, each is a property flag of an attack object. Physical attacks are attack objects that have instant effect and have nearby proximity requirement to take effect. Some magical attacks have instant effect as well, but most abilities other than direct melee have a projectile speed and travel from their spawn at the champion to the target whereupon the damage and other traits of the projectile are applied to the target.

Physical Attacks (weapon defines range, each champion will have pre-defined weapons)
Magic Attacks (ability defines range, each champion has pre-defined abilities)
Ranged Physical Attacks (Arrows (Archery), for example)
Ranged Magic Attacks (Fireballs (D&D), for example)
Point Blank Area Effect Magic Attacks (Arcane Explosion (World of Warcraft), for example)
Point Blank Area Effect Physical Attacks (Wu Kong's ultimate (League of Legends), for example.
	- This is, in truth, just a special type of rapid physical attack
Targeted Area Effect Magic Attacks (Pillar of Fire (EverQuest), for example)
Targeted Area Effect Physical Attacks (Hail of Arrows, for example)
Channeled Effect (Short term buff/debuff basically)

Cone - Limited degree PBAE
Line - Ranged Physical or Magic Attack that effects everyone in the path of travel
Line Alternate - Ranged Magic Attack that starts at a target point and travels in a line applying damage to all in path

   The second dimension has to do with the magic damage system. I will echo the MTG paradigm of "protection magic" "life magic" "death magic" "cold magic" and "fire magic". Each champion that is a Magic based champion will have some combination of power in each of these. There will be three ranked spheres of power in each school, and a champion will have a strength in each school, which unlocks various sets of spells, many spells will be shared among some schools, although with different names.

   Spells, and some physical abilities, will often come in combinations of effects. For example, a spell might do damage and also apply a debuff to the target. Debuffs will be defined as follows:

- stun (interrupted, frozen)
- snare (move slowly)
- slow (attack speed reduction)
- root (cannot move)
- poison (damage over time)
- confound / distract (increase cast time / cooldown)
- aphasia (increase cast time)
- fear (uncontrollable, run away)
- confuse (uncontrollable, move at random)
- silence (cannot cast)

- expose (reduced physical defenses)
- tashina (reduce magical defenses)

- mesmerize (take control of other unit)

   Spells will all operate as cooldown controlled abilities, however, they can be applied in several ways, including channeled spells which are a kind of friendly debuff on the caster that makes them immobile (rooted), and places them in a special state where they can be interrupted. A channeled spell will last for a specified duration, and will have a tick frequency, however, the damage will be applied as an instant hit effect at the raising of each tick during the channeling duration. Normal spells will have an instant effect on the caster as mana cost, but once cast, the caster must wait until the cooldown timer has expired before they can cast the spell again. Cooldown on channeled spells will begin after either interruption or completion.

   Abilities can be expressed as a chain of events, like multiple physical attacks followed by a debuff effect. This can apply to both physical and magical effects.

   Finally, physical and magical attacks may come with a displacement effect, which is an instant effect on contact, applied to the target as defined in the applied velocity-on-hit property of the damage object.

### Cantrips

1. Magic Missile
2. Blink (teleport local)
3. Recall (teleport home)
4. Ensnare (slow move)
5. Poison
6. Flash (blind)
7. Confound (slow casting)
8. Stun (interrupt)huhm
9. Root (cannot move)
10. Silence (cannot cast)

### Caster Archetypes

Wizard - Fire
Necromancer - Death
Conjurer - Air
Shaman - Earth
Priest - Life
Cleric - Water

### Core Casting Mechanics:

- Spell Slots (Must be pre-mapped)
- Casting Time (animation, can be cancelled and interrupted)
- Casting Range
- Cooldown for Recast
- Mana Dependent
- Must Meditate
- Spell Types:
  - Instant - No cast time, can fizzle
  - Normal - Cast time, can fizzle
  - Channeled - Cast time, can fizzle, can be resisted per turn
  - Enchantment - No cast time, cannot fizzle, out of combat, reagent
  - Droppable - Cast time, cannot fizzle, reagent or focus (shaman totem, for example)
