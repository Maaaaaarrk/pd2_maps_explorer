# Changelog

Monster data update — Hell difficulty stats regenerated from `data/Levels.txt` and `data/MonStats.txt`.

## Summary

- **4** new monsters
- **222** monsters with stat changes
- **28** maps affected

## Level spawn list changes

- **River Of Blood** (id 144): added `councilmemberBlood`; removed `councilmembermap`

## Other level (Levels.txt) field changes

Non-monster fields changed on 18 levels. These are mostly cosmetic/layout tweaks — no changes to `Act`, `MonLvl3(Ex)`, `MonDen(H)`, waypoint/quest flags, or level-size fields.

| ID | Map | Field | Old → New |
|---:|---|---|---|
| 155 | Caldeum Map | OffsetX | `3600` → `3550` |
| 169 | Westmarch Map | OffsetY | `2900` → `2200` |
| 173 | Butcher Event Map | OffsetX | `3900` → `3850` |
| 175 | Ashen Plains Map | OffsetY | `3200` → `2150` |
| 188 | Lucion Arena | EntryFile | `U3L1` → `X1L1` |
| 189 | Lucion Vault | EntryFile | `U3L1` → `X1L2` |
| 190 | Skovos Stronghold Map | EntryFile | `M8L5` → `M9L1` |
| 191 | Demon Road Map | EntryFile | `M8L7` → `M9L2` |
| 192 | Imperial Palace Map | EntryFile | `M8L7` → `M9L3` |
| 193 | Halls of Torture Map | OffsetX / OffsetY / EntryFile | `5000`→`4000` / `1500`→`2000` / `M8L7`→`M9L4` |
| 194 | Imperial Boss Map | EntryFile | `M8L7` → `M9L5` |
| 195 | Ureh City Map | OffsetY / EntryFile | `1000`→`2000` / `U2L4`→`M9L6` |
| 196 | Nemyr Monastery Map | EntryFile | `U2L4` → `M9L7` |
| 197 | Djinns Domain Map | OffsetX / OffsetY / EntryFile | `5000`→`3600` / `1700`→`2200` / `M8L7`→`M9L8` |
| 198 | Djinns Domain Red Map | OffsetX / OffsetY / EntryFile | `5200`→`3800` / `1900`→`2200` / `M8L7`→`M9L9` |
| 199 | Djinns Domain Boss Map | OffsetX / OffsetY / EntryFile | `5200`→`3600` / `2300`→`2400` / `M8L7`→`M9LA` |
| 200 | Na-Krul's Abyss Map | SoundEnv / ObjGrp0 / ObjGrp1 / ObjPrb0 / ObjPrb1 | `22`→`32` / `—`→`48` / `—`→`49` / `—`→`30` / `—`→`50` |
| 201 | Kyovoshad Map | OffsetY / SoundEnv / LevelName / LevelWarp / EntryFile / ObjGrp0-2 / ObjPrb0-2 | `3200`→`1900` / `22`→`34` / `Ashen Plains`→`KyovashadMap` / `To The Ashen Plains`→`ToKyovashadMap` / `M8L7`→`M9LB` / `—`→`46/47/77` / `—`→`30/80/70` |

**What the fields mean:**
- `OffsetX`/`OffsetY` — act-world minimap placement coordinates.
- `EntryFile` — the preset/level-code used when loading the map tileset.
- `SoundEnv` — ambient sound environment id.
- `ObjGrp*` / `ObjPrb*` — decoration object group ids and spawn probabilities (visual props only).
- `LevelName`/`LevelWarp` — display text for the area / its warp link.

Biggest behavior change: **Kyovoshad Map** got its own identity (dedicated LevelName/LevelWarp, previously reused "Ashen Plains" strings). **Na-Krul's Abyss Map** and **Kyovoshad Map** also gained full decoration object sets (`ObjGrp0-2` / `ObjPrb0-2`) — they were empty before, meaning the maps got proper visual dressing.

## Average base life & density per map

Avg HP = mean of `(MinHP(H)+MaxHP(H))/2` across every monster that spawns in the map (incl. bosses). Density is `MonDen(H)` from `Levels.txt`. **No map had its density changed.**

| ID  | Map                    | Mons | Avg HP old | Avg HP new |    ΔHP  |   %HP   | Den old | Den new |
|----:|------------------------|-----:|-----------:|-----------:|--------:|--------:|--------:|--------:|
| 138 | Mesa                   |    1 |     7000.0 |     5250.0 | -1750.0 | -25.0%  |     100 |     100 |
| 139 | Siege Map              |    9 |      550.0 |      917.1 |  +367.1 | +66.7%  |    1980 |    1980 |
| 142 | Arcane                 |   10 |      554.1 |      748.1 |  +194.0 | +35.0%  |    1980 |    1980 |
| 143 | Kurast                 |   11 |      201.8 |      159.1 |   -42.7 | -21.2%  |    2062 |    2062 |
| 144 | River Of Blood         |   10 |      223.6 |      239.2 |   +15.6 |  +7.0%  |    1980 |    1980 |
| 145 | Lava                   |   10 |      247.4 |      151.1 |   -96.3 | -38.9%  |    1980 |    1980 |
| 146 | Ice Map                |    9 |      693.1 |      533.8 |  -159.3 | -23.0%  |    1980 |    1980 |
| 149 | Fortress Map           |    9 |      706.8 |      888.8 |  +182.0 | +25.7%  |    1980 |    1980 |
| 150 | Throne Map             |   11 |     1361.8 |     1298.5 |   -63.3 |  -4.6%  |    1815 |    1815 |
| 151 | Tomb Map               |    8 |      203.4 |      152.8 |   -50.6 | -24.9%  |    2860 |    2860 |
| 156 | Pandemonium Map        |    8 |      969.7 |      738.2 |  -231.5 | -23.9%  |    1350 |    1350 |
| 158 | Spider Map             |    9 |      784.4 |      590.8 |  -193.6 | -24.7%  |    2200 |    2200 |
| 160 | Frozen Forest Map      |    9 |      884.4 |      711.9 |  -172.5 | -19.5%  |    1650 |    1650 |
| 167 | Library Map            |    8 |     1252.6 |      989.4 |  -263.2 | -21.0%  |    2310 |    2310 |
| 170 | Crypts Map             |    8 |      144.8 |      250.5 |  +105.7 | +73.0%  |    1980 |    1980 |
| 174 | Ruined Cistern Map     |   10 |     1630.9 |     1210.7 |  -420.2 | -25.8%  |    1980 |    1980 |
| 175 | Ashen Plains Map       |    9 |     1027.0 |      821.7 |  -205.3 | -20.0%  |    1950 |    1950 |
| 176 | Zhar Library           |    8 |      249.1 |      199.4 |   -49.7 | -20.0%  |    1980 |    1980 |
| 190 | Skovos Stronghold Map  |   16 |     3553.2 |     2975.2 |  -578.0 | -16.3%  |    2800 |    2800 |
| 191 | Demon Road Map         |    9 |      902.1 |     1000.8 |   +98.7 | +10.9%  |    2000 |    2000 |
| 192 | Imperial Palace Map    |    8 |      740.4 |     1098.5 |  +358.1 | +48.4%  |    1000 |    1000 |
| 193 | Halls of Torture Map   |    8 |      757.5 |      951.2 |  +193.7 | +25.6%  |    2200 |    2200 |
| 199 | Djinns Domain Boss Map |   10 |       94.2 |       98.8 |    +4.6 |  +4.9%  |    1800 |    1800 |

Density omitted — no map had its `MonDen(H)` changed. Maps not listed had `+0.0%` avg HP movement.

**Buffed (higher avg HP):** Crypts (+73%), Siege (+67%), Imperial Palace (+48%), Arcane (+35%), Fortress (+26%), Halls of Torture (+26%), Demon Road (+11%), River of Blood (+7%), Djinns Boss (+5%).

**Nerfed (lower avg HP):** Lava (-39%), Ruined Cistern (-26%), Mesa (-25%), Spider (-25%), Tomb (-25%), Pandemonium (-24%), Ice (-23%), Kurast (-21%), Library (-21%), Ashen Plains (-20%), Zhar Library (-20%), Frozen Forest (-20%), Skovos (-16%), Throne (-5%).

**Unchanged (31 maps):** Sewers, Desert, Jungle, Monastery (+basement), Graveyard, Caldeum, Necropolis (Jungle/Swamp/Void), Realm of Terror, Hole of Terror, BR Arena, Westmarch, Sanctuary of Sin, Black Abyss, Zhar (Rivers/Ice/Kurast), Outer Void, Hellcaves (+Fortress), Fallen Gardens, Kanemith (Outside/Dungeon), Imperial Boss, Ureh City, Nemyr Monastery, Djinns Domain (Map/Red), Na-Krul's Abyss, Kyovoshad.

## Monster stat changes by map

### Mesa (id 138)

**Stat changes:**

- `TombBoss` — TombBoss
    - MinHP(H): `7000` → `5250`
    - MaxHP(H): `7000` → `5250`
    - A1MinD(H): `120` → `103`
    - A1MaxD(H): `180` → `155`
    - A2MinD(H): `60` → `52`
    - A2MaxD(H): `105` → `90`

### Siege Map (id 139)

**Stat changes:**

- `zombieSiege` — Zombie
    - MinHP(H): `146` → `244`
    - MaxHP(H): `178` → `297`
    - A1MinD(H): `80` → `106`
    - A1MaxD(H): `145` → `193`
    - A2MinD(H): `80` → `106`
    - A2MaxD(H): `145` → `193`
    - ResFi(H): `-` → `15`
    - ResLi(H): `-` → `20`
    - ResPo(H): `85` → `75`
    - ResMa(H): `50` → `30`
- `goatmanSiege` — NightClan
    - MinHP(H): `136` → `227`
    - MaxHP(H): `167` → `279`
    - A1MinD(H): `96` → `128`
    - A1MaxD(H): `141` → `188`
    - ResLi(H): `85` → `65`
    - ResCo(H): `-` → `25`
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `0`
    - El1MinD(H): `38` → `51`
    - El1MaxD(H): `98` → `130`
