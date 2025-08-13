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
```{
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
