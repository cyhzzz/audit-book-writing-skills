# 审计书籍写作专业版 - 插件系统

## 概述
插件系统是审计书籍写作专业版的核心架构，支持动态加载和管理外部专业Skill插件。

## 插件目录结构
```
src/plugins/
├── __init__.py              # 插件系统初始化
├── base.py                  # 插件基类
├── manager.py               # 插件管理器
├── chatlaw_adapter.py       # ChatLaw适配器
├── ai_research_skills_adapter.py  # ai-research-skills适配器
├── lexnlp_adapter.py        # lexnlp适配器
└── zotero_bibtex_adapter.py # zotero-better-bibtex适配器
```

## 使用方式
```python
from src.plugins.manager import SkillPluginManager

# 初始化插件管理器
plugin_manager = SkillPluginManager(config)

# 调用插件
result = plugin_manager.call_plugin('chatlaw', 'process', {'citations': [...]})
```
