"""Generate T{1,2}_XP_S12_vs_S13.txt: per-tier base-XP comparison between
the S12 and S13 tier rosters, using current (S13) MonStats.

T3 is hand-curated — see T3_XP_S12_vs_S13.txt — so this script only writes
T1 and T2 in the matching format.

Base XP per monster (Hell) = MonLvl.XP(H)[monster.Level(H)] * MonStats.Exp(H) / 100
Per-map value              = mean across the map's nmon Hell spawn pool
Tier average               = mean of per-map averages
"""
import csv
import os

REPO = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO, "data")

# Tier rosters from data/tiers.js history.
# S12: commit 2ca4f9e (Add Djinns Domain, Na-Krul's Abyss, and Kyovoshad).
# S13: current data/tiers.js (commit 4bb6996 Reorganize map tiers).
S12_TIERS = {
    1: [
        (139, "Arreat Battlefield"),
        (155, "Fall of Caldeum"),
        (193, "Halls of Torture"),
        (142, "Horazon's Memory"),
        (170, "Royal Crypts"),
        (141, "Sewers of Harrogath"),
        (169, "Shadows of Westmarch"),
        (148, "Torajan Jungle"),
    ],
    2: [
        (146, "Ancestral Trial"),
        (149, "Bastion Keep"),
        (191, "Demon Road"),
        (158, "Lost Temple"),
        (144, "River of Blood"),
        (143, "Ruins of Viz-Jun"),
        (190, "Skovos Stronghold"),
        (151, "Tomb of Zoltun Kulle"),
    ],
}

S13_TIERS = {
    1: [
        (146, "Ancestral Trial"),
        (155, "Fall of Caldeum"),
        (158, "Lost Temple"),
        (145, "Phlegethon"),
        (143, "Ruins of Viz-Jun"),
        (169, "Shadows of Westmarch"),
        (151, "Tomb of Zoltun Kulle"),
        (148, "Torajan Jungle"),
    ],
    2: [
        (175, "Ashen Plains"),
        (160, "Canyon of Sescheron"),
        (193, "Halls of Torture"),
        (142, "Horazon's Memory"),
        (156, "Pandemonium Citadel"),
        (174, "Ruined Cistern"),
        (167, "Sanatorium"),
        (141, "Sewers of Harrogath"),
        (150, "Throne of Insanity"),
    ],
}


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
            "level_H": safe_int(row.get("Level(H)")),
            "exp_H": safe_int(row.get("Exp(H)")),
        }
    return monsters


def load_monlvl_xp_h():
    out = {}
    for row in parse_tsv("MonLvl.txt"):
        lvl = safe_int(row.get("Level"))
        out[lvl] = safe_int(row.get("XP(H)"))
    return out


def map_avg_xp(level_id, levels, monsters, monlvl_xp):
    lvl = levels.get(level_id)
    if not lvl:
        return None
    pool = []
    for mid in lvl["monsters"]:
        m = monsters.get(mid)
        if not m or m["exp_H"] == 0:
            continue
        base_xp_factor = monlvl_xp.get(m["level_H"], 0)
        # Match the rounding used by the original T3 file.
        xp = round(base_xp_factor * m["exp_H"] / 100)
        pool.append(xp)
    if not pool:
        return None
    return {
        "avgXp": int(round(sum(pool) / len(pool))),
        "poolSize": len(pool),
    }


def tier_section(season_label, tier_num, roster, levels, monsters, monlvl_xp):
    rows = []
    for lid, name in sorted(roster, key=lambda x: x[1]):
        s = map_avg_xp(lid, levels, monsters, monlvl_xp)
        rows.append((lid, name, s["poolSize"] if s else 0, s["avgXp"] if s else 0))

    avg_xps = [r[3] for r in rows if r[3] > 0]
    tier_avg = int(round(sum(avg_xps) / len(avg_xps))) if avg_xps else 0
    highest_xp = max(avg_xps) if avg_xps else 0

    lines = []
    lines.append("-" * 64)
    lines.append(f"  {season_label} — TIER {tier_num} ({len(rows)} maps)")
    lines.append("-" * 64)
    lines.append("   ID  Map                       Mons   Avg base XP")
    for lid, name, mons, xp in rows:
        line = f"  {lid:>3d}  {name:<25s}{mons:>5d}       {xp:>6,}"
        if xp == highest_xp and xp > 0:
            line += "   <- highest"
        lines.append(line)
    lines.append("       --------------------------------------------")
    lines.append(f"       TIER AVERAGE                          {tier_avg:>6,}")
    return lines, tier_avg, rows


def roster_section(tier_num, s12_rows, s13_rows):
    s12_by_id = {r[0]: r for r in s12_rows}
    s13_by_id = {r[0]: r for r in s13_rows}
    s12_ids = set(s12_by_id)
    s13_ids = set(s13_by_id)

    stayed = sorted(s12_ids & s13_ids)
    dropped = sorted(s12_ids - s13_ids)
    added = sorted(s13_ids - s12_ids)

    def avg_of(ids, src):
        xps = [src[i][3] for i in ids if src[i][3] > 0]
        return int(round(sum(xps) / len(xps))) if xps else 0

    dropped_avg = avg_of(dropped, s12_by_id)
    added_avg = avg_of(added, s13_by_id)

    def emit_row(rec):
        _, name, _, xp = rec
        return f"    {rec[0]:>3d}  {name:<24s}{xp:>6,}"

    lines = []
    lines.append("-" * 64)
    lines.append("  ROSTER CHANGES")
    lines.append("-" * 64)

    lines.append(f"  Stayed in T{tier_num} ({len(stayed)}):")
    for lid in sorted(stayed, key=lambda i: s12_by_id[i][1]):
        lines.append(emit_row(s12_by_id[lid]))

    lines.append("")
    lines.append(f"  Dropped out of T{tier_num} in S13 ({len(dropped)}):  avg ~{dropped_avg:,}")
    for lid in sorted(dropped, key=lambda i: s12_by_id[i][1]):
        lines.append(emit_row(s12_by_id[lid]))

    lines.append("")
    lines.append(f"  Added to T{tier_num} in S13 ({len(added)}):  avg ~{added_avg:,}")
    for lid in sorted(added, key=lambda i: s13_by_id[i][1]):
        lines.append(emit_row(s13_by_id[lid]))

    return lines, stayed, dropped, added, dropped_avg, added_avg


