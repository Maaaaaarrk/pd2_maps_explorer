"""Generate MAP_HEALTH.md: per-map (tier 1-3) min/max/avg mob HP for Hell difficulty.

HP is scaled the same way the in-app `realHP()` function does it:
    realHP = floor(baseHP * monLvl[areaLvl].lhp_H / 100)
where areaLvl is the level's monLvlEx_H (or monLvl_H fallback).
"""
import csv
import os

REPO = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO, "data")

# Tier groupings copied from data/tiers.js (tiers 1-3).
TIERS = [
    ("Tier 1", 87, [
        (143, "Ruins of Viz-Jun"),
        (145, "Phlegethon"),
        (146, "Ancestral Trial"),
        (148, "Torajan Jungle"),
        (151, "Tomb of Zoltun Kulle"),
        (155, "Fall of Caldeum"),
        (158, "Lost Temple"),
        (169, "Shadows of Westmarch"),
    ]),
    ("Tier 2", 88, [
        (141, "Sewers of Harrogath"),
        (142, "Horazon's Memory"),
        (150, "Throne of Insanity"),
        (156, "Pandemonium Citadel"),
        (160, "Canyon of Sescheron"),
        (167, "Sanatorium"),
        (174, "Ruined Cistern"),
        (175, "Ashen Plains"),
        (193, "Halls of Torture"),
    ]),
    ("Tier 3", 89, [
        (139, "Arreat Battlefield"),
        (144, "River of Blood"),
        (147, "Kehjistan Marketplace"),
        (149, "Bastion Keep"),
        (154, "Blood Moon"),
        (170, "Royal Crypts"),
        (190, "Skovos Stronghold"),
        (191, "Demon Road"),
        (201, "Kyovoshad"),
    ]),
]


def safe_int(v, default=0):
    try:
        return int(v)
    except (ValueError, TypeError):
        return default


def parse_tsv(filename):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_levels():
    levels = {}
    for row in parse_tsv("Levels.txt"):
        lid = safe_int(row.get("Id"))
        if lid == 0:
            continue
        nmons = [row.get(f"nmon{i}", "").strip() for i in range(1, 26)]
        nmons = [m for m in nmons if m]
        mons = [row.get(f"mon{i}", "").strip() for i in range(1, 26)]
        mons = [m for m in mons if m]
        levels[lid] = {
            "monsters": nmons if nmons else mons,
            "monLvl_H": safe_int(row.get("MonLvl3")),
            "monLvlEx_H": safe_int(row.get("MonLvl3Ex")),
        }
    return levels


def load_monstats():
    monsters = {}
    for row in parse_tsv("MonStats.txt"):
        mid = row.get("Id", "").strip()
        if not mid:
            continue
        if row.get("enabled", "").strip() == "0":
            continue
        monsters[mid] = {
            "nameStr": row.get("NameStr", "").strip(),
            "minHP_H": safe_int(row.get("MinHP(H)")),
            "maxHP_H": safe_int(row.get("MaxHP(H)")),
        }
    return monsters


def load_monlvl():
    out = {}
    for row in parse_tsv("MonLvl.txt"):
        lvl = safe_int(row.get("Level"))
        out[lvl] = safe_int(row.get("L-HP(H)"))
    return out


def real_hp(base_hp, area_lvl, monlvl):
    factor = monlvl.get(area_lvl)
    if factor is None or factor == 0:
        return base_hp
    return (base_hp * factor) // 100


def compute_map_stats(level_id, levels, monsters, monlvl):
    lvl = levels.get(level_id)
    if not lvl:
        return None
    area = lvl["monLvlEx_H"] or lvl["monLvl_H"]
    pool = []
    for mid in lvl["monsters"]:
        m = monsters.get(mid)
        if not m:
            continue
        if m["minHP_H"] == 0 and m["maxHP_H"] == 0:
            continue
        min_hp = real_hp(m["minHP_H"], area, monlvl)
        max_hp = real_hp(m["maxHP_H"], area, monlvl)
        pool.append((mid, m["nameStr"], min_hp, max_hp))
    if not pool:
        return None
    overall_min = min(p[2] for p in pool)
    overall_max = max(p[3] for p in pool)
    # Average of each monster's mid-HP, across the pool.
    avg = sum((p[2] + p[3]) / 2 for p in pool) / len(pool)
    return {
        "areaLvl": area,
        "min": overall_min,
        "max": overall_max,
        "avg": int(round(avg)),
        "poolSize": len(pool),
    }


def fmt(n):
    return f"{n:,}"


def main():
    levels = load_levels()
    monsters = load_monstats()
    monlvl = load_monlvl()

    out = []
    out.append("# Map Mob HP Survey (Tiers 1–3)\n")
    out.append(
        "Per-map Hell-difficulty mob HP across the regular spawn pool "
        "(`nmon`/`mon` from Levels.txt). HP is scaled to the area's monster "
        "level using the same formula as the in-app viewer:\n"
    )
    out.append("```")
    out.append("realHP = floor(baseHP * MonLvl[areaLvl].L-HP(H) / 100)")
    out.append("```\n")
    out.append(
        "- **Min HP** — lowest `MinHP(H)` (scaled) in the pool\n"
        "- **Max HP** — highest `MaxHP(H)` (scaled) in the pool\n"
        "- **Avg HP** — mean of each monster's mid-HP `(minHP+maxHP)/2`, averaged across the pool\n"
        "- **Mob Count** — number of distinct enabled monsters contributing to the stats\n"
    )

    headers = ["Map", "Area Lvl", "Min HP", "Max HP", "Avg HP", "Mob Count"]
    aligns = ["left", "right", "right", "right", "right", "right"]

    for tier_label, zone_lvl, maps in TIERS:
        rows = []
        for lid, name in sorted(maps, key=lambda x: x[1]):
            s = compute_map_stats(lid, levels, monsters, monlvl)
            if s is None:
                rows.append([name, "—", "—", "—", "—", "0"])
            else:
                rows.append([
                    name,
                    str(s["areaLvl"]),
                    fmt(s["min"]),
                    fmt(s["max"]),
                    fmt(s["avg"]),
                    str(s["poolSize"]),
                ])

        widths = [
            max(len(headers[i]), max((len(r[i]) for r in rows), default=0))
            for i in range(len(headers))
        ]

        def pad(cell, w, align):
            return cell.ljust(w) if align == "left" else cell.rjust(w)

        def fmt_row(cells):
            return "| " + " | ".join(pad(c, widths[i], aligns[i]) for i, c in enumerate(cells)) + " |"

        sep_cells = []
        for i, w in enumerate(widths):
            cell_w = max(3, w + 2)
            if aligns[i] == "left":
                sep_cells.append("-" * cell_w)
            else:
                sep_cells.append("-" * (cell_w - 1) + ":")
        sep_row = "|" + "|".join(sep_cells) + "|"

        out.append(f"\n## {tier_label} (zone level {zone_lvl})\n")
        out.append(fmt_row(headers))
        out.append(sep_row)
        for r in rows:
            out.append(fmt_row(r))

    out.append("")
    text = "\n".join(out)
    with open(os.path.join(REPO, "MAP_HEALTH.md"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
