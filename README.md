# Audit Book Writing Pro Skills

<div align="center">

**审计专业书籍撰写、审核、优化完整工具集**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/wuying/audit-book-writing-skills)
[![Skills](https://img.shields.io/badge/Skills-1-green.svg)](#available-skills)
[![Plugins](https://img.shields.io/badge/Plugins-4-purple.svg)](#integrated-plugins)
[![Laws](https://img.shields.io/badge/Laws-100-red.svg)](#legal-knowledge-base)

</div>

---

## 📖 概述

**Audit Book Writing Pro Skills** 是专为审计专业书籍设计的完整工具集，提供从撰写、审核到优化的全流程支持。

### 核心特点

- ✅ **四轮评审系统** - 内容准确性、逻辑连贯性、适用性、格式规范化
- ✅ **双模式优化** - 修订模式（保守优化）和重构模式（大幅调整）
- ✅ **多文件留痕输出** - 5个评审文件 + 1个优化稿
- ✅ **法律法规知识库** - 100个法规文件，覆盖国家/省/市三级
- ✅ **智能插件系统** - ChatLaw、ai-research-skills、lexnlp、zotero-better-bibtex

### 适用场景

- 📚 审计书籍章节优化（文化遗产审计、财务审计、内部审计等）
- 📝 审计实务指南编写
- 📊 审计案例分析
- ⚖️ 审计法规解读
- 🎯 审计综述撰写

---

## 🚀 快速开始

### Claude Code 用户（推荐）

```bash
# 添加 marketplace
/plugin marketplace add wuying/audit-book-writing-skills

# 安装所有技能
/plugin install all-skills@audit-book-writing-skills
```

### 其他用户

```bash
# 通用安装器
npx ai-agent-skills install wuying/audit-book-writing-skills
```

详细安装指南请参考 [INSTALLATION.md](INSTALLATION.md)

---

## 📋 可用技能

### audit-book-writing-pro

**审计专业书籍撰写系统**

**版本**: 1.0.0
**路径**: `audit-book-writing-pro/`

**核心功能**:
- 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 双模式优化（修订模式：95%-120%字数控制；重构模式：大幅调整）
- 多文件留痕输出（5个评审文件 + 1个优化稿）
- 法律法规知识库（100个法规文件）
- 审计应用指引模板（800-1500字）
- 审计案例启示模板（800-1500字）

**支持的领域**:
- 文化遗产审计 (Cultural Heritage Audit)
- 财务审计 (Financial Audit)
- 内部控制审计 (Internal Control Audit)
- 内部审计 (Internal Audit)
- 合规审计 (Compliance Audit)

---

## 🔌 集成插件

### Phase 3 插件系统

| 插件 | 功能 | 响应时间 | 状态 |
|------|------|---------|------|
| **ChatLaw** | 法规校对（基于本地法规库grep搜索） | ~2秒 | ✅ 完成 |
| **ai-research-skills** | 逻辑性与结构性分析（基于规则） | ~2秒 | ✅ 完成 |
| **lexnlp** | 术语校对（基于正则表达式） | ~1秒 | ✅ 完成 |
| **zotero-better-bibtex** | 文献校对（基于规则） | <1秒 | ✅ 完成 |

**性能特点**:
- 所有插件均基于规则和正则表达式
- 无需外部AI服务调用
- 响应快速稳定（< 3秒/插件）
- 76个单元测试，通过率98.7%

---

## 📚 法律法规知识库

### 知识库统计

| 级别 | 数量 | 说明 |
|------|------|------|
| 国家层面 | 47个 | 全国人大、国务院及其部门颁布 |
| 浙江省 | 14个 | 浙江省地方法规 |
| 台州市 | 4个 | 台州市地方规范 |
| 国际公约 | 2个 | 联合国教科文组织等国际组织 |
| 其他 | 33个 | 其他相关法规 |

**总计**: 100个法规文件

### 核心法规

1. 中华人民共和国文物保护法（2024修正）
2. 中华人民共和国非物质文化遗产法
3. 历史文化名城名镇名村保护条例
4. 文物保护工程管理办法
5. 博物馆管理办法

---

## 📖 文档

- [MARKETPLACE.md](MARKETPLACE.md) - 技能市场元数据
- [INSTALLATION.md](INSTALLATION.md) - 完整安装指南
- [PROJECT-OVERVIEW.md](audit-book-writing-pro/PROJECT-OVERVIEW.md) - 项目概览
- [SKILL.md](audit-book-writing-pro/SKILL.md) - 核心技能文档

### Phase 3 实施报告

- [Phase 3 第1步：集成ChatLaw](audit-book-writing-pro/docs/phase3-step1-集成ChatLaw实施报告.md)
- [Phase 3 第2步：集成ai-research-skills](audit-book-writing-pro/docs/phase3-step2-集成ai-research-skills实施报告.md)
- [Phase 3 第3步：集成lexnlp](audit-book-writing-pro/docs/phase3-step3-集成lexnlp实施报告.md)
- [Phase 3 第4步：集成zotero-better-bibtex](audit-book-writing-pro/docs/phase3-step4-集成zotero-better-bibtex实施报告.md)

---

## 🎯 核心原则

### ⚠️ 数据验证原则（最高优先级）

**绝对禁止编造任何内容、数据或引用材料**

#### 法律法规引用要求
- ✅ 必须使用法律法规库查询（Grep在法规库中查询）
- ✅ 引用格式必须完整
- ❌ 禁止编造或猜测法律条款

#### 数据验证优先级
```
优先级1（最高）：法律法规库 → 使用Grep在法规库中查询
优先级2（中等）：联网查询 → 使用WebSearch查询权威网站
优先级3（保底）：标注待核实 → 明确标注需要人工核对
```

### ⚠️ 字数控制原则（严格标准）

**修订模式**: 优化稿字符数必须控制在原稿的 **95%-120%** 区间内

```
原稿字符数 = X
优化稿字符数 = Y
比例 = Y / X × 100%

合格标准：95% ≤ 比例 ≤ 120%
```

### ⚠️ 模式选择原则

- **修订模式**: 适用于原稿有明确框架和核心观点（保留原稿核心观点和内涵）
- **重构模式**: 适用于原稿结构混乱或观点不明确（必须先确认观点和结构）

---

## 💡 使用示例

### 示例1：优化审计书籍章节（修订模式）

```
请使用 audit-book-writing-pro 技能，使用修订模式优化以下章节：

# 第3章 文化遗产审计的基本概念

文化遗产审计是指对文化遗产保护、管理、利用情况进行
独立、客观的检查和评价的活动。

根据《中华人民共和国文物保护法》规定，文化遗产
保护应当遵循保护为主、抢救第一、合理利用、加强
管理的方针。
```

技能将：
1. 执行四轮评审（内容准确性、逻辑连贯性、适用性、格式规范化）
2. 生成5个评审文件 + 1个优化稿
3. 字数控制在原稿的95%-120%

### 示例2：优化审计书籍章节（重构模式）

```
请使用 audit-book-writing-pro 技能，使用重构模式优化以下章节：

# 第5章 内部控制审计

[章节内容...]
```

技能将：
1. 先提取学术观点并等待确认
2. 提出结构优化方案并等待确认
3. 用户确认后执行四轮评审
4. 生成重构后的优化稿

---

## 🧪 测试

### 运行单元测试

```bash
cd audit-book-writing-pro

# 运行所有测试
python3 run_tests.py

# 运行特定插件测试
python3 tests/plugins/test_chatlaw_adapter.py
python3 tests/plugins/test_ai_research_skills_adapter.py
python3 tests/plugins/test_lexnlp_adapter.py
python3 tests/plugins/test_zotero_bibtex_adapter.py
```

### 测试统计

| 插件 | 测试用例数 | 通过率 |
|------|-----------|--------|
| ChatLaw | 17 | 100% |
| ai-research-skills | 17 | 94% |
| lexnlp | 21 | 100% |
| zotero-better-bibtex | 21 | 100% |
| **总计** | **76** | **98.7%** |

---

## 📦 项目结构

```
audit-book-writing-skills/
├── README.md                          # 本文件
├── LICENSE                            # MIT License
├── MARKETPLACE.md                     # 技能市场元数据
├── INSTALLATION.md                     # 安装指南
└── audit-book-writing-pro/             # 主技能
    ├── SKILL.md                        # 核心技能文档
    ├── PROJECT-OVERVIEW.md             # 项目概览
    ├── references/                     # 参考文件
    │   ├── audit-book-templates.md     # 审计书籍模板
    │   ├── audit-knowledge-base.md     # 审计知识库
    │   ├── domains-workflow.md         # 审计领域工作流
    │   └── laws-database/             # 法律法规库（100个文件）
    ├── docs/                          # 文档
    │   └── phase3-*.md               # Phase 3 实施报告
    ├── src/                           # 源代码
    │   └── plugins/                   # 插件系统
    │       ├── base.py                # 插件基类
    │       ├── manager.py             # 插件管理器
    │       ├── chatlaw_adapter.py     # ChatLaw适配器
    │       ├── ai_research_skills_adapter.py  # ai-research-skills适配器
    │       ├── lexnlp_adapter.py      # lexnlp适配器
    │       └── zotero_bibtex_adapter.py # zotero-better-bibtex适配器
    ├── tests/                         # 测试
    │   └── plugins/
    │       ├── test_chatlaw_adapter.py
    │       ├── test_ai_research_skills_adapter.py
    │       ├── test_lexnlp_adapter.py
    │       └── test_zotero_bibtex_adapter.py
    └── assets/                        # 资源文件
```

---

## 🤝 贡献

欢迎贡献代码、报告问题或提出新功能建议！

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 开发指南

- 参考 [MARKETPLACE.md](MARKETPLACE.md#development) 添加新技能
- 遵循现有的代码规范和文档格式
- 为新功能添加单元测试
- 更新相关文档

---

## 📝 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

---

## 📧 支持

- **Issues**: https://github.com/wuying/audit-book-writing-skills/issues
- **Discussions**: https://github.com/wuying/audit-book-writing-skills/discussions
- **Documentation**: [审计书籍撰写专业版文档](audit-book-writing-pro/)

---

## 🙏 致谢

- 参考了 [finance_aigc_skills](https://github.com/cyhzzz/finance_aigc_skills) 的多技能仓库框架
- 感谢所有为审计专业写作工具做出贡献的开发者

---

<div align="center">

**Made with ❤️ for Audit Professionals**

**Powered by OpenClaw**

</div>
