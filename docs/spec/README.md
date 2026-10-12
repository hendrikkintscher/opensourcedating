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
| 1 | Accounts and identity (account IDs, devices, recovery) | Very high: every table, every chat key and every block points at an account ID | decided | [01](01-accounts-and-identity.md) |
| 2 | Profile data model: gender, orientation, "looking for", relationship type | Very high: drives the two-way filter, Art. 9 encryption and the queer-community phase | decided (relationship type open) | [02](02-profile-data-model.md) |
| 3 | Visibility stages: what others see before and after a conversation starts | High: data-scope.md still describes the old like/like-back stages | being worked out in a separate thread (exact age and location in conversations decided 12 Oct) | |
| 4 | Conversations: opening message, answer, ending a conversation, chat relay | High: shapes the relay protocol and libsignal sessions | decided | [04](04-conversations.md) |
| 5 | Safety: block, report with evidence, moderation tool, ban evasion | High: safety data must live in its own service to be shareable in stage 2 | decided (backup moderator still to be named) | [05](05-safety.md) |
| 6 | Location tiles and travel-time bands | Medium: decided design and defaults | decided | [06](06-location.md) |
| 7 | Photos: upload pipeline, moderation, who sees which resolution | Medium | being worked out in a separate thread (photo and profile storage) | |
| 8 | Age check (18+) | Medium: must sit behind an interface so the EU age app can be added | decided (stronger check deferred to before real users) | [08](08-age-check.md) |
| 9 | Deletion, retention, export, inactive accounts | Medium: has to be designed into every store, including backups | decided (lawyer confirms ban-record period) | [09](09-deletion-and-retention.md) |
| 10 | Search filters, sort and anti-scraping limits | Low to medium | decided | [10](10-search-limits.md) |
| 11 | Test bots and test data separation | Low, but needed from day one | decided | [11](11-test-bots.md) |
| 12 | Stage 2: one server program on sealed and plain levels | Low now, as long as 1, 2 and 5 are built ready for stage 2 | decided (details open) | [12](12-stage-2-network.md) |

## Inventory

### 1. Accounts and identity
- Sign-in: **decided**, Ory Kratos, passkeys first with email one-time codes as the fallback, no
  passwords, no phone number required. Open: a one-day spike to confirm Kratos supports passkeys
  in native apps.
- **Decided (12 Oct):** account ID is a random opaque 128-bit ID, with no `@server` and not
  derived from a key, bound to the device key by a certificate; email is never a key.
- **Decided:** one phone per account in the pilot, no chat backup; a lost phone means the account
  comes back by email code but old chats are gone.
- **Decided (12 Oct):** account recovery waits 24 hours, with a notice to the old phone that can
  cancel it. See [01](01-accounts-and-identity.md).
- Recommended: session list and "log out everywhere"; re-authentication before deletion, export
  or email change.
- **Decided (12 Oct):** login codes and notices go through an EU-based transactional email
  provider with a DPA, not a US provider; minimal email content, no app name in the subject if
  possible. The provider itself is not chosen yet (comparison in [01](01-accounts-and-identity.md)).

### 2. Profile data model
- Fields from [profile-discovery.md](../design/profile-discovery.md): first name or nickname,
  date of birth, home tile, photos, several free-text sections, interests, relationship type,
  gender, "looking for".
- **Decided:** filtering is two-way: you only see people who are also looking for someone like
  you.
- **Decided:** queer community joins only once gender, preference and safety features are mature,
  which means the data model must already support them in phase 1.
- **Decided (12 Oct):** search groups are self-chosen and separate from gender labels;
  orientation is an optional display-only label, hidden by default, never a filter; "looking
  for" is stored as a list of intentions, one shown in the first version; no trans filter in
  phase 1. See [02](02-profile-data-model.md).
- **Decided (12 Oct):** a new profile is hidden until the person publishes it the first time; the
  publish step holds the privacy choices and the Art. 9 consent.
- Open: gender as one value or several, and a free-text option.
- Open: what describes a relationship type beyond the intention (the "intensity" question).
- Recommended: Art. 9 fields encrypted per field, only the filter service can read them;
  not shown in previews by default.
- Open: which free-text sections the profile has; health fields stay out of v1.

### 3. Visibility stages
- data-scope.md defines stages S0 to S5 around liking and liking back. Those steps no longer
  exist (replaced by opening messages), so the stages need redefining, for example: account,
  in search, opening message sent, conversation started, shared by choice.
- **Decided (12 Oct):** exact age in previews; the date of birth is never shown.
- **Decided (12 Oct):** once a conversation has started, a finer location is shared only phone
  to phone inside the encrypted chat; the server never holds more than the search precision.

### 4. Conversations
- **Decided:** one text-only opening message per person; a reply starts the conversation; weekly
  allowance starting at 5, lower for new accounts; unanswered messages disappear after 30 days;
  no read receipts on opening messages.
