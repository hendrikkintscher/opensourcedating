# Profile discovery: search and filters, no swiping

*Design note, first published 11 Oct 2026, updated the same day (messaging) and on 12 Oct 2026 (design review decisions D4 to D9, and first publishing). Status: decided direction for the prototype; details will change.*

## Decision

People find each other by **searching with filters and browsing the results**, the way classic OkCupid worked. There is **no swiping and no card stack**: the app never shows one profile at a time and asks for an instant yes/no.

Why:

- **Better decisions.** A results list lets people compare, read and come back later, instead of judging a photo in a second.
- **Fits a small, dense pilot.** With few users in Berlin, a search that shows everyone who fits is more useful than a stack that runs out.
- **No dark pattern.** No endless feed, no gamified quick decisions, nothing built to keep people swiping.
- **No legal exposure.** Swipe-card interfaces are covered by other companies' patents and design patents, and have been used to sue smaller dating apps. Search and browse is old, well-known prior art.

## How it works

### 1. Search page (home screen)

The user sets filters, and the app shows everyone who fits as a **list or grid of small profile previews**. The filters are saved, so opening the app shows the last search.

Filters for the prototype:

| Filter | Values | Notes |
|---|---|---|
| Travel time | bands, e.g. "up to 20 / 40 / 60 min by public transport" | Computed from both users' map tiles; no distance in metres, no GPS. **One-way**: it only decides what you see. If you are beyond the other person's travel time, their tile shows a small location symbol |
| Age | range | **Two-way with a 5-year margin**: you are hidden from someone only if your age is more than 5 years outside their range. Within the margin, their tile shows a small age symbol ("you're outside their range") |
| Search groups | multiple choice | Self-chosen, separate from gender labels. **Two-way**: you only see people who are also looking for someone like you, and only appear to them |
| Looking for | intentions, e.g. long-term, short-term, friendship, open to see | Stored as a list; the first version shows one |
| Active recently | this week / this month | Coarse, never "online now" |
| Photo verified | yes / any | Optional on-device check, see [spec 05](../spec/05-safety.md) |
| Interest tags | fixed list plus short tags people type themselves | Replaces free-text keywords |
| Profile texts | words | Only for people who made their own texts searchable (opt-in, off by default), and only finds others who did the same. Search words are never logged |

Orientation is never a filter. It is an optional label for display only, hidden by default.

Saved searches, and alerts about new profiles for a saved search, run on the phone: it re-runs the search and shows a quiet in-app note. Nothing about a saved search is stored on the server.

Sort order is the user's choice: **shortest travel time**, **recently active** or **newest**. There is no hidden ranking algorithm and no paid boosting. A compatibility score from answered questions (as classic OkCupid had) is a possible later addition, but always shown with how it was calculated.

### 2. Profile preview (in the results)

One photo, first name or nickname, exact age (the date of birth is never shown), travel-time band, what they're looking for and the first lines of the profile text. An age or location symbol shows when you are outside their range. Test bots carry a visible "test bot" badge.

### 3. Full profile

Opening a preview shows the whole profile: photos, several free-text sections (for example "About me", "What I'm into", "You should write to me if …"), interest tags, and the details the user chose to show. Long-form text is the centre of the profile, not the photos.

A short **fit checklist** shows why this person is in your results ("you're in each other's age range", "within your travel time", "both looking for long-term") and any differences, using only fields they made visible. What each step reveals is in [spec topic 3](../spec/03-visibility.md).

Actions on a full profile:

- **Write**: send one opening message (see Messaging below).
- **Save**: a private bookmark list. Nobody is told they were saved.
- **Hide**: removes the person from your results. You can see and undo your hidden list at any time.
- **Block**: hides both ways, server-enforced, silent.
- **Report**: always also blocks.

There is no "pass" decision you're pushed to make: you can simply leave a profile and come back later.

### 4. Messaging: one opening message, a reply starts the conversation

Anyone can write to anyone whose profile they can see, but only **one opening message** per person. The recipient starts the conversation by **answering**; until then the sender can't send anything more to that person.

- **Weekly allowance.** Each person can send a limited number of opening messages per week (starting value: 5, tuned during the pilot; lower for new and unverified accounts). This encourages people to choose carefully and stops mass messaging. An opening message that gets an answer doesn't count against the allowance a second time.
- **Text only.** Opening messages can't contain photos or links.
- **No pressure on the recipient.** Not answering is a normal, silent "no". There are no read receipts for opening messages. Unanswered messages disappear after 30 days.
- **Safety stays one tap away.** Every opening message can be reported or blocked directly, and reporting always blocks.
- Once the recipient answers, the conversation continues end-to-end encrypted like any other chat.

**Wording:** the app, its descriptions and its announcements never use the word "match". We talk about writing, answering and conversations.

### 5. Publishing your profile for the first time

A new profile is not visible to anyone until the person actively publishes it the first time. The publish step shows the privacy choices with safe defaults and one honest sentence each: searchable profile texts (off by default), location precision (about 1.5 km by default), which fields are visible, and conversation-only photos. It is also where the separate explicit consent for Art. 9 data is asked.

### 6. What we deliberately don't build

- No swipe gestures, card stacks or one-at-a-time decisions.
- No endless scrolling feed. Results are paginated, and the list ends.
- No "who viewed my profile" list (it creates pressure and leaks who's browsing).
- No "online now" indicator and no exact distance.
- No paid visibility of any kind.
- No secret "both interested" signal (it would bring back liking).

## Privacy and safety in search

- Filtering on search groups, age and "looking for" happens on the server inside a separate filter service, because the server has to filter. Orientation is never filtered on. Gender and orientation are **not shown** in previews unless the user turns that on (see the data-scope rules in the project research).
- Previews show exact age but never the date of birth, a travel-time band rather than a location, and activity only as this week or this month.
- The stored location is only as precise as the person chose (default about 1.5 km). A finer location or meeting spot is only ever shared phone to phone inside the encrypted chat.
- Free text is searchable only for people who opted in, so labels someone chose to hide can't be found through their texts by default.
- **Anti-scraping:** rate limits on searches and profile views, paginated results, a daily cap on profile views for new accounts, and no public profile URLs.
- Blocked and hidden people never appear, in either direction.
- When too few people fit the filters (early pilot), the app shows how many people are on the waitlist nearby and upcoming events, not an empty page.

Not being findable is always possible: **pause** hides you from search, and **"only people I write to"** mode keeps you out of search while the people you write to still see your profile.

## Open questions

- Which free-text sections should the profile have?
