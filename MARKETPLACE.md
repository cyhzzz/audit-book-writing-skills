# Audit Book Writing Skills Marketplace

## Marketplace Metadata

**Name**: Audit Book Writing Pro Skills
**Description**: 审计专业书籍撰写、审核、优化完整工具集（包含v1.0基础版、v2.0增强版、v3.0完整版）
**Version**: 3.0
**Author**: wuying
**License**: MIT
**Repository**: https://github.com/cyhzzz/audit-book-writing-skills

---

## Available Skills

### Audit & Book Writing

#### audit-book-writing-pro (v3.0 - 完整版)

**Path**: `audit-book-writing-pro/`
**Description**: 审计专业书籍撰写系统，集成四轮评审、双模式优化、100个法规知识库、智能插件系统
**Version**: 3.0
**Dependencies**: Python 3.8+, (可选: re, subprocess for grep-based law search)
**Install**: `/plugin install audit-book-writing-pro@cyhzzz/audit-book-writing-skills`

**Features**:
- 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 双模式优化（修订模式：95%-120%字数控制；重构模式：大幅调整）
- 多文件留痕输出（5个评审文件 + 1个优化稿）
- 法律法规知识库（100个法规文件，覆盖国家/省/市三级）
- 审计应用指引模板（800-1500字）
- 审计案例启示模板（800-1500字）
- **智能插件系统**（ChatLaw、ai-research-skills、lexnlp、zotero-better-bibtex）
- **76个单元测试，通过率98.7%**

**Supported Domains**:
- 文化遗产审计 (Cultural Heritage Audit)
- 财务审计 (Financial Audit)
- 内部控制审计 (Internal Control Audit)
- 内部审计 (Internal Audit)
- 合规审计 (Compliance Audit)

**适用场景**: 专业用户，需要智能插件支持和完整的质量控制

---

#### audit-book-writing-v2 (v2.0 - 增强版)

**Path**: `audit-book-writing-v2/`
**Description**: 审计书籍撰写与评审增强版，支持双模式优化、多文件留痕、法律法规库
**Version**: 2.0
**Dependencies**: None
**Install**: `/plugin install audit-book-writing-v2@cyhzzz/audit-book-writing-skills`

**Features**:
- 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 双模式优化（修订模式：95%-120%字数控制；重构模式：大幅调整）
- 多文件留痕输出（5个评审文件 + 1个优化稿）
- 法律法规知识库（100个法规文件，覆盖国家/省/市三级）
- 审计应用指引模板（800-1500字）
- 审计案例启示模板（800-1500字）
- 字数严格控制（修订模式下95%-120%字数控制）

**适用场景**: 需要严格质量控制和多文件留痕的用户，但不需要智能插件

**详细文档**: [audit-book-writing-v2/VERSION.md](audit-book-writing-v2/VERSION.md)

---

#### audit-book-writing-v1 (v1.0 - 基础版)

**Path**: `audit-book-writing-v1/`
**Description**: 审计书籍撰写与评审基础版，提供7阶段工作流和4轮评审系统
**Version**: 1.0
**Dependencies**: None
**Install**: `/plugin install audit-book-writing-v1@cyhzzz/audit-book-writing-skills`

**Features**:
- 7阶段工作流（从项目初始化到最终审校）
- 4轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 标准章节模板（理论章、实务章、案例章、法规解读章）
- 数据验证规范（防止编造数据和引用材料）
- 审计领域分类（财务审计、内部控制审计、合规审计、绩效审计等）

**适用场景**: 快速撰写审计书籍初稿、系统化审计实务指南编写

**详细文档**: [audit-book-writing-v1/VERSION.md](audit-book-writing-v1/VERSION.md)

---

## Version Comparison

| 特性 | v1.0（基础版） | v2.0（增强版） | v3.0（完整版） |
|------|--------------|--------------|--------------|
| 7阶段工作流 | ✅ | ✅ | ✅ |
| 4轮评审系统 | ✅ | ✅ | ✅ |
| 标准章节模板 | ✅ | ✅ | ✅ |
| 数据验证规范 | ✅ | ✅ | ✅ |
| 双模式优化 | ❌ | ✅ | ✅ |
| 多文件留痕输出 | ❌ | ✅ | ✅ |
| 法律法规库（100个文件） | ❌ | ✅ | ✅ |
| 智能插件系统 | ❌ | ❌ | ✅ |
| 法规校对（ChatLaw） | ❌ | ❌ | ✅ |
| 逻辑分析（ai-research-skills） | ❌ | ❌ | ✅ |
| 术语校对（lexnlp） | ❌ | ❌ | ✅ |
| 文献校对（zotero-better-bibtex） | ❌ | ❌ | ✅ |
| 单元测试 | ❌ | ❌ | ✅ |
| 适用场景 | 快速撰写、初学者 | 严格质量控制、多文件留痕 | 专业用户、智能校对 |
| 响应速度 | 最快 | 快快 | 较快（插件处理） |

---

## Installation

### Install All Skills

```bash
# Add marketplace
/plugin marketplace add cyhzzz/audit-book-writing-skills

# Install all skills
/plugin install all-skills@cyhzzz/audit-book-writing-skills
```

### Install Individual Skills

```bash
# v3.0 - 完整版（推荐）
/plugin install audit-book-writing-pro@cyhzzz/audit-book-writing-skills

# v2.0 - 增强版
/plugin install audit-book-writing-v2@cyhzzz/audit-book-writing-skills

# v1.0 - 基础版
/plugin install audit-book-writing-v1@cyhzzz/audit-book-writing-skills
```

---

## Version Management

Skills use git tags for versioning:

| Version | Date | Changes |
|---------|------|---------|
| `v3.0` | 2026-02-27 | 完整版：集成智能插件系统、76个单元测试 |
| `v2.0` | 2026-01-20 | 增强版：双模式优化、多文件留痕、法律法规库 |
| `v1.0` | 2026-01-16 | 基础版：7阶段工作流、4轮评审系统 |

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
| **audit-book-writing-pro** (v3.0) | 审计书籍章节优化 | 专业用户、智能校对、完整质量控制 |
| **audit-book-writing-v2** (v2.0) | 审计书籍章节优化 | 严格质量控制、多文件留痕 |
| **audit-book-writing-v1** (v1.0) | 审计书籍撰写 | 快速撰写、初学者 |

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
├── VERSION.md            # Optional: Version documentation
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
version: 3.0
author: wuying
---
```

---

## Dependencies

### Python Dependencies

For `audit-book-writing-pro` (v3.0) (optional, for advanced features):
```bash
pip install pandas numpy
```

### Sub-Skills (Plugins)

`audit-book-writing-pro` (v3.0) includes bundled plugins:
- `ChatLaw` - 法规校对（基于本地法规库grep搜索）
- `ai-research-skills` - 逻辑性与结构性分析（基于规则）
- `lexnlp` - 术语校对（基于正则表达式）
- `zotero-better-bibtex` - 文献校对（基于规则）

No additional installation required for rule-based versions.

---

## Support

- **Issues**: https://github.com/cyhzzz/audit-book-writing-skills/issues
- **Discussions**: https://github.com/cyhzzz/audit-book-writing-skills/discussions
- **Documentation**: See [README.md](README.md) and individual version VERSION.md files

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

**Last Updated**: 2026-02-27
**Skills Version**: 3.0
**Total Skills**: 3
**Total Plugins**: 4
**Total Laws**: 100