- `quillratSiege` — SpikeFiend
    - MinHP(H): `112` → `187`
    - MaxHP(H): `142` → `237`
    - A1MinD(H): `55` → `73`
    - A1MaxD(H): `92` → `122`
    - A2MinD(H): `60` → `80`
    - A2MaxD(H): `98` → `130`
    - ResLi(H): `-` → `50`
    - ResPo(H): `-` → `40`
    - El1MinD(H): `34` → `45`
    - El1MaxD(H): `68` → `90`
- `bigheadSiege` — Afflicted
    - MinHP(H): `126` → `210`
    - MaxHP(H): `156` → `261`
    - A1MinD(H): `80` → `106`
    - A1MaxD(H): `121` → `161`
    - ResFi(H): `-` → `25`
    - ResLi(H): `100` → `120`
    - ResCo(H): `25` → `30`
    - ResMa(H): `30` → `35`
    - El1MinD(H): `137` → `182`
    - El1MaxD(H): `172` → `229`
    - El2MinD(H): `10` → `20`
    - El2MaxD(H): `20` → `40`
- `reanimatedSiege` — UnholyCorpse
    - MinHP(H): `140` → `234`
    - MaxHP(H): `167` → `279`
    - A1MinD(H): `43` → `57`
    - A1MaxD(H): `73` → `87`
    - A2MinD(H): `43` → `57`
    - A2MaxD(H): `73` → `97`
    - ResFi(H): `130` → `75`
    - ResDm(H): `50` → `15`
    - ResMa(H): `50` → `30`
- `thornhulkSiege` — BrambleHulk
    - MinHP(H): `170` → `284`
    - MaxHP(H): `206` → `344`
    - A1MinD(H): `112` → `149`
    - A1MaxD(H): `169` → `225`
    - A2MinD(H): `112` → `149`
    - A2MaxD(H): `169` → `225`
    - ResCo(H): `80` → `75`
    - ResMa(H): `-` → `0`
- `vultureSiege` — CarrionBird
    - MinHP(H): `118` → `197`
    - MaxHP(H): `140` → `234`
    - A1MinD(H): `104` → `138`
    - A1MaxD(H): `129` → `172`
    - ResFi(H): `25` → `35`
    - ResLi(H): `-` → `75`
    - ResCo(H): `-` → `50`
    - ResPo(H): `75` → `120`
    - ResDm(H): `-` → `0`
- `mosquitoSiege` — BloodWing
    - MinHP(H): `132` → `220`
    - MaxHP(H): `164` → `274`
    - A1MinD(H): `80` → `106`
    - A1MaxD(H): `116` → `164`
    - ResFi(H): `-` → `75`
    - ResCo(H): `-` → `45`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `105`
- `SiegeBoss` — SiegeBoss
    - MinHP(H): `3750` → `6250`
    - MaxHP(H): `3750` → `6250`
    - A1MinD(H): `160` → `190`
    - A1MaxD(H): `220` → `250`

### Sewers (id 141)

**Stat changes:**

- `fetish2Sewer` — Fetish
    - A1MinD(H): `53` → `80`
    - A1MaxD(H): `75` → `113`
    - ResFi(H): `75` → `120`
    - ResLi(H): `-` → `45`
    - ResCo(H): `-` → `20`
    - ResMa(H): `-` → `15`
- `minionSewer` — Minionexp
    - A1MinD(H): `95` → `143`
    - A1MaxD(H): `119` → `179`
    - A2MinD(H): `101` → `152`
    - A2MaxD(H): `126` → `189`
    - ResLi(H): `15` → `35`
    - ResCo(H): `25` → `35`
    - ResPo(H): `15` → `20`
    - ResMa(H): `-` → `35`
- `vilechildSewer` — GrotesqueWyrm
    - A1MinD(H): `72` → `108`
    - A1MaxD(H): `91` → `137`
    - ResFi(H): `-` → `65`
    - ResLi(H): `135` → `75`
    - ResCo(H): `-` → `65`
- `fetishblowSewer` — Flayer
    - A1MinD(H): `66` → `99`
    - A1MaxD(H): `72` → `108`
    - ResFi(H): `-` → `0`
    - ResDm(H): `-` → `15`
    - El1MinD(H): `21` → `26`
    - El1MaxD(H): `91` → `114`
- `vampireSewer` — GhoulLord
    - A1MinD(H): `78` → `117`
    - A1MaxD(H): `112` → `168`
    - ResFi(H): `33` → `75`
    - ResCo(H): `75` → `80`
    - El1MinD(H): `112` → `140`
    - El1MaxD(H): `147` → `184`
- `sandmaggotSewer` — SandMaggot
    - A1MinD(H): `91` → `137`
    - A1MaxD(H): `118` → `177`
    - ResLi(H): `-` → `25`
    - ResCo(H): `85` → `75`
    - ResPo(H): `125` → `120`
    - ResMa(H): `-` → `0`
- `sandraiderSewer` — Marauder
    - A1MinD(H): `88` → `132`
    - A1MaxD(H): `119` → `179`
    - A2MinD(H): `88` → `132`
    - A2MaxD(H): `119` → `179`
    - ResLi(H): `80` → `75`
    - ResMa(H): `-` → `15`
    - El1MinD(H): `84` → `105`
    - El1MaxD(H): `105` → `131`
- `mosquitoSewer` — BloodWing
    - A1MinD(H): `78` → `117`
    - A1MaxD(H): `108` → `162`
    - ResLi(H): `33` → `45`
    - ResCo(H): `-` → `25`
    - ResPo(H): `-` → `30`
    - ResDm(H): `-` → `10`

### Arcane (id 142)

**Stat changes:**

- `flyingscimitarArcane` — FlyingScimitar
    - MinHP(H): `105` → `142`
    - MaxHP(H): `158` → `213`
    - A1MinD(H): `101` → `136`
    - A1MaxD(H): `140` → `189`
    - ResLi(H): `80` → `120`
    - ResCo(H): `-` → `75`
- `zealotArcane` — Zakarumite
    - MinHP(H): `121` → `163`
    - MaxHP(H): `168` → `227`
    - A1MinD(H): `88` → `119`
    - A1MaxD(H): `123` → `166`
    - A2MinD(H): `60` → `96`
    - A2MaxD(H): `105` → `168`
    - ResLi(H): `33` → `25`
    - ResCo(H): `33` → `35`
    - ResMa(H): `-` → `0`
- `painwormArcane` — Pain Worm4
    - MinHP(H): `95` → `128`
    - MaxHP(H): `137` → `185`
    - A1MinD(H): `61` → `82`
    - A1MaxD(H): `88` → `119`
    - ResFi(H): `135` → `75`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `25`
- `cantorArcane` — Cantor
    - MinHP(H): `105` → `142`
    - MaxHP(H): `158` → `213`
    - A1MinD(H): `70` → `95`
    - A1MaxD(H): `110` → `149`
    - ResFi(H): `25` → `45`
    - ResMa(H): `-` → `20`
    - El1MinD(H): `60` → `81`
    - El1MaxD(H): `120` → `162`
- `doomknightArcane` — OblivionKnight
    - MinHP(H): `121` → `163`
    - MaxHP(H): `168` → `227`
    - A1MinD(H): `88` → `119`
    - A1MaxD(H): `154` → `208`
    - ResFi(H): `60` → `75`
    - ResCo(H): `-` → `25`
- `snowyetiArcane` — SnowYeti4
    - MinHP(H): `168` → `227`
    - MaxHP(H): `226` → `305`
    - A1MinD(H): `100` → `135`
    - A1MaxD(H): `136` → `184`
    - A2MinD(H): `75` → `120`
    - A2MaxD(H): `110` → `176`
    - ResFi(H): `-` → `35`
    - ResPo(H): `-` → `25`
    - ResDm(H): `40` → `115`
    - ResMa(H): `-` → `0`
- `frozenhorrorArcane` — Frozen Horror5
    - MinHP(H): `189` → `255`
    - MaxHP(H): `242` → `327`
    - A1MinD(H): `88` → `119`
    - A1MaxD(H): `132` → `178`
    - ResFi(H): `-` → `15`
    - ResCo(H): `130` → `75`
    - ResPo(H): `33` → `35`
- `wraithArcane` — Ghost
    - MinHP(H): `110` → `149`
    - MaxHP(H): `142` → `192`
    - A1MinD(H): `88` → `119`
    - A1MaxD(H): `127` → `171`
    - ResFi(H): `50` → `55`
- `ArcaneBoss` — ArcaneBoss
    - MinHP(H): `4200` → `5670`
    - MaxHP(H): `4200` → `5670`
    - A1MinD(H): `50` → `120`
    - El1MinD(H): `40` → `70`
    - El1MaxD(H): `75` → `105`
- `doomknight1Arcane` — DoomKnight
    - MinHP(H): `120` → `162`
    - MaxHP(H): `150` → `203`
    - A1MinD(H): `65` → `88`
    - A1MaxD(H): `141` → `190`
    - ResFi(H): `60` → `75`
    - ResLi(H): `60` → `40`
    - ResCo(H): `-` → `25`
    - El1MinD(H): `30` → `41`
    - El1MaxD(H): `60` → `81`

### Kurast (id 143)

**Stat changes:**

- `cr_lancermap` — BlackLancer
    - MinHP(H): `166` → `128`
    - MaxHP(H): `192` → `148`
    - ResLi(H): `120` → `75`
    - ResCo(H): `25` → `75`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `35`
- `goatmanmap` — MoonClan
    - MinHP(H): `179` → `138`
    - MaxHP(H): `219` → `169`
    - ResFi(H): `-` → `60`
    - ResLi(H): `-` → `25`
    - ResPo(H): `-` → `50`
    - ResMa(H): `33` → `35`
