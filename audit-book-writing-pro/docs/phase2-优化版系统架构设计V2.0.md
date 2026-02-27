# Phase 2：优化版系统架构设计（V2.0）

## 设计时间
2026-02-27

## 设计目标
基于现有Skill初稿，设计一个模块化、可扩展、插件化的审计书籍写作系统架构，支持无缝集成4个专业Skill/工具。

---

## 一、架构设计原则

### 1.1 核心设计原则

| 原则 | 说明 | 应用场景 |
|------|------|---------|
| **模块化** | 系统按功能模块划分，模块间低耦合高内聚 | 所有模块设计 |
| **插件化** | 支持动态加载和卸载外部Skill | Skill集成 |
| **配置化** | 所有功能开关和参数通过配置文件管理 | 功能控制 |
| **可扩展** | 提供清晰的扩展点，易于添加新功能 | 未来扩展 |
| **可测试** | 每个模块可独立测试 | 质量保证 |
| **向后兼容** | 保留原有Skill的核心功能，增量增强 | 平滑过渡 |

### 1.2 架构分层

```
┌─────────────────────────────────────────────┐
│           应用层 (Application Layer)         │
│  - CLI接口                                │
│  - Web界面（可选）                        │
│  - API接口（可选）                        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│          流程编排层 (Orchestration Layer)     │
│  - 修订模式流程编排器                      │
│  - 重构模式流程编排器                      │
│  - 流水线管理器                            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│           核心服务层 (Core Service Layer)     │
│  - 四轮评审服务                            │
│  - 法规查询服务                            │
│  - 文件生成服务                            │
│  - 质量评估服务                            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         Skill插件层 (Skill Plugin Layer)      │
│  - ai-research-skills 插件                 │
│  - ChatLaw 插件                            │
│  - lexnlp 插件                             │
│  - zotero-better-bibtex 插件                │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│          基础设施层 (Infrastructure Layer)    │
│  - 知识库（法规数据库）                    │
│  - 模板库（章节模板）                      │
│  - 配置管理                                │
│  - 日志系统                                │
└─────────────────────────────────────────────┘
```

---

## 二、优化版系统架构（V2.0）

### 2.1 整体架构图

```
┌─────────────────────────────────────────────────────────────────────┐
│                         用户接口层                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   CLI命令行   │  │   Web界面    │  │   API接口    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      流程编排层                                    │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    流水线管理器                              │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │              修订模式流水线                       │  │  │
│  │  │  原稿 → 第1轮评审 → 第2轮评审 → 第3轮评审 → 第4轮评审 │  │  │
│  │  │    ↓         ↓         ↓         ↓         ↓         │  │  │
│  │  │  生成优化稿 → 文件生成 → 完成                       │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │              重构模式流水线                       │  │  │
│  │  │  原稿 → 观点确认 → 结构确认 → 第1-4轮评审 → 优化 │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      核心服务层                                    │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐   │
│  │   四轮评审服务   │  │   法规查询服务   │  │  文件生成服务│   │
│  └──────────────────┘  └──────────────────┘  └──────────────┘   │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐   │
│  │   质量评估服务   │  │   模板管理服务   │  │  配置管理服务│   │
│  └──────────────────┘  └──────────────────┘  └──────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    Skill插件层（核心增强）                          │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              Skill插件管理器                                │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │  │
│  │  │ ai-research │  │   ChatLaw   │  │   lexnlp    │       │  │
│  │  │  -skills    │  │             │  │             │       │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘       │  │
│  │  ┌────────────────────────────┐                         │  │
│  │  │  zotero-better-bibtex      │                         │  │
│  │  └────────────────────────────┘                         │  │
│  └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    基础设施层                                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  法规知识库  │  │  模板库      │  │  配置文件    │          │
│  │  (100+文件)  │  │  (章节模板)  │  │  (YAML/JSON) │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐                           │
│  │  日志系统    │  │  状态管理    │                           │
│  └──────────────┘  └──────────────┘                           │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 核心模块详解

#### 2.2.1 流水线管理器 (Pipeline Manager)

**职责**:
- 管理修订模式和重构模式的工作流程
- 协调各个核心服务的调用顺序
- 管理流程状态和错误处理
- 支持流程中断和恢复

**关键接口**:
```python
class PipelineManager:
    def execute_revision_mode(self, original_draft: str, config: dict) -> dict:
        """执行修订模式流水线"""
        pass

    def execute_refactor_mode(self, original_draft: str, config: dict) -> dict:
        """执行重构模式流水线"""
        pass

    def get_pipeline_status(self, pipeline_id: str) -> dict:
        """获取流水线状态"""
        pass

    def pause_pipeline(self, pipeline_id: str) -> bool:
        """暂停流水线"""
        pass

    def resume_pipeline(self, pipeline_id: str) -> bool:
        """恢复流水线"""
        pass
