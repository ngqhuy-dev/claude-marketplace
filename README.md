# ngqhuy-marketplace

Claude Code plugin marketplace. Plugins are referenced from their upstream repositories and pinned to a commit SHA;
no third-party code is copied into this repo.

## Install

```bash
/plugin marketplace add ngqhuy-dev/claude-marketplace
/plugin install dart-flutter@ngqhuy-marketplace
```

## Plugins

| Plugin | Upstream | License |
| --- | --- | --- |
| dart-flutter | [flutter/agent-plugins](https://github.com/flutter/agent-plugins) | BSD-3-Clause |
| flutter | [zakariaf/Flutter-Skills](https://github.com/zakariaf/Flutter-Skills) | MIT |
| react-native-best-practices | [petro-nazarenko/mobile-skills](https://github.com/petro-nazarenko/mobile-skills) | MIT |
| hzblj-skills | [hzblj/skills](https://github.com/hzblj/skills) | MIT |
| engineering | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/engineering) | Apache-2.0 |
| document-skills | [anthropics/skills](https://github.com/anthropics/skills) (docx, xlsx, pptx, pdf) | Apache-2.0 |
| skill-creator | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Apache-2.0 |

## Updating a plugin

Replace its `sha` in `.claude-plugin/marketplace.json` with the new upstream commit:

```bash
git ls-remote https://github.com/<owner>/<repo>.git HEAD
```