- `cr_archermap` — DarkRanger
    - MinHP(H): `155` → `119`
    - MaxHP(H): `180` → `139`
    - ResCo(H): `75` → `120`
    - ResMa(H): `-` → `20`
- `bigheadmap` — Disfigured
    - MinHP(H): `148` → `114`
    - MaxHP(H): `191` → `147`
    - ResFi(H): `40` → `50`
    - ResCo(H): `-` → `25`
    - ResPo(H): `-` → `50`
    - ResMa(H): `-` → `0`
- `cantormap` — Heirophant
    - ResFi(H): `25` → `50`
    - ResLi(H): `33` → `50`
- `unravelermap` — HollowOne
    - MinHP(H): `192` → `148`
    - MaxHP(H): `246` → `189`
    - ResFi(H): `20` → `45`
    - ResLi(H): `0` → `45`
- `arachmap` — SpiderMagus
    - MinHP(H): `259` → `199`
    - MaxHP(H): `312` → `240`
    - ResFi(H): `0` → `50`
    - ResCo(H): `-` → `20`
    - ResPo(H): `60` → `75`
    - ResMa(H): `-` → `0`
- `thornhulkmap` — ThornedHulk
    - MinHP(H): `212` → `163`
    - MaxHP(H): `266` → `205`
    - ResFi(H): `-` → `0`
    - ResLi(H): `-` → `75`
    - ResCo(H): `33` → `45`
    - ResDm(H): `80` → `115`
    - ResMa(H): `-` → `0`
- `sandleapermap` — TreeLurker
    - MinHP(H): `152` → `117`
    - MaxHP(H): `212` → `163`
    - ResCo(H): `-` → `50`
    - ResPo(H): `25` → `50`
    - ResDm(H): `-` → `25`
- `mosquitomap` — Sucker
    - MinHP(H): `148` → `114`
    - MaxHP(H): `212` → `163`
    - ResLi(H): `33` → `45`
    - ResCo(H): `-` → `25`
    - ResDm(H): `-` → `0`
- `fetishshamanmap` — FetishShaman
    - MinHP(H): `192` → `148`
    - MaxHP(H): `246` → `189`
    - ResFi(H): `130` → `75`
    - ResLi(H): `25` → `45`
    - ResCo(H): `-` → `45`

### River Of Blood (id 144)

**Added monsters:**

- `councilmemberBlood` — Council Member (Lv88, HP 171-192)

**Stat changes:**

- `doomknightmap` — DoomKnight
    - MinHP(H): `172` → `201`
    - MaxHP(H): `201` → `235`
    - A1MinD(H): `102` → `116`
    - A1MaxD(H): `165` → `188`
    - ResCo(H): `20` → `25`
    - ResMa(H): `-` → `0`
    - El1MinD(H): `50` → `57`
    - El1MaxD(H): `80` → `91`
- `vilemothermap` — FleshSpawner
    - MinHP(H): `168` → `197`
    - MaxHP(H): `246` → `288`
    - A1MinD(H): `149` → `170`
    - A1MaxD(H): `173` → `197`
    - ResFi(H): `-` → `45`
    - ResLi(H): `-` → `25`
    - ResCo(H): `80` → `65`
    - ResPo(H): `-` → `20`
    - ResMa(H): `100` → `105`
- `zealotmap` — Zealot
    - MinHP(H): `177` → `207`
    - MaxHP(H): `194` → `227`
    - A1MinD(H): `106` → `121`
    - A1MaxD(H): `141` → `161`
    - A2MinD(H): `60` → `68`
    - A2MaxD(H): `105` → `120`
    - ResCo(H): `33` → `35`
    - ResMa(H): `-` → `0`
- `oblivionknightmap` — OblivionKnight
    - MinHP(H): `177` → `207`
    - MaxHP(H): `194` → `227`
    - A1MinD(H): `106` → `121`
    - A1MaxD(H): `165` → `188`
    - ResFi(H): `60` → `50`
    - ResCo(H): `180` → `75`
- `deathmaulermap` — Death Mauler1
    - MinHP(H): `168` → `197`
    - MaxHP(H): `194` → `227`
    - A1MinD(H): `118` → `135`
    - A1MaxD(H): `169` → `193`
    - ResLi(H): `85` → `120`
    - ResPo(H): `-` → `20`
    - ResMa(H): `-` → `0`
- `sk_archermap` — SkeletonArcher
    - MinHP(H): `136` → `159`
    - MaxHP(H): `165` → `193`
    - A1MinD(H): `102` → `116`
    - A1MaxD(H): `141` → `161`
    - ResPo(H): `130` → `120`
- `baalminionmap` — Baals Minion
    - MinHP(H): `355` → `415`
    - MaxHP(H): `372` → `435`
    - A1MinD(H): `141` → `161`
    - A1MaxD(H): `173` → `197`
    - A2MinD(H): `80` → `91`
    - A2MaxD(H): `140` → `160`
    - ResFi(H): `90` → `75`
    - ResCo(H): `50` → `65`
    - ResPo(H): `95` → `75`
    - ResDm(H): `50` → `0`
    - ResMa(H): `-` → `25`
- `regurgitatormap` — Corpulent
    - MinHP(H): `284` → `332`
    - MaxHP(H): `312` → `365`
    - A1MinD(H): `149` → `170`
    - A1MaxD(H): `184` → `210`
    - ResFi(H): `-` → `25`
    - ResLi(H): `-` → `45`
    - ResCo(H): `-` → `50`
    - ResDm(H): `15` → `25`

### Lava (id 145)

**Stat changes:**

- `minionmap` — HellSpawn
    - MinHP(H): `252` → `154`
    - MaxHP(H): `275` → `168`
    - A1MinD(H): `136` → `106`
    - A1MaxD(H): `164` → `128`
    - A2MinD(H): `136` → `106`
    - A2MaxD(H): `164` → `128`
    - ResLi(H): `25` → `75`
    - ResDm(H): `33` → `30`
    - ResMa(H): `-` → `0`
- `pantherwomanmap` — HellCat
    - MinHP(H): `207` → `126`
    - MaxHP(H): `257` → `156`
    - A1MinD(H): `92` → `72`
    - A1MaxD(H): `131` → `102`
    - ResFi(H): `-` → `25`
    - ResCo(H): `80` → `75`
- `fallenmap` — Fallen
    - MinHP(H): `165` → `101`
    - MaxHP(H): `223` → `136`
    - A1MinD(H): `119` → `93`
    - A1MaxD(H): `186` → `145`
    - A2MinD(H): `119` → `93`
    - A2MaxD(H): `186` → `145`
    - ResFi(H): `25` → `50`
    - ResLi(H): `-` → `25`
- `slingermap` — HellSlinger
    - MinHP(H): `188` → `115`
    - MaxHP(H): `230` → `140`
    - A1MinD(H): `119` → `93`
    - A1MaxD(H): `157` → `122`
    - ResCo(H): `-` → `25`
    - ResPo(H): `25` → `50`
- `siegebeastmap` — Siege Beast
    - MinHP(H): `286` → `174`
    - MaxHP(H): `315` → `192`
    - A1MinD(H): `198` → `154`
    - A1MaxD(H): `284` → `222`
    - ResFi(H): `140` → `120`
    - ResPo(H): `-` → `25`
    - ResDm(H): `75` → `50`
    - ResMa(H): `-` → `0`
- `bloodlordmap` — Blood Lord1
    - MinHP(H): `246` → `150`
    - MaxHP(H): `286` → `174`
    - A1MinD(H): `131` → `102`
    - A1MaxD(H): `207` → `161`
    - A2MinD(H): `131` → `102`
    - A2MaxD(H): `207` → `161`
    - ResFi(H): `25` → `50`
    - ResPo(H): `-` → `50`
- `councilmembermap` — Council Member
    - MinHP(H): `240` → `146`
    - MaxHP(H): `269` → `164`
    - A1MinD(H): `98` → `76`
    - A1MaxD(H): `175` → `137`
    - ResFi(H): `33` → `75`
    - ResCo(H): `33` → `45`
    - ResMa(H): `-` → `0`
- `reanimatedhordemap` — UnholyCorpse
    - MinHP(H): `188` → `115`
    - MaxHP(H): `217` → `132`
    - A1MinD(H): `108` → `84`
    - A1MaxD(H): `152` → `119`
    - ResFi(H): `-` → `25`
    - ResCo(H): `-` → `75`
    - ResPo(H): `75` → `120`
- `fallenshamanmap` — FallenShaman
    - MinHP(H): `309` → `188`
    - MaxHP(H): `361` → `220`
    - A1MinD(H): `131` → `102`
    - A1MaxD(H): `186` → `145`
    - ResFi(H): `50` → `75`
    - ResLi(H): `125` → `75`
    - ResCo(H): `-` → `45`
- `fetishmap` — Fetish
    - MinHP(H): `202` → `126`
    - MaxHP(H): `232` → `145`
    - A1MinD(H): `140` → `109`
    - A1MaxD(H): `175` → `137`

### Ice Map (id 146)

**Stat changes:**

- `mummyIce` — PreservedDead
    - MinHP(H): `204` → `153`
    - MaxHP(H): `241` → `181`
    - A1MinD(H): `115` → `85`
    - A1MaxD(H): `155` → `114`
    - ResFi(H): `50` → `120`
- `skeletonIce` — BoneWarrior
    - MinHP(H): `182` → `137`
    - MaxHP(H): `219` → `164`
    - A1MinD(H): `89` → `66`
    - A1MaxD(H): `142` → `105`
    - A2MinD(H): `89` → `77`
    - A2MaxD(H): `142` → `122`
    - ResDm(H): `-` → `0`
- `skmage_coldIce` — BoneMage
    - MinHP(H): `160` → `120`
    - MaxHP(H): `197` → `148`
    - ResLi(H): `-` → `25`
    - ResDm(H): `-` → `0`
- `arach5Ice` — SpiderMagus
    - MinHP(H): `211` → `158`
    - MaxHP(H): `248` → `186`
    - A1MinD(H): `133` → `98`
    - A1MaxD(H): `155` → `114`
    - ResFi(H): `-` → `25`
    - ResPo(H): `120` → `75`
    - ResMa(H): `-` → `0`