- **Decided:** chat is libsignal end to end, relay keeps ciphertext only until delivery.
- **Decided:** opening messages are end-to-end encrypted; "no links" is enforced on the
  recipient's phone; spam is handled by allowance, rate limits and reports.
- **Decided:** either person can end a conversation; no further messages or new opening message
  between the two, but no block. See [04](04-conversations.md).
- **Decided (12 Oct):** inbox cap of 15 unanswered opening messages, adjustable by the
  recipient; senders get a "full" notice with no number. The allowance comes back when an
  opening message expires unanswered after 30 days. 5 opening messages a week, 2 for accounts
  under two weeks old or unverified; numbers tuned with pilot data. Future idea, not decided: an
  allowance relative to the number of profiles that fit the sender's search.
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
  the legal research found (legal-gdpr-berlin.md §8). Ban records are kept 2 years, pending the
  lawyer (see [09](09-deletion-and-retention.md)).
- Recommended: moderator web tool with queue, evidence view, warn/suspend/ban, statement of
  reasons (DSA Art. 17).
- **Decided (12 Oct):** seven report reasons (under 18; fake profile or scam; unwanted sexual
  content; harassment or threats; something happened when we met; hate; other). Response
  targets: CSAM and threats to life immediately, under 18 within a few hours, the rest within
  24 hours. Hendrik plus one backup moderate the pilot, both with escalation contacts.
- Open: who the backup moderator is.

### 6. Location
- **Decided:** no GPS; user picks a home tile on a ~500 m Berlin grid, chooses the precision;
  changes are rate-limited; only the current tile is stored; travel-time bands, never distances.
- **Decided (12 Oct):** precision levels 500 m, about 1.5 km (3x3 tiles) and district; the
  default is about 1.5 km.
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
- **Deferred (12 Oct):** which stronger check, decided before real users. Recommended: German
  eID age-only query, with an ID scan through an EU vendor as the fallback.

### 9. Deletion and retention
- **Decided (12 Oct):** instant deletion, with a hold on accounts under an open report (needs a
  DPIA basis); re-login before deleting; deletion list replayed after restores; 30-day backups;
  photos crypto-shredded.
- **Decided (12 Oct):** after a ban only the ban record is kept, 2 years pending the lawyer.
  Export by request during the test, in the app before real users. Inactive accounts hidden at
  3 months, deleted at 12, with warnings.
- **Decided (12 Oct):** no IP logging during the fake-data test; before real users, keyed IP
  hashes (key rotated daily, kept 7 days) in every layer: reverse proxy, Kratos, relay, safety
  service. See [09](09-deletion-and-retention.md).

### 10. Search
- **Decided:** filters (travel time, age, search groups, "looking for", active recently, photo
  verified, interest tags), user-chosen sort, no hidden ranking, paginated results, no "who
  viewed me", no "online now", no paid visibility.
- **Decided (12 Oct):** interest tags (fixed list plus own short tags) instead of free-text
  keywords; profile texts searchable only for people who opt in (off by default, reciprocal);
  search words never logged; saved searches and alerts run on the phone.
- **Decided (12 Oct):** age is two-way with a 5-year margin; travel time is one-way; a symbol on
  a tile shows when you are outside the other person's range.
- **Decided (12 Oct):** "photo verified" means an optional on-device liveness and face
  comparison with its own consent; only a signed yes or no reaches the server. See
  [05](05-safety.md).
- **Decided:** 20 results per page; 50 full-profile views a day for accounts under two weeks old,
  200 after; "Hide" lasts until undone. See [10](10-search-limits.md).

### 11. Test bots
- **Decided** (see [11](11-test-bots.md)): every bot row carries a bot flag, a visible "test bot" badge, generated photos
  only, bot runner on another machine using the public API, all bot data wipeable in one go.

### 12. Stage 2
- **Decided (12 Oct, replaces the sharded design):** one server program on two levels. The
  sealed (enclave) level reads search cards and runs admission and photo checks; it is run only
  by vetted operators in data centres under a signed agreement. The plain level stores and relays
  ciphertext; anyone in the EU who signs the operator agreement can run it. Shards, k-of-n and
  home servers are dropped. See [12](12-stage-2-network.md).
- Open: who holds profile content keys, sealed-server hosting, the protocol between servers and
  deletion across servers.
- What stage 1 must already get right so stage 2 is not a rewrite: account IDs per topic 1,
  safety and admission in their own services (topic 5), and profile storage and search behind
  their own interfaces.

## Outside the topic list

- **Decided (12 Oct):** the e.V. is founded now, before any public announcement or grant press,
  with seven founders. See [GOVERNANCE.md](../../GOVERNANCE.md).
- **Decided (12 Oct):** a section 7 additional permission for app store distribution, in
  [LICENSE-EXCEPTION](../../LICENSE-EXCEPTION). The lawyer is asked once about libsignal (AGPL)
  on iOS.

## Wording

The app, its docs and announcements never use the word "match". We say writing, answering,
conversation.
