# Audit Book Writing Skills Marketplace

## Marketplace Metadata

**Name**: Audit Book Writing Pro Skills
**Description**: 审计专业书籍撰写、审核、优化完整工具集
**Version**: 1.0.0
**Author**: wuying
**License**: MIT
**Repository**: https://github.com/wuying/audit-book-writing-skills

---

## Available Skills

### Audit & Book Writing

#### audit-book-writing-pro

**Path**: `audit-book-writing-pro/`
**Description**: 审计专业书籍撰写系统，集成四轮评审、双模式优化、100个法规知识库
**Version**: 1.0.0
**Dependencies**: Python 3.8+, (可选: re, subprocess for grep-based law search)
**Install**: `/plugin install audit-book-writing-pro@audit-book-writing-skills`

**Features**:
- 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 双模式优化（修订模式：95%-120%字数控制；重构模式：大幅调整）
- 多文件留痕输出（5个评审文件 + 1个优化稿）
- 法律法规知识库（100个法规文件，覆盖国家/省/市三级）
- 审计应用指引模板（800-1500字）
- 审计案例启示模板（800-1500字）
- 智能插件系统（ChatLaw、ai-research-skills、lexnlp、zotero-better-bibtex）

**Supported Domains**:
- 文化遗产审计
- 财务审计
- 内部控制审计
- 内部审计
- 合规审计

---

## Installation

### Install All Skills

```bash
# Add marketplace
/plugin marketplace add wuying/audit-book-writing-skills

# Install all skills
/plugin install all-skills@audit-book-writing-skills
```

### Install Individual Skills

```bash
# 审计书籍撰写工具
/plugin install audit-book-writing-pro@audit-book-writing-skills
```

---

## Version Management

Skills use git tags for versioning:

| Version | Date | Changes |
|---------|------|---------|
| `v1.0.0` | 2026-02-27 | Initial release with Phase 3 plugins integration |

Update all installed skills:
```bash
/plugin update
```

Update specific skill:
```bash
/plugin update audit-book-writing-pro
```

---

## Quick Reference

| Skill | Command | Use Case |
|-------|---------|----------|
| **audit-book-writing-pro** | 审计书籍章节优化 | 审计书籍撰写、审核、优化 |

---

## Development

### Adding New Skills

1. Create skill directory following structure
2. Add `SKILL.md` with proper frontmatter
3. Update this `MARKETPLACE.md`
4. Create a new git tag

### Skill Structure Template

```
skill-name/
├── SKILL.md              # Required: Skill definition with YAML frontmatter
├── CLAUDE.md             # Required: Project instructions
├── README.md             # Optional: Skill documentation
├── PROJECT-OVERVIEW.md    # Optional: Project overview
├── references/           # Optional: Reference materials
│   ├── audit-book-templates.md
│   ├── audit-knowledge-base.md
│   ├── domains-workflow.md
│   └── laws-database/    # 100个法律法规文件
├── docs/                 # Optional: Documentation
│   └── phase3-*.md       # Phase 3 实施报告
├── src/                  # Optional: Source code
│   └── plugins/          # 插件系统
│       ├── base.py
│       ├── manager.py
│       ├── chatlaw_adapter.py
│       ├── ai_research_skills_adapter.py
│       ├── lexnlp_adapter.py
│       └── zotero_bibtex_adapter.py
├── tests/                # Optional: Tests
│   └── plugins/
└── assets/               # Optional: Assets
```

### SKILL.md Frontmatter Template

```yaml
---
name: audit-book-writing-pro
description: 审计专业书籍撰写、审核、优化系统
dependency: Python 3.8+ (optional), re, subprocess
version: 1.0.0
author: wuying
---
```

---

## Dependencies

### Python Dependencies

For `audit-book-writing-pro` (optional, for advanced features):
```bash
pip install pandas numpy
```

### Sub-Skills (Plugins)

`audit-book-writing-pro` includes bundled plugins:
- `ChatLaw` - 法规校对（基于本地法规库grep搜索）
- `ai-research-skills` - 逻辑性与结构性分析（基于规则）
- `lexnlp` - 术语校对（基于正则表达式）
- `zotero-better-bibtex` - 文献校对（基于规则）

No additional installation required for rule-based versions.

---

## Support

- **Issues**: https://github.com/wuying/audit-book-writing-skills/issues
- **Discussions**: https://github.com/wuying/audit-book-writing-skills/discussions
- **Documentation**: See `audit-book-writing-pro/SKILL.md` and `audit-book-writing-pro/PROJECT-OVERVIEW.md`

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

**Last Updated**: 2026-02-27
**Skills Version**: 1.0.0
**Total Skills**: 1
**Total Plugins**: 4
**Total Laws**: 100
