# 7. Photos

*Status: open. The upload pipeline, moderation and resolutions are not decided yet. This file
was added on 12 Oct 2026 so every topic has a home; it collects what is already decided in other
topics and what the research recommends.*

## Decided in other topics

- **Conversation-only photos:** any photo can be marked "conversation only"; at least one stays
  visible in search unless the account is in "only people I write to" mode. See
  [03](03-visibility.md).
- **Photo age bands and "taken in the app" marks;** metadata is stripped on the phone before
  upload. See [02](02-profile-data-model.md).
- **Photo verification** is an optional on-device check; nothing biometric leaves the phone. See
  [05](05-safety.md).
- **Ban evasion** uses perceptual hashes of photo files (for example PDQ), never face templates.
  See [05](05-safety.md).
- **Crypto-shredding:** each photo is stored encrypted with its own key, so deleting the key
  deletes every copy, backups included. See [09](09-deletion-and-retention.md).
- **Test bots** use generated or licensed photos only. See [11](11-test-bots.md).

## Recommended, not yet decided

- Re-encode and strip metadata on the server as well.
- A hash check against known abuse imagery (CSAM) and a nudity pre-screen before a photo is shown.
- Human review before a photo goes public.
- Photos served through signed, short-lived URLs.

## Still open

- How many photos a profile can have, and whether previews get a lower resolution.
- Which abuse-image hash service, and who may run it in which phase (lawyer).
- How photos are stored and checked in stage 2 (see [12](12-stage-2-network.md)).

## Background

Project research: photos (security/photos.md), stage 2 reasoning (security/stage-2.md), safety
and moderation (photo moderation section).
