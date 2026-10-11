# 11. Test bots

*Decided by Hendrik, 11 Oct 2026. Background: data-security.md §12.1 in the project research.*

## Decided

- **Every bot account and everything it creates is marked as bot data**, from the first version,
  so all bot data can be wiped in one go at the end of the test phase.
- **Testers see a visible "test bot" badge** on bot profiles and messages.
- **Bot photos are generated or licensed**, never photos of real people.
- **Bots run on a separate machine, not the app server**, and use the same public HTTPS API as
  the app. Hendrik's own laptops (Windows or Linux Mint) are enough: the server is on the
  internet, so a laptop at home reaches it exactly like a phone does.
- **Attack bots** try to locate a test user (trilateration with tiles and travel-time bands) and
  to copy all profiles. If they succeed beyond the allowed precision or limits, the automated
  tests fail.

## Notes

- All bots from one home connection share one IP address. Rate limits stay on for bots too;
  bot accounts are created slowly (once) rather than exempting the bot runner, so the limits
  themselves get tested.
- **No bots on testers' phones.** The server can't tell a bot on a phone from a bot on a laptop,
  so it adds nothing to the server test, and it would put bot software and bot data on personal
  devices. What phones add (mobile networks, push delivery, the app in the background) is
  covered by the testers using the real app. Scripted UI tests of the app on emulators or a
  spare test phone can come later.
