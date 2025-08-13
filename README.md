## 🌍 Biome Tool ✨
This is a python script for automating the injection of custom features (and more) into vanilla Minecraft biomes.

Before you begin, install the latest version of Python 🐍.

Main functions:
- convenient injection of custom features into biomes ⭐️
- support 3 languages (en/ru/zh) (sorry if the translation is not perfect) 🌐
- the ability to quickly create overlays ⚡️
- the ability to delete unnecessary biomes by dimensions 📤
- global overlay processing ⚙️
- automatic download of biomes from .jar 📦

How does this script work? The script compares the names of overlays and biomes and merges them.

Example overlay:
overlays/forest.json
```
{
  "features": [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [
      "my_namespace:new_tree",
      "my_namespace2:new_flower",
      "my_test_namespace:new_rock"
    ],
    []
  ]
}
```
Decoration steps
Features and structures generate in 11 steps after each other called decoration steps.

1. raw_generation: Small end islands 🌴
2. lakes: Lava lakes 🔥
3. local_modifications: Amethyst geodes and icebergs 💎❄️
4. underground_structures: Trial chambers, buried treasure, mineshafts, trail ruins, monster rooms and fossils 🏹💎
5. surface_structures: All other structures, desert wells and blue ice patches 🏜️🏛️
6. strongholds: Unused, strongholds use the surface_structures step ⚠️
7. underground_ores: Ore blobs and sand/gravel/clay disks ⛏️💎
8. underground_decoration: Infested block blobs, nether gravel and blackstone blobs, and all nether ore blobs 😈🔥
9. fluid_springs: Water and lava springs 💧🔥
10. vegetal_decoration: Trees, bamboo, cacti, kelp, and other ground and ocean vegetation 🌳🌿
11. top_layer_modification: Freeze top layer feature 🥶❄️
