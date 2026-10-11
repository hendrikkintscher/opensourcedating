# 5. Safety and moderation

*Decided by Hendrik, 11 Oct 2026. Background: safety-and-moderation.md, data-security.md §8 and
§12.3, legal-gdpr-berlin.md §8 in the project research.*

## Already decided earlier

- **Hide** removes a person from your results (undoable). **Block** is silent, both ways and
  enforced by the server. **Report** always also blocks.
- Reported users are told nothing when a report is filed; they are told, with reasons and a way
  to appeal, only when action is taken (DSA Art. 17 statement of reasons).

## Decided now

- **A separate safety service from day one.** Bans, reports, moderation decisions, verification
  status and ban-evasion records live in their own service with its own database and API, apart
  from profiles. In stage 2, vetted servers can share a ban list through that API without a
  rewrite.
- **Verifiable reports (message franking) are part of the message format from the first
  version.** Each chat message, opening messages included, carries a cryptographic commitment
  that the relay stamps on delivery. When someone reports a conversation, their phone forwards the
  messages, and moderation can check they are genuine without the server ever reading chats.

## Ban evasion, kept clear of biometric data

To stop banned people from coming back, the safety service keeps, for a fixed period:

- a hashed email address (and a hashed phone number, if one was ever given);
- perceptual hashes of the banned account's **photo files** (for example PDQ), which recognise
  the same or a slightly edited picture uploaded again;
- device attestation signals, as a risk signal only.

It does **not** keep face templates or any face recognition data. Tying bans to a person's face
would mean keeping biometric data (GDPR Art. 9) of banned users without their consent, which
the legal research flags as the riskiest item in the safety design. File hashes are not designed
to identify a person and are not face recognition. The retention period for all ban records
still needs the lawyer.

## Still open

- Report reasons list (safety-and-moderation.md §4 has a proposal), response times and who
  moderates during the test.
- Retention periods for reports, decisions and ban records (lawyer).