- `megademon2Ice` — PitLord
    - MinHP(H): `233` → `175`
    - MaxHP(H): `270` → `203`
    - A1MinD(H): `151` → `112`
    - A1MaxD(H): `222` → `164`
    - ResFi(H): `75` → `50`
    - ResLi(H): `75` → `120`
    - ResMa(H): `-` → `0`
- `baalminion3Ice` — Baals Minion
    - MinHP(H): `263` → `197`
    - MaxHP(H): `297` → `223`
    - A1MinD(H): `133` → `98`
    - A1MaxD(H): `178` → `132`
    - A2MinD(H): `133` → `114`
    - A2MaxD(H): `178` → `153`
    - ResLi(H): `130` → `-`
    - ResPo(H): `75` → `-`
    - ResDm(H): `50` → `-`
- `wraith3Ice` — Specter
    - MinHP(H): `160` → `120`
    - MaxHP(H): `197` → `148`
    - A1MinD(H): `115` → `85`
    - A1MaxD(H): `155` → `114`
    - ResPo(H): `-` → `75`
- `IceBoss` — IceBoss
    - MinHP(H): `4500` → `3500`
    - MaxHP(H): `4500` → `3500`
    - A1MinD(H): `240` → `177`
    - A1MaxD(H): `440` → `325`
    - A2MinD(H): `240` → `206`
    - A2MaxD(H): `440` → `378`
- `fingermage3Ice` — StormCaster
    - MinHP(H): `175` → `131`
    - MaxHP(H): `219` → `164`
    - A1MinD(H): `111` → `82`
    - A1MaxD(H): `169` → `125`
    - ResFi(H): `-` → `25`
    - ResPo(H): `-` → `45`

### Desert Map (id 147)

**Stat changes:**

- `sandraider3Market` — Invader
    - ResCo(H): `-` → `20`
    - ResPo(H): `-` → `30`
    - ResDm(H): `25` → `0`
    - ResMa(H): `-` → `0`
- `flyingscimitarMarket` — FlyingScimitar
    - ResLi(H): `-` → `50`
    - ResCo(H): `-` → `30`
    - ResMa(H): `50` → `35`
- `mosquito2Market` — Feeder
    - ResFi(H): `-` → `15`
    - ResPo(H): `105` → `75`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `10`
- `firetowerMarket` — FireTower
    - ResFi(H): `-` → `75`
    - ResCo(H): `85` → `45`
    - ResPo(H): `1000` → `75`
- `vampire1Market` — GhoulLord
    - ResFi(H): `125` → `120`
    - ResLi(H): `25` → `35`
    - ResDm(H): `30` → `115`
    - ResMa(H): `-` → `40`
- `cr_archer2Market` — VileArcher
    - ResLi(H): `90` → `75`
    - ResCo(H): `130` → `75`
    - ResMa(H): `-` → `15`
- `unraveler3Market` — Unraveler
    - ResMa(H): `50` → `40`

### Jungle Map (id 148)

**Stat changes:**

- `foulcrowJungle` — FoulCrow
    - ResFi(H): `25` → `50`
    - ResLi(H): `-` → `25`
    - ResCo(H): `-` → `45`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `0`
- `sandleaperJungle` — TreeLurker
    - ResFi(H): `125` → `50`
    - ResCo(H): `-` → `0`
    - ResPo(H): `85` → `120`
    - ResDm(H): `-` → `0`
- `quillratJungle` — QuillRat
    - ResFi(H): `-` → `75`
    - ResLi(H): `-` → `45`
    - ResDm(H): `50` → `25`
    - ResMa(H): `-` → `0`
- `deathmaulerJungle` — Death Mauler2
    - ResDm(H): `33` → `35`
- `bruteJungle` — Crusher
    - ResFi(H): `-` → `35`
    - ResLi(H): `-` → `35`
    - ResCo(H): `75` → `120`
- `baboonJungle` — DuneBeast
    - ResDm(H): `33` → `35`
    - ResMa(H): `-` → `25`
- `scarabJungle` — SandWarrior
    - ResFi(H): `-` → `25`
    - ResLi(H): `105` → `75`
    - ResCo(H): `-` → `75`
    - ResPo(H): `-` → `0`
- `councilmemberJungle` — Council Member
    - ResFi(H): `33` → `75`
    - ResDm(H): `50` → `25`
    - ResMa(H): `-` → `40`

### Fortress Map (id 149)

**Stat changes:**

- `fallenBastion` — Devilkin
    - MinHP(H): `107` → `133`
    - MaxHP(H): `161` → `200`
    - A1MinD(H): `80` → `92`
    - A1MaxD(H): `133` → `152`
    - A2MinD(H): `59` → `68`
    - A2MaxD(H): `117` → `134`
    - ResFi(H): `-` → `50`
    - ResMa(H): `-` → `0`
    - El1MaxD(H): `94` → `108`
- `goatmanBastion` — MoonClan
    - MinHP(H): `141` → `175`
    - MaxHP(H): `201` → `249`
    - A1MinD(H): `88` → `101`
    - A1MaxD(H): `144` → `165`
    - ResFi(H): `75` → `50`
    - ResLi(H): `-` → `50`
    - ResCo(H): `130` → `120`
    - ResDm(H): `50` → `25`
    - ResMa(H): `-` → `0`
- `sandmaggotBastion` — GiantLamprey
    - MinHP(H): `174` → `216`
    - MaxHP(H): `221` → `274`
    - A1MinD(H): `112` → `128`
    - A1MaxD(H): `154` → `176`
    - ResCo(H): `-` → `35`
    - ResDm(H): `-` → `0`
- `fallenshamanBastion` — DevilkinShaman
    - MinHP(H): `134` → `166`
    - MaxHP(H): `188` → `233`
    - A1MinD(H): `88` → `101`
    - A1MaxD(H): `135` → `155`
    - ResFi(H): `-` → `75`
    - ResCo(H): `-` → `25`
- `siegebeastBastion` — DeamonSteed
    - MinHP(H): `402` → `498`
    - MaxHP(H): `482` → `598`
    - A1MinD(H): `187` → `214`
    - A1MaxD(H): `267` → `306`
    - ResPo(H): `-` → `15`
    - ResMa(H): `-` → `105`
- `sandraiderBastion` — SandRaider
    - MinHP(H): `201` → `249`
    - MaxHP(H): `248` → `308`
    - A1MinD(H): `108` → `124`
    - A1MaxD(H): `154` → `176`
    - A2MinD(H): `108` → `124`
    - A2MaxD(H): `154` → `176`
    - ResCo(H): `-` → `50`
    - El1MinD(H): `164` → `188`
    - El1MaxD(H): `211` → `242`
- `batdemonBastion` — DesertWing
    - MinHP(H): `121` → `150`
    - MaxHP(H): `174` → `216`
    - A1MinD(H): `94` → `108`
    - A1MaxD(H): `135` → `155`
    - A2MinD(H): `94` → `108`
    - A2MaxD(H): `135` → `155`
    - ResFi(H): `125` → `75`
    - ResLi(H): `-` → `25`
    - ResDm(H): `110` → `115`
    - El1MinD(H): `6` → `7`
    - El1MaxD(H): `281` → `322`
- `succubusBastion` — Hell Temptress
    - MinHP(H): `107` → `133`
    - MaxHP(H): `161` → `200`
    - A1MinD(H): `70` → `80`
    - A1MaxD(H): `117` → `134`
    - ResLi(H): `50` → `65`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `0`
    - El1MinD(H): `47` → `54`
    - El1MaxD(H): `88` → `101`
- `BastionBoss` — BastionBoss
    - MinHP(H): `4750` → `6000`
    - MaxHP(H): `4750` → `6000`
    - El1MinD(H): `500` → `575`
    - El1MaxD(H): `600` → `675`

### Throne Map (id 150)

**Stat changes:**

- `corruptrogueThrone` — FleshHunter
    - MinHP(H): `220` → `176`
    - MaxHP(H): `270` → `216`
    - A1MinD(H): `145` → `127`
    - A1MaxD(H): `165` → `144`
    - ResFi(H): `25` → `45`
    - ResLi(H): `50` → `65`
    - ResCo(H): `65` → `75`
    - ResDm(H): `40` → `25`
- `cr_archerThrone` — FleshArcher
    - MinHP(H): `155` → `124`
    - MaxHP(H): `205` → `164`
    - A1MinD(H): `125` → `79`
    - A1MaxD(H): `185` → `132`
    - ResFi(H): `25` → `40`
    - ResPo(H): `40` → `25`
    - ResMa(H): `0` → `15`
- `cr_lancerThrone` — FleshLancer
    - MinHP(H): `235` → `188`
    - MaxHP(H): `285` → `228`
    - A1MinD(H): `165` → `144`
    - A1MaxD(H): `175` → `153`
    - ResFi(H): `0` → `40`
    - ResDm(H): `45` → `15`
    - ResMa(H): `0` → `15`
- `impThrone` — Imp2
    - MinHP(H): `185` → `148`
    - MaxHP(H): `235` → `188`
    - ResLi(H): `25` → `55`
    - ResCo(H): `0` → `25`
    - ResDm(H): `-` → `0`
- `overseerThrone` — HellWhip
    - MinHP(H): `295` → `236`
    - MaxHP(H): `345` → `276`
    - A1MinD(H): `145` → `157`
    - A1MaxD(H): `170` → `179`
    - A2MinD(H): `145` → `157`
    - A2MaxD(H): `170` → `179`
    - ResCo(H): `0` → `50`
    - ResPo(H): `0` → `25`
    - ResMa(H): `0` → `25`
- `megademonThrone` — Balrog
    - MinHP(H): `310` → `248`
    - MaxHP(H): `360` → `288`
    - A1MinD(H): `195` → `171`
    - A1MaxD(H): `195` → `171`
    - ResFi(H): `130` → `75`
    - ResDm(H): `50` → `20`
