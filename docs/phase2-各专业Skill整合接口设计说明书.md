# 各专业Skill整合接口设计说明书

## 文档信息
- **生成时间**: 2026-02-27
- **版本**: V1.0
- **状态**: 待确认

---

## 一、整合模式总览

### 1.1 整合模式分类

基于各Skill的特点，我们采用两种主要的整合模式：

| 模式 | 描述 | 适用Skill | 优势 |
|------|------|---------|------|
| **包装模式** | 为Skill创建统一的适配器（Wrapper），使其接口与现有框架兼容 | ChatLaw, zotero-better-bibtex | 低侵入、易维护、可替换 |
| **流水线模式** | 将Skill的处理能力作为流水线的一个环节，串联整个处理流程 | ai-research-skills, lexnlp | 灵活组合、易于扩展 |

### 1.2 整合模式对比

```
┌─────────────────────────────────────────────────────────────────────┐
│                          包装模式                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌─────────────────────┐  │
│  │ 现有框架    │───→│  适配器      │───→│  Skill插件          │  │
│  │ (Framework) │    │ (Wrapper)    │    │  (ChatLaw等)       │  │
│  └──────────────┘    └──────────────┘    └─────────────────────┘  │
│                                                              │
│  优点：低侵入、易维护、可替换                                   │
│  缺点：需要编写适配器代码                                       │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                         流水线模式                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ 现有流程1   │→ │ Skill插件A   │→ │ 现有流程2   │→ ...     │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                              │
│  优点：灵活组合、易于扩展、并行处理                               │
│  缺点：需要设计流水线编排器                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 二、Skill整合模式设计

### 2.1 ai-research-skills: 流水线模式

#### 2.1.1 集成位置

```
修订模式流水线：
原稿 → 第1轮评审 → [ai-research-skills] → 第2轮评审 → 第3轮评审 → 第4轮评审 → ...

重构模式流水线：
原稿 → 观点确认 → 结构确认 → 第1轮评审 → [ai-research-skills] → 第2轮评审 → ...
```

#### 2.1.2 调用时机

- **修订模式**: 在第2轮评审（逻辑连贯性审查）之后
- **重构模式**: 在第2轮评审（逻辑连贯性审查）之后

#### 2.1.3 接口规范

##### 输入接口
```yaml
name: ai_research_skills_input
description: ai-research-skills 处理输入

fields:
  content:
    type: string
    required: true
    description: 章节内容

  chapter_type:
    type: enum
    required: false
    values: [theoretical, practical, case_study]
    description: 章节类型

  context:
    type: object
    required: false
    description: 上下文信息
    properties:
      chapter_id:
        type: string
        description: 章节ID

      book_title:
        type: string
        description: 书籍标题

      previous_chapters:
        type: array
        description: 前几章的内容摘要

      next_chapters:
        type: array
        description: 后几章的内容摘要

  options:
    type: object
    required: false
    description: 处理选项
    properties:
      strict_mode:
        type: boolean
        default: false
        description: 严格模式

      quality_threshold:
        type: float
        default: 0.7
        description: 质量阈值

      enable_cross_chapter:
        type: boolean
        default: true
        description: 启用跨章节分析

      max_suggestions:
        type: integer
        default: 5
        description: 最大建议数量
```

##### 输出接口
```yaml
name: ai_research_skills_output
description: ai-research-skills 处理输出

