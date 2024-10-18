# III. World System Design

  This book is meant to describe the systems that drive the procedural world generation. We start from a simplified elemental system and build into various compounds that are used in gameplay.

## Simplified Elemental System

  The game world is composed of voxels, but unlike traditional cubes that represent just one material, our voxels can both change shape, and are but containers for elements. The contents of any given voxel determines the material. While common interactions with voxels can interact at the level of a voxel material, the simulation undergirding the generation of the world is driven by real-world chemistry and real-world environmental processes. Diamonds aren't produced at random, they're the result of a lot of carbon and temperature and pressure, and this is how we generate them here, too.

### Purpose and Design

The **Simplified Elemental System** serves as the foundational mechanism for simulating material properties, crafting resources, and driving environmental interactions within the voxel-based world of our MMORPG. This system is meticulously designed to enhance realism and player engagement by:

1. **Providing a Foundation for Material Properties, Crafting, and Environmental Interactions:**
    - Establishing a core framework that simulates the physical and chemical properties of materials.
    - Enabling a diverse range of crafting possibilities and resource management strategies.
    - Driving environmental interactions that affect gameplay and world dynamics.

2. **Facilitating Environmental Processes:**
    - Simulating natural phenomena such as erosion, sedimentation, and material transformation.
    - Shaping the landscape in a dynamic way, influencing resource distribution and availability.
    - Allowing players to witness and interact with a living world that responds to both natural forces and player actions.

3. **Acting as Interactive Building Blocks for Gameplay Mechanics:**
    - Treating each voxel as a dynamic container holding one or more elements.
    - Allowing the contents of a voxel to be manipulated through mining, building, or environmental forces.
    - Enabling voxels to respond to player actions and natural events, leading to extraction, concentration, compression, and erosion of elements within them.

4. **Creating a Realistic and Engaging World Simulation:**
    - Enhancing player immersion by simulating realistic environmental and geological processes.
    - Encouraging exploration and strategic resource management.
    - Providing a responsive environment where player decisions have tangible effects on the world.

5. **Streamlining Gameplay and Simulation:**
    - Selecting key elements based on essential transformation pathways and biological processes.
    - Focusing on elements that facilitate realistic simulations of erosion, sediment distribution, and plant growth.
    - Simplifying the elemental system to balance complexity with accessibility for players.

## Simplified Periodic Table

| Element | # | Sym | VEs | Uses |
|---------|---|-----|-----|------|
| Hydrogen | 1 | (H) | 1 | Water |

---

### **Group 1-2:**

1. **Hydrogen (H)**
    - **Atomic Number:** 1
    - **Valence Electrons:** 1
    - **Uses:** Fundamental for water formation and energy production.

2. **Sodium (Na)**
    - **Atomic Number:** 11
    - **Valence Electrons:** 1
    - **Uses:** Crucial for salt production and glassmaking.

3. **Potassium (K)**
    - **Atomic Number:** 19
    - **Valence Electrons:** 1
    - **Uses:** Key component in fertilizers for plant growth.

4. **Calcium (Ca)**
    - **Atomic Number:** 20
    - **Valence Electrons:** 2
    - **Uses:** Essential for making limestone, cement, and mortar.

---

### **Group 3-12: Transition Metals**

5. **Titanium (Ti)**
    - **Atomic Number:** 22
    - **Valence Electrons:** 4
    - **Uses:** Ideal for advanced tools and armor due to its strength and light weight.

6. **Chromium (Cr)**
    - **Atomic Number:** 24
    - **Valence Electrons:** 6
    - **Uses:** Used in stainless steel and metal plating.

7. **Iron (Fe)**
    - **Atomic Number:** 26
    - **Valence Electrons:** 2
    - **Uses:** Fundamental for tools, weapons, and construction materials.

8. **Cobalt (Co)**
    - **Atomic Number:** 27
    - **Valence Electrons:** 2
    - **Uses:** Essential for magnets and advanced alloys.

9. **Nickel (Ni)**
    - **Atomic Number:** 28
    - **Valence Electrons:** 2
    - **Uses:** Used in stainless steel and advanced crafting.

10. **Copper (Cu)**
    - **Atomic Number:** 29
    - **Valence Electrons:** 1
    - **Uses:** Used in electrical components, tools, and construction.

11. **Zinc (Zn)**
    - **Atomic Number:** 30
    - **Valence Electrons:** 2
    - **Uses:** Important for galvanization and brass alloy crafting.

12. **Silver (Ag)**
    - **Atomic Number:** 47
    - **Valence Electrons:** 1
    - **Uses:** Valuable for currency, jewelry, and electronics.

13. **Platinum (Pt)**
    - **Atomic Number:** 78
    - **Valence Electrons:** 1
    - **Uses:** Used in advanced technology and high-end crafting.

14. **Gold (Au)**
    - **Atomic Number:** 79
    - **Valence Electrons:** 1
    - **Uses:** Rare metal for high-end crafting and electronics.

15. **Uranium (U)**
    - **Atomic Number:** 92
    - **Valence Electrons:** 6
    - **Uses:** Rare element used for advanced technology or as an energy source.

---

### **Group 13-18:**

16. **Aluminum (Al)**
    - **Atomic Number:** 13
    - **Valence Electrons:** 3
    - **Uses:** Lightweight metal crucial for crafting and construction.

17. **Carbon (C)**
    - **Atomic Number:** 6
    - **Valence Electrons:** 4
    - **Uses:** Foundation of organic materials, coal, and diamonds.