- `frogdemonThrone` — Swamp Dweller
    - MinHP(H): `260` → `208`
    - MaxHP(H): `310` → `248`
    - A1MinD(H): `130` → `114`
    - A1MaxD(H): `135` → `118`
    - ResLi(H): `0` → `25`
    - ResPo(H): `85` → `120`
- `fingermageThrone` — Groper
    - MinHP(H): `230` → `184`
    - MaxHP(H): `280` → `224`
    - A1MinD(H): `155` → `136`
    - A1MaxD(H): `155` → `136`
    - ResCo(H): `130` → `75`
    - ResPo(H): `0` → `75`
    - ResDm(H): `50` → `115`
- `ThroneBoss` — ThroneBoss
    - MinHP(H): `7500` → `6000`
    - MaxHP(H): `7500` → `6000`
- `minion5throne` — HellSpawn
    - MinHP(H): `120` → `96`
    - MaxHP(H): `160` → `128`
    - A1MinD(H): `120` → `105`
    - A1MaxD(H): `180` → `158`
    - A2MinD(H): `120` → `105`
    - A2MaxD(H): `180` → `158`
    - ResFi(H): `65` → `50`
    - ResLi(H): `15` → `50`
    - ResCo(H): `33` → `45`
    - ResPo(H): `35` → `75`
    - ResDm(H): `33` → `35`
    - ResMa(H): `-` → `25`
- `baalminionboss` — StrBelial
    - MinHP(H): `5250` → `6500`
    - MaxHP(H): `5250` → `6500`
    - A1MinD(H): `80` → `90`
    - A1MaxD(H): `130` → `145`
    - A2MinD(H): `80` → `90`
    - A2MaxD(H): `140` → `145`

### Tomb Map (id 151)

**Stat changes:**

- `scarabTomb` — Scarab
    - MinHP(H): `173` → `130`
    - MaxHP(H): `217` → `163`
    - A1MinD(H): `92` → `79`
    - A1MaxD(H): `119` → `102`
    - A2MinD(H): `92` → `79`
    - A2MaxD(H): `119` → `102`
    - ResFi(H): `-` → `25`
    - ResDm(H): `105` → `115`
- `painworm1Tomb` — Pain Worm1
    - MinHP(H): `163` → `122`
    - MaxHP(H): `212` → `159`
    - A1MinD(H): `87` → `75`
    - A1MaxD(H): `115` → `99`
    - ResFi(H): `-` → `50`
    - ResLi(H): `-` → `50`
    - ResPo(H): `110` → `120`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `50`
- `quillrat4Tomb` — RazorSpine
    - MinHP(H): `139` → `104`
    - MaxHP(H): `182` → `137`
    - A1MinD(H): `49` → `42`
    - A1MaxD(H): `68` → `58`
    - A2MinD(H): `49` → `42`
    - A2MaxD(H): `68` → `58`
    - ResLi(H): `-` → `35`
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `0`
- `skmage_ltng5Tomb` — ReturnedMage
    - MinHP(H): `139` → `104`
    - MaxHP(H): `193` → `145`
    - A1MaxD(H): `112` → `96`
    - ResLi(H): `120` → `75`
    - ResCo(H): `-` → `45`
- `baboon1Tomb` — DuneBeast
    - MinHP(H): `173` → `130`
    - MaxHP(H): `230` → `173`
    - A1MinD(H): `105` → `90`
    - A1MaxD(H): `169` → `145`
    - A2MinD(H): `105` → `90`
    - A2MaxD(H): `169` → `145`
    - ResFi(H): `25` → `35`
    - ResPo(H): `25` → `50`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `25`
- `batdemon5Tomb` — DarkFamiliar
    - MinHP(H): `173` → `130`
    - MaxHP(H): `217` → `163`
    - A1MinD(H): `102` → `88`
    - A1MaxD(H): `112` → `96`
    - A2MinD(H): `102` → `88`
    - A2MaxD(H): `112` → `96`
    - ResFi(H): `-` → `75`
    - ResCo(H): `-` → `25`
    - ResPo(H): `-` → `25`
- `arach1Tomb` — Arach
    - MinHP(H): `217` → `163`
    - MaxHP(H): `269` → `202`
    - A1MinD(H): `123` → `106`
    - A1MaxD(H): `160` → `138`
    - ResFi(H): `85` → `75`
    - ResLi(H): `-` → `0`
    - ResCo(H): `-` → `50`
    - ResMa(H): `-` → `25`
- `baalminionTomb` — Baals Minion
    - MinHP(H): `260` → `195`
    - MaxHP(H): `298` → `224`
    - A1MinD(H): `95` → `82`
    - A1MaxD(H): `151` → `130`
    - A2MinD(H): `95` → `82`
    - A2MaxD(H): `151` → `130`
    - ResLi(H): `100` → `75`
    - ResCo(H): `25` → `30`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `0`

### Caldeum Map (id 155)

**Stat changes:**

- `zombieCaldeum` — Zombie
    - ResFi(H): `95` → `50`
    - ResDm(H): `50` → `0`
    - ResMa(H): `-` → `0`
- `pantherwoman1Caldeum` — Huntress
    - ResLi(H): `-` → `35`
    - ResDm(H): `15` → `20`
- `flyingscimitarCaldeum` — FlyingScimitar
    - ResLi(H): `100` → `120`
    - ResCo(H): `-` → `0`
    - ResMa(H): `-` → `25`
- `slinger1Caldeum` — Slinger
    - ResLi(H): `-` → `45`
    - ResPo(H): `-` → `25`
    - ResDm(H): `10` → `0`
- `swarm4Caldeum` — HellSwarm
    - ResFi(H): `-` → `25`
    - ResDm(H): `50` → `115`
    - ResMa(H): `-` → `0`
- `cantor3Caldeum` — Heirophant
    - ResCo(H): `130` → `75`
    - ResDm(H): `10` → `15`
    - ResMa(H): `50` → `105`

### Pandemonium Map (id 156)

**Stat changes:**

- `reanimatedhorde3Pandemonium` — ProwlingDead
    - MinHP(H): `221` → `177`
    - MaxHP(H): `243` → `194`
    - ResFi(H): `-` → `50`
    - ResPo(H): `130` → `75`
    - ResDm(H): `50` → `25`
    - ResMa(H): `-` → `15`
- `fetish3Pandemonium` — Flayer
    - MinHP(H): `143` → `114`
    - MaxHP(H): `166` → `133`
    - A1MinD(H): `60` → `81`
    - A1MaxD(H): `95` → `128`
    - ResFi(H): `25` → `75`
    - ResDm(H): `-` → `0`
- `bighead5Pandemonium` — Damned
    - MinHP(H): `170` → `136`
    - MaxHP(H): `221` → `177`
    - A1MinD(H): `50` → `88`
    - A1MaxD(H): `80` → `128`
    - ResFi(H): `50` → `25`
    - ResLi(H): `135` → `75`
    - ResCo(H): `-` → `0`
    - ResMa(H): `-` → `0`
- `succubuswitch3Pandemonium` — StygianFury
    - MinHP(H): `212` → `170`
    - MaxHP(H): `239` → `191`
    - A1MinD(H): `50` → `88`
    - A1MaxD(H): `70` → `115`
    - ResLi(H): `66` → `50`
    - ResDm(H): `100` → `50`
    - ResMa(H): `25` → `105`
- `baboon5Pandemonium` — TempleGuard
    - MinHP(H): `244` → `195`
    - MaxHP(H): `285` → `228`
    - A1MinD(H): `80` → `108`
    - A1MaxD(H): `140` → `189`
    - ResMa(H): `-` → `20`
- `siegebeast3Pandemonium` — BloodBringer
    - MinHP(H): `460` → `368`
    - MaxHP(H): `515` → `412`
    - A1MinD(H): `150` → `163`
    - A1MaxD(H): `190` → `217`
    - ResLi(H): `-` → `20`
    - ResMa(H): `-` → `0`
- `vampire3Pandemonium` — DarkLord
    - MinHP(H): `175` → `140`
    - MaxHP(H): `221` → `177`
    - A1MinD(H): `50` → `68`
    - A1MaxD(H): `100` → `135`
    - ResCo(H): `75` → `120`
    - ResPo(H): `90` → `80`
    - ResDm(H): `-` → `0`
- `archerBoss` — PandemoniumBoss
    - MinHP(H): `6000` → `4500`
    - MaxHP(H): `6000` → `4500`
    - A1MinD(H): `100` → `90`
    - A1MaxD(H): `160` → `150`
    - A2MinD(H): `100` → `90`
    - A2MaxD(H): `160` → `150`

### Spider Map (id 158)

**Stat changes:**

- `minionSpider` — Minionexp
    - MinHP(H): `190` → `141`
    - MaxHP(H): `230` → `170`
    - ResLi(H): `20` → `50`
    - ResMa(H): `-` → `15`
- `mosquito4Spider` — BloodWing
    - MinHP(H): `147` → `109`
    - MaxHP(H): `188` → `139`
    - ResFi(H): `-` → `15`
    - ResLi(H): `45` → `40`
    - ResCo(H): `-` → `25`
    - ResDm(H): `-` → `25`
- `batdemon6Spider` — Gloombat
    - MinHP(H): `134` → `99`
    - MaxHP(H): `167` → `124`
    - ResFi(H): `33` → `50`
    - ResCo(H): `110` → `120`
    - ResPo(H): `-` → `0`
    - ResMa(H): `-` → `105`
- `unraveler3Spider` — Unraveler
    - MinHP(H): `201` → `149`
    - MaxHP(H): `235` → `174`
    - ResFi(H): `20` → `35`
    - ResDm(H): `33` → `35`
- `fetishblowSpider` — Flayer
    - ResFi(H): `-` → `75`
    - ResDm(H): `-` → `0`
- `blunderbore2Spider` — Gorbelly
    - MinHP(H): `243` → `180`
    - MaxHP(H): `276` → `204`
    - ResMa(H): `-` → `0`
