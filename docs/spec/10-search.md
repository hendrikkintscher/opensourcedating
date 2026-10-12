# 10. Search and browsing

*Decided by Hendrik, 11 Oct 2026 (search instead of swiping, filters, limits). Keyword search
and two-way limits added 12 Oct 2026 (design review decisions D4 and D8). Merged with the former
design note docs/design/profile-discovery.md on 12 Oct 2026. All numbers are settings, easy to
tune during the pilot. What each step of browsing reveals is in [03](03-visibility.md); writing
to someone is in [04](04-conversations.md).*

## Decided: search, never swiping

People find each other by **searching with filters and browsing the results**, the way classic
OkCupid worked. There is **no swiping and no card stack**: the app never shows one profile at a
time and asks for an instant yes or no.

- **Better decisions.** A results list lets people compare, read and come back later, instead of
  judging a photo in a second.
- **Fits a small, dense pilot.** With few users in Berlin, a search that shows everyone who fits
  is more useful than a stack that runs out.
- **No dark pattern.** No endless feed, no gamified quick decisions.
- **No legal exposure.** Swipe-card interfaces are covered by other companies' patents and design
  patents and have been used to sue smaller dating apps. Search and browse is old prior art.

## Decided: the search page

The search page is the home screen. The user sets filters and the app shows everyone who fits as
a list or grid of small previews. The filters are saved, so opening the app shows the last search.

| Filter | Values | Notes |
|---|---|---|
| Travel time | bands, e.g. up to 20 / 40 / 60 min by public transport | From both users' map tiles ([06](06-location.md)); never a distance. **One-way**: it only decides what you see |
| Age | range | **Two-way with a 5-year margin** (below) |
| Search groups | multiple choice | Self-chosen, separate from gender labels ([02](02-profile-data-model.md)). **Two-way**: you only see people who are also looking for someone in your search group |
| Looking for | intentions, e.g. long-term, short-term, friendship, open to see | Stored as a list; the first version shows one |
| Active recently | this week / this month | Coarse, never "online now" |
| Photo verified | yes / any | Optional on-device check, see [05](05-safety.md) |
| Interest tags | fixed list plus short tags people type themselves | Replaces free-text keywords (below) |
| Profile texts | words | Opt-in and reciprocal (below) |

- **Orientation is never a filter.** It is an optional display-only label, hidden by default.
- **Sort order is the user's choice:** shortest travel time, recently active or newest. No hidden
  ranking and no paid boosting.
- **Actions on a full profile:** Write (one opening message, see [04](04-conversations.md)),
  Save (a private bookmark list; nobody is told), Hide, Block and Report (see
  [05](05-safety.md)). There is no "pass" decision you are pushed to make; you can leave a
  profile and come back later.
- **Too few results:** when few people fit (early pilot), the app shows how many people are on
  the waitlist nearby and upcoming events, not an empty page.

## Decided: two-way age, one-way travel time (12 Oct, D8)

- **Age is two-way, with a 5-year margin.** You are hidden from a searcher only if your age is
  more than 5 years outside the age range they set. Inside that margin you still appear.
- **Travel time is one-way.** Your own travel-time filter decides only what you see, not who
  sees you.
- **Symbols instead of hiding:** when you are outside the other person's age range (within the
  margin) or beyond their travel time, their tile in your search shows a small age or location
  symbol meaning "you're outside their range". Accepted leak: the symbols tell a searcher roughly
  where the other person's limits are.

## Decided: tags instead of keyword search (12 Oct, D4)

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

## Decided: limits against scraping (starting values)

- **Results are paginated, 20 per page**, and the list ends. No endless scrolling.
- **Full-profile views per day:** 50 for accounts younger than two weeks, 200 after that.
  Enough for a person, slows down scrapers.
- **"Hide" lasts until the user undoes it.** A hidden person never reappears on their own; the
  hidden list stays visible and editable in settings.
- No public profile URLs. Blocked and hidden people never appear, in either direction.

## Follows from this

- Filtering on search groups, age and "looking for" happens on the server inside a separate
  filter service, because the server has to filter. It reads only the search card fields, never
  the full profile (see [12](12-stage-2-network.md)).

## Still open

- Rate limit on search requests themselves. The design review suggests starting at 30 searches
  per hour and 200 per day per account, lower for accounts under two weeks, tuned with the
  attack bots.

## Background

Project research: visibility (product/visibility.md), profile and identity
(product/profile-and-identity.md), threat model, and the archived design review of 12 Oct.