18. **Silicon (Si)**
    - **Atomic Number:** 14
    - **Valence Electrons:** 4
    - **Uses:** Central to rocks, sand, glass, and ceramics.

19. **Tin (Sn)**
    - **Atomic Number:** 50
    - **Valence Electrons:** 4
    - **Uses:** Used in bronze alloys and various crafting applications.

20. **Lead (Pb)**
    - **Atomic Number:** 82
    - **Valence Electrons:** 4
    - **Uses:** Heavy metal used for radiation shielding and batteries.

21. **Nitrogen (N)**
    - **Atomic Number:** 7
    - **Valence Electrons:** 5
    - **Uses:** Vital for fertilizers and plant growth.

22.  **Phosphorus (P)**
    - **Atomic Number:** 15
    - **Valence Electrons:** 5
    - **Uses:** Important for fertilizers and energy production.

23. **Oxygen (O)**
    - **Atomic Number:** 8
    - **Valence Electrons:** 6
    - **Uses:** Essential for combustion, oxidation, and water formation.

24. **Sulfur (S)**
    - **Atomic Number:** 16
    - **Valence Electrons:** 6
    - **Uses:** Used in crafting and various chemical reactions.

25. **Chlorine (Cl)**
    - **Atomic Number:** 17
    - **Valence Electrons:** 7
    - **Uses:** Used in chemical synthesis and biological functions.

26. **Helium (He)**
    - **Atomic Number:**
    - **Valence Electrons:** 
    - **Uses:** Used to make people laugh and make other stuff float.
  
  --- 

#### **Notes on Valence Electrons and Gameplay Mechanics**

- **Transition Metals:** Transition metals have variable valence electrons due to their d-orbitals. For gameplay purposes, assigning them common valence counts aids in crafting recipes and understanding elemental interactions.

- **Valence Electrons:** Understanding valence electrons helps players predict how elements interact, enhancing the alchemy and crafting systems.

#### **Gameplay Benefits**

- **Intuitive Crafting:** Players can use the atomic number and valence electron information to anticipate crafting outcomes, making the system more engaging.

- **Educational Value:** The organization introduces players to basic chemistry concepts, enriching the gaming experience.

- **Resource Management:** A balanced distribution of common and rare elements ensures progressive gameplay, allowing players to advance from basic to advanced crafting.

---

## Common Compounds in Voxels

Elements combine within voxels to form compounds that represent different materials with unique properties and uses. These compounds are essential for various gameplay mechanics, including crafting, building, and environmental interactions.

### Common Compounds

1. **Water (H₂O)**
    - **Formation:** Composed of hydrogen and oxygen.
    - **Uses:**
      - Essential for plant growth and biological functions.
      - Plays a critical role in erosion processes and sediment transport.
      - Used in crafting recipes and alchemical processes.

2. **Carbon Dioxide (CO₂)**
    - **Formation:** Composed of carbon and oxygen.
    - **Uses:**
      - Vital for plant photosynthesis.
      - Influences environmental processes and atmospheric dynamics.
      - Can be involved in crafting and chemical reactions.

3. **Silicon Dioxide (SiO₂)**
    - **Occurrence:** Found in quartz, sand, and glass.
    - **Uses:**
      - Fundamental material for crafting glass and ceramics.
      - Used in building structures and as a raw material for advanced items.
      - Integral in creating molds and casting components.

4. **Calcium Carbonate (CaCO₃)**
    - **Occurrence:** Found in limestone, marble, and chalk.
    - **Uses:**
      - Essential for construction materials like cement and mortar.
      - Used in crafting decorative items and sculptures.
      - Influences soil pH and can affect plant growth.

5. **Iron Oxide (Fe₂O₃)**
    - **Occurrence:** Found in rust and iron ores.
    - **Uses:**
      - Used for coloring materials and crafting pigments.
      - Important in crafting tools, weapons, and building materials.
      - Can indicate the presence of iron deposits for mining.

6. **Sodium Chloride (NaCl)**
    - **Common Name:** Salt.
    - **Uses:**
      - Used in food preservation and seasoning.
      - Essential in various chemical processes and crafting recipes.
      - Can be employed in curing hides and preserving materials.

7. **Potassium Nitrate (KNO₃)**
    - **Uses:**
      - Key ingredient in fertilizers to enhance plant growth.
      - Used in crafting recipes like gunpowder for explosives.
      - Can be involved in food preservation techniques.

8. **Copper Sulfate (CuSO₄)**
    - **Uses:**
      - Employed in crafting fungicides and pesticides.
      - Used in chemical processes and as a mordant in dyeing.
      - Can be part of advanced crafting and alchemy recipes.

9. **Phosphoric Acid (H₃PO₄)**
    - **Uses:**
      - Essential in producing fertilizers.
      - Used in various industrial and crafting processes.
      - Can be involved in rust removal and metal treatment.

---

### Alloy Compounds

Alloys are combinations of metals that result in materials with enhanced properties, crucial for advanced crafting and construction.

1. **Brass (CuZn)**
  - **Composition:** Alloy of copper (Cu) and zinc (Zn).
  - **Uses:**
    - **Crafting musical instruments, decorative items, and fittings.**
      - Brass is valued for its acoustic properties, making it ideal for trumpets, horns, and other instruments.
      - Its gold-like appearance is popular for ornamental purposes, such as door handles, candlesticks, and jewelry.
    - **Resistance to corrosion.**
      - Brass is more resistant to tarnishing than pure copper, enhancing the durability of crafted items.
    - **Machinability and workability.**
      - Easy to cast and shape, allowing for intricate designs and detailed craftsmanship.