- `arach3Spider` — PoisonSpinner
    - MinHP(H): `196` → `145`
    - MaxHP(H): `229` → `169`
    - ResFi(H): `120` → `75`
    - ResLi(H): `-` → `35`
    - ResCo(H): `-` → `25`
    - ResMa(H): `-` → `0`
- `spiderboss` — spiderboss
    - MinHP(H): `5500` → `4125`
    - MaxHP(H): `5500` → `4125`
    - A1MinD(H): `150` → `130`
    - A1MaxD(H): `240` → `220`
- `willowisp1Spider` — Gloam
    - MinHP(H): `180` → `133`
    - MaxHP(H): `213` → `158`

### Frozen Forest Map (id 160)

**Stat changes:**

- `snowyeti4Frozen` — SnowYeti4
    - MinHP(H): `250` → `205`
    - MaxHP(H): `310` → `254`
    - ResFi(H): `-` → `0`
    - ResPo(H): `-` → `50`
    - ResDm(H): `-` → `0`
- `sandleaper5Frozen` — RazorPitDemon
    - MinHP(H): `180` → `148`
    - MaxHP(H): `260` → `213`
    - ResFi(H): `130` → `120`
    - ResCo(H): `-` → `40`
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `15`
- `doomknight1Frozen` — DoomKnight
    - MinHP(H): `260` → `213`
    - MaxHP(H): `300` → `246`
    - ResLi(H): `20` → `65`
    - ResMa(H): `-` → `25`
- `doomknight3Frozen` — OblivionKnight
    - MinHP(H): `245` → `201`
    - MaxHP(H): `275` → `226`
    - ResLi(H): `60` → `75`
    - ResDm(H): `-` → `0`
- `clawviper5Frozen` — SerpentMagus
    - MinHP(H): `235` → `193`
    - MaxHP(H): `265` → `217`
    - ResDm(H): `120` → `115`
    - ResMa(H): `70` → `55`
- `overseer3Frozen` — OverLord
    - MinHP(H): `300` → `246`
    - MaxHP(H): `340` → `279`
    - ResPo(H): `-` → `25`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `0`
- `fetish4Frozen` — SoulKiller
    - MinHP(H): `155` → `127`
    - MaxHP(H): `215` → `176`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `25`
- `fetishblow4Frozen` — SoulKiller
    - MinHP(H): `135` → `111`
    - MaxHP(H): `195` → `160`
    - ResFi(H): `-` → `45`
    - ResLi(H): `-` → `40`
    - ResCo(H): `-` → `45`
    - ResPo(H): `110` → `75`
- `CanyonBoss` — CanyonBoss
    - MinHP(H): `6000` → `4800`
    - MaxHP(H): `6000` → `4800`

### Library Map (id 167)

**Stat changes:**

- `corruptrogue2Library` — VileHunter
    - MinHP(H): `173` → `138`
    - MaxHP(H): `224` → `179`
    - A1MinD(H): `100` → `90`
    - A1MaxD(H): `164` → `148`
    - ResFi(H): `30` → `35`
    - ResPo(H): `25` → `45`
    - ResMa(H): `20` → `15`
- `cr_archer2Library` — VileArcher
    - MinHP(H): `155` → `124`
    - MaxHP(H): `198` → `158`
    - A1MinD(H): `117` → `105`
    - A1MaxD(H): `153` → `138`
    - ResFi(H): `65` → `75`
    - ResLi(H): `-` → `25`
    - ResPo(H): `25` → `40`
    - ResMa(H): `20` → `15`
- `cr_lancer2Library` — VileLancer
    - MinHP(H): `207` → `166`
    - MaxHP(H): `249` → `199`
    - A1MinD(H): `113` → `102`
    - A1MaxD(H): `187` → `168`
    - ResLi(H): `125` → `120`
    - ResPo(H): `25` → `45`
    - ResMa(H): `15` → `105`
- `deathmauler3Library` — Death Mauler3
    - MinHP(H): `198` → `158`
    - MaxHP(H): `284` → `227`
    - A1MinD(H): `153` → `138`
    - A1MaxD(H): `207` → `186`
    - ResLi(H): `50` → `25`
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `25`
- `willowisp1Library` — Gloam
    - MinHP(H): `138` → `110`
    - MaxHP(H): `180` → `144`
    - A1MinD(H): `100` → `90`
    - A1MaxD(H): `153` → `138`
    - ResFi(H): `-` → `25`
    - ResCo(H): `-` → `25`
    - ResPo(H): `130` → `120`
    - ResMa(H): `35` → `0`
- `vampire1Library` — GhoulLord
    - MinHP(H): `258` → `206`
    - MaxHP(H): `345` → `276`
    - A1MinD(H): `106` → `95`
    - A1MaxD(H): `174` → `157`
    - ResLi(H): `25` → `50`
    - ResMa(H): `-` → `35`
- `bloodlord5Library` — Blood Lord5
    - MinHP(H): `414` → `331`
    - MaxHP(H): `518` → `414`
    - A1MinD(H): `127` → `114`
    - A1MaxD(H): `176` → `158`
    - A2MinD(H): `124` → `95`
    - A2MaxD(H): `172` → `166`
    - ResCo(H): `35` → `40`
    - ResDm(H): `-` → `0`
    - ResMa(H): `33` → `25`
- `doomknight3LibraryBoss` — LibraryBoss
    - MinHP(H): `8250` → `6500`
    - MaxHP(H): `8250` → `6500`

### Westmarch Map (id 169)

**Stat changes:**

- `minion4Westmarch` — FireBoar
    - ResLi(H): `50` → `70`
    - ResCo(H): `-` → `25`
    - ResDm(H): `-` → `25`
    - ResMa(H): `-` → `0`
- `goatmanBastionWestmarch` — MoonClan
    - ResDm(H): `100` → `50`
    - ResMa(H): `45` → `25`
- `zombie1Westmarch` — Zombie
    - ResFi(H): `-` → `50`
    - ResCo(H): `-` → `50`
    - ResPo(H): `135` → `120`
- `slinger1Westmarch` — Slinger
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `0`
- `overseer1Westmarch` — OverSeer
    - ResFi(H): `75` → `120`
- `succubus1Westmarch` — Succubusexp
    - ResPo(H): `65` → `75`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `105`

### Crypts Map (id 170)

**Stat changes:**

- `skeleton3Crypt` — BoneWarrior
    - MinHP(H): `114` → `197`
    - MaxHP(H): `168` → `291`
    - A1MinD(H): `70` → `95`
    - A1MaxD(H): `123` → `166`
    - A2MinD(H): `70` → `103`
    - A2MaxD(H): `123` → `178`
    - ResLi(H): `-` → `35`
    - ResDm(H): `35` → `25`
    - ResMa(H): `-` → `25`
- `scarab3Crypt` — Scarab
    - MinHP(H): `129` → `223`
    - MaxHP(H): `173` → `299`
    - A1MinD(H): `76` → `103`
    - A1MaxD(H): `132` → `178`
    - A2MinD(H): `76` → `122`
    - A2MaxD(H): `132` → `149`
    - ResFi(H): `-` → `40`
    - ResPo(H): `-` → `25`
    - ResDm(H): `-` → `20`
    - ResMa(H): `-` → `0`
    - El1MinD(H): `15` → `20`
    - El1MaxD(H): `30` → `41`
- `batdemon3Crypt` — Gloombat
    - MinHP(H): `109` → `189`
    - MaxHP(H): `144` → `249`
    - A1MinD(H): `90` → `122`
    - A1MaxD(H): `110` → `149`
    - A2MinD(H): `90` → `100`
    - A2MaxD(H): `110` → `248`
    - ResFi(H): `75` → `120`
    - ResCo(H): `-` → `25`
    - ResPo(H): `-` → `50`
    - El1MinD(H): `131` → `177`
    - El1MaxD(H): `181` → `244`
- `sk_archer3Crypt` — BoneArcher
    - MinHP(H): `109` → `189`
    - MaxHP(H): `139` → `240`
    - A1MinD(H): `92` → `124`
    - A1MaxD(H): `105` → `142`
    - A2MinD(H): `0` → `-`
    - A2MaxD(H): `258` → `-`
    - ResCo(H): `-` → `45`
    - ResPo(H): `105` → `75`
    - ResMa(H): `150` → `45`
- `bighead1Crypt` — Afflicted
    - MinHP(H): `114` → `197`
    - MaxHP(H): `168` → `291`
    - A1MinD(H): `80` → `108`
    - A1MaxD(H): `126` → `170`
    - A2MinD(H): `-` → `119`
    - A2MaxD(H): `-` → `220`
    - ResFi(H): `-` → `55`
    - ResPo(H): `-` → `40`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `30`
    - El1MinD(H): `181` → `244`
    - El1MaxD(H): `221` → `298`
    - El2MinD(H): `30` → `40`
    - El2MaxD(H): `40` → `53`
- `baboon1Crypt` — DuneBeast
    - MinHP(H): `149` → `258`
    - MaxHP(H): `194` → `336`
    - A1MinD(H): `88` → `119`
    - A1MaxD(H): `163` → `220`
    - A2MinD(H): `88` → `95`
    - A2MaxD(H): `163` → `136`
    - ResLi(H): `25` → `45`
    - ResCo(H): `125` → `120`
    - ResDm(H): `-` → `25`
    - ResMa(H): `-` → `0`
- `clawviper2Crypt` — ClawViper
    - MinHP(H): `119` → `206`
    - MaxHP(H): `159` → `275`
    - A1MinD(H): `70` → `95`
    - A1MaxD(H): `101` → `136`
    - ResCo(H): `-` → `50`
    - ResDm(H): `60` → `40`
    - ResMa(H): `-` → `45`
    - El1MinD(H): `70` → `95`
    - El1MaxD(H): `90` → `122`
