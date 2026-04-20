"""Convert Levels.txt and MonStats.txt to JSON for the web viewer."""
import csv
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def parse_tsv(filename):
    rows = []
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            rows.append(row)
    return rows

def safe_int(val, default=0):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

LEVEL_NAME_OVERRIDES = {
    139: "Arreat Battlefield",
    141: "Sewers of Harrogath",
    142: "Horazon's Memory",
    143: "Ruins of Viz-jun",
    144: "River of Blood",
    145: "Phlegethon",
    146: "Ancestral Trial",
    147: "Kehjistan Marketplace",
    148: "Torajan Jungle",
    149: "Bastion Keep",
    150: "Throne of Insanity",
    151: "Tomb of Zoltun Kulle",
    152: "Cathedral of Light",
    154: "Blood Moon",
    155: "Fall of Caldeum",
    156: "Pandemonium Citadel",
    158: "Lost Temple",
    160: "Canyon of Sescheron",
    164: "Plains of Torment",
    167: "Sanatorium",
    169: "Shadows of Westmarch",
    170: "Royal Crypts",
    171: "Sanctuary of Sin",
    174: "Ruined Cistern",
    175: "Ashen Plains",
    177: "Zhar Rivers",
    178: "Zhar Ice",
    179: "Zhar Kurast",
    180: "Outer Void",
    181: "Hellcaves",
    183: "Fallen Gardens",
    186: "Steppes of Daken-Shar",
    190: "Skovos Stronghold",
    191: "Demon Road",
    192: "Imperial Palace",
    193: "Halls of Torture",
    195: "City of Ureh",
    # Boss / sub-zone overrides
    137: "Uber Diablo",
    153: "Cathedral of Light (Basement)",
    161: "Necropolis - Jungle",
    162: "Necropolis - Swamp",
    163: "Necropolis - Void",
    165: "Hole of Terror",
    168: "Uber Ancients",
    172: "Black Abyss",
    173: "Butcher's Lair",
    176: "Zhar's Sanctum",
    182: "Hellcave Fortress",
    184: "Diamond Gate",
    185: "Pandemonium Finale",
    187: "Kanemith Dungeon",
    188: "Lucion Arena",
    189: "Lucion Vault",
    194: "Imperial Boss Arena",
    196: "Nemyr Monastery",
    197: "Djinns Domain",
    198: "Djinns Domain (Red)",
    199: "Djinns Domain (Boss)",
    200: "Na-Krul's Abyss",
    201: "Kyovoshad",
}

def convert_levels():
    rows = parse_tsv("Levels.txt")
    levels = []
    for row in rows:
        level_id = safe_int(row.get("Id"))
        name = LEVEL_NAME_OVERRIDES.get(level_id, row.get("Name", "").strip())
        if not name or name == "Null" or level_id == 0:
            continue

        # Collect nightmare/hell monster ids (nmon columns) - these are used in NM and Hell
        nmons = []
        for i in range(1, 26):
            m = row.get(f"nmon{i}", "").strip()
            if m:
                nmons.append(m)

        # Normal monsters (mon columns)
        mons = []
        for i in range(1, 26):
            m = row.get(f"mon{i}", "").strip()
            if m:
                mons.append(m)

        # Unique/champion monsters
        umons = []
        for i in range(1, 26):
            m = row.get(f"umon{i}", "").strip()
            if m:
                umons.append(m)

        level = {
            "id": level_id,
            "name": name,
            "act": safe_int(row.get("Act")),
            "levelName": row.get("LevelName", "").strip(),
            "sizeX_H": safe_int(row.get("SizeX(H)")),
            "sizeY_H": safe_int(row.get("SizeY(H)")),
            "teleport": safe_int(row.get("Teleport")),
            "isInside": safe_int(row.get("IsInside")),
            "monLvl_H": safe_int(row.get("MonLvl3")),
            "monLvlEx_H": safe_int(row.get("MonLvl3Ex")),
            "monDen_H": safe_int(row.get("MonDen(H)")),
            "monUMin_H": safe_int(row.get("MonUMin(H)")),
            "monUMax_H": safe_int(row.get("MonUMax(H)")),
            "monsters_normal": mons,
            "monsters_hell": nmons if nmons else mons,
            "monsters_unique": umons,
            "waypoint": safe_int(row.get("Waypoint"), 255),
        }
        levels.append(level)
    return levels