2. **Pewter (SnPb)**
  - **Composition:** Alloy of tin (Sn) and lead (Pb).
  - **Uses:**
    - **Crafting tableware, tankards, and decorative objects.**
      - Historically significant for household items before the widespread use of porcelain and glass.
    - **Malleability and low melting point.**
      - Easy to cast into molds, making it suitable for intricate designs like figurines and ornaments.
    - **Affordable alternative to silver.**
      - Provides a lustrous appearance similar to silver at a lower cost.

3. **Cast Iron (FeC)**
  - **Composition:** Alloy of iron (Fe) with a higher carbon content (2-4%) than steel.
  - **Uses:**
    - **Crafting cookware, pipes, and machinery parts.**
      - Ideal for items requiring good heat retention, like skillets and stoves.
    - **Construction of heavy-duty items and infrastructure components.**
      - Used in building bridges, columns, and frameworks due to its compressive strength.
    - **Resistance to deformation.**
      - Provides durability for items subjected to heavy use.


4. **Solder (SnPb)**
  - **Composition:** Alloy of tin (Sn) and lead (Pb) in varying proportions.
  - **Uses:**
    - **Joining metal parts together, especially in tinwork and plumbing.**
      - Essential for binding metals without damaging them due to its low melting point.
    - **Crafting and repairing metal items.**
      - Used in jewelry making and assembling intricate metal components.
    - **Electrical applications.**
      - Provides conductive joints in electrical components and circuitry.

5. **Sterling Silver (AgCu)**
  - **Composition:** Alloy of silver (Ag) (92.5%) and copper (Cu) (7.5%).
  - **Uses:**
    - **Crafting high-quality jewelry, utensils, and decorative items.**
      - Copper adds strength to silver, which is otherwise too soft for durable items.
    - **Monetary uses and trade.**
      - Often used in coinage and as a standard of wealth.
    - **Antimicrobial properties.**
      - Suitable for crafting medical instruments and containers for perishables.

6. **Electrum (AuAg)**
  - **Composition:** Natural alloy of gold (Au) and silver (Ag).
  - **Uses:**
    - **Historical coinage and jewelry.**
      - Used by ancient civilizations for coins due to its durability and distinct color.
    - **Decorative and ceremonial objects.**
      - Valued for its pale yellow appearance and ease of workability.
    - **Symbol of wealth and status.**
      - Can be integrated into quests or as rewards for achievements.

7. **Gunmetal (CuSnZn)**
  - **Composition:** Alloy of copper (Cu), tin (Sn), and zinc (Zn).
  - **Uses:**
    - **Crafting cannons, guns, and machinery parts.**
      - Offers strength and corrosion resistance vital for weaponry.
    - **Marine applications.**
      - Resistant to saltwater corrosion, suitable for ship fittings and propellers.
    - **Decorative items.**
      - Has a dark, lustrous appearance favored in statues and medals.

8. **Nickel Silver (CuNiZn)**
  - **Composition:** Alloy of copper (Cu), nickel (Ni), and zinc (Zn).
  - **Uses:**
    - **Crafting cutlery, musical instruments, and decorative items.**
      - Known for its silvery appearance despite containing no actual silver.
    - **Durable and corrosion-resistant components.**
      - Suitable for outdoor fixtures and everyday items.
    - **Jewelry making.**
      - Provides an affordable alternative to silver with similar aesthetics.

9. **Wrought Iron (Fe with Slag Inclusions)**
  - **Composition:** Iron (Fe) with very low carbon content and fibrous slag inclusions.
  - **Uses:**
    - **Crafting gates, railings, and decorative ironwork.**
      - Offers ductility and toughness, allowing for intricate designs.
    - **Historical construction material.**
      - Used in building structures before the advent of steel.
    - **Tools and hardware.**
      - Suitable for making nails, hooks, and chains.

10. **White Gold (AuNi)**
  - **Composition:** Alloy of gold (Au) and nickel (Ni), sometimes with palladium.
  - **Uses:**
    - **Crafting jewelry and ornamental pieces.**
      - Nickel whitens the color of gold and adds hardness.
    - **Alternative to traditional yellow gold.**
      - Offers a different aesthetic, appealing to varied tastes.
    - **Setting for gemstones.**
      - Provides a neutral backdrop that enhances the appearance of diamonds and colored stones.

11. **Bronze Variations**
  - **Phosphor Bronze (CuSnP)**
    - **Composition:** Copper (Cu), tin (Sn), and phosphorus (P).
    - **Uses:**
      - **Springs, bolts, and bearings.**
        - Offers increased wear resistance and stiffness.
      - **Musical instruments.**
        - Used in guitar strings and cymbals for its acoustic properties.
  - **Aluminum Bronze (CuAl)**
    - **Composition:** Copper (Cu) and aluminum (Al).
    - **Uses:**
      - **Marine hardware and pumps.**
        - Excellent corrosion resistance in seawater.
      - **Coins and medals.**
        - Durable with a golden appearance.

12. **Steel Variations**
  - **Carbon Steel (FeC)**
    - **Composition:** Iron (Fe) with varying carbon (C) content.
    - **Uses:**
      - **Construction materials and tools.**
        - Higher carbon content increases hardness and strength.
      - **Blades and cutting instruments.**
        - Essential for crafting swords, knives, and axes.
  - **Stainless Steel (FeCrNi)**
    - **Composition:** Iron (Fe), chromium (Cr), and nickel (Ni).
    - **Uses:**
      - **Corrosion-resistant tools and cookware.**
        - Chromium provides a protective oxide layer.
      - **Medical instruments and devices.**
        - Hygienic and easy to sterilize.

