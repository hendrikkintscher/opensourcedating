# 9. Deletion, retention, export, inactive accounts and IP logging

*Decided by Hendrik, 12 Oct 2026 (design review decisions D11 and D12). Background:
deletion-retention-export.md and design-review-2026-10-12.md §6 in the project research.*

Every period below is a setting, not structure: a longer period applies from then on, a shorter
one deletes older data at the next cleanup run. The privacy policy changes each time.

## Deleting an account (decided)

- **Instant deletion.** Profile, photos and undelivered messages leave the live system at once.
  Contacts see "account deleted" and the conversation closes; their copy of past messages stays
  on their phone, which the privacy policy says.
- **Hold under an open report.** If a report against the account is still open, the account
  disappears for everyone at once, but the safety service keeps the report and its evidence until
  a moderator closes it (then it is deleted or becomes a ban record). This hold needs its own
  legal basis in the DPIA, because the user's Art. 9 consent ends with the deletion (lawyer).
- **Re-login before deleting**, with a passkey or an email code.
- **Backups expire after 30 days.**
- **Deletion list replayed after restores.** The IDs of deleted accounts are kept until the last
  backup that contains them has expired, and replayed after any restore, so deleted people don't
  come back.
- **Photos are crypto-shredded.** Each photo is stored encrypted with its own key; deleting the
  key makes every copy unreadable at once, including the copies in backups, so the 30-day backup
  window doesn't apply to photos.

## What is kept after deletion (decided)

- Nothing, unless the account was banned.
- After a ban, only the **ban record** (keyed hashes of the email and photo files, as in
  [05](05-safety.md)) and the moderation decision, in the safety service only, for **2 years**.
  The lawyer still has to confirm the 2 years and the legal basis.

## Export (decided)

- **During the fake-data test:** by request, assembled by hand within a month.
- **Before real users:** self-service in the app. Re-login first; download in the app only, with
  a link valid for minutes. Never sent as an email attachment.
- **Included:** profile, photos, settings, location tile, contact list and opening-message counts,
  blocks, reports you made, account and ban decisions about you with their reasons.
- **Left out:** who reported you (Art. 15(4), protects reporters), other people's data, chat
  content (the server never has it).

## Inactive accounts (decided)

- **Hidden from search after 3 months** without opening the app; one tap makes the profile
  visible again.
- **Deleted after 12 months**, with warning emails 30 days and 7 days before. Opening the app
  resets both clocks.
- Banned accounts follow the ban-record rule above, not this one.

## IP addresses in logs (decided, D11)

- **During the fake-data test: no IP logging.** Rate limits work in memory.
- **Before real users: keyed hashes of IP addresses**, never raw addresses. The key is rotated
  daily and the hashes are kept 7 days. That is enough to spot sign-up farms and link abuse
  within a week, and the hashes can't be handed over as addresses. Hashed IPs are still personal
  data and appear in access requests.
- **Configured in every layer:** the reverse proxy access log, Ory Kratos (it records the IP on
  sessions by default), the chat relay and the safety service. "No raw IPs" has to hold in each
  of them, not only in our own code.

## Still open

- The legal basis for the open-report hold and for ban records after consent is withdrawn
  (lawyer, DPIA).
- The 2-year ban-record period (lawyer).
- Deletion across servers in stage 2 (GDPR Art. 17(2)), see [12](12-stage-2-network.md).
