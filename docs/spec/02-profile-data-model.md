# 2. Profile data model and first publishing

*Decided by Hendrik, 11 and 12 Oct 2026 (design review decisions D5 and D7, deliberate first
publishing, gender labels and one search group). Profile items from topic 13 (common
frustrations) added 12 Oct 2026. Relationship dimensions are still open. Search filters are in
[10](10-search.md); who sees which field is in [03](03-visibility.md).*

## Decided: identity and intentions

- **Gender labels and one search group.** People pick or add any number of gender labels,
  freely. Separately, each person chooses exactly one search group: woman, man or non-binary.
  Gender labels are what the profile shows; the search group is what the filter uses
  (Hendrik, 12 Oct).
- **Only gender and age are two-way.** You only see people who are also looking for someone in
  your search group, and age is two-way with a 5-year margin (see [10](10-search.md)).
  Relationship types, openness and relationship status are the searcher's own filters only and
  never hide anyone (Hendrik, 11 Oct).
- **Openness** is its own field: mono / open / poly.
- **Relationship status** is its own field. Draft values: single, in a relationship, married,
  it's complicated.
- **Orientation is an optional label for display only.** It is hidden by default and is never
  used as a filter.
- **"Looking for" is stored as a list of intentions.** The first version of the app shows and
  lets people pick one, but the data model holds a list, so more can be shown later without a
  migration.
- **No trans filter in the fake-data phases.** Before phase 4 (community test) we ask the
  queer community whether and how to offer a T4T option.
- **Exact age in previews; the date of birth is never shown.** Age filters reveal the exact age
  by stepping anyway, so age bands would only look private.
- **The data model is complete from the first deployed version** (phase 2), so the queer
  community can test it in phase 4 without a migration.

## Decided: profile content (topic 13)

- **Narrative prompts instead of a blank "About me".** The three profile texts are prompts that
  invite specifics (for example "a Saturday I'd gladly repeat", "something I've changed my mind
  about", "write to me if …"). The wording of the prompts is a later detail. Long-form text is
  the centre of the profile, not the photos.
- **"How soon do you like to meet?"** Optional field with four values: after a few messages,
  after a week or two of writing, after a call first, no rush. One-way (your own filter only),
  shown on the full profile and in the fit checklist.
- **Photo age bands.** On upload the phone reads the capture date, asks the person to confirm or
  correct it, and strips all metadata before upload. The profile shows one line per photo or for
  the set: "from the last year" / "from 1 to 2 years ago" / "older than 2 years". The server
  stores the band, never the date.
- **"Taken in the app" photos.** The in-app camera can take a photo straight into the profile;
  it gets a "taken in the app, Oct 2026" mark. Optional.
- Accepted: photo age bands and "taken in the app" marks are claims, not proof; a modified app
  could fake them. They set a norm; the verification badge (with app attestation, see
  [05](05-safety.md)) carries the proof.

## Decided: deliberate first publishing

- **A new profile is hidden until the person actively publishes it the first time.**
- The publish step shows the privacy choices with safe defaults and one honest sentence each:
  searchable profile texts (off by default), location precision (about 1.5 km by default, see
  [06](06-location.md)), which fields are visible, and conversation-only photos.
- The publish step is also where the separate explicit consent for Art. 9 data is asked.
- **Community agreement** shown at first publish. It includes: "If you lose interest, end the
  conversation with a tap. Don't just disappear." and "We can't read your chats and we won't try.
  Please write your own messages; the people here want to meet you, not your assistant."

## Recommended, not yet decided

- Art. 9 fields encrypted per field, readable only by the filter service; not shown in previews
  by default.
- Health fields stay out of the first version.

## Still open

- **Relationship dimensions:** "intensity" is replaced by several dimensions (Hendrik, 12 Oct).
  Which dimensions, their answers and the layout are still being worked out and are **not
  decided** (draft: product/relationship-dimensions.md in the project research).
- The wording of the narrative prompts.

## Background

Project research: profile and identity (product/profile-and-identity.md), relationship
dimensions (open draft), visibility, frustrations (product/frustrations.md).
