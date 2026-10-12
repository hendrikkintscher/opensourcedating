# 6. Location

*Decided by Hendrik, 11 Oct 2026. Precision levels and default added 12 Oct 2026 (design review
decision D6).*

## Decided: map tiles, no GPS

- No GPS and no location permission. The user picks a home tile on a Berlin map with a ~500 m
  grid and chooses how precisely it is stored.
- Results show travel-time bands by public transport, never distances. Travel times come from a
  precomputed tile-to-tile matrix built from public timetables (no personal data).
- Only the current home tile is stored; no location history.

## Decided: stored precision and rate limits

- **The server stores only the precision the user chose.** If the user picks "district" (or any
  area coarser than the 500 m tile), the finer tile never leaves the phone. Travel times are then
  computed from the centre of the chosen area. A database leak reveals no more than the user
  chose to share.
- **Home tile changes are rate-limited:** at most once per 24 hours and at most 4 times in any
  30 days. This stops someone from moving step by step across the map to pin down another
  person's location, while still allowing a real move.

## Decided: precision levels (12 Oct, D6)

- **Precision levels for search:** 500 m tile, about 1.5 km (a 3x3 block of 500 m tiles) and
  district. **The default is about 1.5 km.** 500 m and district can be chosen instead.
  - Why: a determined attacker with many accounts can narrow anyone down to their stored tile, so
    the stored precision is the real limit. A 500 m tile around someone's home is a handful of
    streets; 1.5 km is a neighbourhood. Districts in Berlin are large (up to about 30 km across),
    which makes travel-time bands much less useful.
- **Finer location only phone to phone in a conversation.** The server never holds anything
  finer than the search precision the person chose. If someone wants to share a finer tile or a
  meeting spot, their phone sends it to the other phone inside the end-to-end encrypted chat,
  never through the server in readable form. So the server never sees a finer tile, before or
  after a conversation starts.

## Still open

- Grids and travel-time data for places beyond Berlin (phase 7).

## Background

Project research: security baseline (security/security-baseline.md, location section and the
location attacks).
