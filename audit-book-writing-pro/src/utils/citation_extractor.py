"""
法规引用提取器 - CitationExtractor

从文本中提取法规引用信息。
"""

import re
import logging
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class LawCitation:
    """
    法规引用数据类

    Attributes:
        law_name: 法规全称
        year: 年份
        article: 条款号
        content: 引用的条款内容
        source_text: 原文中的引用文本
        location: 引用位置（页码、行号等）
        span: 在原文中的字符范围
    """
    law_name: str
    year: Optional[str] = None
    article: Optional[str] = None
    content: Optional[str] = None
    source_text: Optional[str] = None
    location: Optional[Dict[str, Any]] = None
    span: Optional[Tuple[int, int]] = None


class CitationExtractor:
    """
    法规引用提取器

    从文本中提取法规引用信息。
    """

    # 法规引用正则表达式（匹配《法规名称》或「法规名称」）
    LAW_CITATION_PATTERN = re.compile(
        r'[《|「]([^》」]+)[》|」]',
        re.MULTILINE
    )

    # 条款号正则表达式（匹配第X条、第X款、第X项等）
    ARTICLE_PATTERN = re.compile(
        r'第([一二三四五六七八九十百千0-9]+)[条款项]',
        re.MULTILINE
    )

    # 年份正则表达式（匹配XXXX年格式）
    YEAR_PATTERN = re.compile(
        r'(\d{4})年'
    )

    # 常见法规关键词（用于提高识别准确率）
    KEYWORDS = [
        '审计准则', '会计法', '审计法', '公司法', '证券法',
        '内部控制', '风险管理', '审计', '法规', '准则'
    ]

    def __init__(self):
        """初始化提取器"""
        self.law_citation_pattern = self.LAW_CITATION_PATTERN
        self.article_pattern = self.ARTICLE_PATTERN
        self.year_pattern = self.YEAR_PATTERN

    def extract_citations(self, text: str) -> List[LawCitation]:
        """
        从文本中提取所有法规引用

        Args:
            text: 输入文本

        Returns:
            List[LawCitation]: 法规引用列表
        """
        citations = []

        # 查找所有法规引用
        matches = self.law_citation_pattern.finditer(text)

        for match in matches:
            try:
                law_name = match.group(1)

                # 过滤：只保留包含关键词的引用
                if not self._contains_keyword(law_name):
                    continue

                # 提取年份
                year = self._extract_year(law_name)

                # 提取条款号
                article = self._extract_article_after(match, text)

                # 提取引用文本（原文中的引用）
                source_text = match.group(0)

                # 提取位置信息
                span = match.span()
                location = self._calculate_location(text, span)

                # 创建引用对象
                citation = LawCitation(
                    law_name=law_name,
                    year=year,
                    article=article,
                    source_text=source_text,
                    location=location,
                    span=span
                )

                citations.append(citation)

            except Exception as e:
                logger.warning(f"Failed to extract citation at position {match.span()}: {e}")

        logger.info(f"Extracted {len(citations)} citations from text")
        return citations

    def extract_citation_with_context(self, text: str, span: Tuple[int, int]) -> LawCitation:
        """
        从指定位置提取法规引用（包含上下文）

        Args:
            text: 输入文本
            span: 文本范围

        Returns:
            LawCitation: 法规引用
        """
        # 提取引用文本
        citation_text = text[span[0]:span[1]]

        # 提取法规名称
        match = self.law_citation_pattern.search(citation_text)
        if not match:
            raise ValueError("No law citation found in the specified span")

        law_name = match.group(1)

        # 提取年份
        year = self._extract_year(law_name)

        # 提取条款号
        article = self._extract_article_after(match, text)

        # 提取位置信息
        location = self._calculate_location(text, span)

        # 创建引用对象
        return LawCitation(
            law_name=law_name,
            year=year,
            article=article,
            source_text=citation_text,
            location=location,
            span=span
        )

    def _contains_keyword(self, text: str) -> bool:
        """
        检查文本是否包含关键词

        Args:
            text: 输入文本

        Returns:
            bool: 是否包含关键词
        """
        return any(keyword in text for keyword in self.KEYWORDS)

    def _extract_year(self, law_name: str) -> Optional[str]:
        """
        提取年份

        Args:
            law_name: 法规名称

        Returns:
            Optional[str]: 年份
        """
        match = self.year_pattern.search(law_name)
        if match:
            return match.group(1)
        return None

    def _extract_article_after(self, match: re.Match, text: str) -> Optional[str]:
        """
        提取法规引用后面的条款号

        Args:
            match: 正则匹配对象
            text: 输入文本

        Returns:
            Optional[str]: 条款号
        """
        # 查找引用后面的文本（最多100个字符）
        after_text = text[match.end():match.end() + 100]

        # 提取条款号
        article_match = self.article_pattern.search(after_text)
        if article_match:
            article_text = article_match.group(1)

            # 转换中文数字
            return self._chinese_number_to_arabic(article_text)

        return None

    def _calculate_location(self, text: str, span: Tuple[int, int]) -> Dict[str, Any]:
        """
        计算位置信息（页码、行号）

        Args:
            text: 输入文本
            span: 文本范围

        Returns:
            Dict[str, Any]: 位置信息
        """
        # 计算行号
        text_before = text[:span[0]]
        line_number = text_before.count('\n') + 1

        # 计算列号
        last_newline_index = text_before.rfind('\n')
        column_number = span[0] - last_newline_index

        return {
            'line': line_number,
            'column': column_number,
            'start': span[0],
            'end': span[1]
        }

    def _chinese_number_to_arabic(self, chinese_number: str) -> str:
        """
        转换中文数字为阿拉伯数字

        Args:
            chinese_number: 中文数字

        Returns:
            str: 阿拉伯数字
        """
        chinese_to_arabic = {
            '一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
            '六': '6', '七': '7', '八': '8', '九': '9', '十': '10',
            '百': '100', '千': '1000'
        }

        # 如果已经是阿拉伯数字，直接返回
        if chinese_number.isdigit():
            return chinese_number

        # 转换
        result = ''
        for char in chinese_number:
            result += chinese_to_arabic.get(char, char)

        return result

    def to_dict(self, citation: LawCitation) -> Dict[str, Any]:
        """
        将法规引用转换为字典

        Args:
            citation: 法规引用

        Returns:
            Dict[str, Any]: 字典形式
        """
        return {
            'law_name': citation.law_name,
            'year': citation.year,
            'article': citation.article,
            'content': citation.content,
            'source_text': citation.source_text,
            'location': citation.location,
            'span': citation.span
        }

    def to_dict_list(self, citations: List[LawCitation]) -> List[Dict[str, Any]]:
        """
        将法规引用列表转换为字典列表

        Args:
            citations: 法规引用列表

        Returns:
            List[Dict[str, Any]]: 字典列表
        """
        return [self.to_dict(citation) for citation in citations]


# 全局提取器实例
_global_extractor = None


def get_extractor() -> CitationExtractor:
    """
    获取全局提取器实例

    Returns:
        CitationExtractor: 提取器实例
    """
    global _global_extractor
    if _global_extractor is None:
        _global_extractor = CitationExtractor()
    return _global_extractor


def extract_citations(text: str) -> List[Dict[str, Any]]:
    """
    从文本中提取所有法规引用（便捷函数）

    Args:
        text: 输入文本

    Returns:
        List[Dict[str, Any]]: 法规引用字典列表
    """
    extractor = get_extractor()
    citations = extractor.extract_citations(text)
    return extractor.to_dict_list(citations)