```

#### 2.2.2 四轮评审服务 (FourRoundReviewService)

**职责**:
- 执行四轮评审（准确性、逻辑性、适用性、规范性）
- 集成专业Skill增强评审能力
- 生成评审记录和优化建议
- 管理评审优先级（P0/P1/P2）

**关键接口**:
```python
class FourRoundReviewService:
    def execute_round1(self, content: str, context: dict) -> dict:
        """第1轮：内容准确性审查"""
        # 集成 ChatLaw 验证法规引用
        pass

    def execute_round2(self, content: str, context: dict) -> dict:
        """第2轮：逻辑连贯性审查"""
        # 集成 ai-research-skills 进行逻辑分析
        pass

    def execute_round3(self, content: str, context: dict) -> dict:
        """第3轮：适用性审查"""
        pass

    def execute_round4(self, content: str, context: dict) -> dict:
        """第4轮：格式规范化审查"""
        pass

    def generate_review_summary(self, rounds: list) -> dict:
        """生成综合评审总结"""
        pass
```

#### 2.2.3 法规查询服务 (LawQueryService)

**职责**:
- 提供法规查询能力
- 集成 ChatLaw 进行法规校验
- 支持本地法规库和外部API双查询
- 管理法规更新和版本

**关键接口**:
```python
class LawQueryService:
    def search_laws(self, keyword: str, filters: dict = None) -> list:
        """搜索法规"""
        pass

    def validate_citation(self, citation: dict) -> dict:
        """验证法规引用准确性"""
        # 集成 ChatLaw
        pass

    def check_law_effectiveness(self, law_name: str, article: str) -> bool:
        """检查法规是否现行有效"""
        pass

    def extract_article_content(self, law_name: str, article: str) -> str:
        """提取法规条文内容"""
        pass
```

#### 2.2.4 文件生成服务 (FileGenerationService)

**职责**:
- 生成评审文件（第X章-综合四轮评审.md）
- 生成优化文件（优化说明、优化对比、优化稿、完成报告）
- 集成 lexnlp 进行术语校对
- 集成 zotero-better-bibtex 进行参考文献格式化

**关键接口**:
```python
class FileGenerationService:
    def generate_review_file(self, review_data: dict, chapter_id: str) -> str:
        """生成评审文件"""
        pass

    def generate_optimization_file(self, opt_data: dict, chapter_id: str) -> str:
        """生成优化说明文件"""
        pass

    def generate_comparison_file(self, comparison_data: dict, chapter_id: str) -> str:
        """生成优化对比文件"""
        pass

    def generate_optimized_draft(self, draft_data: dict, chapter_id: str) -> str:
        """生成优化稿"""
        pass

    def generate_completion_report(self, report_data: dict, chapter_id: str) -> str:
        """生成完成报告"""
        pass

    def post_process(self, content: str, config: dict) -> str:
        """后处理（术语校对、参考文献格式化）"""
        # 集成 lexnlp 和 zotero-better-bibtex
        pass