fields:
  structure_analysis:
    type: object
    required: true
    description: 章节结构分析
    properties:
      detected_type:
        type: enum
        values: [theoretical, practical, case_study, mixed]
        description: 检测到的章节类型

      confidence:
        type: float
        description: 置信度（0-1）

      suggestions:
        type: array
        description: 结构优化建议
        items:
          type: object
          properties:
            type:
              type: string
              description: 建议类型

            message:
              type: string
              description: 建议内容

            severity:
              type: string
              description: 严重程度

  logic_analysis:
    type: object
    required: true
    description: 逻辑连贯性分析
    properties:
      coherence_score:
        type: float
        description: 逻辑连贯性得分（0-1）

      issues:
        type: array
        description: 逻辑问题列表
        items:
          type: object
          properties:
            type:
              type: string
              description: 问题类型

            location:
              type: string
              description: 问题位置

            message:
              type: string
              description: 问题描述

            severity:
              type: string
              description: 严重程度

      improvements:
        type: array
        description: 改进建议列表

  quality_assessment:
    type: object
    required: true
    description: 内容质量评估
    properties:
      overall_score:
        type: float
        description: 整体质量得分（0-1）

      dimensions:
        type: object
        description: 各维度得分
        properties:
          clarity:
            type: float
            description: 清晰度得分

          completeness:
            type: float
            description: 完整性得分

          consistency:
            type: float
            description: 一致性得分

          readability:
            type: float
            description: 可读性得分

      strengths:
        type: array
        description: 优点列表

      weaknesses:
        type: array
        description: 不足列表

  cross_chapter_analysis:
    type: object
    required: false
    description: 跨章节分析
    properties:
      relations:
        type: array
        description: 与其他章节的关系
        items:
          type: object
          properties:
            chapter_id:
              type: string
              description: 相关章节ID

            relation_type:
              type: string
              description: 关系类型

            strength:
              type: float
              description: 关联强度

      duplicates:
        type: array
        description: 重复内容列表
        items:
          type: object
          properties:
            content:
              type: string
              description: 重复内容

            locations:
              type: array
              description: 重复位置列表

            similarity:
              type: float
              description: 相似度

  metadata:
    type: object
    required: true
    description: 元数据
    properties:
      processing_time:
        type: float
        description: 处理时间（秒）

      model_version:
        type: string
        description: 模型版本

      timestamp:
        type: string
        description: 时间戳
```

#### 2.1.4 错误处理

```python
class AIResearchSkillsError(Exception):
    """ai-research-skills 错误基类"""

    class InitializationError(Exception):
        """初始化错误"""

    class ProcessingError(Exception):
        """处理错误"""

    class APIError(Exception):
        """API错误"""

    class TimeoutError(Exception):
        """超时错误"""
```

#### 2.1.5 降级策略

当 ai-research-skills 调用失败时，采用以下降级策略：

1. **API失败**: 降级到基础逻辑分析（基于规则）
2. **超时**: 返回部分结果，标记为不完整
3. **严重错误**: 跳过该步骤，记录错误日志

```python
def fallback_logic_analysis(content: str) -> dict:
    """降级逻辑分析（基于规则）"""
    # 实现基于规则的逻辑分析
    pass
```

---

### 2.2 ChatLaw: 包装模式

#### 2.2.1 集成位置

```
第1轮评审（内容准确性审查）：
├─ 法规引用准确性检查
│  └─ 提取所有法规引用 → [ChatLaw验证] → 验证结果
├─ 概念定义准确性检查
├─ 数据支撑准确性检查
└─ 事实陈述准确性检查
```

#### 2.2.2 调用时机

- **修订模式**: 在第1轮评审（内容准确性审查）中的"法规引用准确性"检查时
- **重构模式**: 在第1轮评审（内容准确性审查）中的"法规引用准确性"检查时

#### 2.2.3 接口规范

##### 输入接口
```yaml
name: chatlaw_input
description: ChatLaw 法规验证输入

fields:
  citations:
    type: array
    required: true
    description: 法规引用列表
    items:
      type: object
      properties:
        law_name:
          type: string
          required: true
          description: 法规全称

        year:
          type: string
          required: true
          description: 年份

        article:
          type: string
          required: true
          description: 条款号

        content:
          type: string
          required: false
          description: 引用的条款内容

        source_text:
          type: string
          required: false
          description: 原文中的引用文本

        location:
          type: object
          required: false
          description: 引用位置
          properties:
            page:
              type: integer
              description: 页码

            line:
              type: integer
              description: 行号

  options:
    type: object
    required: false
    description: 验证选项
    properties:
      strict_mode:
        type: boolean
        default: true
        description: 严格模式（所有引用必须验证通过）

      auto_fix:
        type: boolean
        default: false
        description: 自动修正（尝试自动修正错误引用）

      warn_expired:
        type: boolean
        default: true
        description: 警告失效引用

      check_effectiveness:
        type: boolean
        default: true
        description: 检查法规有效性

      update_check_interval:
        type: string
        default: 24h
        description: 法规更新检查间隔
