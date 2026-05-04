"""Regenerate MAP_RESISTANCES.md from current data/Levels.txt and data/MonStats.txt."""
import csv
import os

REPO = os.path.dirname(os.path.abspath(__file__))

SURVEY = [
    ("Tier 1", "t11", "Ruins of Viz-Jin", [143]),
    ("Tier 1", "t21", "Phlegethon", [145]),
    ("Tier 1", "t34", "Ancestral Trial", [146]),
    ("Tier 1", "t22", "Torajan Jungle", [148]),
    ("Tier 1", "t24", "Tomb of Zoltun Kulle", [151]),
    ("Tier 1", "t36", "Fall of Caldeum", [155]),
    ("Tier 1", "t33", "Lost Temple", [158]),
    ("Tier 1", "t26", "Shadows of Westmarch", [169]),
    ("Tier 2", "t25", "Sewers of Harrogath", [141]),
    ("Tier 2", "t12", "Horazon's Memory", [142]),
    ("Tier 2", "t32", "Throne of Insanity", [150]),
    ("Tier 2", "t37", "Pandemonium Citadel", [156]),
    ("Tier 2", "t38", "Canyon of Sescheron", [160]),
    ("Tier 2", "t14", "Sanatorium", [167]),
    ("Tier 2", "t16", "Ruined Cistern", [174]),
    ("Tier 2", "t3a", "Ashen Plains", [175]),
    ("Tier 2", "t17", "Halls of Torture", [193]),
    ("Tier 3", "t23", "Arreat Battlefield", [139]),
    ("Tier 3", "t31", "River of Blood", [144]),
    ("Tier 3", "t39", "Kehjistan Marketplace", [147]),
    ("Tier 3", "t13", "Bastion Keep", [149]),
    ("Tier 3", "t35", "Blood Moon", [154]),
    ("Tier 3", "t15", "Royal Crypts", [170]),
    ("Tier 3", "t28", "Skovos Stronghold", [190]),
    ("Tier 3", "t27", "Demon Road", [191]),
    ("Tier 3", "t3b", "Kyovoshad", [201]),
    ("Tier 4 — Corrupted maps (`t4x`)", "t41", "Cathedral of Light", [152]),
    ("Tier 4 — Corrupted maps (`t4x`)", "t42", "Plains of Torment", [164]),
    ("Tier 4 — Corrupted maps (`t4x`)", "t43", "Sanctuary of Sin", [171]),
    ("Tier 4 — Corrupted maps (`t4x`)", "t44", "Steppes of Daken-Shar", [186]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t51", "Zhar Rivers", [177]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t51", "Zhar Ice", [178]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t51", "Zhar Kurast", [179]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t51", "Zhar (combined)", [177, 178, 179]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t52", "Hellcaves", [181]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t53", "Fallen Gardens", [183]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t54", "Imperial Palace", [192]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t55", "Outer Void", [180]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t56", "City of Ureh", [195]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t57", "Djinn's Domain", [197, 198, 199]),
    ("Tier 5 — Uber / special maps (`t5x`)", "t58", "Na-Krul's Abyss", [200]),
]

ELEMENTS = [
    ("Fire", "ResFi(H)"),
    ("Cold", "ResCo(H)"),
    ("Light", "ResLi(H)"),
    ("Poison", "ResPo(H)"),
    ("Magic", "ResMa(H)"),
    ("Phys", "ResDm(H)"),
]

TIER_ORDER = [
    "Tier 1",
    "Tier 2",
    "Tier 3",
    "Tier 4 — Corrupted maps (`t4x`)",
    "Tier 5 — Uber / special maps (`t5x`)",
]


def safe_int(v, default=0):
    try:
        return int(v)
    except (ValueError, TypeError):
        return default


def read_file(path):
    with open(os.path.join(REPO, path), encoding="utf-8-sig") as f:
        return f.read()


def load_levels(text):
    levels_by_id = {}
    for row in csv.DictReader(text.splitlines(), delimiter="\t"):
        lid = safe_int(row.get("Id"))
        if lid == 0:
            continue
        nmons = [row.get(f"nmon{i}", "").strip() for i in range(1, 26)]
        nmons = [m for m in nmons if m]
        mons = [row.get(f"mon{i}", "").strip() for i in range(1, 26)]
        mons = [m for m in mons if m]
        umons = [row.get(f"umon{i}", "").strip() for i in range(1, 26)]
        umons = [m for m in umons if m]
        spawn_pool = (nmons if nmons else mons) + umons
        levels_by_id[lid] = spawn_pool
    return levels_by_id


def load_monstats(text):
    monsters = {}
    for row in csv.DictReader(text.splitlines(), delimiter="\t"):
        mid = row.get("Id", "").strip()
        if not mid:
            continue
        if row.get("enabled", "").strip() == "0":
            continue
        monsters[mid] = row
    return monsters


def survey_resistances(levels_by_id, monsters, level_ids):
    pool = []
    for lid in level_ids:
        pool.extend(levels_by_id.get(lid, []))
    result = {}
    for label, col in ELEMENTS:
        best = None
        for mid in pool:
            m = monsters.get(mid)
            if not m:
                continue
            v = safe_int(m.get(col))
            if label == "Poison" and v >= 1000:
                continue
            if best is None or v > best:
                best = v
        result[label] = best
    return result


def fmt_cell(v):
    if v is None:
        return "—"
    s = str(v)
    if v >= 100:
        return f"**{s}**"
    return s


def main():
    levels = load_levels(read_file("data/Levels.txt"))
    mons = load_monstats(read_file("data/MonStats.txt"))

    out = []
    out.append("# Monster Resistance Survey by Map\n")
    out.append(
        "Highest Hell-difficulty resistance value across the regular spawn pool in each "
        "map (monsters referenced via `nmon/mon/umon` in `Levels.txt`). Hardcoded "
        "event/quest bosses are **not** included because their map-association can't be "
        "inferred reliably from naming. Poison resistance values of `1000` (hardcoded "
        '"fully immune" placeholders) are excluded so the listed poison res reflects '
        "what normal spawns actually carry.\n"
    )
    out.append("Values ≥ 100 mean the monster is **immune** to that element.\n")

    by_tier = {}
    for tier, code, name, ids in SURVEY:
        by_tier.setdefault(tier, []).append((code, name, ids))

    for tier in TIER_ORDER:
        entries = by_tier.get(tier, [])
        if not entries:
            continue
        out.append(f"\n## {tier}\n")
        for code, name, ids in entries:
            res = survey_resistances(levels, mons, ids)
            out.append(f"### `{code}` — {name}  ")
            out.append(f"*Level id(s): {', '.join(str(i) for i in ids)}*\n")
            out.append("| Element | Max Res |")
            out.append("|---------|--------:|")
            # Determine column width: max width of formatted values for alignment
            cells = [fmt_cell(res[label]) for label, _ in ELEMENTS]
            width = max(len(c) for c in cells)
            width = max(width, len("Max Res"))
            for (label, _), cell in zip(ELEMENTS, cells):
                out.append(f"| {label:<7} | {cell:>{width}} |")
            out.append("")

    text = "\n".join(out).rstrip() + "\n"
    with open(os.path.join(REPO, "MAP_RESISTANCES.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Wrote MAP_RESISTANCES.md ({len(text)} bytes)")


if __name__ == "__main__":
    main()
