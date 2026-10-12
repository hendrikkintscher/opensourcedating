# 10. Search limits

*Decided by Hendrik, 11 Oct 2026. The search design itself is in
[profile-discovery.md](../design/profile-discovery.md). All numbers below are settings, easy to
tune during the pilot. Keyword search and two-way limits added 12 Oct 2026 (design review
decisions D4 and D8).*

## Decided (starting values)

- **Results are paginated, 20 per page**, and the list ends. No endless scrolling.
- **Full-profile views per day:** 50 for accounts younger than two weeks, 200 after that.
  Enough for a person, slows down scrapers.
- **"Hide" lasts until the user undoes it.** A hidden person never reappears on their own; the
  hidden list stays visible and editable in settings.

## Decided 12 Oct: keyword search

Free-text keyword search over everyone's profile texts is replaced. It would need readable texts
in the search index and would find people by labels they chose to hide (for example someone who
hid "trans" or "bi" but mentions it in a text).

- **Interest tags:** a fixed list of tags plus short tags people type themselves (shown as
  written). Everyone can filter by tags.
- **Searchable profile texts, opt-in:** each person can choose "make my profile texts
  searchable". It is off by default, comes with a plain warning, and can be withdrawn at any
  time.
- **Reciprocal:** only people whose own texts are searchable can search other people's texts,
  and only the texts of people who opted in.
- **Search words are never logged.**
- **Saved searches and alerts run on the phone.** The phone re-runs a saved search and shows a
  quiet in-app note about new profiles; nothing about the saved search is stored on the server.

## Decided 12 Oct: two-way age, one-way travel time

- **Age is two-way, with a 5-year margin.** You are hidden from a searcher only if your age is
  more than 5 years outside the age range they set. Inside that margin you still appear.
- **Travel time is one-way.** Your own travel-time filter decides only what you see, not who
  sees you.
- **Symbols instead of hiding:** when you are outside the other person's age range (within the
  margin) or beyond their travel time, their tile in your search shows a small age or location
  symbol meaning "you're outside their range". Accepted leak: the symbols tell a searcher roughly
  where the other person's limits are.

## Still open

- Rate limit on search requests themselves. The design review suggests starting at 30 searches
  per hour and 200 per day per account, lower for accounts under two weeks, tuned with the
  attack bots.