```

##### 输出接口
```yaml
name: chatlaw_output
description: ChatLaw 法规验证输出

fields:
  validation_results:
    type: object
    required: true
    description: 验证结果汇总
    properties:
      total_count:
        type: integer
        description: 总引用数量

      valid_count:
        type: integer
        description: 有效引用数量

      invalid_count:
        type: integer
        description: 无效引用数量

      expired_count:
        type: integer
        description: 失效引用数量

      warning_count:
        type: integer
        description: 警告数量

  details:
    type: array
    required: true
    description: 详细验证结果
    items:
      type: object
      properties:
        original_citation:
          type: object
          description: 原始引用
          properties:
            law_name:
              type: string
              description: 法规全称

            year:
              type: string
              description: 年份

            article:
              type: string
              description: 条款号

        validation:
          type: object
          required: true
          description: 验证结果
          properties:
            status:
              type: enum
              values: [valid, invalid, expired, warning]
              description: 验证状态

            confidence:
              type: float
              description: 置信度（0-1）

            matched_law:
              type: object
              description: 匹配到的法规
              properties:
                name:
                  type: string
                  description: 法规名称

                source:
                  type: string
                  description: 法规来源

                update_date:
                  type: string
                  description: 最近更新日期

                effective:
                  type: boolean
                  description: 是否现行有效

            matched_article:
              type: object
              description: 匹配到的条款
              properties:
                number:
                  type: string
                  description: 条款号

                content:
                  type: string
                  description: 条款内容

        issues:
          type: array
          description: 问题列表
          items:
            type: object
            properties:
              type:
                type: string
                description: 问题类型

              message:
                type: string
                description: 问题描述

              severity:
                type: string
                description: 严重程度

        suggestions:
          type: array
          description: 修正建议
          items:
            type: object
            properties:
              type:
                type: string
                description: 建议类型

              suggestion:
                type: string
                description: 建议内容

              auto_fix:
                type: boolean
                description: 是否可自动修正

  law_updates:
    type: array
    required: false
    description: 法规更新信息
    items:
      type: object
      properties:
        law_name:
          type: string
          description: 法规名称

        update_type:
          type: enum
          values: [amended, revised, repealed, promulgated]
          description: 更新类型

        update_date:
          type: string
          description: 更新日期

        new_version:
          type: string
          description: 新版本

        summary:
          type: string
          description: 更新摘要

  metadata:
    type: object
    required: true
    description: 元数据
    properties:
      processing_time:
        type: float
        description: 处理时间（秒）

      api_version:
        type: string
        description: API版本

      timestamp:
        type: string
        description: 时间戳
```

#### 2.2.4 错误处理

```python
class ChatLawError(Exception):
    """ChatLaw 错误基类"""

    class InitializationError(Exception):
        """初始化错误"""

    class APICallError(Exception):
        """API调用错误"""

    class ValidationError(Exception):
        """验证错误"""

    class LawNotFoundError(Exception):
        """法规未找到"""

    class ArticleNotFoundError(Exception):
        """条款未找到"""

    class TimeoutError(Exception):
        """超时错误"""
