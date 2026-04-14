// Shared constants and utilities used by both index.html and map-dmg-calc.html

const CAMPAIGN_MAX_ID = 136;

const DISABLED_LEVELS = new Set([152, 153, 157, 159, 165, 166, 172, 182, 184, 187, 194, 196]);

function realHP(baseHP, areaLevel) {
  const entry = monLvlData[String(areaLevel)];
  if (!entry) return baseHP;
  return Math.floor(baseHP * entry.lhp_H / 100);
}
