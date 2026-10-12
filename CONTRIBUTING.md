# Contributing

Thanks for helping. A few rules keep this project free and legally clean.

## Licence

All code in this repository is licensed under the **GNU Affero General Public License v3.0 or later** (AGPL-3.0-or-later), see [LICENSE](LICENSE), with the app store permission in [LICENSE-EXCEPTION](LICENSE-EXCEPTION). By contributing you agree that your contribution is released under the same licence, including that permission. There is no contributor licence agreement: you keep the copyright in your contribution, and nobody (including the maintainers) can relicense the project under closed terms.

## Sign off every commit (DCO)

Every commit must carry a `Signed-off-by` line, which certifies the [Developer Certificate of Origin 1.1](https://developercertificate.org/): that you wrote the change or otherwise have the right to submit it under the project's licence.

```
git commit -s -m "Describe the change"
```

This adds `Signed-off-by: Your Name <you@example.org>` to the commit message. Pull requests with unsigned commits can't be merged.

The `DCO sign-off` check on every pull request enforces this; it ignores merge commits. To fix a missed sign-off on your own branch, run `git rebase --signoff main` and force-push. Commits made before 12 Oct 2026 are not signed off; they are all the owner's own work.

Commits made by an AI assistant on the owner's behalf carry the owner's sign-off, which the owner authorised for commits they ask for.

## Your own work only

- Contribute only work you have the right to give. If your employment contract gives your employer rights to code you write, get their permission first.
- **Never bring in confidential information** (code, designs, internal documents, unreleased plans) from any current or former employer, in particular from other dating companies.
- Don't copy code from other projects unless its licence is compatible with AGPL-3.0, and say where it came from in the pull request.

## AI-assisted contributions

AI tools are welcome. Say in the pull request when a substantial part was generated, and make sure you understand and can explain every line you submit.

## Security issues

Don't open public issues for security problems. See [SECURITY.md](SECURITY.md).