```

#### 2.2.5 降级策略

当 ChatLaw 调用失败时，采用以下降级策略：

1. **API失败**: 降级到本地法规库查询（Grep）
2. **法规未找到**: 标记为"待人工核实"，继续处理
3. **超时**: 返回部分验证结果，标记为不完整

```python
def fallback_law_validation(citation: dict) -> dict:
    """降级法规验证（使用本地Grep）"""
    # 使用本地法规库进行简单验证
    pattern = f"{citation['law_name']}"
    result = grep_search(pattern, path="references/laws-database/*.md")
    return {
        'status': 'pending' if not result else 'valid',
        'source': 'local'
    }
```

---

### 2.3 lexnlp: 流水线模式

#### 2.3.1 集成位置

```
优化稿生成后 → 后处理流程：
└─ [lexnlp术语校对] → [lexnlp法律分析] → [lexnlp条文抽取] → 最终优化稿
```

#### 2.3.2 调用时机

- **修订模式**: 在生成优化稿之后、生成完成报告之前
- **重构模式**: 在生成优化稿之后、生成完成报告之前

#### 2.3.3 接口规范

##### 输入接口
```yaml
name: lexnlp_input
description: lexnlp 处理输入

fields:
  text:
    type: string
    required: true
    description: 文本内容

  domain:
    type: enum
    required: true
    values: [financial_audit, internal_control, cultural_heritage, internal_audit, compliance]
    description: 审计领域

  glossary:
    type: array
    required: false
    description: 自定义术语库
    items:
      type: object
      properties:
        term:
          type: string
          required: true
          description: 术语

        definition:
          type: string
          description: 定义

        synonyms:
          type: array
          description: 同义词列表

  options:
    type: object
    required: false
    description: 处理选项
    properties:
      strict_mode:
        type: boolean
        default: false
        description: 严格模式

      consistency_threshold:
        type: float
        default: 0.8
        description: 一致性阈值

      enable_synonym_check:
        type: boolean
        default: true
        description: 启用同义词检查

      enable_ambiguity_detection:
        type: boolean
        default: true
        description: 启用歧义检测

      extract_articles:
        type: boolean
        default: true
        description: 抽取法律条文

      extract_entities:
        type: boolean
        default: true
        description: 抽取法律实体
```

##### 输出接口
```yaml
name: lexnlp_output
description: lexnlp 处理输出

fields:
  terminology_check:
    type: object
    required: true
    description: 术语校对结果
    properties:
      terms:
        type: array
        description: 识别的术语列表
        items:
          type: object
          properties:
            term:
              type: string
              description: 术语

            count:
              type: integer
              description: 出现次数

            synonyms:
              type: array
              description: 同义词列表

            consistency:
              type: float
              description: 一致性得分（0-1）

            issues:
              type: array
              description: 不一致问题列表
              items:
                type: object
                properties:
                  type:
                    type: string
                    description: 问题类型

                  location:
                    type: string
                    description: 问题位置

                  message:
                    type: string
                    description: 问题描述

      overall_consistency:
        type: float
        description: 整体一致性得分（0-1）

      suggestions:
        type: array
        description: 统一建议

  legal_analysis:
    type: object
    required: true
    description: 法律分析结果
    properties:
      entities:
        type: array
        description: 识别的法律实体
        items:
          type: object
          properties:
            type:
              type: enum
              values: [law, article, subject, date, amount, organization]
              description: 实体类型

            text:
              type: string
              description: 实体文本

            span:
              type: object
              description: 文本位置
              properties:
                start:
                  type: integer
                  description: 起始位置

                end:
                  type: integer
                  description: 结束位置

            confidence:
              type: float
              description: 置信度（0-1）

            normalized:
              type: string
              description: 规范化后的实体

      sentences:
        type: array
        description: 法律句子分析
        items:
          type: object
          properties:
            text:
              type: string
              description: 句子文本

            legal_complexity:
              type: float
              description: 法律复杂度（0-1）

            key_entities:
              type: array
              description: 关键实体列表

  article_extraction:
    type: object
    required: false
    description: 法律条文抽取结果
    properties:
      articles:
        type: array
        description: 抽取的条文
        items:
          type: object
          properties:
            citation:
              type: object
              description: 法规引用
              properties:
                law_name:
                  type: string
                  description: 法规全称

                year:
                  type: string
                  description: 年份

                article:
                  type: string
                  description: 条款号

            content:
              type: string
              description: 条文内容

            confidence:
              type: float
              description: 置信度（0-1）

            source:
              type: string
              description: 抽取来源（lexnlp/ChatLaw）

      summary:
        type: object
        description: 抽取总结
        properties:
          total_count:
            type: integer
            description: 总条文数

          unique_laws:
            type: integer
            description: 涉及的法规数量

          coverage:
            type: float
            description: 覆盖率（0-1）

  metadata:
    type: object
    required: true
    description: 元数据
    properties:
      processing_time:
        type: float
        description: 处理时间（秒）

      model_version:
        type: string
        description: 模型版本

      timestamp:
        type: string
        description: 时间戳
