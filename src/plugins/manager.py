"""
插件管理器 - SkillPluginManager

管理所有Skill插件的加载、卸载、调用和状态查询。
"""

import logging
from typing import Dict, Any, List, Optional
import os
import sys

from .base import SkillPlugin, SkillPluginError

# 添加src目录到Python路径
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

logger = logging.getLogger(__name__)


class SkillPluginManager:
    """
    Skill插件管理器

    管理所有插件的加载、卸载、调用和状态查询。
    """

    def __init__(self, config_manager=None):
        """
        初始化插件管理器

        Args:
            config_manager: 配置管理器实例（可选）
        """
        self.config_manager = config_manager
        self.plugins: Dict[str, SkillPlugin] = {}
        self.plugin_configs: Dict[str, Dict[str, Any]] = {}
        self._initialized = False

    def initialize(self):
        """初始化插件管理器，加载所有启用的插件"""
        if self._initialized:
            logger.warning("PluginManager already initialized")
            return

        if self.config_manager is None:
            logger.warning("ConfigManager not provided, skipping plugin loading")
            self._initialized = True
            return

        # 获取插件配置
        plugins_config = self.config_manager.get('plugins', {})

        # 加载所有启用的插件
        for plugin_name, plugin_config in plugins_config.items():
            if plugin_config.get('enabled', False):
                self.load_plugin(plugin_name, plugin_config)

        self._initialized = True
        logger.info(f"PluginManager initialized, loaded {len(self.plugins)} plugins")

    def load_plugin(self, plugin_name: str, config: Dict[str, Any]) -> bool:
        """
        加载插件

        Args:
            plugin_name: 插件名称
            config: 插件配置

        Returns:
            bool: 加载是否成功
        """
        try:
            logger.info(f"Loading plugin: {plugin_name}")

            # 获取插件类
            plugin_class = self._get_plugin_class(plugin_name)
            if plugin_class is None:
                raise SkillPluginError(f"Plugin class not found: {plugin_name}")

            # 创建插件实例
            plugin = plugin_class()

            # 验证配置
            plugin_config = config.get('config', {})
            if not plugin.validate_config(plugin_config):
                raise SkillPluginError(f"Invalid config for plugin: {plugin_name}")

            # 初始化插件
            if not plugin.initialize(plugin_config):
                raise SkillPluginError(f"Failed to initialize plugin: {plugin_name}")

            # 保存插件
            self.plugins[plugin_name] = plugin
            self.plugin_configs[plugin_name] = config

            logger.info(f"Plugin loaded successfully: {plugin_name}")
            return True

        except Exception as e:
            logger.error(f"Failed to load plugin {plugin_name}: {e}")
            return False

    def unload_plugin(self, plugin_name: str) -> bool:
        """
        卸载插件

        Args:
            plugin_name: 插件名称

        Returns:
            bool: 卸载是否成功
        """
        try:
            if plugin_name not in self.plugins:
                logger.warning(f"Plugin not loaded: {plugin_name}")
                return False

            plugin = self.plugins[plugin_name]

            # 清理资源
            if not plugin.cleanup():
                logger.warning(f"Plugin cleanup returned False: {plugin_name}")

            # 删除插件
            del self.plugins[plugin_name]
            del self.plugin_configs[plugin_name]

            logger.info(f"Plugin unloaded successfully: {plugin_name}")
            return True

        except Exception as e:
            logger.error(f"Failed to unload plugin {plugin_name}: {e}")
            return False

    def enable_plugin(self, plugin_name: str) -> bool:
        """
        启用插件

        Args:
            plugin_name: 插件名称

        Returns:
            bool: 启用是否成功
        """
        try:
            if plugin_name not in self.plugin_configs:
                logger.warning(f"Plugin config not found: {plugin_name}")
                return False

            # 更新配置
            self.plugin_configs[plugin_name]['enabled'] = True

            # 如果插件未加载，则加载插件
            if plugin_name not in self.plugins:
                return self.load_plugin(plugin_name, self.plugin_configs[plugin_name])

            logger.info(f"Plugin enabled: {plugin_name}")
            return True

        except Exception as e:
            logger.error(f"Failed to enable plugin {plugin_name}: {e}")
            return False

    def disable_plugin(self, plugin_name: str) -> bool:
        """
        禁用插件

        Args:
            plugin_name: 插件名称

        Returns:
            bool: 禁用是否成功
        """
        try:
            if plugin_name not in self.plugin_configs:
                logger.warning(f"Plugin config not found: {plugin_name}")
                return False

            # 更新配置
            self.plugin_configs[plugin_name]['enabled'] = False

            # 卸载插件
            if plugin_name in self.plugins:
                self.unload_plugin(plugin_name)

            logger.info(f"Plugin disabled: {plugin_name}")
            return True

        except Exception as e:
            logger.error(f"Failed to disable plugin {plugin_name}: {e}")
            return False

    def call_plugin(self, plugin_name: str, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        调用插件方法

        Args:
            plugin_name: 插件名称
            method: 方法名
            params: 方法参数

        Returns:
            Dict[str, Any]: 方法返回结果

        Raises:
            SkillPluginError: 调用失败时抛出
        """
        try:
            if plugin_name not in self.plugins:
                raise SkillPluginError(f"Plugin not loaded: {plugin_name}")

            plugin = self.plugins[plugin_name]
            plugin_method = getattr(plugin, method, None)

            if plugin_method is None:
                raise AttributeError(f"Plugin {plugin_name} has no method {method}")

            # 调用方法
            result = plugin_method(params)

            logger.debug(f"Plugin {plugin_name}.{method} called successfully")
            return result

        except Exception as e:
            logger.error(f"Failed to call plugin {plugin_name}.{method}: {e}")
            raise SkillPluginError(f"Plugin call failed: {e}")

    def is_plugin_enabled(self, plugin_name: str) -> bool:
        """
        检查插件是否启用

        Args:
            plugin_name: 插件名称

        Returns:
            bool: 是否启用
        """
        if plugin_name not in self.plugin_configs:
            return False
        return self.plugin_configs[plugin_name].get('enabled', False)

    def is_plugin_loaded(self, plugin_name: str) -> bool:
        """
        检查插件是否已加载

        Args:
            plugin_name: 插件名称

        Returns:
            bool: 是否已加载
        """
        return plugin_name in self.plugins

    def get_plugin_status(self, plugin_name: str) -> Dict[str, Any]:
        """
        获取插件状态

        Args:
            plugin_name: 插件名称

        Returns:
            Dict[str, Any]: 插件状态
        """
        if plugin_name not in self.plugins:
            return {
                'name': plugin_name,
                'status': 'not_loaded',
                'enabled': self.is_plugin_enabled(plugin_name)
            }

        plugin = self.plugins[plugin_name]
        health_status = plugin.health_check()

        return {
            'name': plugin_name,
            'enabled': self.is_plugin_enabled(plugin_name),
            'loaded': True,
            'status': health_status['status'],
            'initialized': health_status['initialized'],
            'last_error': health_status['last_error']
        }

    def get_all_plugins_status(self) -> Dict[str, Dict[str, Any]]:
        """
        获取所有插件状态

        Returns:
            Dict[str, Dict[str, Any]]: 所有插件状态
        """
        status = {}

        # 已加载的插件
        for plugin_name in self.plugins:
            status[plugin_name] = self.get_plugin_status(plugin_name)

        # 已配置但未加载的插件
        for plugin_name in self.plugin_configs:
            if plugin_name not in status:
                status[plugin_name] = self.get_plugin_status(plugin_name)

        return status

    def _get_plugin_class(self, plugin_name: str):
        """
        获取插件类

        Args:
            plugin_name: 插件名称

        Returns:
            插件类
        """
        try:
            # 插件类映射
            plugin_classes = {
                'chatlaw': self._import_plugin_class('chatlaw_adapter', 'ChatLawAdapter'),
                'ai_research_skills': self._import_plugin_class('ai_research_skills_adapter', 'AIResearchSkillsAdapter'),
                'lexnlp': self._import_plugin_class('lexnlp_adapter', 'LexNLPAdapter'),
                'zotero_better_bibtex': self._import_plugin_class('zotero_bibtex_adapter', 'ZoteroBibtexAdapter')
            }

            return plugin_classes.get(plugin_name)

        except Exception as e:
            logger.error(f"Failed to get plugin class {plugin_name}: {e}")
            return None

    def _import_plugin_class(self, module_name: str, class_name: str):
        """
        导入插件类

        Args:
            module_name: 模块名称
            class_name: 类名称

        Returns:
            插件类
        """
        try:
            module = __import__(f'src.plugins.{module_name}', fromlist=[class_name])
            return getattr(module, class_name)
        except Exception as e:
            logger.error(f"Failed to import plugin class {class_name} from {module_name}: {e}")
            return None

    def get_plugin_priority(self, plugin_name: str) -> Optional[int]:
        """
        获取插件优先级

        Args:
            plugin_name: 插件名称

        Returns:
            Optional[int]: 插件优先级（越小优先级越高）
        """
        if plugin_name not in self.plugin_configs:
            return None
        return self.plugin_configs[plugin_name].get('priority')

    def sort_plugins_by_priority(self, plugin_names: List[str]) -> List[str]:
        """
        按优先级排序插件

        Args:
            plugin_names: 插件名称列表

        Returns:
            List[str]: 排序后的插件名称列表
        """
        return sorted(
            plugin_names,
            key=lambda x: self.get_plugin_priority(x) if self.get_plugin_priority(x) is not None else 999
        )