13. **Bell Metal (CuSn)**
  - **Composition:** Alloy of copper (Cu) and tin (Sn) with a higher tin content than bronze.
  - **Uses:**
    - **Casting bells and gongs.**
      - Produces a resonant tone ideal for musical instruments.
    - **Sculptures and art pieces.**
      - Allows for detailed casting with a pleasant aesthetic.
    - **Historical currency.**
      - Occasionally used in coinage due to its distinctive sound.

14. **Coinage Alloys**
  - **Billon (AgCu)**
    - **Composition:** Silver (Ag) and copper (Cu) with a higher proportion of copper.
    - **Uses:**
      - **Minting lower-value coins.**
        - Economical use of precious metals.
      - **Jewelry and decorative items.**
        - Provides a balance between appearance and cost.
  - **Cupro-Nickel (CuNi)**
    - **Composition:** Copper (Cu) and nickel (Ni).
    - **Uses:**
      - **Modern coinage and medals.**
        - Resistant to wear and corrosion.
      - **Marine engineering.**
        - Suitable for applications exposed to seawater.

---

### Biological Compounds

In addition to inorganic compounds, voxels can contain biological chemicals crucial for plant growth, decay processes, and ecosystem dynamics. These organic compounds play significant roles in the game's environmental simulation and resource management.

1. **Lignin**
  - **Occurrence:** Found in wood.
  - **Uses:**
    - Provides rigidity and resistance to decay in plants.
    - Can be processed into materials for crafting and construction.
    - Influences the durability of wooden structures.

2. **Cellulose**
  - **Occurrence:** Found in plant cell walls.
  - **Uses:**
    - Provides structural support to plants.
    - Can be used to produce paper, textiles, and other materials.
    - Involved in crafting items like ropes and fabrics.

3. **Chlorophyll**
   - **Occurrence:** Green pigment in plants.
   - **Uses:**
     - Essential for photosynthesis.
     - May be used in crafting dyes and pigments.
     - Could have alchemical properties in gameplay.

4. **Resin**
   - **Occurrence:** Produced by plants, especially conifers.
   - **Uses:**
     - Used in crafting adhesives, varnishes, and sealants.
     - Essential for creating torches and flammable materials.
     - Can be a component in medicinal or alchemical recipes.

5. **Nectar**
   - **Occurrence:** Produced by flowers.
   - **Uses:**
     - Attracts pollinators, influencing plant reproduction.
     - Can be collected to produce sweeteners or fermented beverages.
     - May have applications in alchemy and potion-making.

6. **Pollen**
   - **Occurrence:** Produced by plants for reproduction.
   - **Uses:**
     - Can affect allergies in characters, adding gameplay dynamics.
     - Used in crafting and alchemy, possibly as a reagent.
     - Influences plant breeding and agriculture mechanics.

7. **Humus**
   - **Occurrence:** Organic component of soil.
   - **Uses:**
     - Enhances soil fertility, crucial for agriculture.
     - Affects plant growth rates and crop yields.
     - Can be transported or cultivated by players for farming.

8. **Wax**
   - **Occurrence:** Produced by plants and insects (e.g., bees).
   - **Uses:**
     - Used in crafting candles, polishes, and waterproofing materials.
     - Essential for creating molds in metal casting.
     - Can be a component in healing salves or protective coatings.

9. **Oils**
   - **Occurrence:** Found in seeds and fruits.
   - **Uses:**
     - Used in cooking, crafting, and as fuel for lamps.
     - Essential in creating soaps, lotions, and medicinal items.
     - Can be used in alchemy and potion recipes.

---

#### **Integration into Gameplay**

- **Expanded Crafting Options:**
  - Players can experiment with different alloys to create items with specific properties, such as increased durability, corrosion resistance, or aesthetic appeal.
- **Resource Management:**
  - The need for specific metals encourages exploration and trade, as players seek out rare materials like nickel or zinc.
- **Technological Progression:**
  - Unlocking new alloys can represent technological advancements within the game, rewarding players for their progression.
- **Economic Systems:**
  - Valuable alloys like sterling silver and electrum can serve as currency or high-value trade goods, influencing the in-game economy.
- **Quest and Story Integration:**
  - Rare alloys or items made from them can be tied to quests, legendary items, or faction-specific equipment.

---

### Mineral Compounds

For each mineral, we provide its composition, the element that can be extracted from it, and its uses in the game.

1. **Halite (NaCl)**
  - **Composition:** Sodium Chloride (common salt).
  - **Extracted Element:** **Sodium (Na)**
  - **Uses:**
    - Used in food preservation, seasoning, and chemical processes.
    - Essential for crafting items like glass and for tanning hides.
    - Source of chlorine for crafting disinfectants and bleaching agents (though chlorine is not assigned a unique mineral here).

2. **Sylvite (KCl)**
  - **Composition:** Potassium Chloride.
  - **Extracted Element:** **Potassium (K)**
  - **Uses:**
    - Key ingredient in fertilizers to enhance plant growth.
    - Used in crafting certain chemical compounds and alchemical recipes.