```

#### 2.3.4 错误处理

```python
class LexNLPError(Exception):
    """lexnlp 错误基类"""

    class InitializationError(Exception):
        """初始化错误"""

    class ProcessingError(Exception):
        """处理错误"""

    class APIError(Exception):
        """API错误"""

    class EntityExtractionError(Exception):
        """实体抽取错误"""

    class TimeoutError(Exception):
        """超时错误"""
```

#### 2.3.5 降级策略

当 lexnlp 调用失败时，采用以下降级策略：

1. **API失败**: 跳过术语校对，记录警告
2. **实体抽取失败**: 使用正则表达式简单抽取
3. **超时**: 返回部分处理结果

```python
def fallback_terminology_check(text: str) -> dict:
    """降级术语校对（基于规则）"""
    # 使用简单的关键词匹配进行术语检查
    pass
```

---

### 2.4 zotero-better-bibtex: 包装模式

#### 2.4.1 集成位置

```
生成完成报告之前 → 出版准备流程：
└─ [zotero-better-bibtex] → 参考文献 + 脚注 → 完成报告
```

#### 2.4.2 调用时机

- **修订模式**: 在生成完成报告之前
- **重构模式**: 在生成完成报告之前

#### 2.4.3 接口规范

##### 输入接口
```yaml
name: zotero_bibtex_input
description: zotero-better-bibtex 处理输入

fields:
  citations:
    type: array
    required: true
    description: 引用列表
    items:
      type: object
      properties:
        type:
          type: enum
          values: [law, academic, book, article, report, website]
          required: true
          description: 引用类型

        title:
          type: string
          required: true
          description: 标题

        authors:
          type: array
          required: false
          description: 作者列表
          items:
            type: string

        year:
          type: string
          required: false
          description: 年份

        journal:
          type: string
          required: false
          description: 期刊名

        volume:
          type: string
          required: false
          description: 卷号

        issue:
          type: string
          required: false
          description: 期号

        pages:
          type: string
          required: false
          description: 页码

        publisher:
          type: string
          required: false
          description: 出版社

        url:
          type: string
          required: false
          description: URL

        doi:
          type: string
          required: false
          description: DOI

        custom_fields:
          type: object
          required: false
          description: 自定义字段

  footnotes:
    type: array
    required: false
    description: 脚注列表
    items:
      type: object
      properties:
        number:
          type: integer
          required: true
          description: 编号

        content:
          type: string
          required: true
          description: 内容

        location:
          type: object
          required: false
          description: 位置信息
          properties:
            page:
              type: integer
              description: 页码

            section:
              type: string
              description: 章节

        reference_id:
          type: string
          required: false
          description: 关联的参考文献ID

  format:
    type: enum
    required: false
    values: [APA, MLA, Chicago, GB/T7714, IEEE]
    default: APA
    description: 输出格式

  options:
    type: object
    required: false
    description: 处理选项
    properties:
      auto_numbering:
        type: boolean
        default: true
        description: 自动编号

      cross_ref_check:
        type: boolean
        default: true
        description: 跨文件引用检查

      latex_mode:
        type: boolean
        default: false
        description: LaTeX模式

      custom_style:
        type: string
        required: false
        description: 自定义样式

      sort_by:
        type: enum
        values: [author, date, citation_order]
        default: citation_order
        description: 排序方式

      include_url:
        type: boolean
        default: true
        description: 包含URL
