# 6. Location

*Decided by Hendrik, 11 Oct 2026. Background: data-security.md §6 and §12.4 in the project
research. How precisely other people see a location is part of the "who sees what, and when"
topic, worked out separately.*

## Already decided earlier

- No GPS and no location permission. The user picks a home tile on a Berlin map with a ~500 m
  grid and chooses how precisely it is stored.
- Results show travel-time bands by public transport, never distances. Travel times come from a
  precomputed tile-to-tile matrix built from public timetables (no personal data).
- Only the current home tile is stored; no location history.

## Decided now

- **The server stores only the precision the user chose.** If the user picks "district" (or any
  area coarser than the 500 m tile), the finer tile never leaves the phone. Travel times are then
  computed from the centre of the chosen area. A database leak reveals no more than the user
  chose to share.
- **Home tile changes are rate-limited:** at most once per 24 hours and at most 4 times in any
  30 days. This stops someone from moving step by step across the map to pin down another
  person's location, while still allowing a real move.

## Still open

- Which precision levels are offered (500 m tile, ~1 km, district) and which is the default;
  belongs to the "who sees what, and when" topic.
