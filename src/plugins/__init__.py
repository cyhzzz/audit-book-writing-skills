"""
插件系统初始化
"""

from .base import (
    SkillPlugin,
    SkillPluginError,
    InitializationError,
    ProcessingError,
    APIError,
    ValidationError,
    TimeoutError
)

from .manager import SkillPluginManager

from .chatlaw_adapter import ChatLawAdapter
from .ai_research_skills_adapter import AIResearchSkillsAdapter
from .lexnlp_adapter import LexNLPAdapter
from .zotero_bibtex_adapter import ZoteroBibtexAdapter

__all__ = [
    # Base classes
    'SkillPlugin',
    'SkillPluginError',
    'InitializationError',
    'ProcessingError',
    'APIError',
    'ValidationError',
    'TimeoutError',

    # Manager
    'SkillPluginManager',

    # Adapters
    'ChatLawAdapter',
    'AIResearchSkillsAdapter',
    'LexNLPAdapter',
    'ZoteroBibtexAdapter',
]
