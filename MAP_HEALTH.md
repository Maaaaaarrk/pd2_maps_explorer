# Map Mob HP Survey (Tiers 1–3)

Per-map Hell-difficulty mob HP across the regular spawn pool (`nmon`/`mon` from Levels.txt). HP is scaled to the area's monster level using the same formula as the in-app viewer:

```
realHP = floor(baseHP * MonLvl[areaLvl].L-HP(H) / 100)
```

- **Min HP** — lowest `MinHP(H)` (scaled) in the pool
- **Max HP** — highest `MaxHP(H)` (scaled) in the pool
- **Avg HP** — mean of each monster's mid-HP `(minHP+maxHP)/2`, averaged across the pool
- **Mob Count** — number of distinct enabled monsters contributing to the stats


## Tier 1 (zone level 87)

| Map                  | Area Lvl | Min HP | Max HP | Avg HP | Mob Count |
|----------------------|---------:|-------:|-------:|-------:|----------:|
| Ancestral Trial      |       87 |  7,694 | 14,298 | 10,593 |         7 |
| Fall of Caldeum      |       87 |  7,309 | 12,054 |  9,724 |         6 |
| Lost Temple          |       87 |  6,347 | 13,080 |  9,585 |         7 |
| Phlegethon           |       87 |  6,476 | 14,106 |  9,688 |        10 |
| Ruins of Viz-Jun     |       88 |  7,440 | 15,664 | 10,383 |        11 |
| Shadows of Westmarch |       87 |  6,283 | 18,210 | 10,140 |         7 |
| Tomb of Zoltun Kulle |       87 |  6,668 | 14,362 |  9,794 |         8 |
| Torajan Jungle       |       87 |  7,694 | 13,914 | 10,199 |         8 |

## Tier 2 (zone level 88)

| Map                 | Area Lvl | Min HP | Max HP | Avg HP | Mob Count |
|---------------------|---------:|-------:|-------:|-------:|----------:|
| Ashen Plains        |       88 |  5,939 | 28,261 | 13,017 |         8 |
| Canyon of Sescheron |       88 |  7,244 | 18,210 | 13,115 |         8 |
| Halls of Torture    |       88 |  4,568 | 22,844 | 11,748 |         7 |
| Horazon's Memory    |       88 |  8,354 | 21,343 | 13,290 |         8 |
| Pandemonium Citadel |       88 |  7,440 | 26,891 | 13,109 |         7 |
| Ruined Cistern      |       88 |  6,592 | 25,324 | 13,106 |         8 |
| Sanatorium          |       88 |  7,179 | 27,021 | 13,193 |         7 |
| Sewers of Harrogath |       88 |  6,657 | 13,837 | 10,055 |         8 |
| Throne of Insanity  |       88 |  8,093 | 18,797 | 13,641 |         8 |

## Tier 3 (zone level 89)

| Map                   | Area Lvl | Min HP | Max HP | Avg HP | Mob Count |
|-----------------------|---------:|-------:|-------:|-------:|----------:|
| Arreat Battlefield    |       89 | 12,420 | 22,848 | 16,638 |         8 |
| Bastion Keep          |       89 |  8,833 | 39,719 | 16,596 |         8 |
| Blood Moon            |       89 | 14,612 | 17,933 | 16,272 |         6 |
| Demon Road            |       89 |  8,900 | 29,291 | 16,667 |         8 |
| Kehjistan Marketplace |       89 |  7,306 | 30,553 | 16,912 |         8 |
| Kyovoshad             |       89 |  9,697 | 28,560 | 16,596 |         8 |
| River of Blood        |       89 | 10,560 | 28,892 | 16,512 |         9 |
| Royal Crypts          |       89 | 12,553 | 22,317 | 16,638 |         8 |
| Skovos Stronghold     |       89 |  8,966 | 24,243 | 16,638 |         7 |