3. **Calcite (CaCO₃)**
  - **Composition:** Calcium Carbonate.
  - **Extracted Element:** **Calcium (Ca)**
  - **Uses:**
    - Primary material for construction (cement, mortar, concrete).
    - Used in agriculture to adjust soil pH and improve fertility.
    - Found in limestone and marble, useful for building and crafting.

4. **Ilmenite (FeTiO₃)**
  - **Composition:** Iron Titanium Oxide.
  - **Extracted Element:** **Titanium (Ti)**
  - **Uses:**
    - Source of titanium for crafting advanced tools and armor.
    - Important for creating high-strength alloys.
    - Used in specialized equipment and machinery.

5. **Chromite (FeCr₂O₄)**
  - **Composition:** Iron Chromium Oxide.
  - **Extracted Element:** **Chromium (Cr)**
  - **Uses:**
    - Used in crafting stainless steel and corrosion-resistant materials.
    - Enhances durability of tools and weapons.
    - Important for metal plating and finishes.

6. **Hematite (Fe₂O₃)**
  - **Composition:** Iron(III) Oxide.
  - **Extracted Element:** **Iron (Fe)**
  - **Uses:**
    - Fundamental for crafting tools, weapons, and building materials.
    - Abundant and essential for early-game progression.
    - Used in creating steel when combined with carbon.

7. **Linnaeite (Co₃S₄)**
  - **Composition:** Cobalt Sulfide.
  - **Extracted Element:** **Cobalt (Co)**
  - **Uses:**
    - Used in crafting magnets and advanced alloys.
    - Important for high-tech equipment and weaponry.
    - Adds strength and durability to metal products.

8. **Millerite (NiS)**
  - **Composition:** Nickel Sulfide.
  - **Extracted Element:** **Nickel (Ni)**
  - **Uses:**
    - Essential for crafting stainless steel and advanced metal components.
    - Used in coinage and specialty alloys.
    - Enhances corrosion resistance in metal items.

9. **Chalcopyrite (CuFeS₂)**
  - **Composition:** Copper Iron Sulfide.
  - **Extracted Element:** **Copper (Cu)**
  - **Uses:**
    - Used in electrical components, tools, and construction.
    - Fundamental for creating bronze when alloyed with tin.
    - Important for wiring and conductive materials.

10. **Sphalerite (ZnS)**
  - **Composition:** Zinc Sulfide.
  - **Extracted Element:** **Zinc (Zn)**
  - **Uses:**
    - Used in galvanization to prevent rusting of iron and steel.
    - Essential for crafting brass when combined with copper.
    - Important in creating alloys and metal treatments.

11. **Argentite (Ag₂S)**
  - **Composition:** Silver Sulfide.
  - **Extracted Element:** **Silver (Ag)**
  - **Uses:**
    - Valuable for currency, jewelry, and high-end crafting.
    - Used in decorative items and ceremonial objects.
    - Essential for electrical components due to high conductivity.

12. **Native Platinum (Pt)**
  - **Composition:** Pure Platinum.
  - **Extracted Element:** **Platinum (Pt)**
  - **Uses:**
    - Used in advanced technology and high-end crafting.
    - Extremely rare and valuable.
    - Integral in catalytic processes and specialized equipment.

13. **Native Gold (Au)**
  - **Composition:** Pure Gold.
  - **Extracted Element:** **Gold (Au)**
  - **Uses:**
    - Used for currency, jewelry, and crafting prestigious items.
    - Sought after for trade and wealth accumulation.
    - Utilized in high-end electronic components.

14. **Uraninite (UO₂)**
  - **Composition:** Uranium Dioxide.
  - **Extracted Element:** **Uranium (U)**
  - **Uses:**
    - Rare element used for advanced technology or as an energy source.
    - Could be part of high-level quests or powerful artifacts.
    - Potential for crafting unique items with special properties.

15. **Bauxite (Al(OH)₃)**
  - **Composition:** Hydrated Aluminum Oxide.
  - **Extracted Element:** **Aluminum (Al)**
  - **Uses:**
    - Lightweight metal for crafting and construction.
    - Used in making utensils, building materials, and certain alloys.
    - Important for transportation devices and structures.

16. **Coal (C)**
  - **Composition:** Primarily Carbon.
  - **Extracted Element:** **Carbon (C)**
  - **Uses:**
    - Used as a fuel source for smelting and heating.
    - Can be processed into graphite for specialized crafting.
    - Essential in steel production when combined with iron.

17. **Quartz (SiO₂)**
  - **Composition:** Silicon Dioxide.
  - **Extracted Element:** **Silicon (Si)**
  - **Uses:**
    - Essential for crafting glass, ceramics, and silicon-based components.
    - Abundant in sand and rock formations.
    - Used in creating molds and high-temperature materials.

18. **Cassiterite (SnO₂)**
  - **Composition:** Tin Dioxide.
  - **Extracted Element:** **Tin (Sn)**
  - **Uses:**
    - Used in crafting bronze when alloyed with copper.
    - Important for making pewter and soldering materials.
    - Utilized in coating and plating processes.

19. **Galena (PbS)**
  - **Composition:** Lead Sulfide.
  - **Extracted Element:** **Lead (Pb)**
  - **Uses:**
    - Used in crafting batteries, pipes, and radiation shielding.
    - Can be employed in creating weights and ammunition.
    - Important for protective equipment and infrastructure.

20. **Saltpeter (KNO₃)**
  - **Composition:** Potassium Nitrate.
  - **Extracted Element:** **Nitrogen (N)**
  - **Uses:**
    - Essential for making fertilizers to enhance crop yields.
    - Key ingredient in crafting gunpowder for explosives.
    - Used in food preservation techniques.

