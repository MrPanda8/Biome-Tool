# 🌍 Biome Tool ✨

**Automated Feature Injection for Minecraft Biomes**

This Python script automates the process of injecting custom features into vanilla Minecraft biomes. Designed for datapack creators and modders, it provides a streamlined workflow for biome customization.

## 🚀 Features

- ⭐ **Custom Feature Injection** - Seamlessly add custom features to biomes
- 🌐 **Multilingual Support** - Interface in English, Russian, and Chinese
- ⚡ **Overlay Management** - Quickly create and manage biome overlays
- 📤 **Biome Filtering** - Delete biomes by dimension or custom groups
- ⚙️ **Global Overlays** - Apply changes to all biomes at once
- 📦 **Auto-Download** - Extract biomes directly from Minecraft .jar files
- 🔄 **Backup System** - Automatic backups on every launch
- 👥 **Group System** - Organize biomes into custom groups
- 💾 **Pre-made Groups** - Includes ready-to-use biome groups (see `pre_made_groups` folder)

## 📋 Requirements

- Python 3.8+
- Minecraft Java Edition (for biome extraction)

## 🛠 Installation

1. Download the tool archive
2. Extract to a folder of your choice
3. Run `main.py` or `start.bat` (Windows)

## 🏗 Project Structure
`biome_tool/`  
├── `pre_made_groups/` - Ready-to-use biome groups (copy to groups/)  
├── `backups/` - Automatic backups  
├── `biomes/` - Vanilla Minecraft biomes  
├── `export/` - Processed biomes (output)  
├── `groups/` - Custom biome groups  
├── `overlays/` - Biome overlays  
│   └── `all/` - Global overlay  
├── `main.py` - Main script  
└── `start.bat` - Launch script for Windows

## 🧰 How It Works

The script matches overlay files with biome files and merges their features:

1. **Overlay Preparation**: Create JSON files in `overlays` directory
2. **Processing**: Run the tool to merge overlays with vanilla biomes
3. **Output**: Modified biomes appear in `export` folder

### Example Overlay
`overlays/forest.json`:
```json
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
8. underground_decoration: Infested block blobs, nether gravel and blackstone blobs, and all nether ore blobs 😈
9. fluid_springs: Water and lava springs 💧🔥
10. vegetal_decoration: Trees, bamboo, cacti, kelp, and other ground and ocean vegetation 🌳🌿
11. top_layer_modification: Freeze top layer feature 🥶❄️
