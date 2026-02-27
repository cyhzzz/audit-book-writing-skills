"""
zotero-better-bibtex适配器 - ZoteroBibtexAdapter

基于规则的参考文献格式化，支持APA、MLA、Chicago、GB/T7714等格式。
"""

import logging
import re
from typing import Dict, Any, List, Optional
from collections import defaultdict

from .base import (
    SkillPlugin,
    InitializationError,
    ProcessingError,
    ValidationError
)

logger = logging.getLogger(__name__)


class ZoteroBibtexAdapter(SkillPlugin):
    """
    zotero-better-bibtex 插件适配器（基于规则版本）

    实现参考文献处理的核心能力：
    - 参考文献格式化（支持APA、MLA、Chicago、GB/T7714等格式）
    - 脚注管理和格式化
    - 跨文件引用一致性检查
    - 自动编号
    """

    def __init__(self):
        super().__init__()
        self.name = "zotero-better_bibtex"
        self.version = "1.0.0"
        self.description = "参考文献格式化、脚注管理、跨文件引用检查"
        self.capabilities = [
            'bibliography_formatting',
            'footnote_management',
            'cross_ref_check',
            'auto_numbering'
        ]
        self.config = None
        self.timeout = 30
        self.max_retries = 3

    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        初始化插件

        Args:
            config: 插件配置
                - format: 默认格式（APA, MLA, Chicago, GB7714）
                - auto_numbering: 自动编号
                - cross_ref_check: 跨文件引用检查
                - include_url: 包含URL
                - sort_by: 排序方式（citation_order, author, year）
                - timeout: 超时时间（秒）
                - max_retries: 最大重试次数

        Returns:
            bool: 初始化是否成功
        """
        try:
            self.config = config

            # 获取超时配置
            self.timeout = config.get('timeout', 30)
            self.max_retries = config.get('max_retries', 3)

            # 预定义格式
            self.formats = {
                'APA': self._format_apa,
                'MLA': self._format_mla,
                'Chicago': self._format_chicago,
                'GB7714': self._format_gb7714
            }

            self.is_initialized = True
            logger.info("zotero-better-bibtex plugin (rule-based) initialized successfully")
            return True

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to initialize zotero-better-bibtex plugin: {e}")
            raise InitializationError(f"zotero-better-bibtex initialization failed: {e}")

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理数据

        Args:
            input_data: 输入数据
                - citations: 参考文献列表
                    - author: 作者
                    - year: 年份
                    - title: 标题
                    - source: 来源
                    - url: URL（可选）
                    - doi: DOI（可选）
                - footnotes: 脚注列表
                    - id: 脚注ID
                    - text: 脚注文本
                    - references: 引用的参考文献ID列表
                - format: 格式（APA, MLA, Chicago, GB7714）
                - options: 处理选项
                    - auto_numbering: 自动编号
                    - cross_ref_check: 跨文件引用检查
                    - include_url: 包含URL

        Returns:
            Dict[str, Any]: 处理结果
                - bibliography: 参考文献列表
                - footnotes: 脚注列表
                - consistency_report: 一致性检查报告
        """
        try:
            import time
            start_time = time.time()

            # 获取输入数据
            citations = input_data.get('citations', [])
            footnotes = input_data.get('footnotes', [])
            format_type = input_data.get('format', self.config.get('format', 'APA'))
            options = input_data.get('options', {})

            # 合并配置选项
            merged_options = {**self.config, **options}

            logger.info(f"Processing {len(citations)} citations with zotero-better-bibtex")

            # 生成参考文献列表
            bibliography = self._generate_bibliography(citations, format_type, merged_options)

            # 生成脚注
            footnotes_result = self._generate_footnotes(footnotes, format_type, merged_options)

            # 检查一致性
            consistency_report = None
            if merged_options.get('cross_ref_check', True):
                consistency_report = self._check_consistency(bibliography, footnotes_result, citations, merged_options)

            processing_time = time.time() - start_time

            return {
                'bibliography': bibliography,
                'footnotes': footnotes_result,
                'consistency_report': consistency_report,
                'metadata': {
                    'processing_time': processing_time,
                    'plugin_version': self.version,
                    'total_citations': len(citations),
                    'total_footnotes': len(footnotes),
                    'format': format_type,
                    'mode': 'rule_based'
                }
            }

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"zotero-better-bibtex process failed: {e}")
            raise ProcessingError(f"zotero-better-bibtex processing failed: {e}")

    def _generate_bibliography(self, citations: List[Dict[str, Any]], format_type: str, options: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        生成参考文献列表

        Args:
            citations: 参考文献列表
            format_type: 格式类型
            options: 处理选项

        Returns:
            List[Dict[str, Any]]: 参考文献列表
        """
        # 获取格式化函数
        formatter = self.formats.get(format_type, self._format_apa)

        # 格式化参考文献
        bibliography = []
        for i, citation in enumerate(citations):
            formatted = formatter(citation, options)

            entry = {
                'id': citation.get('id', i + 1),
                'original': citation,
                'formatted': formatted,
                'number': i + 1 if options.get('auto_numbering', True) else None
            }

            bibliography.append(entry)

        # 排序
        sort_by = options.get('sort_by', 'citation_order')
        if sort_by == 'author':
            bibliography.sort(key=lambda x: x['original'].get('author', ''))
        elif sort_by == 'year':
            bibliography.sort(key=lambda x: x['original'].get('year', ''))

        # 重新编号
        if options.get('auto_numbering', True):
            for i, entry in enumerate(bibliography):
                entry['number'] = i + 1

        return bibliography

    def _format_apa(self, citation: Dict[str, Any], options: Dict[str, Any]) -> str:
        """
        APA格式化

        Args:
            citation: 参考文献
            options: 处理选项

        Returns:
            str: 格式化后的文本
        """
        author = citation.get('author', '未知作者')
        year = citation.get('year', '无年份')
        title = citation.get('title', '无标题')
        source = citation.get('source', '无来源')

        # APA格式：Author. (Year). Title. Source.
        formatted = f"{author}. ({year}). {title}. {source}."

        # 添加URL（如果启用且有URL）
        if options.get('include_url', True) and citation.get('url'):
            formatted += f" Retrieved from {citation['url']}"

        return formatted

    def _format_mla(self, citation: Dict[str, Any], options: Dict[str, Any]) -> str:
        """
        MLA格式化

        Args:
            citation: 参考文献
            options: 处理选项

        Returns:
            str: 格式化后的文本
        """
        author = citation.get('author', '未知作者')
        title = citation.get('title', '无标题')
        source = citation.get('source', '无来源')
        year = citation.get('year', '无年份')

        # MLA格式：Author. "Title." Source, Year.
        formatted = f"{author}. \"{title}\". {source}, {year}."

        # 添加URL（如果启用且有URL）
        if options.get('include_url', True) and citation.get('url'):
            formatted += f" {citation['url']}."

        return formatted

    def _format_chicago(self, citation: Dict[str, Any], options: Dict[str, Any]) -> str:
        """
        Chicago格式化

        Args:
            citation: 参考文献
            options: 处理选项

        Returns:
            str: 格式化后的文本
        """
        author = citation.get('author', '未知作者')
        title = citation.get('title', '无标题')
        source = citation.get('source', '无来源')
        year = citation.get('year', '无年份')

        # Chicago格式：Author. Title. Source, Year.
        formatted = f"{author}. {title}. {source}, {year}."

        return formatted

    def _format_gb7714(self, citation: Dict[str, Any], options: Dict[str, Any]) -> str:
        """
        GB/T 7714格式化

        Args:
            citation: 参考文献
            options: 处理选项

        Returns:
            str: 格式化后的文本
        """
        author = citation.get('author', '未知作者')
        title = citation.get('title', '无标题')
        source = citation.get('source', '无来源')
        year = citation.get('year', '无年份')

        # GB/T 7714格式：Author. Title[M]. Source, Year.
        if year:
            formatted = f"{author}. {title}[M]. {source}, {year}."
        else:
            formatted = f"{author}. {title}[M]. {source}."

        return formatted

    def _generate_footnotes(self, footnotes: List[Dict[str, Any]], format_type: str, options: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        生成脚注

        Args:
            footnotes: 脚注列表
            format_type: 格式类型
            options: 处理选项

        Returns:
            List[Dict[str, Any]]: 脚注列表
        """
        footnotes_result = []

        for i, footnote in enumerate(footnotes):
            # 格式化脚注
            formatted = self._format_footnote(footnote, format_type, options)

            entry = {
                'id': footnote.get('id', i + 1),
                'original': footnote,
                'formatted': formatted,
                'number': i + 1
            }

            footnotes_result.append(entry)

        return footnotes_result

    def _format_footnote(self, footnote: Dict[str, Any], format_type: str, options: Dict[str, Any]) -> str:
        """
        格式化脚注

        Args:
            footnote: 脚注
            format_type: 格式类型
            options: 处理选项

        Returns:
            str: 格式化后的文本
        """
        text = footnote.get('text', '')
        references = footnote.get('references', [])

        # 简单格式化：文本 + 参考文献
        formatted = text

        if references:
            formatted += f" [{', '.join(str(r) for r in references)}]"

        return formatted

    def _check_consistency(self, bibliography: List[Dict[str, Any]], footnotes: List[Dict[str, Any]], citations: List[Dict[str, Any]], options: Dict[str, Any]) -> Dict[str, Any]:
        """
        检查一致性

        Args:
            bibliography: 参考文献列表
            footnotes: 脚注列表
            citations: 原始参考文献列表
            options: 处理选项

        Returns:
            Dict[str, Any]: 一致性检查报告
        """
        issues = []

        # 检查引用完整性
        issues.extend(self._check_citation_completeness(footnotes, bibliography))

        # 检查引用格式一致性
        issues.extend(self._check_format_consistency(bibliography))

        # 检查引用编号一致性
        issues.extend(self._check_numbering_consistency(bibliography, footnotes))

        return {
            'total_issues': len(issues),
            'issues': issues,
            'is_consistent': len(issues) == 0
        }

    def _check_citation_completeness(self, footnotes: List[Dict[str, Any]], bibliography: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        检查引用完整性

        Args:
            footnotes: 脚注列表
            bibliography: 参考文献列表

        Returns:
            List[Dict[str, Any]]: 问题列表
        """
        issues = []

        # 获取所有参考文献ID
        citation_ids = set(b['id'] for b in bibliography)

        # 检查脚注中的引用是否都存在于参考文献列表中
        for footnote in footnotes:
            references = footnote.get('original', {}).get('references', [])
            for ref_id in references:
                if ref_id not in citation_ids:
                    issues.append({
                        'type': 'missing_citation',
                        'message': f'脚注引用的参考文献ID {ref_id} 不存在于参考文献列表中',
                        'severity': 'error',
                        'footnote_id': footnote.get('id'),
                        'citation_id': ref_id
                    })

        return issues

    def _check_format_consistency(self, bibliography: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        检查引用格式一致性

        Args:
            bibliography: 参考文献列表

        Returns:
            List[Dict[str, Any]]: 问题列表
        """
        issues = []

        # 简化实现：检查是否所有参考文献都有作者和年份
        for entry in bibliography:
            citation = entry.get('original', {})
            if not citation.get('author'):
                issues.append({
                    'type': 'missing_author',
                    'message': f'参考文献ID {entry["id"]} 缺少作者',
                    'severity': 'warning',
                    'citation_id': entry.get('id')
                })

            if not citation.get('year'):
                issues.append({
                    'type': 'missing_year',
                    'message': f'参考文献ID {entry["id"]} 缺少年份',
                    'severity': 'warning',
                    'citation_id': entry.get('id')
                })

        return issues

    def _check_numbering_consistency(self, bibliography: List[Dict[str, Any]], footnotes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        检查引用编号一致性

        Args:
            bibliography: 参考文献列表
            footnotes: 脚注列表

        Returns:
            List[Dict[str, Any]]: 问题列表
        """
        issues = []

        # 简化实现：检查编号是否连续
        bib_numbers = [b['number'] for b in bibliography if b['number'] is not None]
        if bib_numbers:
            expected_numbers = list(range(1, len(bib_numbers) + 1))
            if bib_numbers != expected_numbers:
                issues.append({
                    'type': 'numbering_inconsistency',
                    'message': f'参考文献编号不连续，期望：{expected_numbers}，实际：{bib_numbers}',
                    'severity': 'warning'
                })

        # 检查脚注编号是否连续
        footnote_numbers = [f['number'] for f in footnotes]
        expected_numbers = list(range(1, len(footnote_numbers) + 1))
        if footnote_numbers != expected_numbers:
            issues.append({
                'type': 'footnote_numbering_inconsistency',
                'message': f'脚注编号不连续，期望：{expected_numbers}，实际：{footnote_numbers}',
                'severity': 'warning'
            })

        return issues

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
            'supported_formats': list(self.formats.keys()),
            'mode': 'rule_based'
        }

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        验证配置

        Args:
            config: 配置字典

        Returns:
            bool: 配置是否有效
        """
        # 检查格式是否支持
        if 'format' in config:
            format_type = config['format']
            if format_type not in self.formats:
                logger.error(f"Unsupported format: {format_type}")
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
            logger.info("zotero-better-bibtex plugin (rule-based) cleaned up successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to cleanup zotero-better-bibtex plugin: {e}")
            return False