21. **Apatite (Ca₅(PO₄)₃(F,Cl,OH))**
  - **Composition:** Calcium Phosphate.
  - **Extracted Element:** **Phosphorus (P)**
  - **Uses:**
    - Vital for crafting fertilizers to improve soil fertility.
    - Used in creating certain alloys and chemical compounds.
    - Important for agricultural development.

22. **Native Sulfur (S₈)**
  - **Composition:** Elemental Sulfur.
  - **Extracted Element:** **Sulfur (S)**
  - **Uses:**
    - Used in crafting gunpowder, matches, and insecticides.
    - Important for vulcanizing rubber and in alchemy.
    - Essential for various chemical processes.

### Useful Compounds

These minerals were widely known and utilized, serving as fundamental resources for various applications in crafting, building, and technology.

1. **Flint (SiO₂)**
  - **Composition:** Microcrystalline Quartz.
  - **Uses:**
    - Used to make sharp tools and weapons.
    - Essential for creating sparks in fire-starting kits.
    - Important for survival and hunting equipment.

2. **Gypsum (CaSO₄·2H₂O)**
  - **Composition:** Calcium Sulfate Dihydrate.
  - **Uses:**
    - Used in plaster for construction and artistic works.
    - Employed in soil conditioning for agriculture.
    - Utilized in crafting molds and casts.

3. **Slate**
  - **Composition:** Fine-grained Metamorphic Rock.
  - **Uses:**
    - Used as a building material for roofing and flooring.
    - Employed in writing tablets and blackboards.
    - Important for construction and educational tools.

4. **Limestone (CaCO₃)**
  - **Composition:** Calcium Carbonate.
  - **Uses:**
    - Widely used in building construction and road-making.
    - Essential for producing lime for mortar and cement.
    - Utilized in sculpting and decorative architecture.

5. **Sandstone**
  - **Composition:** Composed mainly of Sand-sized Mineral Particles.
  - **Uses:**
    - Used in construction for buildings and paving.
    - Can be carved into statues and architectural details.
    - Important for structural and aesthetic purposes.

6. **Obsidian**
  - **Composition:** Volcanic Glass rich in Silica.
  - **Uses:**
    - Used to craft sharp blades and arrowheads.
    - Valued for its aesthetic appeal in decorative items.
    - Integral in crafting high-quality cutting tools.

7. **Granite**
  - **Composition:** Coarse-grained Igneous Rock.
  - **Uses:**
    - Used extensively in construction, monuments, and sculptures.
    - Known for its durability and strength.
    - Important for large-scale building projects.

8. **Clay (Al₂Si₂O₅(OH)₄)**
  - **Composition:** Hydrated Aluminum Silicate.
  - **Uses:**
    - Essential for pottery, bricks, and ceramics.
    - Used in crafting containers, tiles, and art pieces.
    - Fundamental for early settlement development.

9. **Charcoal (C)**
  - **Composition:** Carbon-rich Material.
  - **Uses:**
    - Used as a fuel and in smelting metals.
    - Employed in blacksmithing and gunpowder production.
    - Important for metallurgical processes.

10. **Saltpeter (KNO₃)**
  - **Composition:** Potassium Nitrate.
  - **Uses:**
    - Used in gunpowder, fertilizers, and food preservation.
    - Essential for military applications and agriculture.
    - Integral in crafting explosives and enhancing crops.

11. **Graphite (C)**
  - **Composition:** Pure carbon.
  - **Uses:**
    - Used in crafting pencils, lubricants, and as a refractory material.
    - Essential for creating electrodes and battery components.
    - Can be processed into diamonds under high-pressure conditions.

12. **Feldspar (KAlSi₃O₈, NaAlSi₃O₈)**
  - **Composition:** Potassium or sodium aluminum silicate.
  - **Uses:**
    - Common rock-forming mineral.
    - Used in crafting glass, ceramics, and glazes.
    - Essential for making pottery and decorative items.

### Gemstone Compounds

Gemstones add value and variety to the game, providing opportunities for trade, crafting, and quests. Below are some common gemstones available within the Simplified Elemental System.

1. **Diamond (C)**
  - **Composition:** Crystalline form of Carbon.
  - **Uses:**
    - Used in crafting high-durability tools and weapons.
    - Valued for jewelry and high-end trade items.
    - Rare and highly sought after, encouraging deep mining.

2. **Emerald (Simplified as Green Beryl)**
  - **Composition:** For gameplay purposes, can be considered a variety of Quartz (SiO₂) colored by trace elements.
  - **Uses:**
    - Used in crafting jewelry and ornamental items.
    - Can be part of quests or magical artifacts.
    - Valued for its vibrant green color.

3. **Ruby (Simplified as Red Corundum)**
  - **Composition:** Aluminum Oxide (Al₂O₃) colored by impurities.
  - **Uses:**
    - Valued for its deep red color in jewelry.
    - Used in crafting decorative items and ceremonial objects.
    - Could be associated with magical properties.

4. **Sapphire (Al₂O₃)**
  - **Composition:** Aluminum Oxide.
  - **Uses:**
    - Used in jewelry and high-end crafting.
    - Available in various colors depending on impurities.
    - May be linked to quests or special abilities.

5. **Amethyst (SiO₂)**
  - **Composition:** Purple Variety of Quartz.
  - **Uses:**
    - Used in crafting decorative items and jewelry.
    - Can be found in geodes or special rock formations.
    - Valued for its aesthetic appeal.

