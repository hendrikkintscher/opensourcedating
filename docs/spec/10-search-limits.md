# 10. Search limits

*Decided by Hendrik, 11 Oct 2026. The search design itself is in
[profile-discovery.md](../design/profile-discovery.md). All numbers below are settings, easy to
tune during the pilot.*

## Decided (starting values)

- **Results are paginated, 20 per page**, and the list ends. No endless scrolling.
- **Full-profile views per day:** 50 for accounts younger than two weeks, 200 after that.
  Enough for a person, slows down scrapers.
- **"Hide" lasts until the user undoes it.** A hidden person never reappears on their own; the
  hidden list stays visible and editable in settings.

## Still open

- Rate limit on search requests themselves (per minute and per day).
