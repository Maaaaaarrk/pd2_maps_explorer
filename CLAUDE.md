# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PD2 Maps Explorer is a static web page for browsing Project Diablo 2 level and monster data in Hell difficulty. Raw tab-separated game data files are converted to JSON via Python, then consumed by a single-page vanilla HTML/CSS/JS app.

## Commands

**Convert data (run after editing any .txt file in data/):**
```
python convert_data.py
```
This reads `data/Levels.txt` and `data/MonStats.txt`, outputs `data/levels.js` and `data/monstats.js`.

The page can be opened directly as a file (no server needed) since data is loaded via `<script>` tags, not fetch.

## Architecture

- `data/Levels.txt`, `data/MonStats.txt` — Raw TSV game data (source of truth)
- `convert_data.py` — Python script that parses TSV files and outputs JS files with Hell-difficulty-relevant fields
- `data/levels.js`, `data/monstats.js` — Generated JS data files (do not hand-edit; regenerate via convert_data.py)
- `index.html` — Entire frontend in one file: HTML structure, CSS (dark Diablo-themed), and JS (UI logic, monster table rendering). Loads data via script tags from the .js files above.

## Data Model

**Levels** are split into two categories by ID: campaign (ID <= 136) and endgame/maps (ID > 136). Each level references monsters by their MonStats ID strings in `monsters_hell` (the `nmon1-25` columns from Levels.txt, falling back to `mon1-25`).

**MonStats** are keyed by their string `Id` field. The webpage looks up each monster referenced by a level and displays Hell-difficulty stats: HP, AC, damage, resistances, elemental damage, and type tags (undead/demon/boss).

## Data Sources

- **Levels.txt** format: https://d2mods.info/forum/kb/viewarticle?a=301
  Key columns: `Id`, `Name`, `Act`, `MonLvl3`/`MonLvl3Ex` (Hell area level), `MonDen(H)`, `nmon1-25` (Hell monster spawns), `mon1-25` (Normal monster spawns), `umon1-25` (unique/champion pool), `LevelName`, `Waypoint`

- **MonStats.txt** format: https://d2mods.info/forum/kb/viewarticle?a=360
  Key columns: `Id` (string key used by Levels.txt), `NameStr` (display name), `Level(H)`, `MinHP(H)`/`MaxHP(H)`, `AC(H)`, `A1MinD(H)`/`A1MaxD(H)` (attack damage), `ResFi(H)`/`ResLi(H)`/`ResCo(H)`/`ResPo(H)`/`ResDm(H)`/`ResMa(H)` (resistances, >=100 = immune), `El1Type`/`El1MinD(H)`/`El1MaxD(H)` (elemental damage), `lUndead`/`hUndead`/`demon`/`boss` (type flags)
