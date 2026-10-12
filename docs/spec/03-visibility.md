# 3. Who sees what, and when

*Decided by Hendrik, 12 Oct 2026, following the recommendations in the project research note
"visibility-and-mutual-discovery". Exact age, two-way age with a margin and location precision
were decided earlier the same day (design review decisions D5, D6, D8); they are repeated here so
the steps read as one picture. Replaces the like/like-back stages in the data-scope research.*

## Principle

Details about a person only become more precise when **that person** takes an action: publishing
their profile, writing, or answering. Nobody learns more about someone just by looking.

## Six steps

| Step | What happened | What the other person sees |
|---|---|---|
| **S0 Not findable** | Profile not yet published, paused, or in "only people I write to" mode | Nothing. The person is in nobody's results. |
| **S1 Search preview** | Both pass each other's two-way rules (search groups; age with the 5-year margin) | One photo, first name or nickname, exact age (never the date of birth), travel-time band, what they're looking for, the first lines of the profile text, "active this week/month", verified and test-bot badges, and an age or location symbol if you are outside their range. No gender labels, orientation or other relationship fields in previews. |
| **S2 Full profile** | The searcher opens the preview | All photos except those marked "conversation only", profile texts, interest tags, the fit checklist, and every field set to "everyone who can see my profile". Opening a profile is never reported to the person. |
| **S3 Opening message** | A wrote to B | B sees the message and A's full profile (S2 level), even if A is in "only people I write to" mode. A sees only "sent", and later "expired" after 30 days. No read receipts. |
| **S4 Conversation** | B answered | Both also see fields set to "people in a conversation with me" and conversation-only photos. A finer location is shared only phone to phone in the encrypted chat. Ending the conversation returns both to S2 with no further messages (see [04](04-conversations.md)); a block returns both to nothing. |
| **S5 Shared by choice** | Someone types a phone number, meeting spot or social account | Only the other person. End-to-end encrypted; the server never sees it. |

**Never shown at any step:** who viewed you, who saved you, who hid you, that you were blocked,
how many messages someone receives (the inbox "full" notice is yes or no only), and counts of
people by gender or orientation.

## Visibility per field

Each sensitive field has one of three settings: **nobody (used for search only)**, **people in a
conversation with me**, **everyone who can see my profile**. The defaults are chosen in the
publish step (see [02](02-profile-data-model.md)).

## Decided 12 Oct

- **Fit checklist on every full profile.** A short, factual list of why this person is in your
  results, for example "you're in each other's age range", "within your travel time", "both
  looking for long-term", and differences such as "they want mono, you said poly". It is computed
  by the filter service and uses only fields the other person made visible, so it never reveals a
  hidden field. Relationship types never hide anyone; the checklist only shows the difference.
- **"Only people I write to" mode.** You don't appear in anyone's search, but the people you
  write to see your full profile. Free for everyone. Your weekly allowance still applies.
- **Pause.** Disappear from search at any time with one switch; existing conversations continue.
- **Conversation-only photos.** Any photo can be marked "conversation only". At least one photo
  must be visible in search unless the account is in "only people I write to" mode, so search
  doesn't fill with faceless profiles.
- **No secret "both interested" signal.** A hidden "I'm interested" that is revealed only when
  both press it would bring back liking, which opening messages replaced. Not built. The private
  Save list is never compared with anyone else's.

## Later, not in the prototype

- **Compatibility questions with a visible score**, in the style of classic OkCupid: optional
  questions, accepted answers and importance, combined so a high score means both sides would be
  satisfied. If built: the formula is published, only shared questions count, the score shows
  "based on N shared questions", and sorting by it is a user choice, never the default. Answers
  touching sex, religion, politics or health are Art. 9 data and live in the filter service.
  Phase 5 at the earliest.

## Accepted leaks

- Appearing in someone's results tells them you are looking for someone of their search group
  and that their age is within 5 years of your range (decided with D8).
- The age and location symbols tell a searcher roughly where the other person's limits are.
- The fit checklist shows only what the person already made visible, so it adds no leak.
