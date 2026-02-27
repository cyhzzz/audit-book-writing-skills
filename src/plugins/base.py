"""
插件基类 - SkillPlugin

所有插件必须继承此基类并实现抽象方法。
"""

from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class SkillPlugin(ABC):
    """
    Skill插件基类

    所有插件必须继承此基类并实现以下抽象方法：
    - initialize(config: dict) -> bool: 初始化插件
    - process(input_data: dict) -> dict: 处理数据
    - get_metadata() -> dict: 获取插件元数据
    - validate_config(config: dict) -> bool: 验证配置
    - cleanup() -> bool: 清理资源
    """

    def __init__(self):
        self.name = self.__class__.__name__
        self.version = "1.0.0"
        self.description = ""
        self.capabilities = []
        self.is_initialized = False
        self.last_error = None

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        初始化插件

        Args:
            config: 插件配置字典

        Returns:
            bool: 初始化是否成功

        Raises:
            InitializationError: 初始化失败时抛出
        """
        pass

    @abstractmethod
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理数据

        Args:
            input_data: 输入数据字典

        Returns:
            Dict[str, Any]: 处理结果字典

        Raises:
            ProcessingError: 处理失败时抛出
            TimeoutError: 超时时抛出
        """
        pass

    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """
        获取插件元数据

        Returns:
            Dict[str, Any]: 插件元数据
            - name: 插件名称
            - version: 插件版本
            - description: 插件描述
            - capabilities: 插件能力列表
        """
        pass

    @abstractmethod
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        验证配置

        Args:
            config: 配置字典

        Returns:
            bool: 配置是否有效
        """
        pass

    @abstractmethod
    def cleanup(self) -> bool:
        """
        清理资源

        Returns:
            bool: 清理是否成功
        """
        pass

    def health_check(self) -> Dict[str, Any]:
        """
        健康检查

        Returns:
            Dict[str, Any]: 健康状态
            - status: healthy/unhealthy
            - initialized: 是否已初始化
            - last_error: 最后一次错误
        """
        return {
            'name': self.name,
            'version': self.version,
            'status': 'healthy' if self.is_initialized else 'uninitialized',
            'initialized': self.is_initialized,
            'last_error': self.last_error
        }


class SkillPluginError(Exception):
    """Skill插件错误基类"""

    pass


class InitializationError(SkillPluginError):
    """初始化错误"""

    pass


class ProcessingError(SkillPluginError):
    """处理错误"""

    pass


class APIError(SkillPluginError):
    """API错误"""

    pass


class ValidationError(SkillPluginError):
    """验证错误"""

    pass


class TimeoutError(SkillPluginError):
    """超时错误"""

    pass