```

##### 输出接口
```yaml
name: zotero_bibtex_output
description: zotero-better-bibtex 处理输出

fields:
  bibliography:
    type: object
    required: true
    description: 参考文献列表
    properties:
      format:
        type: string
        description: 格式名称

      entries:
        type: array
        description: 参考文献条目
        items:
          type: object
          properties:
            index:
              type: integer
              description: 编号

            citation:
              type: string
              description: 格式化后的引用

            metadata:
              type: object
              description: 元数据
              properties:
                type:
                  type: string
                  description: 引用类型

                title:
                  type: string
                  description: 标题

                authors:
                  type: array
                  description: 作者列表

                year:
                  type: string
                  description: 年份

                zotero_key:
                  type: string
                  description: Zotero键

  footnotes:
    type: object
    required: false
    description: 脚注列表
    properties:
      format:
        type: string
        description: 格式名称

      entries:
        type: array
        description: 脚注条目
        items:
          type: object
          properties:
            number:
              type: integer
              description: 编号

            content:
              type: string
              description: 格式化后的脚注

            references:
              type: array
              description: 关联的参考文献
              items:
                type: integer
                description: 参考文献索引

  consistency_report:
    type: object
    required: true
    description: 一致性检查报告
    properties:
      status:
        type: enum
        values: [pass, warning, fail]
        description: 检查结果

      issues:
        type: array
        description: 不一致问题列表
        items:
          type: object
          properties:
            type:
              type: string
              description: 问题类型

            location:
              type: string
              description: 问题位置

            message:
              type: string
              description: 问题描述

            severity:
              type: string
              description: 严重程度

      statistics:
        type: object
        description: 统计信息
        properties:
          total_citations:
            type: integer
            description: 总引用数

          total_footnotes:
            type: integer
            description: 总脚注数

          unique_references:
            type: integer
            description: 唯一参考文献数

          consistency_score:
            type: float
            description: 一致性得分（0-1）

  metadata:
    type: object
    required: true
    description: 元数据
    properties:
      processing_time:
        type: float
        description: 处理时间（秒）

      api_version:
        type: string
        description: API版本

      timestamp:
        type: string
        description: 时间戳
```

#### 2.4.4 错误处理

```python
class ZoteroBibtexError(Exception):
    """zotero-better-bibtex 错误基类"""

    class InitializationError(Exception):
        """初始化错误"""

    class APIError(Exception):
        """API错误"""

    class FormatConversionError(Exception):
        """格式转换错误"""

    class ReferenceNotFoundError(Exception):
        """参考文献未找到"""

    class TimeoutError(Exception):
        """超时错误"""
```

#### 2.4.5 降级策略

当 zotero-better-bibtex 调用失败时，采用以下降级策略：

1. **API失败**: 使用内置格式化器生成基础格式
2. **参考文献未找到**: 保持原引用，标记为"待检查"
3. **格式转换失败**: 使用默认格式

```python
def fallback_bibliography_format(citations: list, format: str) -> dict:
    """降级参考文献格式化（使用内置格式化器）"""
    # 使用内置格式化器生成基础格式
    pass
