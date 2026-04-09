# PD2 Maps Explorer

A reference tool for [Project Diablo 2](https://www.projectdiablo2.com/) that lets you browse level and monster data for Hell difficulty.

**Live site:** [https://maaaaaarrk.github.io/pd2_maps_explorer/](https://maaaaaarrk.github.io/pd2_maps_explorer/)

## Features

### Maps Explorer
- Browse campaign levels (Acts 1-5) and endgame maps (Tier 1-4, Unique Maps, Bosses)
- View level stats: area level, monster density, size, unique/champion counts
- Monster table with HP, AC, damage, resistances (with immunity highlighting), elemental damage, treasure classes, and base exp
- Highest resistance summary row per level

### Damage Calculator
- Multi-source DPS calculator with per-source type, damage, pierce, and FPA (frames per attack)
- Breaking pierce (Conviction, Lower Resist) separated as global settings
- Player count HP scaling (70% per player after 1)
- Map mods: Fortification (2x HP), +Max HP %
- Per-element DPS breakdown and time-to-kill (TTK) display

## Updating Data

The raw game data lives in `data/Levels.txt`, `data/MonStats.txt`, and `data/MonLvl.txt`. To regenerate the JS data files after editing:

```
python convert_data.py
```

Map tier assignments and display names are in `data/tiers.js`.