```

#### 2.2.5 Skill插件管理器 (SkillPluginManager)

**职责**:
- 管理4个专业Skill插件
- 提供统一的插件接口
- 支持插件的加载、卸载、启用、禁用
- 管理插件配置和依赖

**关键接口**:
```python
class SkillPluginManager:
    def load_plugin(self, plugin_name: str, config: dict) -> bool:
        """加载插件"""
        pass

    def unload_plugin(self, plugin_name: str) -> bool:
        """卸载插件"""
        pass

    def enable_plugin(self, plugin_name: str) -> bool:
        """启用插件"""
        pass

    def disable_plugin(self, plugin_name: str) -> bool:
        """禁用插件"""
        pass

    def call_plugin(self, plugin_name: str, method: str, params: dict) -> dict:
        """调用插件方法"""
        pass

    def get_plugin_status(self, plugin_name: str) -> dict:
        """获取插件状态"""
        pass
```

---

## 三、数据流向设计

### 3.1 修订模式数据流向

```
┌─────────────┐
│  用户输入   │
│ (原稿文件)  │
└─────────────┘
      ↓
┌─────────────────────────────────────────┐
│  第1轮评审：内容准确性                │
│  - 法规引用准确性 → ChatLaw验证       │
│  - 概念定义准确性                     │
│  - 数据支撑准确性                     │
│  - 事实陈述准确性                     │
└─────────────────────────────────────────┘
      ↓ 生成评审记录1
┌─────────────────────────────────────────┐
│  第2轮评审：逻辑连贯性                │
│  - 章节逻辑连贯性 → ai-research-skills │
│  - 概念层次连贯性                     │
│  - 审计论证逻辑性                     │
└─────────────────────────────────────────┘
      ↓ 生成评审记录2
┌─────────────────────────────────────────┐
│  第3轮评审：适用性                    │
│  - 审计指引实用性                     │
│  - 框架实用性                         │
│  - 案例适用性                         │
└─────────────────────────────────────────┘
      ↓ 生成评审记录3
┌─────────────────────────────────────────┐
│  第4轮评审：格式规范化                │
│  - 标题层级规范                       │
│  - 法规引用格式                       │
│  - 术语使用一致性                     │
└─────────────────────────────────────────┘
      ↓ 生成评审记录4
┌─────────────────────────────────────────┐
│  汇总四轮评审 → 生成综合优化说明      │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  选择典型优化案例 → 生成优化对比      │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  根据综合优化说明 → 生成优化稿        │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  后处理流程：                         │
│  - lexnlp术语校对                    │
│  - zotero-better-bibtex参考文献格式化  │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  统计成果和提升 → 生成完成报告        │
└─────────────────────────────────────────┘
      ↓
┌─────────────┐
│  用户输出   │
│ (5个文件)  │
└─────────────┘
```

### 3.2 重构模式数据流向

```
┌─────────────┐
│  用户输入   │
│ (原稿文件)  │
└─────────────┘
      ↓
┌─────────────────────────────────────────┐
│  提取学术观点 → 生成观点确认文档    │
└─────────────────────────────────────────┘
      ↓ 等待用户确认
┌─────────────────────────────────────────┐
│  提出结构优化方案 → 生成结构方案    │
└─────────────────────────────────────────┘
      ↓ 等待用户确认
┌─────────────────────────────────────────┐
│  第1轮评审：内容准确性                │
│  - 法规引用准确性 → ChatLaw验证       │
│  - 概念定义准确性                     │
│  - 数据支撑准确性                     │
│  - 事实陈述准确性                     │
└─────────────────────────────────────────┘
      ↓ 生成评审记录1
┌─────────────────────────────────────────┐
│  第2轮评审：逻辑连贯性                │
│  - 章节逻辑连贯性 → ai-research-skills │
│  - 概念层次连贯性                     │
│  - 审计论证逻辑性                     │
└─────────────────────────────────────────┘
      ↓ 生成评审记录2
┌─────────────────────────────────────────┐
│  第3轮评审：适用性                    │
│  - 审计指引实用性                     │
│  - 框架实用性                         │
│  - 案例适用性                         │
└─────────────────────────────────────────┘
      ↓ 生成评审记录3