def convert_monstats():
    rows = parse_tsv("MonStats.txt")
    monsters = {}
    for row in rows:
        mon_id = row.get("Id", "").strip()
        if not mon_id:
            continue
        enabled = row.get("enabled", "").strip()
        if enabled == "0":
            continue

        monster = {
            "id": mon_id,
            "nameStr": row.get("NameStr", "").strip(),
            "baseId": row.get("BaseId", "").strip(),
            "code": row.get("Code", "").strip(),
            "enabled": safe_int(enabled),
            "rangedtype": safe_int(row.get("rangedtype")),
            "level_H": safe_int(row.get("Level(H)")),
            "minHP_H": safe_int(row.get("MinHP(H)")),
            "maxHP_H": safe_int(row.get("MaxHP(H)")),
            "ac_H": safe_int(row.get("AC(H)")),
            "exp_H": safe_int(row.get("Exp(H)")),
            "a1MinD_H": safe_int(row.get("A1MinD(H)")),
            "a1MaxD_H": safe_int(row.get("A1MaxD(H)")),
            "a1TH_H": safe_int(row.get("A1TH(H)")),
            "a2MinD_H": safe_int(row.get("A2MinD(H)")),
            "a2MaxD_H": safe_int(row.get("A2MaxD(H)")),
            "a2TH_H": safe_int(row.get("A2TH(H)")),
            "s1MinD_H": safe_int(row.get("S1MinD(H)")),
            "s1MaxD_H": safe_int(row.get("S1MaxD(H)")),
            "s1TH_H": safe_int(row.get("S1TH(H)")),
            "resDm_H": safe_int(row.get("ResDm(H)")),
            "resMa_H": safe_int(row.get("ResMa(H)")),
            "resFi_H": safe_int(row.get("ResFi(H)")),
            "resLi_H": safe_int(row.get("ResLi(H)")),
            "resCo_H": safe_int(row.get("ResCo(H)")),
            "resPo_H": safe_int(row.get("ResPo(H)")),
            "drain": safe_int(row.get("Drain")),
            "drain_N": safe_int(row.get("Drain(N)")),
            "drain_H": safe_int(row.get("Drain(H)")),
            "coldeffect_H": safe_int(row.get("coldeffect(H)")),
            "lUndead": safe_int(row.get("lUndead")),
            "hUndead": safe_int(row.get("hUndead")),
            "demon": safe_int(row.get("demon")),
            "boss": safe_int(row.get("boss")),
            "primeevil": safe_int(row.get("primeevil")),
            "velocity": safe_int(row.get("Velocity")),
            "run": safe_int(row.get("Run")),
            "toBlock_H": safe_int(row.get("ToBlock(H)")),
            "el1Type": row.get("El1Type", "").strip(),
            "el1MinD_H": safe_int(row.get("El1MinD(H)")),
            "el1MaxD_H": safe_int(row.get("El1MaxD(H)")),
            "el1Dur_H": safe_int(row.get("El1Dur(H)")),
            "el1Pct_H": safe_int(row.get("El1Pct(H)")),
            "el2Type": row.get("El2Type", "").strip(),
            "el2MinD_H": safe_int(row.get("El2MinD(H)")),
            "el2MaxD_H": safe_int(row.get("El2MaxD(H)")),
            "el2Dur_H": safe_int(row.get("El2Dur(H)")),
            "el2Pct_H": safe_int(row.get("El2Pct(H)")),
            "el3Type": row.get("El3Type", "").strip(),
            "el3MinD_H": safe_int(row.get("El3MinD(H)")),
            "el3MaxD_H": safe_int(row.get("El3MaxD(H)")),
            "el3Dur_H": safe_int(row.get("El3Dur(H)")),
            "el3Pct_H": safe_int(row.get("El3Pct(H)")),
            "tc_H": row.get("TreasureClass1(H)", "").strip(),
            "tcChamp_H": row.get("TreasureClass2(H)", "").strip(),
            "tcUnique_H": row.get("TreasureClass3(H)", "").strip(),
            "tcQuest_H": row.get("TreasureClass4(H)", "").strip(),
            "exp": safe_int(row.get("Exp")),
        }
        monsters[mon_id] = monster
    return monsters

def convert_monlvl():
    """Parse MonLvl.txt and return a dict of level -> L-HP(H) scaling factor."""
    rows = parse_tsv("MonLvl.txt")
    monlvl = {}
    for row in rows:
        lvl = safe_int(row.get("Level"))
        monlvl[lvl] = {
            "hp_H": safe_int(row.get("HP(H)")),
            "lhp_H": safe_int(row.get("L-HP(H)")),
        }
    return monlvl

if __name__ == "__main__":
    levels = convert_levels()
    monsters = convert_monstats()
    monlvl = convert_monlvl()

    with open(os.path.join(DATA_DIR, "levels.js"), "w", encoding="utf-8") as f:
        f.write("const levelsData = ")
        json.dump(levels, f, separators=(",", ":"))
        f.write(";\n")

    with open(os.path.join(DATA_DIR, "monstats.js"), "w", encoding="utf-8") as f:
        f.write("const monstersData = ")
        json.dump(monsters, f, separators=(",", ":"))
        f.write(";\n")

    with open(os.path.join(DATA_DIR, "monlvl.js"), "w", encoding="utf-8") as f:
        f.write("const monLvlData = ")
        json.dump(monlvl, f, separators=(",", ":"))
        f.write(";\n")

    print(f"Converted {len(levels)} levels, {len(monsters)} monsters, {len(monlvl)} MonLvl entries to JS.")
