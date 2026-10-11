# Profile discovery: search and filters, no swiping

*Design note, first published 11 Oct 2026. Status: decided direction for the prototype; details will change.*

## Decision

People find each other by **searching with filters and browsing the results**, the way classic OkCupid worked. There is **no swiping and no card stack**: the app never shows one profile at a time and asks for an instant yes/no.

Why:

- **Better decisions.** A results list lets people compare, read and come back later, instead of judging a photo in a second.
- **Fits a small, dense pilot.** With few users in Berlin, a search that shows everyone who fits is more useful than a stack that runs out.
- **No dark pattern.** No endless feed, no gamified quick decisions, nothing built to keep people swiping.
- **No legal exposure.** Swipe-card interfaces are covered by other companies' patents and design patents, and have been used to sue smaller dating apps. Search and browse is old, well-known prior art.

## How it works

### 1. Search page (home screen)

The user sets filters, and the app shows everyone who matches as a **list or grid of small profile previews**. The filters are saved, so opening the app shows the last search.

Filters for the prototype:

| Filter | Values | Notes |
|---|---|---|
| Travel time | bands, e.g. "up to 20 / 40 / 60 min by public transport" | Computed from both users' map tiles; no distance in metres, no GPS |
| Age | range, shown as bands in previews | Exact age only after a match (see "Privacy and safety in search" below) |
| Gender and "looking for" | multiple choice | **Two-way**: you only see people who are also looking for someone like you, and only appear to them |
| Relationship type | e.g. long-term, short-term, friendship, open to see | |
| Active recently | this week / this month | Coarse, never "online now" |
| Photo verified | yes / any | |
| Keywords | free text in profile texts and interests | Simple full-text search |

Sort order is the user's choice: **shortest travel time**, **recently active** or **newest**. There is no hidden ranking algorithm and no paid boosting. A compatibility score (like OkCupid's match percentage from answered questions) is a possible later addition, but always shown with how it was calculated.

### 2. Profile preview (in the results)

One photo, first name or nickname, age band, travel-time band, relationship type and the first lines of the profile text. Test bots carry a visible "test bot" badge.

### 3. Full profile

Opening a preview shows the whole profile: photos, several free-text sections (for example "About me", "What I'm into", "You should write to me if …"), interests, and the details the user chose to show. Long-form text is the centre of the profile, not the photos.

Actions on a full profile:

- **Like**: private. If both people like each other, they match and can chat.
- **Hide**: removes the person from your results. You can see and undo your hidden list at any time.
- **Block**: hides both ways, server-enforced, silent.
- **Report**: always also blocks.

There is no "pass" decision you're pushed to make: you can simply leave a profile and come back later.

### 4. Messaging

For the pilot, chat opens only after a **mutual like** (safer for the communities we want to invite later). Messaging someone directly from their profile, as classic OkCupid allowed, may come back later with rate limits for new and unverified accounts.

### 5. What we deliberately don't build

- No swipe gestures, card stacks or one-at-a-time decisions.
- No endless scrolling feed. Results are paginated, and the list ends.
- No "who viewed my profile" list (it creates pressure and leaks who's browsing).
- No "online now" indicator and no exact distance.
- No paid visibility of any kind.

## Privacy and safety in search

- Filtering on gender, orientation and "looking for" happens on the server inside the matching service, because the server has to filter. These fields are **not shown** in previews unless the user turns that on (see the data-scope rules in the project research).
- Previews show only coarse data: age band, travel-time band, activity this week or this month.
- **Anti-scraping:** rate limits on searches and profile views, paginated results, a daily cap on profile views for new accounts, and no public profile URLs.
- Blocked and hidden people never appear, in either direction.
- When too few people match (early pilot), the app shows how many people are on the waitlist nearby and upcoming events, not an empty page.

## Open questions

- Show exact age or an age band in previews?
- Should "Hide" expire after a while (so people can reappear), or stay until undone?
- Which free-text sections should the profile have?
- When, if ever, to allow messaging before a match.