┌─────────────────────────────────────────┐
│  第4轮评审：格式规范化                │
│  - 标题层级规范                       │
│  - 法规引用格式                       │
│  - 术语使用一致性                     │
└─────────────────────────────────────────┘
      ↓ 生成评审记录4
┌─────────────────────────────────────────┐
│  汇总四轮评审 → 生成综合优化说明      │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  选择典型优化案例 → 生成优化对比      │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  根据综合优化说明 → 生成优化稿(重构)  │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  后处理流程：                         │
│  - lexnlp术语校对                    │
│  - zotero-better-bibtex参考文献格式化  │
└─────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────┐
│  统计成果和提升 → 生成完成报告        │
└─────────────────────────────────────────┘
      ↓
┌─────────────┐
│  用户输出   │
│ (7个文件)  │
└─────────────┘
```

---

## 四、插件集成架构

### 4.1 插件接口标准

所有Skill插件必须实现统一的接口标准：

```python
class SkillPlugin(ABC):
    """Skill插件基类"""

    @abstractmethod
    def initialize(self, config: dict) -> bool:
        """初始化插件"""
        pass

    @abstractmethod
    def process(self, input_data: dict) -> dict:
        """处理数据"""
        pass

    @abstractmethod
    def get_metadata(self) -> dict:
        """获取插件元数据"""
        pass

    @abstractmethod
    def validate_config(self, config: dict) -> bool:
        """验证配置"""
        pass

    @abstractmethod
    def cleanup(self) -> bool:
        """清理资源"""
        pass
```

### 4.2 插件适配器模式

为每个Skill创建适配器，使其符合统一接口标准：

#### 4.2.1 ai-research-skills 适配器

```python
class AIResearchSkillsAdapter(SkillPlugin):
    """ai-research-skills 插件适配器"""

    def __init__(self):
        self.client = None
        self.config = None

    def initialize(self, config: dict) -> bool:
        """初始化插件"""
        self.config = config
        # 初始化 ai-research-skills 客户端
        self.client = AIResearchSkillsClient(config.get('api_key'))
        return True

    def process(self, input_data: dict) -> dict:
        """处理数据"""
        # 调用 ai-research-skills API
        result = self.client.analyze_structure(input_data['content'])
        return {
            'structure_analysis': result,
            'logic_analysis': self._analyze_logic(input_data),
            'quality_assessment': self._assess_quality(input_data)
        }

    def _analyze_logic(self, input_data: dict) -> dict:
        """分析逻辑连贯性"""
        # 实现逻辑分析逻辑
        pass

    def _assess_quality(self, input_data: dict) -> dict:
        """评估内容质量"""
        # 实现质量评估逻辑
        pass

    def get_metadata(self) -> dict:
        """获取插件元数据"""
        return {
            'name': 'ai-research-skills',
            'version': '1.0.0',
            'description': '学术写作、逻辑优化、章节结构化',
            'capabilities': ['structure_analysis', 'logic_analysis', 'quality_assessment']
        }

    def validate_config(self, config: dict) -> bool:
        """验证配置"""
        return 'api_key' in config

    def cleanup(self) -> bool:
        """清理资源"""
        if self.client:
            self.client.close()
        return True
