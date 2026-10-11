# App spec: features, rules and open decisions

*Started 11 Oct 2026. Goes through every key feature and rule of the app, one topic at a time,
before prototype code is written. The aim: find the decisions that would cause a lot of rework if
we got them wrong now, and settle them first. Each topic gets its own file in this folder once
Hendrik has decided it.*

Status words: **decided** (Hendrik decided), **recommended** (research suggests it, not yet
confirmed), **open** (needs a decision).

## Topics, costliest to change first

"Cost" means how much code and data would have to be rewritten or migrated if we changed our mind
after the prototype is built.

| # | Topic | Cost to change later | Status | Spec |
|---|---|---|---|---|
| 1 | Accounts and identity (account IDs, devices, recovery, federation-ready addresses) | Very high: every table, every chat key and every block points at an account ID | decided | [01](01-accounts-and-identity.md) |
| 2 | Profile data model: gender, orientation, "looking for", relationship type | Very high: drives the two-way filter, Art. 9 encryption and the queer-community phase | being worked out in a separate thread | |
| 3 | Visibility stages: what others see before and after a conversation starts | High: data-scope.md still describes the old like/like-back stages | being worked out in a separate thread | |
| 4 | Conversations: opening message, answer, ending a conversation, chat relay | High: shapes the relay protocol and libsignal sessions | decided | [04](04-conversations.md) |
| 5 | Safety: block, report with evidence, moderation tool, ban evasion | High: safety data must live in its own service to be shareable in stage 2 | decided (details open) | [05](05-safety.md) |
| 6 | Location tiles and travel-time bands | Medium: decided design, defaults still open | decided (display defaults open) | [06](06-location.md) |
| 7 | Photos: upload pipeline, moderation, who sees which resolution | Medium | being worked out in a separate thread (photo and profile storage) | |
| 8 | Age check (18+) | Medium: must sit behind an interface so the EU age app can be added | decided | [08](08-age-check.md) |
| 9 | Deletion, retention, export, inactive accounts | Medium: has to be designed into every store, including backups | being worked out in a separate thread (pros and cons) | |
| 10 | Search filters, sort and anti-scraping limits | Low to medium | decided | [10](10-search-limits.md) |
| 11 | Test bots and test data separation | Low, but needed from day one | recommended | |
| 12 | Stage 2: network of vetted servers | Low now, as long as 1, 2 and 5 are built federation-ready | planned | |

## Inventory

### 1. Accounts and identity
- Sign-in: **decided**, Ory Kratos, passkeys plus email one-time codes, no passwords, no phone
  number required.
- **Decided:** account ID is a random ID plus the home server (`id@server`); email is never a key.
- **Decided:** one phone per account in the pilot, no chat backup; a lost phone means the account
  comes back by email code but old chats are gone. See [01](01-accounts-and-identity.md).
- Recommended: session list and "log out everywhere"; re-authentication before deletion, export
  or email change.

### 2. Profile data model
- Fields from [profile-discovery.md](../design/profile-discovery.md): first name or nickname,
  date of birth, home tile, photos, several free-text sections, interests, relationship type,
  gender, "looking for".
- **Decided:** "looking for" filtering is two-way: you only see people who are also looking for
  someone like you.
- **Decided:** queer community joins only once gender, preference and safety features are mature,
  which means the data model must already support them in phase 1.
- Open: gender as one value or several, a free-text option, and how "looking for" is expressed
  (genders, relationship types, both).
- Open: is orientation a stored field at all, or only implied by gender plus "looking for"?
- Recommended: Art. 9 fields encrypted per field, only the filter service can read them;
  not shown in previews by default.
- Open: which free-text sections the profile has; health fields stay out of v1.

### 3. Visibility stages
- data-scope.md defines stages S0 to S5 around liking and liking back. Those steps no longer
  exist (replaced by opening messages), so the stages need redefining, for example: account,
  in search, opening message sent, conversation started, shared by choice.
- Open: exact age or age band in previews.
- Open: what precision of location the other person sees once a conversation has started.