- `flyingscimitarCrypt` — FlyingScimitar
    - MinHP(H): `149` → `258`
    - MaxHP(H): `179` → `310`
    - A1MinD(H): `101` → `136`
    - A1MaxD(H): `151` → `204`
    - ResCo(H): `-` → `20`
    - ResMa(H): `50` → `20`

### Ruined Cistern Map (id 174)

**Stat changes:**

- `blunderbore2Cistern` — Gorbelly
    - MinHP(H): `393` → `314`
    - MaxHP(H): `485` → `388`
    - ResPo(H): `0` → `45`
    - ResMa(H): `0` → `25`
- `clawviper3Cistern` — Salamander
    - MinHP(H): `172` → `138`
    - MaxHP(H): `253` → `202`
    - ResFi(H): `50` → `55`
    - ResLi(H): `0` → `45`
    - ResCo(H): `115` → `75`
    - ResPo(H): `0` → `65`
    - ResDm(H): `0` → `25`
- `corruptrogue2Cistern` — VileHunter
    - MinHP(H): `138` → `110`
    - MaxHP(H): `305` → `244`
    - ResFi(H): `45` → `50`
    - ResPo(H): `0` → `25`
- `mummy1Cistern` — DriedCorpse
    - MinHP(H): `230` → `184`
    - MaxHP(H): `321` → `257`
    - ResFi(H): `0` → `25`
    - ResPo(H): `75` → `120`
    - ResMa(H): `0` → `35`
- `skmage_ltng1Cistern` — ReturnedMage
    - MinHP(H): `126` → `101`
    - MaxHP(H): `200` → `160`
    - ResLi(H): `135` → `75`
    - ResDm(H): `33` → `35`
    - ResMa(H): `0` → `25`
- `frogdemon2Cistern` — Bog Creature
    - MinHP(H): `263` → `210`
    - MaxHP(H): `331` → `265`
    - ResLi(H): `0` → `45`
    - ResMa(H): `0` → `35`
- `cr_archer2Cistern` — VileArcher
    - MinHP(H): `126` → `101`
    - MaxHP(H): `218` → `174`
    - ResDm(H): `0` → `15`
- `fingermage2Cistern` — Strangler
    - MinHP(H): `194` → `155`
    - MaxHP(H): `263` → `210`
    - ResFi(H): `25` → `50`
    - ResCo(H): `0` → `75`
    - ResMa(H): `125` → `105`
- `lernaeanhydra1` — CisternBoss
    - MinHP(H): `6800` → `5000`
    - MaxHP(H): `6800` → `5000`
- `lernaeanhydra2` — CisternBoss
    - MinHP(H): `7500` → `5500`
    - MaxHP(H): `7500` → `5500`

### Ashen Plains Map (id 175)

**Stat changes:**

- `baboon4Ash` — DoomApe
    - MinHP(H): `227` → `182`
    - MaxHP(H): `341` → `273`
    - A1MinD(H): `60` → `72`
    - A1MaxD(H): `156` → `187`
    - A2MinD(H): `60` → `72`
    - A2MaxD(H): `132` → `187`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `25`
- `thornhulk3Ash` — Thrasher
    - MinHP(H): `440` → `352`
    - MaxHP(H): `541` → `433`
    - A1MinD(H): `108` → `130`
    - A1MaxD(H): `192` → `230`
    - A2MinD(H): `90` → `130`
    - A2MaxD(H): `180` → `230`
    - ResFi(H): `-` → `0`
    - ResPo(H): `130` → `75`
    - ResMa(H): `-` → `0`
- `pantherwoman6Ash` — SaberCat
    - MinHP(H): `152` → `122`
    - MaxHP(H): `252` → `202`
    - A1MinD(H): `60` → `72`
    - A1MaxD(H): `108` → `130`
    - ResCo(H): `50` → `65`
- `foulcrow3Ash` — BlackRaptor
    - MinHP(H): `167` → `134`
    - MaxHP(H): `194` → `155`
    - A1MinD(H): `84` → `101`
    - A1MaxD(H): `132` → `158`
    - ResLi(H): `-` → `50`
    - ResPo(H): `-` → `65`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `45`
- `fetish3Ash` — Flayer
    - MinHP(H): `139` → `111`
    - MaxHP(H): `202` → `162`
    - A1MinD(H): `72` → `86`
    - A1MaxD(H): `114` → `137`
    - ResMa(H): `-` → `15`
- `slinger2Ash` — SpearCat
    - MinHP(H): `139` → `111`
    - MaxHP(H): `205` → `164`
    - A1MinD(H): `60` → `72`
    - A1MaxD(H): `102` → `122`
    - ResLi(H): `-` → `75`
    - ResCo(H): `50` → `65`
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `15`
- `deathmauler4Ash` — Death Mauler4
    - MinHP(H): `292` → `234`
    - MaxHP(H): `366` → `293`
    - A1MinD(H): `90` → `108`
    - A1MaxD(H): `168` → `202`
    - ResFi(H): `75` → `120`
    - ResCo(H): `-` → `30`
    - ResPo(H): `-` → `50`
    - ResMa(H): `120` → `50`
- `willowisp8Ash` — BurningSoul
    - MinHP(H): `114` → `91`
    - MaxHP(H): `215` → `172`
    - ResFi(H): `-` → `45`
    - ResLi(H): `80` → `50`
    - ResPo(H): `85` → `60`
    - ResMa(H): `50` → `25`
- `AshenBoss` — AshenBoss
    - MinHP(H): `7250` → `5800`
    - MaxHP(H): `7250` → `5800`

### Zhar Library (id 176)

**Stat changes:**

- `baboon4Ash` — DoomApe
    - MinHP(H): `227` → `182`
    - MaxHP(H): `341` → `273`
    - A1MinD(H): `60` → `72`
    - A1MaxD(H): `156` → `187`
    - A2MinD(H): `60` → `72`
    - A2MaxD(H): `132` → `187`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `25`
- `thornhulk3Ash` — Thrasher
    - MinHP(H): `440` → `352`
    - MaxHP(H): `541` → `433`
    - A1MinD(H): `108` → `130`
    - A1MaxD(H): `192` → `230`
    - A2MinD(H): `90` → `130`
    - A2MaxD(H): `180` → `230`
    - ResFi(H): `-` → `0`
    - ResPo(H): `130` → `75`
    - ResMa(H): `-` → `0`
- `pantherwoman6Ash` — SaberCat
    - MinHP(H): `152` → `122`
    - MaxHP(H): `252` → `202`
    - A1MinD(H): `60` → `72`
    - A1MaxD(H): `108` → `130`
    - ResCo(H): `50` → `65`
- `foulcrow3Ash` — BlackRaptor
    - MinHP(H): `167` → `134`
    - MaxHP(H): `194` → `155`
    - A1MinD(H): `84` → `101`
    - A1MaxD(H): `132` → `158`
    - ResLi(H): `-` → `50`
    - ResPo(H): `-` → `65`
    - ResDm(H): `-` → `0`
    - ResMa(H): `-` → `45`
- `fetish3Ash` — Flayer
    - MinHP(H): `139` → `111`
    - MaxHP(H): `202` → `162`
    - A1MinD(H): `72` → `86`
    - A1MaxD(H): `114` → `137`
    - ResMa(H): `-` → `15`
- `slinger2Ash` — SpearCat
    - MinHP(H): `139` → `111`
    - MaxHP(H): `205` → `164`
    - A1MinD(H): `60` → `72`
    - A1MaxD(H): `102` → `122`
    - ResLi(H): `-` → `75`
    - ResCo(H): `50` → `65`
    - ResPo(H): `-` → `25`
    - ResMa(H): `-` → `15`
- `deathmauler4Ash` — Death Mauler4
    - MinHP(H): `292` → `234`
    - MaxHP(H): `366` → `293`
    - A1MinD(H): `90` → `108`
    - A1MaxD(H): `168` → `202`
    - ResFi(H): `75` → `120`
    - ResCo(H): `-` → `30`
    - ResPo(H): `-` → `50`
    - ResMa(H): `120` → `50`
- `willowisp8Ash` — BurningSoul
    - MinHP(H): `114` → `91`
    - MaxHP(H): `215` → `172`
    - ResFi(H): `-` → `45`
    - ResLi(H): `80` → `50`
    - ResPo(H): `85` → `60`
    - ResMa(H): `50` → `25`

### Skovos Stronghold Map (id 190)

**Stat changes:**

- `corruptrogue2Skovos` — VileHunter
    - MinHP(H): `190` → `238`
    - MaxHP(H): `246` → `308`
    - A1MinD(H): `112` → `128`
    - A1MaxD(H): `183` → `209`
- `cr_archer2Skovos` — VileArcher
    - MinHP(H): `171` → `214`
    - MaxHP(H): `218` → `273`
    - A1MinD(H): `131` → `149`
    - A1MaxD(H): `171` → `195`
    - ResLi(H): `0` → `55`
    - ResCo(H): `85` → `120`
    - El1MinD(H): `65` → `74`
    - El1MaxD(H): `65` → `74`
- `cr_lancer2Skovos` — VileLancer
    - MinHP(H): `228` → `285`
    - MaxHP(H): `274` → `343`
    - A1MinD(H): `126` → `144`
    - A1MaxD(H): `209` → `238`
    - ResLi(H): `20` → `40`
    - ResCo(H): `0` → `50`
    - ResDm(H): `15` → `25`
    - El1MinD(H): `90` → `103`
    - El1MaxD(H): `90` → `103`
- `deathmauler3Skovos` — Death Mauler3
    - MinHP(H): `198` → `248`
    - MaxHP(H): `292` → `365`
    - A1MinD(H): `171` → `195`
    - A1MaxD(H): `231` → `263`
    - ResFi(H): `125` → `75`
    - ResPo(H): `0` → `65`
    - ResMa(H): `20` → `35`
- `bighead6Skovos` — Afflicted
    - MinHP(H): `108` → `135`
    - MaxHP(H): `152` → `190`
    - A1MinD(H): `56` → `64`
    - A1MaxD(H): `112` → `128`
    - ResCo(H): `0` → `40`