```

#### 4.2.2 ChatLaw 适配器

```python
class ChatLawAdapter(SkillPlugin):
    """ChatLaw 插件适配器"""

    def __init__(self):
        self.client = None
        self.config = None

    def initialize(self, config: dict) -> bool:
        """初始化插件"""
        self.config = config
        # 初始化 ChatLaw 客户端
        self.client = ChatLawClient(config.get('api_key'))
        return True

    def process(self, input_data: dict) -> dict:
        """处理数据"""
        citations = input_data.get('citations', [])
        validation_results = []

        for citation in citations:
            # 调用 ChatLaw API 验证引用
            result = self.client.validate_citation(citation)
            validation_results.append(result)

        return {
            'validation_results': validation_results,
            'summary': self._generate_summary(validation_results)
        }

    def _generate_summary(self, results: list) -> dict:
        """生成验证总结"""
        valid_count = sum(1 for r in results if r['status'] == 'valid')
        invalid_count = sum(1 for r in results if r['status'] == 'invalid')

        return {
            'valid_count': valid_count,
            'invalid_count': invalid_count,
            'total_count': len(results)
        }

    def get_metadata(self) -> dict:
        """获取插件元数据"""
        return {
            'name': 'ChatLaw',
            'version': '1.0.0',
            'description': '法规数据库、法规校验、失效条文检查',
            'capabilities': ['citation_validation', 'law_effectiveness_check', 'law_update_tracking']
        }

    def validate_config(self, config: dict) -> bool:
        """验证配置"""
        return 'api_key' in config

    def cleanup(self) -> bool:
        """清理资源"""
        if self.client:
            self.client.close()
        return True
```

#### 4.2.3 lexnlp 适配器

```python
class LexNLPAdapter(SkillPlugin):
    """lexnlp 插件适配器"""

    def __init__(self):
        self.client = None
        self.config = None

    def initialize(self, config: dict) -> bool:
        """初始化插件"""
        self.config = config
        # 初始化 lexnlp 客户端
        self.client = LexNLPClient(config.get('api_key'))
        return True

    def process(self, input_data: dict) -> dict:
        """处理数据"""
        text = input_data['content']

        # 调用 lexnlp API 进行术语校对
        terminology_check = self.client.check_terminology(text)

        # 调用 lexnlp API 进行法律分析
        legal_analysis = self.client.analyze_legal(text)

        # 调用 lexnlp API 进行条文抽取
        article_extraction = self.client.extract_articles(text)

        return {
            'terminology_check': terminology_check,
            'legal_analysis': legal_analysis,
            'article_extraction': article_extraction
        }

    def get_metadata(self) -> dict:
        """获取插件元数据"""
        return {
            'name': 'lexnlp',
            'version': '1.0.0',
            'description': '法律文本解析、实体识别、术语提取',
            'capabilities': ['terminology_check', 'legal_analysis', 'article_extraction']
        }

    def validate_config(self, config: dict) -> bool:
        """验证配置"""
        return 'api_key' in config

    def cleanup(self) -> bool:
        """清理资源"""
        if self.client:
            self.client.close()
        return True
```

#### 4.2.4 zotero-better-bibtex 适配器

```python
class ZoteroBibtexAdapter(SkillPlugin):
    """zotero-better-bibtex 插件适配器"""

    def __init__(self):
        self.zotero = None
        self.config = None

    def initialize(self, config: dict) -> bool:
        """初始化插件"""
        self.config = config
        # 初始化 Zotero 连接
        self.zotero = ZoteroAPI(
            library_id=config.get('library_id'),
            api_key=config.get('api_key')
        )
        return True

    def process(self, input_data: dict) -> dict:
        """处理数据"""
        citations = input_data.get('citations', [])
        format_type = input_data.get('format', 'APA')

        # 生成参考文献列表
        bibliography = self.zotero.generate_bibliography(citations, format_type)

        # 生成脚注
        footnotes = self.zotero.generate_footnotes(citations, format_type)

        # 检查一致性
        consistency_report = self._check_consistency(bibliography, footnotes)

        return {
            'bibliography': bibliography,
            'footnotes': footnotes,
            'consistency_report': consistency_report
        }

    def _check_consistency(self, bibliography: dict, footnotes: dict) -> dict:
        """检查一致性"""
        # 实现一致性检查逻辑
        pass

    def get_metadata(self) -> dict:
        """获取插件元数据"""
        return {
            'name': 'zotero-better-bibtex',
            'version': '1.0.0',
            'description': '引用管理、参考文献格式化',
            'capabilities': ['bibliography_generation', 'footnote_management', 'format_conversion']
        }

    def validate_config(self, config: dict) -> bool:
        """验证配置"""
        return 'library_id' in config and 'api_key' in config

    def cleanup(self) -> bool:
        """清理资源"""
        if self.zotero:
            self.zotero.close()
        return True
