# 2. Profile data model and first publishing

*Partly decided by Hendrik, 12 Oct 2026 (design review decisions D5 and D7, and deliberate first
publishing). Background: the gender and identity research doc (§7) and the visibility doc in the
project research. Search filters are in [10](10-search-limits.md) and
[profile-discovery.md](../design/profile-discovery.md).*

## Decided

- **Gender labels and one search group.** People pick or add any number of gender labels,
  freely. Separately, each person chooses exactly one search group: woman, man or non-binary.
  Gender labels are what the profile shows; the search group is what the filter uses
  (Hendrik, 12 Oct).
- **Only gender and age are two-way.** You only see people who are also looking for someone in
  your search group, and age is two-way with a 5-year margin (see [10](10-search-limits.md)).
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

## Added 12 Oct (topic 13: common frustrations)

- **"How soon do you like to meet?"** Optional field with four values: after a few messages,
  after a week or two of writing, after a call first, no rush. One-way (your own filter only),
  shown on the full profile and in the fit checklist.
- **Narrative prompts.** The profile texts are prompts (confirmed by Hendrik on 12 Oct over a single "About me") that invite specifics instead of a blank
  "About me"; the wording of the prompts is a later detail.
- **Photo age bands and "taken in the app".** Each photo carries a self-declared band (from the
  last year / 1 to 2 years / older), read from the capture date on the phone and confirmed by the
  person; metadata is stripped before upload and the server stores only the band. Photos taken
  with the in-app camera carry a "taken in the app, <month>" mark.
- **Community agreement** shown at first publish, including: end a conversation with a tap
  instead of disappearing; write your own messages. See [13](13-frustrations.md).

## Deliberate first publishing

- **A new profile is hidden until the person actively publishes it the first time.**
- The publish step shows the privacy choices with safe defaults and one honest sentence each:
  searchable profile texts (off by default), location precision (about 1.5 km by default, see
  [06](06-location.md)), which fields are visible, and conversation-only photos.
- The publish step is also where the separate explicit consent for Art. 9 data is asked.

## Still open

- **Relationship dimensions:** "intensity" is replaced by several dimensions (Hendrik, 12 Oct).
  Which dimensions, their answers and the layout are still being worked out and are not decided.
