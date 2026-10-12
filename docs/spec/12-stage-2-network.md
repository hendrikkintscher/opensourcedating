# 12. Stage 2: one server program on two levels

*First decided by Hendrik, 11 Oct 2026. Rewritten 12 Oct 2026 after design review decision D2,
which replaces the earlier sharded design. Stage 1 (the Berlin pilot) stays one server.
Stage 1 runs project phases 2 to 6; stage 2 is built in phase 6 and is the natural setup for
phase 7 (see [docs/phases.md](../phases.md)).*

## Decided (12 Oct)

- **The "3e" shape: one server program that runs on two levels.**
  - **Sealed level:** the parts that have to read data (search cards, admission and ban checks,
    photo checks) run inside hardware enclaves (confidential computing) that phones check by
    remote attestation before trusting them. Sealed servers are run **only by vetted operators,
    in professional data centres, under a signed operator agreement.**
  - **Plain level:** stores and relays ciphertext only (encrypted profile items and photos,
    opening messages, chat). It is **open to anyone in the EU who signs the operator agreement.**
- **Why vetted operators for the sealed level:** published 2025 attacks on AMD SEV-SNP and Intel
  TDX with cheap memory-bus hardware show that an operator with physical access to their own
  machine can break an enclave. Enclaves protect against breaches, hosting staff and remote
  attackers; vetting and the signed agreement cover the operator. Legally, everyone who runs a
  server processes Art. 9 data (even ciphertext they can't read), so every operator has to be
  bound as the e.V.'s processor or as a joint controller, and has to be in the EU.
- **Shards and k-of-n are dropped.** Profiles are no longer split into redundant pieces across
  servers. Content is already encrypted on the phone, so erasure coding and secret sharing added
  a lot of engineering for little privacy. This replaces the 11 Oct decision that "no single
  server holds a full profile" by splitting it into pieces.
- **No home servers.** Account IDs carry no server name (see [01](01-accounts-and-identity.md));
  a person is not tied to one server.
- Still from 11 Oct: a shared ban list through the safety service (see [05](05-safety.md)), and
  pure phone-to-phone stays rejected (bans can't be enforced, IP addresses are exposed, messages
  only arrive while both phones are on).

## Proposed details (from the storage work and the design review, not yet decided)

See sections 3d and 3e of photos-and-profile-storage.md and section 5.6 of the design review in
the project research.

- Search cards in the sealed level stay minimal (age, location tile, search groups, "looking
  for", interest tags, visibility limits), so an enclave break exposes little. Search is
  replicated across sealed servers.
- Releases of the sealed program are logged in a public transparency log, signed with a release
  key split across board members' hardware keys (3 of 5), and accepted by phones only after a
  delay (7 days).
- Per-chip attestation keys can be revoked once a compromise is known.
- Plain operators join after automated checks (uptime, correct protocol) and must delete on the
  e.V.'s instruction. A central revocation list removes operators who break the agreement.

## Still open

- **Who holds profile content keys.** If the sealed level also holds every profile's content key
  (to hand to permitted viewers), an enclave break exposes full profiles, not just search cards.
  Either accept that openly in the threat model and DPIA, or move to proxy re-encryption before
  stage 2.
- Hosting for sealed servers: confidential VMs at the large clouds, or dedicated hardware
  (whether Hetzner exposes SEV-SNP to customers is unconfirmed).
- The protocol between servers, and how deletion reaches every server (GDPR Art. 17(2)).
- The operator agreement: processor (Art. 28) or joint controller (Art. 26), for each level
  (lawyer).
- Anonymous allowance tokens: the review recommends leaving them out unless sealed sender and
  the opening-message rules are designed together, because the mailbox has to know the sender
  anyway. Stage 1 counts allowance per account.

## What stage 1 must do so this isn't a rewrite

- Account IDs in the form decided in [01](01-accounts-and-identity.md), from the first migration.
- Profile storage sits behind its own interface ("put item / get item / delete item", able to
  hold ciphertext with a key per item), so the single-server store can later move to the plain
  level without touching search, chat or safety.
- Search reads only the search card fields through a separate interface, never the full profile.
- Safety and admission run as their own services, so they can move to the sealed level.
- A device signing key is registered at sign-up (see [01](01-accounts-and-identity.md)).