6. **Topaz (Simplified as Colored Quartz)**
  - **Composition:** For gameplay, can be considered a colored form of Quartz.
  - **Uses:**
    - Used in crafting and as a trade commodity.
    - Valued for its range of colors and clarity.
    - Enhances the variety of gemstones available.

7. **Opal (SiO₂·nH₂O)**
  - **Composition:** Hydrated Silicon Dioxide.
  - **Uses:**
    - Known for its iridescent play-of-color.
    - Used in crafting unique jewelry pieces.
    - May be associated with luck or special in-game effects.

8. **Garnet (Simplified as Silicate Mineral)**
  - **Composition:** Silicate Minerals with various elements.
  - **Uses:**
    - Used in crafting and as an abrasive material.
    - Valued for its deep red color in jewelry.
    - Adds diversity to gemstone options.

9. **Pearl (CaCO₃)**
  - **Composition:** Calcium Carbonate layers produced by mollusks.
  - **Uses:**
    - Used in crafting jewelry and decorative items.
    - Can be harvested from oysters or found in treasure chests.
    - Symbolizes wealth and rarity.

10. **Turquoise (Simplified as Copper Mineral)**
  - **Composition:** For gameplay, can be considered a copper-based mineral.
  - **Uses:**
    - Valued for its blue-green color in jewelry.
    - May be used in crafting talismans or amulets.
    - Associated with protection and healing properties.

---

#### Integration into Gameplay

- **Resource Exploration:** Players are encouraged to explore various biomes and geological formations to find these minerals and gemstones.
- **Crafting and Trade:** Minerals and gemstones enhance crafting possibilities, allowing for the creation of unique items, weapons, and armor.
- **Economy Development:** Rare minerals and gemstones can become valuable commodities, promoting trade and economic growth within the game
- **Environmental Interaction:** Minerals influence terrain features, such as mountain ranges rich in ores or deserts abundant in quartz sand.
- **Educational Aspect:** Players learn about historical uses of minerals and gemstones, enriching their gaming experience.

#### Notes on Mineral Availability

- **Exotic Elements:** While some minerals in reality contain elements not present in the Simplified Elemental System, the selected minerals are derived using only the included elements.
- **Substitutions and Simplifications:** For gameplay purposes, certain minerals may be simplified or adjusted to fit within the elemental constraints while maintaining their essential characteristics.

## Materia Transformations and Interactions

Material transformation and interactions are fundamental to creating a realistic and dynamic world. The combination of elements and compounds within voxels leads to the formation of specific materials, influenced by environmental factors such as pressure, temperature, and chemical reactions. This section explores how these transformations occur and how they integrate with gameplay mechanics, all within the context of the **Simplified Elemental System**.

---

## A. Material Transformation

1. Formation of Specific Materials

- **Element and Compound Combinations**: Elements within a voxel can combine to form compounds, which represent different materials with unique properties and uses. For example, iron (Fe) and sulfur (S) can combine to form iron sulfide (FeS), a mineral known as pyrite.
  
- **Voxel Dynamics**: Voxels act as dynamic containers that hold one or more elements or compounds. The contents of a voxel can change through player actions or environmental processes, leading to material transformations like melting, solidification, or chemical reactions.

2. Environmental Influences

- **Pressure and Temperature**: Environmental factors such as pressure and temperature can significantly influence material transformations. High pressure can compress elements into different structural forms, while temperature changes can cause materials to melt, vaporize, or crystallize.
  
- **Chemical Reactions**: Exposure to other elements or compounds can trigger chemical reactions within a voxel. For example, iron exposed to oxygen and moisture will form iron oxide (rust).

---

## B. Examples of Material Interactions

1. **Carbon to Diamond**

- **Process**: Under extreme pressure and high temperatures, carbon atoms are forced into a crystalline lattice structure, forming diamond.
  
- **Gameplay Integration**: Players can simulate this transformation by subjecting carbon-rich materials (like coal) to high-pressure environments, possibly deep underground or using specialized equipment.

2. **Iron to Rust (Iron Oxide Formation)**

- **Process**: Iron reacts with oxygen and moisture in the environment to form iron oxide (Fe₂O₃), commonly known as rust.
  
- **Gameplay Integration**: Iron tools and structures can degrade over time when exposed to air and moisture, encouraging players to protect or maintain their equipment.

3. **Limestone to Marble**

- **Process**: Limestone (calcium carbonate, CaCO₃) transforms into marble through metamorphism, involving heat and pressure that recrystallize the mineral structure.
  
- **Gameplay Integration**: Players can convert limestone blocks into marble by exposing them to high-temperature and pressure conditions, allowing for the crafting of refined building materials.

4. **Plant Decay to Humus**

- **Process**: Organic materials like lignin and cellulose in plants decompose due to environmental factors and organisms, transforming into humus—a nutrient-rich component of soil.
  
- **Gameplay Integration**: Dead plant matter decomposes over time, enriching the soil and affecting plant growth, agriculture, and ecosystem health.

---

## C. Integration with Gameplay Mechanics

1. Crafting System

- **Material Utilization**: Players use elements and compounds to craft tools, weapons, and structures. Understanding material properties and transformations enables more effective crafting strategies.
  
- **Alloy Creation**: Combining metals like copper and tin to create bronze, or iron and carbon to make steel, allows players to produce superior equipment with enhanced properties.

2. Environmental Simulation