```

---

## 五、配置管理架构

### 5.1 配置文件结构

```yaml
# audit_book_config.yaml

version: "2.0"

# 全局配置
global:
  debug: false
  log_level: INFO
  max_retries: 3
  timeout: 300

# 流程配置
pipeline:
  mode: revision  # revision 或 refactor
  enable_parallel: true
  max_parallel_tasks: 3
  checkpoint_interval: 600  # 600秒保存一次检查点

# 四轮评审配置
review:
  round1:
    enabled: true
    strict_mode: false
    auto_fix: false
  round2:
    enabled: true
    strict_mode: false
    use_ai_research_skills: true
  round3:
    enabled: true
    strict_mode: false
    min_guidance_words: 800
    max_guidance_words: 1500
    min_insight_words: 800
    max_insight_words: 1500
  round4:
    enabled: true
    strict_mode: false

# Skill插件配置
plugins:
  ai_research_skills:
    enabled: true
    priority: 2
    config:
      api_key: ${AI_RESEARCH_SKILLS_API_KEY}
      strict_mode: false
      quality_threshold: 0.7
      enable_cross_chapter: true
      max_suggestions: 5

  chatlaw:
    enabled: true
    priority: 1
    config:
      api_key: ${CHATLAW_API_KEY}
      strict_mode: true
      auto_fix: false
      warn_expired: true
      update_check_interval: 24h

  lexnlp:
    enabled: true
    priority: 3
    config:
      api_key: ${LEXNLP_API_KEY}
      strict_mode: false
      consistency_threshold: 0.8
      enable_synonym_check: true
      enable_ambiguity_detection: true

  zotero_better_bibtex:
    enabled: true
    priority: 4
    config:
      library_id: ${ZOTERO_LIBRARY_ID}
      api_key: ${ZOTERO_API_KEY}
      format: APA
      auto_numbering: true
      cross_ref_check: true
      latex_mode: false

# 输出配置
output:
  directory: ./output
  format: markdown
  encoding: utf-8
  keep_intermediate: true

# 字数控制配置
word_count:
  revision_mode:
    min_ratio: 0.95
    max_ratio: 1.20
  refactor_mode:
    enable_tracking: true

# 质量标准配置
quality:
  target_level: A
  min_improvement: 1.5
  required_framework_tables: 3
  required_references: 2
```

### 5.2 配置加载机制

```python
class ConfigManager:
    """配置管理器"""

    def __init__(self, config_path: str = 'audit_book_config.yaml'):
        self.config_path = config_path
        self.config = None
        self._load_config()

    def _load_config(self):
        """加载配置文件"""
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        # 替换环境变量
        self._replace_env_vars()

    def _replace_env_vars(self):
        """替换环境变量"""
        def replace_env(value):
            if isinstance(value, str):
                match = re.match(r'^\$\{(.+)\}$', value)
                if match:
                    return os.environ.get(match.group(1), value)
            elif isinstance(value, dict):
                return {k: replace_env(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [replace_env(item) for item in value]
            return value

        self.config = replace_env(self.config)

    def get(self, key: str, default=None):
        """获取配置值"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value else default

    def set(self, key: str, value):
        """设置配置值"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value

    def save(self):
        """保存配置文件"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(self.config, f, allow_unicode=True)
```

---

## 六、Phase 2 产出物总结

### 6.1 已完成
- ✅ 优化版系统架构图（V2.0）
  - 整体架构图（5层架构）
  - 核心模块详解
  - 数据流向设计（修订模式、重构模式）
  - 插件集成架构
  - 配置管理架构

### 6.2 待完成
- [ ] 《各专业Skill整合接口设计说明书》

---

## 七、下一步行动

1. ✅ 完成优化版系统架构图（V2.0）
2. ⏳ 生成《各专业Skill整合接口设计说明书》
3. ⏳ 等待用户确认后进入Phase 3

---

🦞 **Phase 2 第1部分完成，等待生成《各专业Skill整合接口设计说明书》**
