"""
lexnlp适配器 - LexNLPAdapter

基于规则的法律文本处理，实现术语校对、法律实体识别、条文抽取等功能。
"""

import logging
import re
from typing import Dict, Any, List, Optional
from collections import Counter

from .base import (
    SkillPlugin,
    InitializationError,
    ProcessingError,
    ValidationError
)

logger = logging.getLogger(__name__)


class LexNLPAdapter(SkillPlugin):
    """
    lexnlp 插件适配器（基于规则版本）

    实现法律文本处理的核心能力：
    - 术语校对（检查术语使用是否统一）
    - 法律实体识别（识别法规、条款、主体等）
    - 条文精准抽取（精准抽取法律条文内容）
    - 术语同义词识别（识别同一概念的不同表述）
    - 术语歧义检测（检测术语在不同上下文中的歧义）
    """

    def __init__(self):
        super().__init__()
        self.name = "lexnlp"
        self.version = "1.0.0"
        self.description = "法律文本解析、实体识别、术语提取（基于规则）"
        self.capabilities = [
            'terminology_check',
            'legal_entity_recognition',
            'article_extraction',
            'synonym_detection',
            'ambiguity_detection'
        ]
        self.config = None
        self.timeout = 60
        self.max_retries = 3

    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        初始化插件

        Args:
            config: 插件配置
                - timeout: 超时时间（秒）
                - max_retries: 最大重试次数
                - strict_mode: 严格模式
                - consistency_threshold: 一致性阈值
                - enable_synonym_check: 启用同义词检测
                - enable_ambiguity_detection: 启用歧义检测
                - extract_articles: 启用条文抽取
                - extract_entities: 启用实体抽取
                - terminology_dict: 术语字典（可选）

        Returns:
            bool: 初始化是否成功
        """
        try:
            self.config = config

            # 获取超时配置
            self.timeout = config.get('timeout', 60)
            self.max_retries = config.get('max_retries', 3)

            # 预加载术语字典（如果有）
            self.terminology_dict = config.get('terminology_dict', {})

            self.is_initialized = True
            logger.info("lexnlp plugin (rule-based) initialized successfully")
            return True

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to initialize lexnlp plugin: {e}")
            raise InitializationError(f"lexnlp initialization failed: {e}")

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理数据

        Args:
            input_data: 输入数据
                - content: 文本内容
                - domain: 领域（可选，默认：audit）
                - context: 上下文信息
                    - chapter_id: 章节ID
                    - book_title: 书籍标题
                - options: 处理选项
                    - strict_mode: 严格模式
                    - consistency_threshold: 一致性阈值
                    - enable_synonym_check: 启用同义词检测
                    - enable_ambiguity_detection: 启用歧义检测
                    - extract_articles: 启用条文抽取
                    - extract_entities: 启用实体抽取

        Returns:
            Dict[str, Any]: 处理结果
                - terminology_check: 术语校对结果
                - legal_analysis: 法律分析结果
                - article_extraction: 条文抽取结果（如果启用）
        """
        try:
            import time
            start_time = time.time()

            # 获取输入数据
            content = input_data.get('content', '')
            domain = input_data.get('domain', 'audit')
            context = input_data.get('context', {})
            options = input_data.get('options', {})

            # 合并配置选项
            merged_options = {**self.config, **options}

            logger.info(f"Processing text with lexnlp (length: {len(content)})")

            # 术语校对
            terminology_check = self._check_terminology(content, domain, merged_options)

            # 法律分析（实体识别）
            legal_analysis = None
            if merged_options.get('extract_entities', True):
                legal_analysis = self._analyze_legal(content, domain, merged_options)

            # 条文抽取（如果启用）
            article_extraction = None
            if merged_options.get('extract_articles', True):
                article_extraction = self._extract_articles(content, domain, merged_options)

            processing_time = time.time() - start_time

            return {
                'terminology_check': terminology_check,
                'legal_analysis': legal_analysis,
                'article_extraction': article_extraction,
                'metadata': {
                    'processing_time': processing_time,
                    'plugin_version': self.version,
                    'content_length': len(content),
                    'mode': 'rule_based'
                }
            }

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"lexnlp process failed: {e}")
            raise ProcessingError(f"lexnlp processing failed: {e}")

    def _check_terminology(self, text: str, domain: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """
        检查术语统一性

        Args:
            text: 文本内容
            domain: 领域
            options: 处理选项

        Returns:
            Dict[str, Any]: 术语校对结果
        """
        # 提取术语
        terms = self._extract_terms(text, domain)

        # 检查术语统一性
        consistency_issues = self._check_consistency(terms, options)

        # 计算整体一致性得分
        consistency_threshold = options.get('consistency_threshold', 0.8)
        overall_consistency = self._calculate_overall_consistency(terms, consistency_issues)

        # 生成修正建议
        suggestions = self._generate_terminology_suggestions(terms, consistency_issues, options)

        return {
            'terms': terms,
            'overall_consistency': overall_consistency,
            'consistency_issues': consistency_issues,
            'suggestions': suggestions
        }

    def _extract_terms(self, text: str, domain: str) -> List[Dict[str, Any]]:
        """
        提取术语

        Args:
            text: 文本内容
            domain: 领域

        Returns:
            List[Dict[str, Any]]: 术语列表
        """
        # 预定义的审计术语列表
        audit_terms = [
            '审计', '内部审计', '外部审计', '审计师', '审计人员',
            '审计程序', '审计证据', '审计报告', '审计意见',
            '重大错报', '审计风险', '审计计划', '审计目标',
            '内部控制', '控制测试', '实质性程序', '抽样审计',
            '持续经营', '关联方交易', '或有事项', '资产负债表日后事项',
            '审计准则', '国际审计准则', '中国注册会计师审计准则'
        ]

        # 预定义的法律术语列表
        legal_terms = [
            '法规', '法律', '条例', '规定', '办法', '准则', '规范',
            '最高人民法院', '最高人民检察院', '司法部', '证监会',
            '合同法', '公司法', '证券法', '破产法', '民法典'
        ]

        # 选择领域相关的术语
        if domain == 'audit':
            domain_terms = audit_terms
        elif domain == 'legal':
            domain_terms = legal_terms
        else:
            domain_terms = audit_terms + legal_terms

        # 提取文本中的术语
        extracted_terms = []
        for term in domain_terms:
            # 使用正则表达式查找术语出现的位置
            pattern = re.compile(re.escape(term))
            matches = pattern.finditer(text)

            for match in matches:
                extracted_terms.append({
                    'term': term,
                    'position': match.start(),
                    'length': len(term),
                    'context': self._get_context(text, match.start(), match.end())
                })

        return extracted_terms

    def _get_context(self, text: str, start: int, end: int, context_size: int = 30) -> str:
        """
        获取上下文

        Args:
            text: 文本内容
            start: 起始位置
            end: 结束位置
            context_size: 上下文大小

        Returns:
            str: 上下文
        """
        context_start = max(0, start - context_size)
        context_end = min(len(text), end + context_size)
        return text[context_start:context_end]

    def _check_consistency(self, terms: List[Dict[str, Any]], options: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        检查术语统一性

        Args:
            terms: 术语列表
            options: 处理选项

        Returns:
            List[Dict[str, Any]]: 一致性问题列表
        """
        # 统计术语出现次数
        term_counts = Counter(t['term'] for t in terms)

        # 检查术语使用是否统一
        consistency_issues = []

        # 检查术语同义词（如果启用）
        if options.get('enable_synonym_check', True):
            synonym_groups = self._detect_synonyms(terms)
            for group in synonym_groups:
                if len(group) > 1:
                    consistency_issues.append({
                        'type': 'inconsistent_synonyms',
                        'message': f'同一概念使用了不同术语: {", ".join(group)}',
                        'severity': 'warning',
                        'terms': list(group)
                    })

        # 检查术语歧义（如果启用）
        if options.get('enable_ambiguity_detection', True):
            ambiguity_issues = self._detect_ambiguity(terms)
            consistency_issues.extend(ambiguity_issues)

        return consistency_issues

    def _detect_synonyms(self, terms: List[Dict[str, Any]]) -> List[List[str]]:
        """
        检测同义词

        Args:
            terms: 术语列表

        Returns:
            List[List[str]]: 同义词组列表
        """
        # 预定义的同义词组
        synonym_groups = [
            ['审计师', '审计人员', '注册会计师'],
            ['审计程序', '审计方法'],
            ['审计证据', '证据'],
            ['审计报告', '审计意见'],
            ['内部控制', '内控'],
            ['审计准则', '审计规范']
        ]

        detected_groups = []

        for group in synonym_groups:
            # 检查是否多个术语同时出现
            present_terms = [term for term in group if any(t['term'] == term for t in terms)]
            if len(present_terms) > 1:
                detected_groups.append(present_terms)

        return detected_groups

    def _detect_ambiguity(self, terms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        检测术语歧义

        Args:
            terms: 术语列表

        Returns:
            List[Dict[str, Any]]: 歧义问题列表
        """
        ambiguity_issues = []

        # 检查术语在不同上下文中的使用是否一致
        # 简化实现：检查"审计"在不同上下文中的使用
        audit_contexts = [t['context'] for t in terms if '审计' in t['term']]

        # 如果上下文差异较大，可能存在歧义
        unique_contexts = len(set(audit_contexts))
        if unique_contexts > 5:  # 假设超过5种不同的上下文就可能有歧义
            ambiguity_issues.append({
                'type': 'ambiguous_term',
                'message': '"审计"在不同上下文中使用，可能存在歧义',
                'severity': 'warning',
                'term': '审计',
                'context_count': unique_contexts
            })

        return ambiguity_issues

    def _calculate_overall_consistency(self, terms: List[Dict[str, Any]], consistency_issues: List[Dict[str, Any]]) -> float:
        """
        计算整体一致性得分

        Args:
            terms: 术语列表
            consistency_issues: 一致性问题列表

        Returns:
            float: 一致性得分（0-1）
        """
        if not terms:
            return 1.0

        # 计算一致性得分
        error_count = len(consistency_issues)
        total_terms = len(terms)

        # 基础得分
        base_score = 1.0 - (error_count / max(total_terms, 1)) * 0.5

        # 确保得分在0-1范围内
        score = max(0.0, min(1.0, base_score))

        return score

    def _generate_terminology_suggestions(self, terms: List[Dict[str, Any]], consistency_issues: List[Dict[str, Any]], options: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        生成术语修正建议

        Args:
            terms: 术语列表
            consistency_issues: 一致性问题列表
            options: 处理选项

        Returns:
            List[Dict[str, Any]]: 修正建议列表
        """
        suggestions = []

        # 根据一致性问题生成建议
        for issue in consistency_issues:
            if issue['type'] == 'inconsistent_synonyms':
                # 建议统一术语
                suggested_term = issue['terms'][0]  # 使用第一个术语作为建议
                suggestions.append({
                    'type': 'unify_terminology',
                    'message': f'建议统一术语为: {suggested_term}',
                    'severity': 'info',
                    'terms': issue['terms'],
                    'suggested_term': suggested_term
                })

            elif issue['type'] == 'ambiguous_term':
                # 建议明确术语含义
                suggestions.append({
                    'type': 'clarify_ambiguity',
                    'message': f'建议明确"{issue["term"]}"在不同上下文中的含义',
                    'severity': 'info',
                    'term': issue['term']
                })

        # 通用建议
        suggestions.append({
            'type': 'terminology_consistency',
            'message': '建议检查全文术语使用是否统一',
            'severity': 'info'
        })

        return suggestions

    def _analyze_legal(self, text: str, domain: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """
        分析法律文本（实体识别）

        Args:
            text: 文本内容
            domain: 领域
            options: 处理选项

        Returns:
            Dict[str, Any]: 法律分析结果
        """
        # 识别法律实体
        entities = self._extract_legal_entities(text, domain)

        # 分析句子结构
        sentences = self._analyze_sentences(text)

        return {
            'entities': entities,
            'sentences': sentences
        }

    def _extract_legal_entities(self, text: str, domain: str) -> List[Dict[str, Any]]:
        """
        提取法律实体

        Args:
            text: 文本内容
            domain: 领域

        Returns:
            List[Dict[str, Any]]: 法律实体列表
        """
        entities = []

        # 识别法规名称
        law_pattern = r'《([^》]+)》'
        laws = re.finditer(law_pattern, text)
        for match in laws:
            entities.append({
                'type': 'law',
                'text': match.group(0),
                'name': match.group(1),
                'position': match.start()
            })

        # 识别条款号
        article_pattern = r'第[一二三四五六七八九十百千万零\d]+条'
        articles = re.finditer(article_pattern, text)
        for match in articles:
            entities.append({
                'type': 'article',
                'text': match.group(0),
                'number': match.group(0),
                'position': match.start()
            })

        # 识别审计主体
        audit_subject_pattern = r'(审计机构|会计师事务所|注册会计师|审计师)'
        subjects = re.finditer(audit_subject_pattern, text)
        for match in subjects:
            entities.append({
                'type': 'audit_subject',
                'text': match.group(0),
                'name': match.group(0),
                'position': match.start()
            })

        return entities

    def _analyze_sentences(self, text: str) -> List[Dict[str, Any]]:
        """
        分析句子结构

        Args:
            text: 文本内容

        Returns:
            List[Dict[str, Any]]: 句子列表
        """
        # 简单的句子分割（基于句号、问号、感叹号）
        sentences = re.split(r'[。！？]', text)

        analyzed_sentences = []
        for i, sentence in enumerate(sentences):
            if sentence.strip():
                analyzed_sentences.append({
                    'index': i + 1,
                    'text': sentence.strip(),
                    'length': len(sentence.strip())
                })

        return analyzed_sentences

    def _extract_articles(self, text: str, domain: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """
        抽取法律条文

        Args:
            text: 文本内容
            domain: 领域
            options: 处理选项

        Returns:
            Dict[str, Any]: 条文抽取结果
        """
        # 抽取法律条文
        articles = self._extract_articles_from_text(text, domain)

        # 生成摘要
        summary = self._generate_article_summary(articles)

        return {
            'articles': articles,
            'summary': summary
        }

    def _extract_articles_from_text(self, text: str, domain: str) -> List[Dict[str, Any]]:
        """
        从文本中抽取法律条文

        Args:
            text: 文本内容
            domain: 领域

        Returns:
            List[Dict[str, Any]]: 法律条文列表
        """
        articles = []

        # 抽取条文引用格式：第X条规定：...
        article_pattern = r'第[一二三四五六七八九十百千万零\d]+条.*?[：:](.*?)(?=第|$|。|。|$)'
        matches = re.finditer(article_pattern, text, re.DOTALL)

        for match in matches:
            articles.append({
                'reference': match.group(0)[:30],  # 取前30个字符作为引用
                'content': match.group(1).strip(),
                'position': match.start()
            })

        return articles

    def _generate_article_summary(self, articles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        生成条文摘要

        Args:
            articles: 法律条文列表

        Returns:
            Dict[str, Any]: 摘要信息
        """
        return {
            'total_count': len(articles),
            'average_length': sum(len(a['content']) for a in articles) / len(articles) if articles else 0
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

        if 'consistency_threshold' in config:
            threshold = config['consistency_threshold']
            if not isinstance(threshold, (int, float)) or not (0 <= threshold <= 1):
                logger.error("Invalid consistency_threshold value")
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
            logger.info("lexnlp plugin (rule-based) cleaned up successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to cleanup lexnlp plugin: {e}")
            return False