- **Dynamic World Changes**: Elemental interactions with environmental factors (e.g., erosion, heat, moisture) lead to natural phenomena like river formation, cave systems, and weathering of materials.
  
- **Resource Availability**: Environmental processes can expose or bury resources, influencing mining and exploration activities.

3. Biological Processes

- **Plant Growth and Decay**: Elements like nitrogen (N), phosphorus (P), and potassium (K) are essential for plant growth. Their availability in the soil affects agriculture and forestry within the game.
  
- **Ecosystem Interactions**: The role of elements in plant decay and interaction with insects adds depth to ecological simulations, impacting food chains and biodiversity.

---

## D. Procedural Plant System

# Overview

The procedural plant system simulates realistic plant growth, reproduction, and evolution within the game world. It leverages the **Simplified Elemental System** to manage resources and interactions with the environment, creating an immersive and dynamic ecosystem.

1. Plant Growth Mechanics

  a. Core Components

- **Branching Frequency and Pattern**

  - **Definition**: Determines the morphology of the plant, including its shape and structure.
  - **Influence**: Affects how plants compete for sunlight and resources, impacting their survival and growth rates.

- **Self-Pruning Techniques**

  - **Definition**: Mechanisms by which plants shed unnecessary or resource-draining parts.
  - **Influence**: Optimizes resource allocation, allowing taller or larger plants to maintain structural integrity.

- **Material Balance**

  - **Components**: The ratio of cellulose, lignin, resin, and chlorophyll within the plant.
  - **Influence**: Affects the plant's strength, flexibility, growth rate, and photosynthetic efficiency.

  b. Growth Algorithm

- **Step-by-Step Growth Process**

  - Plants grow procedurally, adding new branches, leaves, and roots based on environmental conditions and available resources.
  - The algorithm considers factors like nutrient availability, sunlight exposure, and space constraints.

- **Environmental Interaction**

  - **Voxel Composition**: Plants extract nutrients and water from surrounding voxels, affecting and being affected by the local environment.
  - **Adaptation**: Plants may alter their growth patterns in response to obstacles or changes in their surroundings.

2. Environmental Resource Management

  a. Resource Requirements

- **Nutrients and Minerals**

  - Essential elements (N, P, K) are required for producing advanced chemicals like lignin and resin.
  - Deficiency or abundance of these elements affects plant health and growth.

  b. Root Structure and Nutrient Uptake

- **Root Expansion**

  - Roots spread through the voxel grid to absorb water and nutrients, influencing soil composition.
  - Deep or widespread root systems can access resources beyond the immediate vicinity.

- **Impact on Plant Growth**

  - Efficient nutrient uptake leads to robust growth and higher resistance to stress.
  - Competition with other plants for resources can limit growth potential.

3. Flowering and Fruit Production

  a. Flowering Mechanic

- **Triggers for Flowering**

  - Factors include plant maturity, nutrient levels, environmental conditions (temperature, light).
  - Adequate resources and optimal conditions promote flowering.

- **Flowering Process**

  - Involves bud formation, bloom, and potential pollination by insects or environmental factors.
  - Successful pollination is necessary for fruit and seed production.

  b. Fruit Development

- **From Pollination to Maturation**

  - After pollination, energy and nutrients are allocated to developing fruits.
  - Fruit maturation times can vary based on species and environmental conditions.

- **Resource Allocation**

  - Plants balance growth with reproduction, sometimes sacrificing further growth for seed development.
  - Players may influence fruit yield through cultivation practices.

4. Randomization and Natural Selection

  a. Seed Trait Variation

- **Genetic Diversity**

  - Seeds inherit traits from parent plants with random mutations, leading to variation.
  - Traits can include growth rate, drought tolerance, pest resistance.

  b. Environmental Selection

- **Survival of the Fittest**

  - Environmental conditions favor plants with advantageous traits.
  - Less adapted plants may fail to thrive, influencing species composition.

  c. Evolution and Diversity

- **Long-Term Adaptation**

  - Over time, plant populations evolve, leading to new varieties better suited to the environment.
  - Increases biodiversity and resilience of ecosystems.

---

## E. Application in Gameplay

1. Crafting System

- **Material Quality**

  - The properties of plant-derived materials affect the quality of crafted items (e.g., stronger wood for better tools).
  - Access to diverse plant materials expands crafting options.

- **Resource Management**

  - Players must manage resources sustainably to maintain supplies.
  - Over-harvesting can lead to depletion of valuable materials.

2. Environmental Simulation

- **Ecosystem Dynamics**

  - Player actions impact the environment, such as deforestation leading to soil erosion.
  - Environmental stewardship can be a gameplay element, encouraging reforestation or conservation.

- **Elemental Interactions**

  - Elements within voxels interact with environmental factors like erosion, heat, and moisture, influencing terrain and resource availability.
  - Natural disasters (e.g., wildfires) can result from or affect material interactions.

3. Biological Processes

- **Agriculture and Forestry**

  - Understanding plant needs and soil composition helps players cultivate crops and manage forests.
  - Crop rotation and soil amendments can improve yields.

- **Pest Management**

  - Insects and diseases can affect plant health.
  - Players may develop methods to protect plants, such as crafting pesticides or breeding resistant varieties.

---

## F. Conclusion

Material transformation and interactions enrich the game world by introducing realistic and dynamic processes. The integration of the **Simplified Elemental System** ensures consistency and depth across various gameplay mechanics, from crafting and environmental simulation to biological systems. By understanding and engaging with these processes, players can influence the world around them, leading to a more immersive and interactive experience.