```

---

## 三、插件管理接口

### 3.1 插件管理器接口

```python
class SkillPluginManager:
    """Skill插件管理器"""

    def __init__(self, config: ConfigManager):
        self.config = config
        self.plugins = {}
        self._load_plugins()

    def _load_plugins(self):
        """加载所有插件"""
        plugin_configs = self.config.get('plugins', {})

        for plugin_name, plugin_config in plugin_configs.items():
            if plugin_config.get('enabled', False):
                self.load_plugin(plugin_name, plugin_config)

    def load_plugin(self, plugin_name: str, config: dict) -> bool:
        """加载插件"""
        try:
            plugin_class = self._get_plugin_class(plugin_name)
            plugin = plugin_class()
            plugin.initialize(config.get('config', {}))
            self.plugins[plugin_name] = plugin
            return True
        except Exception as e:
            logger.error(f"Failed to load plugin {plugin_name}: {e}")
            return False

    def unload_plugin(self, plugin_name: str) -> bool:
        """卸载插件"""
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            plugin.cleanup()
            del self.plugins[plugin_name]
            return True
        return False

    def enable_plugin(self, plugin_name: str) -> bool:
        """启用插件"""
        if plugin_name in self.plugins:
            # 更新配置
            return True
        return False

    def disable_plugin(self, plugin_name: str) -> bool:
        """禁用插件"""
        if plugin_name in self.plugins:
            # 更新配置
            return True
        return False

    def call_plugin(self, plugin_name: str, method: str, params: dict) -> dict:
        """调用插件方法"""
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} not loaded")

        plugin = self.plugins[plugin_name]
        plugin_method = getattr(plugin, method, None)

        if plugin_method is None:
            raise AttributeError(f"Plugin {plugin_name} has no method {method}")

        return plugin_method(params)

    def get_plugin_status(self, plugin_name: str) -> dict:
        """获取插件状态"""
        if plugin_name not in self.plugins:
            return {'status': 'not_loaded'}

        plugin = self.plugins[plugin_name]
        return {
            'status': 'loaded',
            'metadata': plugin.get_metadata(),
            'last_error': getattr(plugin, 'last_error', None)
        }

    def get_all_plugins_status(self) -> dict:
        """获取所有插件状态"""
        status = {}
        for plugin_name in self.plugins:
            status[plugin_name] = self.get_plugin_status(plugin_name)
        return status

    def _get_plugin_class(self, plugin_name: str):
        """获取插件类"""
        plugin_classes = {
            'ai_research_skills': AIResearchSkillsAdapter,
            'chatlaw': ChatLawAdapter,
            'lexnlp': LexNLPAdapter,
            'zotero_better_bibtex': ZoteroBibtexAdapter
        }
        return plugin_classes.get(plugin_name)
```

---

## 四、数据交换格式

### 4.1 统一数据格式

所有插件之间的数据交换使用统一的JSON格式：

```json
{
  "header": {
    "version": "2.0",
    "timestamp": "2026-02-27T19:30:00Z",
    "pipeline_id": "pipeline-12345",
    "stage": "round1"
  },
  "input": {
    // 输入数据
  },
  "output": {
    // 输出数据
  },
  "metadata": {
    "processing_time": 12.5,
    "plugin_version": "1.0.0",
    "errors": []
  }
}
```

### 4.2 错误格式

统一的错误格式：

```json
{
  "error": {
    "code": "PLUGIN_API_ERROR",
    "message": "API调用失败",
    "details": {
      "plugin": "chatlaw",
      "method": "validate_citation",
      "original_error": "Connection timeout"
    },
    "severity": "error",
    "recoverable": true
  }
}
```

---

## 五、Phase 2 产出物总结

### 5.1 已完成
- ✅ 《优化版系统架构图（V2.0）》
  - 整体架构图（5层架构）
  - 核心模块详解
  - 数据流向设计（修订模式、重构模式）
  - 插件集成架构
  - 配置管理架构

- ✅ 《各专业Skill整合接口设计说明书》
  - 整合模式总览
  - 4个Skill的详细整合设计（接口规范、错误处理、降级策略）
  - 插件管理接口
  - 数据交换格式

---

## 六、下一步行动

1. ✅ 完成优化版系统架构图（V2.0）
2. ✅ 完成各专业Skill整合接口设计说明书
3. ⏳ **等待用户确认Phase 2产出物**
4. ⏳ 确认后进入 Phase 3: 增量集成实施与测试

---

🦞 **Phase 2 全部完成，等待用户确认**