- `mummy1Skovos` — DriedCorpse
    - MinHP(H): `110` → `138`
    - MaxHP(H): `154` → `193`
    - A1MinD(H): `67` → `76`
    - A1MaxD(H): `117` → `133`
    - ResFi(H): `0` → `75`
    - ResPo(H): `85` → `120`
    - ResDm(H): `125` → `55`
    - ResMa(H): `10` → `40`
    - El1MinD(H): `33` → `38`
    - El1MaxD(H): `33` → `38`
- `thornhulk2Skovos` — BrambleHulk
    - MinHP(H): `209` → `261`
    - MaxHP(H): `253` → `316`
    - A1MinD(H): `101` → `115`
    - A1MaxD(H): `179` → `204`
    - A2MinD(H): `94` → `107`
    - A2MaxD(H): `188` → `214`
    - ResFi(H): `0` → `15`
    - ResLi(H): `130` → `75`
    - ResMa(H): `20` → `25`
- `InvaderAmazon` — InvaderAmazon
    - MinHP(H): `6750` → `5000`
    - MaxHP(H): `6750` → `5000`
    - A1MinD(H): `60` → `25`
    - A1MaxD(H): `75` → `40`
- `InvaderAssassin` — InvaderAssassin
    - MinHP(H): `7000` → `5600`
    - MaxHP(H): `7000` → `5600`
    - A1MinD(H): `35` → `10`
    - A1MaxD(H): `55` → `20`
- `InvaderBarbarian` — InvaderBarbarian
    - MinHP(H): `7500` → `6000`
    - MaxHP(H): `7500` → `6000`
    - A1MinD(H): `50` → `20`
    - A1MaxD(H): `65` → `60`
- `InvaderDruid` — InvaderDruid
    - MinHP(H): `6500` → `5200`
    - MaxHP(H): `6500` → `5200`
- `InvaderNecromancer` — InvaderNecromancer
    - MinHP(H): `6750` → `5400`
    - MaxHP(H): `6750` → `5400`
- `InvaderPaladin` — InvaderPaladin
    - MinHP(H): `7000` → `5600`
    - MaxHP(H): `7000` → `5600`
    - A1MinD(H): `35` → `8`
    - A1MaxD(H): `50` → `12`
- `InvaderSorceress` — InvaderSorceress
    - MinHP(H): `6500` → `5200`
    - MaxHP(H): `6500` → `5200`
- `SkovosBoss` — SkovosBoss
    - MinHP(H): `6650` → `6850`
    - MaxHP(H): `6650` → `6850`
- `zealot2SkovosBoss` — Faithful
    - MinHP(H): `740` → `925`
    - MaxHP(H): `860` → `1075`
    - A1MinD(H): `60` → `75`
    - A1MaxD(H): `106` → `133`
    - A2MinD(H): `106` → `133`
    - A2MaxD(H): `176` → `220`

### Demon Road Map (id 191)

**Stat changes:**

- `wraith3DemonRoad` — Specter
    - MinHP(H): `137` → `170`
    - MaxHP(H): `182` → `226`
    - A1MinD(H): `93` → `106`
    - A1MaxD(H): `163` → `187`
    - ResFi(H): `0` → `35`
    - ResLi(H): `0` → `45`
- `goatman3DemonRoad` — NightClan
    - MinHP(H): `180` → `223`
    - MaxHP(H): `234` → `290`
    - A1MinD(H): `109` → `125`
    - A1MaxD(H): `194` → `222`
    - ResFi(H): `0` → `50`
    - ResCo(H): `0` → `75`
    - ResPo(H): `0` → `25`
    - ResDm(H): `45` → `25`
    - El1MinD(H): `15` → `112`
    - El1MaxD(H): `85` → `198`
- `skmage_fire1DemonRoad` — ReturnedMage
    - MinHP(H): `129` → `160`
    - MaxHP(H): `174` → `216`
    - ResFi(H): `85` → `120`
    - ResMa(H): `10` → `15`
    - El1MinD(H): `70` → `76`
    - El1MaxD(H): `170` → `198`
- `succubus4DemonRoad` — Hell Temptress
    - MinHP(H): `108` → `134`
    - MaxHP(H): `162` → `201`
    - A1MinD(H): `78` → `89`
    - A1MaxD(H): `140` → `160`
    - ResPo(H): `25` → `35`
    - ResMa(H): `0` → `25`
    - El1MinD(H): `40` → `227`
    - El1MaxD(H): `75` → `292`
- `blunderbore2DemonRoad` — Gorbelly
    - MinHP(H): `284` → `352`
    - MaxHP(H): `356` → `441`
    - A1MinD(H): `140` → `160`
    - A1MaxD(H): `217` → `248`
    - A2MinD(H): `173` → `198`
    - A2MaxD(H): `223` → `255`
    - ResLi(H): `50` → `65`
    - ResCo(H): `125` → `75`
    - ResDm(H): `45` → `25`
    - ResMa(H): `0` → `25`
    - El1MinD(H): `-` → `112`
    - El1MaxD(H): `-` → `198`
- `clawviper1DemonRoad` — TombViper
    - MinHP(H): `135` → `167`
    - MaxHP(H): `198` → `246`
    - A1MinD(H): `93` → `106`
    - A1MaxD(H): `124` → `142`
    - A2MinD(H): `86` → `98`
    - A2MaxD(H): `151` → `173`
    - ResLi(H): `20` → `35`
    - ResPo(H): `0` → `50`
    - ResDm(H): `40` → `15`
    - El1MinD(H): `60` → `-`
    - El1MaxD(H): `70` → `-`
- `unraveler1DemonRoad` — HollowOne
    - MinHP(H): `271` → `336`
    - MaxHP(H): `343` → `425`
    - A1MinD(H): `171` → `196`
    - A1MaxD(H): `217` → `248`
    - ResLi(H): `85` → `120`
    - ResDm(H): `35` → `115`
    - El1MinD(H): `33` → `-`
    - El1MaxD(H): `33` → `-`
- `skeleton2DemonRoad` — Returned
    - MinHP(H): `150` → `186`
    - MaxHP(H): `195` → `242`
    - A1MinD(H): `62` → `71`
    - A1MaxD(H): `155` → `177`
    - A2MinD(H): `58` → `66`
    - A2MaxD(H): `151` → `173`
    - ResPo(H): `135` → `75`
    - El1MinD(H): `-` → `227`
    - El1MaxD(H): `-` → `292`
- `DemonRoadBoss` — DemonRoadBoss
    - MinHP(H): `6500` → `7000`
    - MaxHP(H): `6500` → `7000`
    - A1MinD(H): `150` → `172`
    - A1MaxD(H): `250` → `286`

### Imperial Palace Map (id 192)

**Stat changes:**

- `leoricGuards` — LeoricGuards
    - MinHP(H): `140` → `450`
    - MaxHP(H): `180` → `600`
- `leoricMapBoss` — LeoricBoss
    - MinHP(H): `4250` → `6750`
    - MaxHP(H): `4250` → `6750`
    - A1MinD(H): `120` → `160`
    - A1MaxD(H): `160` → `200`
    - A2MinD(H): `120` → `160`
    - A2MaxD(H): `160` → `200`

### Halls of Torture Map (id 193)

**Stat changes:**

- `sandleaper3TortureHalls` — TombCreeper
    - ResFi(H): `25` → `50`
    - ResPo(H): `35` → `45`
- `zealot1TortureHalls` — Zakarumite
    - ResLi(H): `85` → `120`
    - ResCo(H): `35` → `45`
- `sk_archer2TortureHalls` — ReturnedArcher
    - ResLi(H): `0` → `25`
    - ResCo(H): `85` → `120`
- `blunderbore1TortureHalls` — Blunderbore
    - ResPo(H): `0` → `25`
- `vampire3TortureHalls` — DarkLord
    - ResFi(H): `85` → `75`
    - ResLi(H): `25` → `45`
- `councilmember3TortureHalls` — Council Member
    - ResFi(H): `25` → `35`
    - ResLi(H): `65` → `75`
    - ResMa(H): `0` → `25`
- `regurgitator1TortureHalls` — Corpulent
    - ResFi(H): `0` → `25`
    - ResCo(H): `0` → `45`
- `TortureHallsBoss` — TortureHallsBoss
    - MinHP(H): `4800` → `6350`
    - MaxHP(H): `4800` → `6350`
    - A1MinD(H): `85` → `99`
    - A1MaxD(H): `140` → `164`
    - A2MinD(H): `60` → `70`
    - A2MaxD(H): `125` → `146`

### Djinns Domain Boss Map (id 199)

**Stat changes:**

- `flyingscimitarArcane` — FlyingScimitar
    - MinHP(H): `105` → `142`
    - MaxHP(H): `158` → `213`
    - A1MinD(H): `101` → `136`
    - A1MaxD(H): `140` → `189`
    - ResLi(H): `80` → `120`
    - ResCo(H): `-` → `75`

## Other monster changes (shared / unassigned)

- `fetish2ruins` (added) — Fetish Lv79
- `fetishblow2ruins` (added) — Fetish Lv79
- `imp1phlegethon` (added) — Imp1 Lv80
- `megademonboss` — Megademon Boss
    - MinHP(H): `7600` → `5500`
    - MaxHP(H): `7600` → `5500`
- `skeleton2ruins` — Returned
    - ResFi(H): `-` → `25`
    - ResLi(H): `-` → `35`
    - ResCo(H): `-` → `75`
    - ResMa(H): `-` → `25`
- `succubuswitchmap` — VileWitch
    - MinHP(H): `119` → `92`
    - MaxHP(H): `159` → `122`
- `unravelerboss` — Unraveler Boss
    - MinHP(H): `3600` → `3400`
    - MaxHP(H): `3600` → `3400`
    - A1MinD(H): `110` → `100`
    - A1MaxD(H): `140` → `130`
- `unravelerbossskeleton` — BurningDead
    - A1MinD(H): `61` → `60`
    - A1MaxD(H): `97` → `90`