def takeaway(tier_num, s12_avg, s13_avg, dropped, added,
             s12_by_id, s13_by_id, dropped_avg, added_avg):
    delta = s13_avg - s12_avg
    pct = (delta / s12_avg * 100.0) if s12_avg else 0.0
    direction = "leaner" if delta < 0 else "richer"

    def top(ids, src, k):
        items = [(src[i][1], src[i][3]) for i in ids if src[i][3] > 0]
        items.sort(key=lambda x: -x[1])
        return items[:k]

    top_dropped = top(dropped, s12_by_id, 2)
    top_added_full = top(added, s13_by_id, 1)

    lines = []
    lines.append("-" * 64)
    lines.append("  TAKEAWAY")
    lines.append("-" * 64)

    if not dropped and not added:
        lines.append(f"  T{tier_num} roster unchanged between S12 and S13.")
        lines.append("=" * 64)
        return lines

    drop_str = ", ".join(f"{n} {x // 1000}k" for n, x in top_dropped)
    swap_phrase = (
        "gained higher-XP maps" if added_avg > dropped_avg
        else "gained mostly mid/low maps"
    )
    if not dropped:
        sentence1 = f"T{tier_num} kept its S12 roster and added new maps."
    elif len(dropped) == len(added) and not (set(s12_by_id) & set(s13_by_id)):
        sentence1 = (
            f"T{tier_num} swapped its entire roster — lost top maps "
            f"({drop_str}) and {swap_phrase}."
        )
    else:
        sentence1 = (
            f"T{tier_num} lost its heaviest XP maps ({drop_str}) and "
            f"{swap_phrase}."
        )

    if top_added_full:
        an, ax = top_added_full[0]
        sentence2 = f"{an} ({ax // 1000}k) is the new XP standout."
    else:
        sentence2 = ""

    paragraph = " ".join(s for s in (sentence1, sentence2) if s)
    paragraph += f" Net: T{tier_num} is ~{abs(pct):.1f}% {direction} in base XP per monster."
    paragraph += " Density (MonDen) is NOT factored in — this is per-mob average across the spawn pool only."

    # Wrap to ~62 chars after the leading "  ".
    width = 62
    words = paragraph.split()
    line = ""
    for w in words:
        if line and len(line) + 1 + len(w) > width:
            lines.append("  " + line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        lines.append("  " + line)
    lines.append("=" * 64)
    return lines


def build(tier_num, levels, monsters, monlvl_xp):
    s12_section, s12_avg, s12_rows = tier_section(
        "SEASON 12", tier_num, S12_TIERS[tier_num], levels, monsters, monlvl_xp
    )
    s13_section, s13_avg, s13_rows = tier_section(
        "SEASON 13", tier_num, S13_TIERS[tier_num], levels, monsters, monlvl_xp
    )
    delta = s13_avg - s12_avg
    pct = (delta / s12_avg * 100.0) if s12_avg else 0.0
    sign = "+" if delta >= 0 else ""

    out = []
    out.append("=" * 64)
    out.append(f"  PD2 Tier {tier_num} Map Comparison — Season 12 vs Season 13")
    out.append("  Average base XP per monster across the Hell spawn pool")
    out.append("=" * 64)
    out.append("")
    out.append("Method:")
    out.append("  Base XP per monster (Hell) = MonLvl.XP(H)[level] * MonStats.Exp(H) / 100")
    out.append("  Per-map value              = mean across the map's nmon Hell spawn pool")
    out.append("  Tier average               = mean across the maps in the tier")
    out.append("  All XP values use CURRENT monster stats (S13 MonStats.txt). This")
    out.append("  isolates the effect of the tier roster change; underlying monster")
    out.append("  Exp% changes between seasons are not captured.")
    out.append("")
    out.extend(s12_section)
    out.append("")
    out.extend(s13_section)
    out.append("")
    out.append("-" * 64)
    out.append("  RESULT")
    out.append("-" * 64)
    out.append(f"  Tier-avg base XP:  {s12_avg:,}  ->  {s13_avg:,}")
    out.append(f"  Delta:             {sign}{delta:,}  ({sign}{pct:.1f}%)")
    out.append("")
    rost, _, dropped, added, drop_avg, add_avg = roster_section(
        tier_num, s12_rows, s13_rows
    )
    out.extend(rost)
    out.append("")
    s12_by_id = {r[0]: r for r in s12_rows}
    s13_by_id = {r[0]: r for r in s13_rows}
    out.extend(takeaway(
        tier_num, s12_avg, s13_avg, dropped, added,
        s12_by_id, s13_by_id, drop_avg, add_avg,
    ))
    return "\n".join(out) + "\n"


def main():
    levels = load_levels()
    monsters = load_monstats()
    monlvl_xp = load_monlvl_xp_h()

    for tier_num in (1, 2):
        text = build(tier_num, levels, monsters, monlvl_xp)
        path = os.path.join(REPO, f"T{tier_num}_XP_S12_vs_S13.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