### 4. Conversations
- **Decided:** one text-only opening message per person; a reply starts the conversation; weekly
  allowance starting at 5, lower for new accounts; unanswered messages disappear after 30 days;
  no read receipts on opening messages.
- **Decided:** chat is libsignal end to end, relay keeps ciphertext only until delivery.
- **Decided:** opening messages are end-to-end encrypted; "no links" is enforced on the
  recipient's phone; spam is handled by allowance, rate limits and reports.
- **Decided:** either person can end a conversation; no further messages or new opening message
  between the two, but no block. See [04](04-conversations.md).
- Open: allowance numbers, and whether an unanswered message gives its slot back.
- Recommended: photos in chat off for the prototype; push payloads never carry content.

### 5. Safety
- **Decided:** hide, block (silent, both ways, server-enforced), report (always also blocks).
  Reported users are told only when action is taken, with reasons and appeal.
- Recommended: report attaches the reported messages from the reporter's phone.
- **Decided:** message franking in the message format from the first version, so forwarded
  evidence can be verified.
- **Decided:** bans, reports, verification and photo hashes in their own service with an API.
  See [05](05-safety.md).
- Ban evasion uses hashes of the photo files (like PDQ), hashed email and device signals, never
  face templates. Keeping biometric data of banned users without consent is the riskiest item
  the legal research found (legal-gdpr-berlin.md §8); retention periods still need the lawyer.
- Recommended: moderator web tool with queue, evidence view, warn/suspend/ban, statement of
  reasons (DSA Art. 17).
- Open: report reasons list, response times, who moderates during the test.

### 6. Location
- **Decided:** no GPS; user picks a home tile on a ~500 m Berlin grid, chooses the precision;
  changes are rate-limited; only the current tile is stored; travel-time bands, never distances.
- Open: default precision shown in search (research says coarser than 500 m, e.g. district or
  1 km, with 500 m opt-in).
- **Decided:** the server stores only the precision the user chose; tile changes at most once a
  day and 4 times in 30 days. See [06](06-location.md).

### 7. Photos
- Recommended: re-encode and strip metadata on the server, CSAM hash check, nudity pre-screen,
  human review before a photo goes public; signed short-lived URLs; perceptual hash for ban
  evasion.
- Open: how many photos, and whether previews get a lower resolution.

### 8. Age check
- Recommended: date of birth plus on-device selfie age estimation, stronger check near the line,
  EU age-verification app once Germany offers it; store only the result, never images or IDs.
- **Decided:** self-declared date of birth for the fake-data test; the stronger check before real
  users join; only the result is stored. See [08](08-age-check.md).

### 9. Deletion and retention
- Recommended: in-app deletion, immediate from live systems, backups expire after 30 days; ban
  records (hashed email, photo hashes) kept for a defined period; IP logs 7 days; data export in
  the app; inactive accounts deleted after 12 to 24 months with a warning.
- Open: inactive period, ban-record period (lawyer).

### 10. Search
- **Decided:** filters (travel time, age, gender and "looking for", relationship type, active
  recently, photo verified, keywords), user-chosen sort, no hidden ranking, paginated results,
  no "who viewed me", no "online now", no paid visibility.
- **Decided:** 20 results per page; 50 full-profile views a day for accounts under two weeks old,
  200 after; "Hide" lasts until undone. See [10](10-search-limits.md).

### 11. Test bots
- Recommended: every bot row carries a bot flag, a visible "test bot" badge, generated photos
  only, bot runner on another machine using the public API, all bot data wipeable in one go.

### 12. Stage 2
- Planned: allow-listed servers under a shared policy. Open questions are on the dashboard
  (cross-server search, protocol, deletion across servers).
- What stage 1 must already get right so stage 2 is not a rewrite: account IDs that include the
  home server (topic 1), safety data in its own service (topic 5), and keeping profile data on the
  user's home server.

## Wording

The app, its docs and announcements never use the word "match". We say writing, answering,
conversation.
