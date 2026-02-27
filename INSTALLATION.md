# Installation Guide - Audit Book Writing Pro Skills

完整的安装指南，适用于 Claude Code 和其他 AI 代码工具。

---

## Table of Contents

- [Quick Start](#quick-start)
- [Claude Code Native Marketplace](#claude-code-native-marketplace-recommended)
- [Universal Installer](#universal-installer)
- [Manual Installation](#manual-installation)
- [Verification & Testing](#verification--testing)
- [Troubleshooting](#troubleshooting)
- [Uninstallation](#uninstallation)

---

## Quick Start

**Choose your installation method:**

### For Claude Code Users (Recommended)

```bash
# Add marketplace
/plugin marketplace add wuying/audit-book-writing-skills

# Install all skills
/plugin install all-skills@audit-book-writing-skills
```

### For All Other Agents (Cursor, VS Code, etc.)

```bash
npx ai-agent-skills install wuying/audit-book-writing-skills
```

---

## Claude Code Native Marketplace (Recommended)

**Best for Claude Code users** - 原生集成，自动更新。

### Step 1: Add Marketplace

```bash
/plugin marketplace add wuying/audit-book-writing-skills
```

### Step 2: Install Skills

#### Install All Skills

```bash
/plugin install all-skills@audit-book-writing-skills
```

#### Install Individual Skills

```bash
# 审计书籍撰写工具
/plugin install audit-book-writing-pro@audit-book-writing-skills
```

### Step 3: Verify Installation

```bash
# List installed skills
/plugin list

# Test a skill
# Start a conversation and use the skill
```

Example in Claude Code:
```
请使用 audit-book-writing-pro 技能，优化以下审计书籍章节...
```

### Update Skills

```bash
# Update all installed plugins
/plugin update

# Update specific plugin
/plugin update audit-book-writing-pro
```

### Remove Skills

```bash
# Remove specific plugin
/plugin remove audit-book-writing-pro

# Remove marketplace
/plugin marketplace remove wuying/audit-book-writing-skills
```

**Benefits:**
- ✅ Native Claude Code integration
- ✅ Automatic updates with `/plugin update`
- ✅ Version management with git tags
- ✅ Managed through Claude Code UI

---

## Universal Installer

通用安装器使用 [ai-agent-skills](https://github.com/skillcreatorai/Ai-Agent-Skills) 包，支持多平台同时安装。

### Install All Skills

```bash
# Install to all supported agents
npx ai-agent-skills install wuying/audit-book-writing-skills
```

**This installs to:**
- Claude Code → `~/.claude/skills/`
- Cursor → `.cursor/skills/`
- VS Code/Copilot → `.github/skills/`
- And more...

### Install to Specific Agent

```bash
# Claude Code only
npx ai-agent-skills install wuying/audit-book-writing-skills --agent claude

# Cursor only
npx ai-agent-skills install wuying/audit-book-writing-skills --agent cursor

# VS Code/Copilot only
npx ai-agent-skills install wuying/audit-book-writing-skills --agent vscode
```

### Install Individual Skills

```bash
# audit-book-writing-pro
npx ai-agent-skills install wuying/audit-book-writing-skills/audit-book-writing-pro
```

### Preview Before Installing

```bash
# Dry run to see what will be installed
npx ai-agent-skills install wuying/audit-book-writing-skills --dry-run
```

---

## Manual Installation

用于开发、定制或离线使用。

### Prerequisites

- **Git**
- **Claude Code** (for using skills)
- **Python 3.8+** (optional, for advanced features)

### Step 1: Clone Repository

```bash
git clone https://github.com/wuying/audit-book-writing-skills.git
cd audit-book-writing-skills
```

### Step 2: Copy to Agent Directory

#### For Claude Code

```bash
# Copy all skills
cp -r audit-book-writing-pro ~/.claude/skills/

# Or copy single skill
cp -r audit-book-writing-pro ~/.claude/skills/
```

#### For Cursor

```bash
# Copy to project directory
mkdir -p .cursor/skills
cp -r audit-book-writing-pro .cursor/skills/
```

#### For VS Code/Copilot

```bash
# Copy to project directory
mkdir -p .github/skills
cp -r audit-book-writing-pro .github/skills/
```

### Step 3: Install Python Dependencies (Optional)

```bash
# Optional: For advanced features
pip install pandas numpy
```

**Note:** The core functionality works without any external dependencies. Python packages are optional for advanced features.

---

## Verification & Testing

### Verify Installation

```bash
# Check Claude Code installation
ls ~/.claude/skills/

# You should see:
# - audit-book-writing-pro/

# Verify skill structure
ls -la ~/.claude/skills/audit-book-writing-pro/

# You should see:
# SKILL.md
# PROJECT-OVERVIEW.md
# references/
# src/
# docs/
# tests/
```

### Test Skill Usage

In Claude Code:
```
请使用 audit-book-writing-pro 技能，帮我优化以下审计书籍章节：

# 第X章 审计的基本概念

[章节内容...]
```

The skill should:
1. Ask for the optimization mode (修订模式 or 重构模式)
2. Execute four rounds of review
3. Generate optimization outputs
4. Create 5 review files + 1 optimized draft

### Test Plugin System

The skill includes 4 bundled plugins (rule-based, no external dependencies):

1. **ChatLaw** - 法规校对
2. **ai-research-skills** - 逻辑性与结构性分析
3. **lexnlp** - 术语校对
4. **zotero-better-bibtex** - 文献校对

All plugins are self-contained and work without external API calls.

---

## Troubleshooting

### Issue: "Command not found: npx"

**Solution:** Install Node.js and npm

```bash
# macOS
brew install node

# Ubuntu/Debian
sudo apt-get install nodejs npm

# Windows
# Download from https://nodejs.org/
```

### Issue: "Skills not showing in Claude Code"

**Solution:** Verify installation and restart

```bash
# Check installation
ls -la ~/.claude/skills/

# Verify SKILL.md exists
cat ~/.claude/skills/audit-book-writing-pro/SKILL.md

# Restart Claude Code
```

### Issue: "Law database not found"

**Solution:** Verify references/laws-database/ exists

```bash
# Check laws database
ls -la ~/.claude/skills/audit-book-writing-pro/references/laws-database/

# You should see 100+ .md files

# If missing, re-install the skill
/plugin remove audit-book-writing-pro
/plugin install audit-book-writing-pro@audit-book-writing-skills
```

### Issue: "Marketplace not found"

**Solution:** Check repository URL

```bash
# Verify repository exists
curl https://github.com/wuying/audit-book-writing-skills

# Try removing and re-adding
/plugin marketplace remove wuying/audit-book-writing-skills
/plugin marketplace add wuying/audit-book-writing-skills
```

### Issue: "Python module not found"

**Solution:** Install dependencies (optional)

```bash
# For advanced features
pip install pandas numpy

# Or skip Python dependencies
# The core functionality works without them
```

### Issue: "Plugin not working"

**Solution:** Check plugin initialization

```bash
# Verify plugin files exist
ls -la ~/.claude/skills/audit-book-writing-pro/src/plugins/

# You should see:
# base.py
# manager.py
# chatlaw_adapter.py
# ai_research_skills_adapter.py
# lexnlp_adapter.py
# zotero_bibtex_adapter.py

# All plugins are rule-based, no external dependencies required
```

---

## Uninstallation

### Claude Code Native Marketplace

```bash
# Remove specific skill
/plugin remove audit-book-writing-pro

# Remove marketplace
/plugin marketplace remove wuying/audit-book-writing-skills
```

### Universal Installer

```bash
# Remove from Claude Code
rm -rf ~/.claude/skills/audit-book-writing-pro/

# Remove from Cursor
rm -rf .cursor/skills/audit-book-writing-pro/

# Remove from VS Code
rm -rf .github/skills/audit-book-writing-pro/
```

### Manual Installation

```bash
# Remove cloned directory
rm -rf audit-book-writing-skills/

# Remove copied skills
rm -rf ~/.claude/skills/audit-book-writing-pro/
```

---

## Advanced: Installation Locations Reference

| Agent | Default Location | Flag | Notes |
|-------|------------------|------|-------|
| **Claude Code** | `~/.claude/skills/` | `--agent claude` | User-level installation |
| **Cursor** | `.cursor/skills/` | `--agent cursor` | Project-level installation |
| **VS Code/Copilot** | `.github/skills/` | `--agent vscode` | Project-level installation |
| **Project** | `.skills/` | `--agent project` | Portable, project-specific |

---

## Skill Features

### audit-book-writing-pro

**Core Features:**
- ✅ 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- ✅ 双模式优化（修订模式、重构模式）
- ✅ 多文件留痕输出（5个评审文件 + 1个优化稿）
- ✅ 法律法规知识库（100个法规文件）
- ✅ 审计应用指引模板（800-1500字）
- ✅ 审计案例启示模板（800-1500字）

**Integrated Plugins (Phase 3):**
- ✅ ChatLaw - 法规校对（基于本地法规库grep搜索）
- ✅ ai-research-skills - 逻辑性与结构性分析（基于规则）
- ✅ lexnlp - 术语校对（基于正则表达式）
- ✅ zotero-better-bibtex - 文献校对（基于规则）

**Performance:**
- All plugins are rule-based
- No external API calls required
- Fast response time (< 3 seconds per plugin)
- 76 unit tests with 98.7% pass rate

**Supported Domains:**
- 文化遗产审计 (Cultural Heritage Audit)
- 财务审计 (Financial Audit)
- 内部控制审计 (Internal Control Audit)
- 内部审计 (Internal Audit)
- 合规审计 (Compliance Audit)

---

## Support

**Installation Issues?**
- Check [Troubleshooting](#troubleshooting) section above
- Review [ai-agent-skills documentation](https://github.com/skillcreatorai/Ai-Agent-Skills)
- Open issue: https://github.com/wuying/audit-book-writing-skills/issues

**Feature Requests:**
- Submit via GitHub Issues with `enhancement` label

**Questions:**
- Start a discussion: https://github.com/wuying/audit-book-writing-skills/discussions

---

**Last Updated:** 2026-02-27
**Skills Version:** 1.0.0
**Total Skills:** 1
**Total Plugins:** 4
**Total Laws:** 100
**Universal Installer:** [ai-agent-skills](https://github.com/skillcreatorai/Ai-Agent-Skills)
