# Audit Book Writing Pro Skills

<div align="center">

**审计专业书籍撰写、审核、优化完整工具集**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-4.0-blue.svg)](https://github.com/cyhzzz/audit-book-writing-skills)
[![Skills](https://img.shields.io/badge/Skills-4-green.svg)](#available-skills)
[![Plugins](https://img.shields.io/badge/Plugins-4-purple.svg)](#integrated-plugins)
[![Laws](https://img.shields.io/badge/Laws-100-red.svg)](#legal-knowledge-base)

</div>

---

## 📖 概述

**Audit Book Writing Pro Skills** 是专为审计专业书籍设计的完整工具集，提供从撰写、审核到优化的全流程支持。本仓库包含四个版本，用户可以根据需求灵活选择使用。

### 核心特点

- ✅ **智能标记系统** - 8种标记类型（法规条文、条款引用、发文字号、地名案例）
- ✅ **多源法规验证** - 1-8个法规汇总文件交叉验证，确保法规表述准确
- ✅ **权威案例替换** - 从官方网站查找并替换权威案例，标注来源
- ✅ **内容智能扩充** - 基于法规自动补充（条文原文+案例+审计应用）
- ✅ **结构优化整理** - 自动归并重复内容，优化文档结构
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

## 🔄 版本对比

| 特性 | v1.0（基础版） | v2.0（增强版） | v3.0（完整版） | v4.0（校对优化版） |
|------|--------------|--------------|--------------|------------------|
| 7阶段工作流 | ✅ | ✅ | ✅ | ❌ |
| 4轮评审系统 | ✅ | ✅ | ✅ | ❌ |
| 标准章节模板 | ✅ | ✅ | ✅ | ❌ |
| 数据验证规范 | ✅ | ✅ | ✅ | ❌ |
| 智能标记系统（8种） | ❌ | ❌ | ❌ | ✅ |
| 多源法规验证 | ❌ | ❌ | ❌ | ✅ |
| 权威案例替换 | ❌ | ❌ | ❌ | ✅ |
| 内容智能扩充 | ❌ | ❌ | ❌ | ✅ |
| 结构优化整理 | ❌ | ❌ | ❌ | ✅ |
| 双模式优化 | ❌ | ✅ | ✅ | ❌ |
| 多文件留痕输出 | ❌ | ✅ | ✅ | ❌ |
| 法律法规库（100个文件） | ❌ | ✅ | ✅ | ❌ |
| 智能插件系统 | ❌ | ❌ | ✅ | ❌ |
| 法规校对（ChatLaw） | ❌ | ❌ | ✅ | ❌ |
| 逻辑分析（ai-research-skills） | ❌ | ❌ | ✅ | ❌ |
| 术语校对（lexnlp） | ❌ | ❌ | ✅ | ❌ |
| 文献校对（zotero-better-bibtex） | ❌ | ❌ | ✅ | ❌ |
| 单元测试 | ❌ | ❌ | ✅ | ❌ |
| 适用场景 | 快速撰写、初学者 | 严格质量控制、多文件留痕 | 专业用户、智能校对 | 智能校对优化、法规验证 |
| 响应速度 | 最快 | 快快 | 较快（插件处理） | 中等（多阶段处理） |

---

## 🚀 快速开始

### Claude Code 用户（推荐）

```bash
# 添加 marketplace
/plugin marketplace add cyhzzz/audit-book-writing-skills

# 安装所有技能
/plugin install all-skills@cyhzzz/audit-book-writing-skills

# 或安装单个技能
/plugin install audit-book-writing-pro@cyhzzz/audit-book-writing-skills
/plugin install audit-book-writing-v2@cyhzzz/audit-book-writing-skills
/plugin install audit-book-writing-v1@cyhzzz/audit-book-writing-skills
```

### 其他用户

```bash
# 通用安装器
npx ai-agent-skills install cyhzzz/audit-book-writing-skills
```

详细安装指南请参考 [INSTALLATION.md](INSTALLATION.md)

也可直接下载源码，将对应版本的文件夹移动至对应AI应用的skill文件夹内使用，或将文件夹压缩为.skill格式的技能文件根据对应产品的技能安装说明进行安装使用。
---

## 📋 可用技能

### audit-book-writing-pro (v3.0 - 完整版)

**审计专业书籍撰写系统**

**版本**: 3.0
**路径**: `audit-book-writing-pro/`

**核心功能**:
- 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 双模式优化（修订模式：95%-120%字数控制；重构模式：大幅调整）
- 多文件留痕输出（5个评审文件 + 1个优化稿）
- 法律法规知识库（100个法规文件）
- 审计应用指引模板（800-1500字）
- 审计案例启示模板（800-1500字）
- **智能插件系统**（ChatLaw、ai-research-skills、lexnlp、zotero-better-bibtex）

**支持的领域**:
- 文化遗产审计 (Cultural Heritage Audit)
- 财务审计 (Financial Audit)
- 内部控制审计 (Internal Control Audit)
- 内部审计 (Internal Audit)
- 合规审计 (Compliance Audit)

**适用场景**: 专业用户，需要智能插件支持和完整的质量控制

---

### audit-book-writing-v4 (v4.0 - 智能校对优化版)

**审计书籍智能校对优化技能**

**版本**: 4.0
**路径**: `audit-book-writing-v4/`

**核心功能**:
- **智能标记系统** - 8种标记类型（FA1/FA2法规条文、FB1/FB2条款引用、FC1/FC2发文字号、A1/A2地名案例）
- **多源法规验证** - 支持1-8个法规汇总文件交叉验证，自动修正条款序号和文字表述
- **权威案例替换** - 从官方网站查找并替换权威案例（优先级：国家文物局 > 浙江省文物局 > 其他省份文物局）
- **内容智能扩充** - 基于法规自动补充相关内容（法规条文原文 + 相关案例 + 审计应用）
- **结构优化整理** - 自动识别并归并重复内容，优化"审计内容"与"审计重点"分配
- **质量保证系统** - 多维度质量检查（法规准确度、案例权威性、内容完整性、结构清晰度）

**适用场景**:
- 审计书籍章节校对优化
- 法规类文档审核
- 案例型文档标准化
- 审计报告质量提升
- 文档法规合规性检查

**核心优势**:
- 法规准确度 100% - 多源交叉验证，确保法规表述准确无误
- 案例权威性 100% - 强制使用官方网站案例，标注来源网址
- 内容合规性 100% - 严格围绕审计主题，无离题内容
- 效率提升 3-5倍 - 自动化处理，大幅提高校对效率

**详细文档**: [audit-book-writing-v4/SKILL.md](audit-book-writing-v4/SKILL.md) | [audit-book-writing-v4/VERSION.md](audit-book-writing-v4/VERSION.md)

---

### audit-book-writing-v2 (v2.0 - 增强版)

**审计书籍撰写与评审增强版**

**版本**: 2.0
**路径**: `audit-book-writing-v2/`

**核心功能**:
- 四轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 双模式优化（修订模式：95%-120%字数控制；重构模式：大幅调整）
- 多文件留痕输出（5个评审文件 + 1个优化稿）
- 法律法规知识库（100个法规文件）
- 审计应用指引模板（800-1500字）
- 审计案例启示模板（800-1500字）

**适用场景**: 需要严格质量控制和多文件留痕的用户，但不需要智能插件

**详细文档**: [audit-book-writing-v2/VERSION.md](audit-book-writing-v2/VERSION.md)

---

### audit-book-writing-v1 (v1.0 - 基础版)

**审计书籍撰写与评审基础版**

**版本**: 1.0
**路径**: `audit-book-writing-v1/`

**核心功能**:
- 7阶段工作流（从项目初始化到最终审校）
- 4轮评审系统（内容准确性、逻辑连贯性、适用性、格式规范化）
- 标准章节模板（理论章、实务章、案例章、法规解读章）
- 数据验证规范（防止编造数据和引用材料）
- 审计领域分类（财务审计、内部控制审计、合规审计等）

**适用场景**: 快速撰写审计书籍初稿、系统化审计实务指南编写

**详细文档**: [audit-book-writing-v1/VERSION.md](audit-book-writing-v1/VERSION.md)

---

## 🔌 集成插件（v3.0专用）

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

## 📚 法律法规知识库（v2.0和v3.0）

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
- [audit-book-writing-v4/SKILL.md](audit-book-writing-v4/SKILL.md) - v4.0技能说明
- [audit-book-writing-v4/PROJECT-OVERVIEW.md](audit-book-writing-v4/PROJECT-OVERVIEW.md) - v4.0项目概览
- [audit-book-writing-v4/docs/EXAMPLE.md](audit-book-writing-v4/docs/EXAMPLE.md) - v4.0使用示例
- [PROJECT-OVERVIEW.md](audit-book-writing-pro/PROJECT-OVERVIEW.md) - v3.0项目概览
- [audit-book-writing-v2/VERSION.md](audit-book-writing-v2/VERSION.md) - v2.0版本说明
- [audit-book-writing-v1/VERSION.md](audit-book-writing-v1/VERSION.md) - v1.0版本说明

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

### 示例1：使用v3.0优化审计书籍章节（修订模式）

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
2. 调用智能插件（ChatLaw、ai-research-skills、lexnlp、zotero-better-bibtex）
3. 生成5个评审文件 + 1个优化稿
4. 字数控制在原稿的95%-120%

### 示例2：使用v2.0优化审计书籍章节（重构模式）

```
请使用 audit-book-writing-v2 技能，使用重构模式优化以下章节：

# 第5章 内部控制审计

[章节内容...]
```

技能将：
1. 先提取学术观点并等待确认
2. 提出结构优化方案并等待确认
3. 用户确认后执行四轮评审
4. 生成重构后的优化稿
5. 使用法律法规库进行法规校对

### 示例3：使用v1.0快速撰写审计书籍

```
请使用 audit-book-writing-v1 技能，帮我撰写以下章节：

# 第2章 审计的基本概念
- 审计的定义
- 审计的分类
- 审计的功能
```

技能将：
1. 按照7阶段工作流执行
2. 使用标准章节模板
3. 执行4轮评审
4. 生成审计书籍初稿

---

## 📦 项目结构

```
audit-book-writing-skills/
├── README.md                          # 本文件
├── LICENSE                            # MIT License
├── MARKETPLACE.md                     # 技能市场元数据
├── INSTALLATION.md                     # 安装指南
├── audit-book-writing-pro/             # v3.0（完整版）
│   ├── SKILL.md                        # 核心技能文档
│   ├── PROJECT-OVERVIEW.md             # 项目概览
│   ├── references/                     # 参考文件
│   │   ├── audit-book-templates.md     # 审计书籍模板
│   │   ├── audit-knowledge-base.md     # 审计知识库
│   │   ├── domains-workflow.md         # 审计领域工作流
│   │   └── laws-database/             # 法律法规库（100个文件）
│   ├── docs/                          # 文档
│   │   └── phase3-*.md               # Phase 3 实施报告
│   ├── src/                           # 源代码
│   │   └── plugins/                   # 插件系统
│   │       ├── base.py
│   │       ├── manager.py
│   │       ├── chatlaw_adapter.py
│   │       ├── ai_research_skills_adapter.py
│   │       ├── lexnlp_adapter.py
│   │       └── zotero_bibtex_adapter.py
│   ├── tests/                         # 测试
│   │   └── plugins/
│   └── assets/                        # 资源文件
├── audit-book-writing-v2/              # v2.0（增强版）
│   ├── SKILL.md                        # 核心技能文档
│   ├── VERSION.md                      # 版本说明
│   └── references/                     # 参考文件
│       ├── audit-book-templates.md
│       ├── audit-knowledge-base.md
│       ├── domains-workflow.md
│       └── laws-database/             # 法律法规库（100个文件）
├── audit-book-writing-v1/              # v1.0（基础版）
│   ├── SKILL.md                        # 核心技能文档
│   ├── VERSION.md                      # 版本说明
│   ├── WORKFLOW.md                     # 7阶段工作流
│   ├── TEMPLATES.md                    # 模板文件
│   ├── DOMAINS.md                      # 审计领域分类
│   └── DATA_VERIFICATION.md            # 数据验证规范
└── audit-book-writing-v4/              # v4.0（智能校对优化版）
    ├── SKILL.md                        # 核心技能文档
    ├── VERSION.md                      # 版本说明
    ├── README.md                       # 项目说明
    ├── PROJECT-OVERVIEW.md             # 项目概览
    ├── INSTALLATION.md                 # 安装指南
    ├── docs/                           # 文档
    │   └── EXAMPLE.md                # 使用示例
    ├── references/                     # 参考资料
    ├── assets/                        # 资源目录
    ├── src/                           # 源代码目录
    ├── config.yaml                     # 配置文件
    ├── requirements.txt               # Python 依赖
    └── package.json                   # Node.js 配置
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

- **Issues**: https://github.com/cyhzzz/audit-book-writing-skills/issues
- **Discussions**: https://github.com/cyhzzz/audit-book-writing-skills/discussions
- **Documentation**: [审计书籍撰写专业版文档](audit-book-writing-pro/)

---

<div align="center">

**Made with ❤️ for Audit Professionals**

**Powered by OpenClaw**

</div>
