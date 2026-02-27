"""
ChatLaw适配器 - ChatLawAdapter（本地检索版本）

使用本地法规库（references/laws-database/）进行法规验证，
学习ChatLaw的校验机制。
"""

import logging
import os
import subprocess
import json
import time
from typing import Dict, Any, List, Optional

from .base import (
    SkillPlugin,
    InitializationError,
    ProcessingError,
    ValidationError
)

logger = logging.getLogger(__name__)


class ChatLawAdapter(SkillPlugin):
    """
    ChatLaw 插件适配器（本地检索版本）

    使用本地法规库进行法规验证，学习ChatLaw的校验机制：
    - 法规引用准确性验证
    - 法规时效性检查
    - 失效条文检查
    - 法规更新追踪
    """

    def __init__(self):
        super().__init__()
        self.name = "ChatLaw"
        self.version = "1.0.0"
        self.description = "法规数据库、法规校验、失效条文检查（本地检索版本）"
        self.capabilities = [
            'citation_validation',
            'law_effectiveness_check',
            'law_update_tracking'
        ]
        self.config = None
        self.laws_database_path = None
        self.timeout = 30
        self.max_retries = 3

    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        初始化插件

        Args:
            config: 插件配置
                - laws_database_path: 法规库路径（可选，默认：references/laws-database/）
                - timeout: 超时时间（秒）
                - max_retries: 最大重试次数
                - strict_mode: 严格模式
                - auto_fix: 自动修正
                - warn_expired: 警告失效引用

        Returns:
            bool: 初始化是否成功
        """
        try:
            self.config = config

            # 获取法规库路径
            default_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                'references', 'laws-database'
            )
            self.laws_database_path = config.get('laws_database_path', default_path)

            # 检查法规库路径是否存在
            if not os.path.exists(self.laws_database_path):
                raise InitializationError(f"Laws database path not found: {self.laws_database_path}")

            logger.info(f"Laws database path: {self.laws_database_path}")

            # 获取超时配置
            self.timeout = config.get('timeout', 30)
            self.max_retries = config.get('max_retries', 3)

            self.is_initialized = True
            logger.info("ChatLaw plugin (local) initialized successfully")
            return True

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to initialize ChatLaw plugin: {e}")
            raise InitializationError(f"ChatLaw initialization failed: {e}")

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理数据

        Args:
            input_data: 输入数据
                - citations: 法规引用列表
                    - law_name: 法规全称
                    - year: 年份
                    - article: 条款号
                    - content: 引用的条款内容（可选）
                    - source_text: 原文中的引用文本（可选）
                    - location: 引用位置（可选）
                - options: 处理选项
                    - strict_mode: 严格模式
                    - auto_fix: 自动修正
                    - warn_expired: 警告失效引用

        Returns:
            Dict[str, Any]: 处理结果
                - validation_results: 验证结果汇总
                - details: 详细验证结果
                - metadata: 元数据
        """
        try:
            start_time = time.time()

            # 获取输入数据
            citations = input_data.get('citations', [])
            options = input_data.get('options', {})

            # 合并配置选项
            merged_options = {**self.config, **options}

            logger.info(f"Processing {len(citations)} citations with ChatLaw (local)")

            # 验证法规引用
            validation_results = []
            for citation in citations:
                try:
                    result = self._validate_citation(citation, merged_options)
                    validation_results.append(result)
                except Exception as e:
                    logger.error(f"Failed to validate citation {citation.get('law_name', 'unknown')}: {e}")
                    validation_results.append({
                        'citation': citation,
                        'validation': {
                            'status': 'error',
                            'confidence': 0.0,
                            'error': str(e)
                        },
                        'issues': [{
                            'type': 'validation_error',
                            'message': f"验证失败: {e}",
                            'severity': 'error'
                        }]
                    })

            # 生成汇总
            summary = self._generate_summary(validation_results)

            processing_time = time.time() - start_time

            return {
                'validation_results': summary,
                'details': validation_results,
                'metadata': {
                    'processing_time': processing_time,
                    'total_citations': len(citations),
                    'plugin_version': self.version,
                    'mode': 'local_database'
                }
            }

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"ChatLaw process failed: {e}")
            raise ProcessingError(f"ChatLaw processing failed: {e}")

    def _validate_citation(self, citation: Dict[str, Any], options: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证单个法规引用（使用本地法规库）

        Args:
            citation: 法规引用
            options: 处理选项

        Returns:
            Dict[str, Any]: 验证结果
        """
        law_name = citation.get('law_name', '')
        year = citation.get('year', '')
        article = citation.get('article', '')

        # 步骤1：在法规库中搜索法规
        search_results = self._search_law_in_database(law_name)

        if not search_results:
            # 未找到法规
            return {
                'citation': citation,
                'validation': {
                    'status': 'invalid',
                    'confidence': 0.0,
                    'source': 'local_database',
                    'message': f"未找到法规: {law_name}"
                },
                'issues': [{
                    'type': 'invalid_citation',
                    'message': f"未找到法规: {law_name}",
                    'severity': 'error'
                }],
                'suggestions': []
            }

        # 步骤2：验证时效性（检查年份）
        matched_law = search_results[0]  # 使用第一个匹配结果
        status, issues = self._validate_effectiveness(law_name, year, matched_law)

        # 步骤3：验证条款号
        if status != 'invalid' and article:
            article_result = self._validate_article(law_name, article, matched_law)
            issues.extend(article_result['issues'])

            # 如果条款验证失败，更新状态
            if article_result['status'] == 'invalid':
                status = 'invalid'

        # 步骤4：生成验证结果
        validation = {
            'status': status,
            'confidence': 0.9 if status == 'valid' else 0.5,
            'matched_law': {
                'name': law_name,
                'source': 'local_database',
                'file': matched_law.get('file', '')
            }
        }

        # 生成修正建议
        suggestions = []
        if status == 'invalid' and options.get('auto_fix', False):
            suggestions.append({
                'type': 'manual_fix',
                'suggestion': f"请核实法规名称和条款号: {law_name}",
                'auto_fix': False
            })

        return {
            'citation': citation,
            'validation': validation,
            'issues': issues,
            'suggestions': suggestions
        }

    def _search_law_in_database(self, law_name: str) -> List[Dict[str, Any]]:
        """
        在法规库中搜索法规

        Args:
            law_name: 法规名称

        Returns:
            List[Dict[str, Any]]: 搜索结果
        """
        try:
            # 提取关键词（去掉《》和修饰词）
            keywords = self._extract_keywords(law_name)

            # 构建搜索模式
            pattern = '|'.join(keywords)

            # 调用grep搜索
            result = self._grep_search(pattern, self.laws_database_path)

            return result

        except Exception as e:
            logger.error(f"Failed to search law in database: {e}")
            return []

    def _extract_keywords(self, law_name: str) -> List[str]:
        """
        从法规名称中提取关键词

        Args:
            law_name: 法规名称

        Returns:
            List[str]: 关键词列表
        """
        # 去掉《》
        law_name = law_name.replace('《', '').replace('》', '')

        # 分割关键词
        keywords = law_name.split('、')

        # 过滤掉常见修饰词
        filter_words = ['中华人民共和国', '中华人民共和国', '修正', '修订', '通过']
        keywords = [kw for kw in keywords if kw not in filter_words and len(kw) > 2]

        # 如果没有关键词，使用完整名称
        if not keywords:
            keywords = [law_name]

        return keywords

    def _grep_search(self, pattern: str, path: str) -> List[Dict[str, Any]]:
        """
        使用grep搜索法规库

        Args:
            pattern: 搜索模式
            path: 搜索路径

        Returns:
            List[Dict[str, Any]]: 搜索结果
        """
        try:
            # 使用subprocess调用grep
            cmd = ['grep', '-l', pattern, f'{path}/*.md']
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            # 解析结果
            files = result.stdout.strip().split('\n') if result.stdout.strip() else []

            # 返回匹配的文件列表
            return [{'file': f} for f in files if f]

        except subprocess.TimeoutExpired:
            logger.warning(f"Grep search timeout: {pattern}")
            return []
        except Exception as e:
            logger.error(f"Failed to grep search: {e}")
            return []

    def _validate_effectiveness(self, law_name: str, year: str, matched_law: Dict[str, Any]) -> tuple:
        """
        验证法规时效性

        Args:
            law_name: 法规名称
            year: 年份
            matched_law: 匹配的法规

        Returns:
            tuple: (status, issues)
        """
        status = 'valid'
        issues = []

        # 读取法规文件，获取修正年份
        try:
            file_path = matched_law.get('file', '')
            if os.path.exists(file_path):
                # 从文件名中提取年份
                filename = os.path.basename(file_path)

                # 检查是否包含修正年份
                # 文件名格式如：2024.5.31-《...》.md
                if '修正' in filename or '修订' in filename:
                    # 提取最新修正年份
                    import re
                    year_match = re.search(r'(\d{4})\.', filename)
                    if year_match:
                        latest_year = year_match.group(1)

                        # 如果引用的年份不是最新修正年份，发出警告
                        if year and year != latest_year:
                            issues.append({
                                'type': 'outdated_citation',
                                'message': f"法规引用的年份（{year}）不是最新修正年份（{latest_year}）",
                                'severity': 'warning'
                            })

        except Exception as e:
            logger.warning(f"Failed to validate effectiveness: {e}")

        return status, issues

    def _validate_article(self, law_name: str, article: str, matched_law: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证条款号

        Args:
            law_name: 法规名称
            article: 条款号
            matched_law: 匹配的法规

        Returns:
            Dict[str, Any]: 验证结果
        """
        status = 'valid'
        issues = []

        try:
            file_path = matched_law.get('file', '')
            if os.path.exists(file_path):
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 搜索条款号
                import re
                article_pattern = f'第.*{article}.*条'
                if not re.search(article_pattern, content):
                    issues.append({
                        'type': 'invalid_article',
                        'message': f"未找到条款: 第{article}条",
                        'severity': 'warning'
                    })

        except Exception as e:
            logger.warning(f"Failed to validate article: {e}")

        return {
            'status': status,
            'issues': issues
        }

    def _generate_summary(self, validation_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        生成验证总结

        Args:
            validation_results: 验证结果列表

        Returns:
            Dict[str, Any]: 验证总结
        """
        total_count = len(validation_results)
        valid_count = sum(1 for r in validation_results if r['validation']['status'] == 'valid')
        invalid_count = sum(1 for r in validation_results if r['validation']['status'] == 'invalid')
        warning_count = sum(1 for r in validation_results
                           if any(i['severity'] == 'warning' for i in r.get('issues', [])))

        return {
            'total_count': total_count,
            'valid_count': valid_count,
            'invalid_count': invalid_count,
            'warning_count': warning_count,
            'success_rate': valid_count / total_count if total_count > 0 else 0.0
        }

    def get_metadata(self) -> Dict[str, Any]:
        """
        获取插件元数据

        Returns:
            Dict[str, Any]: 插件元数据
        """
        return {
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'capabilities': self.capabilities,
            'mode': 'local_database',
            'laws_database_path': self.laws_database_path
        }

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        验证配置

        Args:
            config: 配置字典

        Returns:
            bool: 配置是否有效
        """
        # 检查法规库路径
        laws_database_path = config.get('laws_database_path')
        if laws_database_path and not os.path.exists(laws_database_path):
            logger.error(f"Laws database path not found: {laws_database_path}")
            return False

        # 检查可选配置项的格式
        if 'timeout' in config:
            timeout = config['timeout']
            if not isinstance(timeout, (int, float)) or timeout <= 0:
                logger.error("Invalid timeout value")
                return False

        if 'max_retries' in config:
            max_retries = config['max_retries']
            if not isinstance(max_retries, int) or max_retries < 0:
                logger.error("Invalid max_retries value")
                return False

        return True

    def cleanup(self) -> bool:
        """
        清理资源

        Returns:
            bool: 清理是否成功
        """
        try:
            self.is_initialized = False
            logger.info("ChatLaw plugin (local) cleaned up successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to cleanup ChatLaw plugin: {e}")
            return False
