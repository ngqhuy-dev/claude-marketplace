# ngqhuy-marketplace

**One command to get a curated set of Claude Code skills for Flutter & React Native developers. Every plugin is pinned to an upstream commit SHA, so nothing changes under you without a reviewed PR.**

[![Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fngqhuy-dev%2Fclaude-marketplace%2Fmain%2F.claude-plugin%2Fmarketplace.json&query=%24.plugins.length&label=plugins&color=blue)](.claude-plugin/marketplace.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/ngqhuy-dev/claude-marketplace)](https://github.com/ngqhuy-dev/claude-marketplace/commits/main)
[![Validate](https://github.com/ngqhuy-dev/claude-marketplace/actions/workflows/validate.yml/badge.svg)](https://github.com/ngqhuy-dev/claude-marketplace/actions/workflows/validate.yml)

<!-- Demo GIF: record `/plugin marketplace add` + `/plugin install`, save as docs/demo.gif, then uncomment:
![Demo](docs/demo.gif)
-->

## Quick start

```bash
# 1. Add the marketplace (once)
/plugin marketplace add ngqhuy-dev/claude-marketplace

# 2. Install what you need
/plugin install dart-flutter@ngqhuy-marketplace
/plugin install building-react-native-apps@ngqhuy-marketplace
```

Browse everything interactively with `/plugin` → **Discover**.

## Why this marketplace?

- **Mobile-first curation.** Instead of searching dozens of repos, you get the Flutter and React Native skills worth installing, in one place.
- **Pinned, not floating.** Each plugin points to an exact upstream commit (see [Why pinned?](#why-pinned)).
- **No copied code.** Plugins are fetched straight from their upstream repos. This repo only holds the manifest.
- **Kept fresh.** A weekly GitHub Action checks every upstream and opens a PR with diff links when there are new commits.

## Plugins

### Flutter

| Plugin | Use it when | Upstream | License |
| --- | --- | --- | --- |
| `dart-flutter` | You want the official Dart/Flutter skills and the Dart MCP server (analyze, run, hot reload from Claude). | [flutter/agent-plugins](https://github.com/flutter/agent-plugins) | BSD-3-Clause |
| `flutter` | You're designing app architecture, Riverpod state, tests, persistence, i18n/RTL, accessibility or CI. | [zakariaf/Flutter-Skills](https://github.com/zakariaf/Flutter-Skills) | MIT |

### React Native

| Plugin | Use it when | Upstream | License |
| --- | --- | --- | --- |
| `building-react-native-apps` | You need help with performance, navigation, TV, library development or RN upgrades. | [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills/tree/main/plugins/building-react-native-apps) | MIT |
| `testing-react-native-apps` | You're writing tests, automating devices, or digging through CI artifacts. | [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills/tree/main/plugins/testing-react-native-apps) | MIT |
| `migrating-to-react-native` | You're assessing or incrementally migrating a native iOS/Android app to RN. | [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills/tree/main/plugins/migrating-to-react-native) | MIT |
| `react-native-best-practices` | You're choosing Expo vs bare, FlatList vs ScrollView, tuning Metro or React Navigation. | [petro-nazarenko/mobile-skills](https://github.com/petro-nazarenko/mobile-skills) | MIT |
| `hzblj-skills` | You work with Reanimated, Skia, GSAP, Tailwind or Next.js and want type-safe, clean-code guidance. | [hzblj/skills](https://github.com/hzblj/skills) | MIT |

### General engineering

| Plugin | Use it when | Upstream | License |
| --- | --- | --- | --- |
| `andrej-karpathy-skills` | You want Claude to think first, keep changes small and surgical, and avoid common LLM coding mistakes. | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | MIT |
| `engineering` | You're writing standups, reviewing code, recording architecture decisions or handling incidents. | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/engineering) | Apache-2.0 |
| `postman` | You're mocking APIs, writing collection tests, or wiring Postman checks into CI. | [postmanlabs/postman-plugin](https://github.com/postmanlabs/postman-plugin) | Apache-2.0 |
| `document-skills` | You need to read or produce Word, Excel, PowerPoint or PDF files. | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| `skill-creator` | You're writing, improving or evaluating your own skills. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Apache-2.0 |

## Why pinned?

Plugins can run commands and ship MCP servers, so a plugin that silently changes upstream is a supply-chain risk. Pinning each plugin to a commit SHA means:

- **What you install is what was reviewed.** A compromised or broken upstream commit does not reach you automatically.
- **Updates are visible.** Every bump arrives as a PR with a compare link per plugin, so you can read the diff before it lands.
- **Installs are reproducible.** Teammates who add this marketplace get exactly the same plugin code.

## Keeping plugins up to date

- `.github/workflows/bump-shas.yml` runs every Monday (and on demand from the Actions tab). It runs `scripts/bump_shas.py` and opens a PR on `chore/bump-upstream-shas`.
- `.github/workflows/validate.yml` checks the manifest on every push and PR: valid JSON, unique names, and every pinned SHA still exists upstream.

To bump manually:

```bash
python3 scripts/bump_shas.py
```

## Contributing

Suggestions for good Flutter / React Native plugins are welcome. Open an issue or PR with the upstream repo, what it's useful for, and its license.

## License

The files in this repo are [MIT](LICENSE). Each plugin is fetched from its upstream repository and stays under its own license, listed above.
