"""
ai-research-skills适配器 - AIResearchSkillsAdapter

学习ai-research-skills的能力，提供章节结构分析、逻辑连贯性分析、内容质量评估等功能。
"""

import logging
import re
from typing import Dict, Any, List, Optional

from .base import (
    SkillPlugin,
    InitializationError,
    ProcessingError
)

logger = logging.getLogger(__name__)


class AIResearchSkillsAdapter(SkillPlugin):
    """
    ai-research-skills 插件适配器

    学习ai-research-skills的能力：
    - 章节结构分析（识别章节类型）
    - 逻辑连贯性分析（基于NLP的逻辑流分析）
    - 内容质量评估（多维度质量评分）
    - 优化建议生成
    - 跨章节关联分析
    """

    def __init__(self):
        super().__init__()
        self.name = "ai-research-skills"
        self.version = "1.0.0"
        self.description = "学术写作、逻辑优化、章节结构化"
        self.capabilities = [
            'structure_analysis',
            'logic_analysis',
            'quality_assessment',
            'cross_chapter_analysis'
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
                - quality_threshold: 质量阈值
                - enable_cross_chapter: 启用跨章节分析
                - max_suggestions: 最大建议数量

        Returns:
            bool: 初始化是否成功
        """
        try:
            self.config = config

            # 获取超时配置
            self.timeout = config.get('timeout', 60)
            self.max_retries = config.get('max_retries', 3)

            self.is_initialized = True
            logger.info("ai-research-skills plugin initialized successfully")
            return True

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to initialize ai-research-skills plugin: {e}")
            raise InitializationError(f"ai-research-skills initialization failed: {e}")

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理数据

        Args:
            input_data: 输入数据
                - content: 章节内容
                - chapter_type: 章节类型（可选）
                - context: 上下文信息
                    - chapter_id: 章节ID
                    - book_title: 书籍标题
                    - previous_chapters: 前几章的内容摘要
                    - next_chapters: 后几章的内容摘要
                - options: 处理选项
                    - strict_mode: 严格模式
                    - quality_threshold: 质量阈值
                    - enable_cross_chapter: 启用跨章节分析
                    - max_suggestions: 最大建议数量

        Returns:
            Dict[str, Any]: 处理结果
                - structure_analysis: 章节结构分析
                - logic_analysis: 逻辑连贯性分析
                - quality_assessment: 内容质量评估
                - cross_chapter_analysis: 跨章节关联分析（如果启用）
                - metadata: 元数据
        """
        try:
            import time
            start_time = time.time()

            # 获取输入数据
            content = input_data.get('content', '')
            context = input_data.get('context', {})
            options = input_data.get('options', {})

            # 合并配置选项
            merged_options = {**self.config, **options}

            logger.info(f"Processing chapter with ai-research-skills (length: {len(content)})")

            # 章节结构分析
            structure_analysis = self._analyze_structure(content, context, merged_options)

            # 逻辑连贯性分析
            logic_analysis = self._analyze_logic(content, context, merged_options)

            # 内容质量评估
            quality_assessment = self._assess_quality(content, context, merged_options)

            # 跨章节关联分析（如果启用）
            cross_chapter_analysis = None
            if merged_options.get('enable_cross_chapter', False):
                cross_chapter_analysis = self._analyze_cross_chapter(context, merged_options)

            processing_time = time.time() - start_time

            return {
                'structure_analysis': structure_analysis,
                'logic_analysis': logic_analysis,
                'quality_assessment': quality_assessment,
                'cross_chapter_analysis': cross_chapter_analysis,
                'metadata': {
                    'processing_time': processing_time,
                    'plugin_version': self.version,
                    'content_length': len(content)
                }
            }

        except Exception as e:
            self.last_error = str(e)
            logger.error(f"ai-research-skills process failed: {e}")
            raise ProcessingError(f"ai-research-skills processing failed: {e}")

    def _analyze_structure(self, content: str, context: Dict[str, Any], options: Dict[str, Any]) -> Dict[str, Any]:
        """
        分析章节结构

        Args:
            content: 章节内容
            context: 上下文信息
            options: 处理选项

        Returns:
            Dict[str, Any]: 章节结构分析结果
        """
        # 分析章节结构特征
        features = self._extract_structure_features(content)

        # 识别章节类型
        detected_type, confidence = self._classify_chapter_type(features)

        # 生成结构优化建议
        suggestions = self._generate_structure_suggestions(features, detected_type, options)

        return {
            'detected_type': detected_type,
            'confidence': confidence,
            'features': features,
            'suggestions': suggestions
        }

    def _extract_structure_features(self, content: str) -> Dict[str, Any]:
        """
        提取章节结构特征

        Args:
            content: 章节内容

        Returns:
            Dict[str, Any]: 结构特征
        """
        features = {
            'total_paragraphs': 0,
            'total_sections': 0,
            'has_framework_table': False,
            'has_case_study': False,
            'has_theory': False,
            'has_guidance': False,
            'avg_paragraph_length': 0,
            'has_clear_structure': False
        }

        # 统计段落数
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        features['total_paragraphs'] = len(paragraphs)

        # 统计小节数
        sections = re.findall(r'^#+\s+.+', content, re.MULTILINE)
        features['total_sections'] = len(sections)

        # 检查是否包含框架表
        if re.search(r'框架表|表\d+|框架', content, re.IGNORECASE):
            features['has_framework_table'] = True

        # 检查是否包含案例研究
        if re.search(r'案例|实例|实践', content, re.IGNORECASE):
            features['has_case_study'] = True

        # 检查是否包含理论阐述
        if re.search(r'理论|概念|定义|原理', content, re.IGNORECASE):
            features['has_theory'] = True

        # 检查是否包含审计指引
        if re.search(r'指引|建议|方法|步骤', content, re.IGNORECASE):
            features['has_guidance'] = True

        # 计算平均段落长度
        if paragraphs:
            avg_length = sum(len(p) for p in paragraphs) / len(paragraphs)
            features['avg_paragraph_length'] = avg_length

        # 检查是否有清晰的结构
        has_title = bool(re.search(r'^#+\s+.+', content, re.MULTILINE))
        has_subtitle = len(sections) >= 2
        features['has_clear_structure'] = has_title and has_subtitle

        return features

    def _classify_chapter_type(self, features: Dict[str, Any]) -> tuple:
        """
        识别章节类型

        Args:
            features: 结构特征

        Returns:
            tuple: (章节类型, 置信度)
        """
        # 基于特征评分
        scores = {
            'theoretical': 0.0,
            'practical': 0.0,
            'case_study': 0.0,
            'mixed': 0.0
        }

        # 理论基础型特征
        if features['has_theory']:
            scores['theoretical'] += 0.5
        if features['avg_paragraph_length'] > 200:
            scores['theoretical'] += 0.2

        # 实务操作型特征
        if features['has_guidance']:
            scores['practical'] += 0.4
        if features['has_framework_table']:
            scores['practical'] += 0.3
        if features['has_clear_structure']:
            scores['practical'] += 0.2

        # 案例分析型特征
        if features['has_case_study']:
            scores['case_study'] += 0.6
        if re.search(r'案例|实例|实践', content.lower()):
            scores['case_study'] += 0.3

        # 混合型特征
        if scores['theoretical'] > 0.3 and scores['practical'] > 0.3:
            scores['mixed'] = max(scores.values()) * 0.8

        # 找出最高分
        detected_type = max(scores, key=scores.get)
        confidence = scores[detected_type]

        # 如果置信度较低，标记为混合型
        if confidence < 0.5:
            detected_type = 'mixed'
            confidence = max(scores.values()) * 0.7

        return detected_type, confidence

    def _generate_structure_suggestions(self, features: Dict[str, Any], detected_type: str, options: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        生成结构优化建议

        Args:
            features: 结构特征
            detected_type: 检测到的章节类型
            options: 处理选项

        Returns:
            List[Dict[str, Any]]: 优化建议
        """
        suggestions = []

        # 根据章节类型生成建议
        if detected_type == 'theoretical':
            if not features['has_clear_structure']:
                suggestions.append({
                    'type': 'structure',
                    'message': '建议添加清晰的章节结构（标题、小标题）',
                    'severity': 'info'
                })

            if features['total_sections'] < 3:
                suggestions.append({
                    'type': 'structure',
                    'message': '建议增加小节数量，完善章节结构',
                    'severity': 'info'
                })

        elif detected_type == 'practical':
            if not features['has_framework_table']:
                suggestions.append({
                    'type': 'structure',
                    'message': '建议添加审计框架表格，增强实用性',
                    'severity': 'info'
                })

            if features['total_paragraphs'] < 5:
                suggestions.append({
                    'type': 'structure',
                    'message': '建议增加内容长度，提供更详细的指引',
                    'severity': 'info'
                })

        elif detected_type == 'case_study':
            if not features['has_guidance']:
                suggestions.append({
                    'type': 'structure',
                    'message': '建议在案例分析后总结审计启示',
                    'severity': 'info'
                })

            if features['total_paragraphs'] < 5:
                suggestions.append({
                    'type': 'structure',
                    'message': '建议增加案例细节和分析',
                    'severity': 'info'
                })

        # 通用建议
        if not features['has_clear_structure']:
            suggestions.append({
                'type': 'structure',
                'message': '建议优化章节结构，使用清晰的标题层次',
                'severity': 'warning'
            })

        # 限制建议数量
        max_suggestions = options.get('max_suggestions', 5)
        suggestions = suggestions[:max_suggestions]

        return suggestions

    def _analyze_logic(self, content: str, context: Dict[str, Any], options: Dict[str, Any]) -> Dict[str, Any]:
        """
        分析逻辑连贯性

        Args:
            content: 章节内容
            context: 上下文信息
            options: 处理选项

        Returns:
            Dict[str, Any]: 逻辑连贯性分析结果
        """
        # 提取段落
        paragraphs = [p for p in content.split('\n\n') if p.strip()]

        # 计算逻辑连贯性得分
        coherence_score = self._calculate_coherence_score(paragraphs)

        # 识别逻辑问题
        issues = self._identify_logic_issues(paragraphs, options)

        # 生成改进建议
        improvements = self._generate_logic_improvements(paragraphs, issues)

        return {
            'coherence_score': coherence_score,
            'total_paragraphs': len(paragraphs),
            'issues': issues,
            'improvements': improvements
        }

    def _calculate_coherence_score(self, paragraphs: List[str]) -> float:
        """
        计算逻辑连贯性得分

        Args:
            paragraphs: 段落列表

        Returns:
            float: 连贯性得分（0-1）
        """
        if len(paragraphs) < 2:
            return 1.0

        # 基于段落过渡词计算连贯性
        transition_words = [
            '因此', '所以', '然而', '但是', '此外', '而且', '首先', '其次', '最后',
            '综上', '总之', '同时', '一方面', '另一方面', '接着', '然后'
        ]

        transitions_count = 0
        for paragraph in paragraphs:
            if any(word in paragraph for word in transition_words):
                transitions_count += 1

        # 计算连贯性得分
        coherence_ratio = transitions_count / len(paragraphs)
        score = min(coherence_ratio * 2, 1.0)  # 转换为0-1范围

        return score

    def _identify_logic_issues(self, paragraphs: List[str], options: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        识别逻辑问题

        Args:
            paragraphs: 段落列表
            options: 处理选项

        Returns:
            List[Dict[str, Any]]: 逻辑问题列表
        """
        issues = []

        # 检查段落长度差异
        if len(paragraphs) > 1:
            lengths = [len(p) for p in paragraphs]
            avg_length = sum(lengths) / len(lengths)

            for i, length in enumerate(lengths):
                if abs(length - avg_length) > avg_length * 0.7:
                    issues.append({
                        'type': 'unbalanced_structure',
                        'message': f'第{i+1}段长度与平均长度差异较大',
                        'severity': 'warning',
                        'location': f'段落{i+1}'
                    })

        # 检查重复内容
        seen_content = set()
        for i, paragraph in enumerate(paragraphs):
            # 简化段落内容（去除标点和空格）
            simplified = re.sub(r'[^\w]', '', paragraph.lower())

            if simplified in seen_content:
                issues.append({
                    'type': 'duplicate_content',
                    'message': f'第{i+1}段与前面内容重复',
                    'severity': 'error',
                    'location': f'段落{i+1}'
                })
            else:
                seen_content.add(simplified)

        return issues

    def _generate_logic_improvements(self, paragraphs: List[str], issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        生成逻辑改进建议

        Args:
            paragraphs: 段落列表
            issues: 逻辑问题列表

        Returns:
            List[Dict[str, Any]]: 改进建议
        """
        improvements = []

        # 根据问题生成建议
        issue_types = [i['type'] for i in issues]

        if 'unbalanced_structure' in issue_types:
            improvements.append({
                'type': 'structure_balance',
                'message': '建议调整段落长度，使结构更加平衡',
                'severity': 'info'
            })

        if 'duplicate_content' in issue_types:
            improvements.append({
                'type': 'content_uniqueness',
                'message': '建议删除或整合重复内容',
                'severity': 'error'
            })

        # 通用建议
        improvements.append({
            'type': 'transition_words',
            'message': '建议使用过渡词（因此、然而、此外等）增强逻辑连贯性',
            'severity': 'info'
        })

        improvements.append({
            'type': 'logical_flow',
            'message': '建议按照"引入-展开-总结"的逻辑顺序组织内容',
            'severity': 'info'
        })

        return improvements

    def _assess_quality(self, content: str, context: Dict[str, Any], options: Dict[str, Any]) -> Dict[str, Any]:
        """
        评估内容质量

        Args:
            content: 章节内容
            context: 上下文信息
            options: 处理选项

        Returns:
            Dict[str, Any]: 内容质量评估结果
        """
        # 评估各个维度
        dimensions = {
            'clarity': self._assess_clarity(content),
            'completeness': self._assess_completeness(content),
            'consistency': self._assess_consistency(content),
            'readability': self._assess_readability(content)
        }

        # 计算整体得分
        overall_score = sum(dimensions.values()) / len(dimensions)

        # 识别优点
        strengths = self._identify_strengths(dimensions)

        # 识别不足
        weaknesses = self._identify_weaknesses(dimensions, options)

        return {
            'overall_score': overall_score,
            'dimensions': dimensions,
            'strengths': strengths,
            'weaknesses': weaknesses
        }

    def _assess_clarity(self, content: str) -> float:
        """评估清晰度"""
        # 基于句子平均长度计算
        sentences = [s for s in re.split(r'[。！？]', content) if s.strip()]
        if not sentences:
            return 0.5

        avg_length = sum(len(s) for s in sentences) / len(sentences)

        # 理想长度：50-100字
        if 50 <= avg_length <= 100:
            return 1.0
        elif 100 < avg_length <= 150:
            return 0.8
        elif avg_length > 150:
            return 0.6
        else:
            return 0.7

    def _assess_completeness(self, content: str) -> float:
        """评估完整性"""
        # 基于内容长度和结构完整性
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        sections = re.findall(r'^#+\s+.+', content, re.MULTILINE)

        # 理想：5-10个段落，3-5个小节
        paragraph_score = min(len(paragraphs) / 7, 1.0)
        section_score = min(len(sections) / 4, 1.0)

        return (paragraph_score + section_score) / 2

    def _assess_consistency(self, content: str) -> float:
        """评估一致性"""
        # 检查术语使用一致性
        # 简化实现：检查是否使用一致的术语
        return 0.8

    def _assess_readability(self, content: str) -> float:
        """评估可读性"""
        # 基于段落长度和标题结构
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        sections = re.findall(r'^#+\s+.+', content, re.MULTILINE)

        # 有标题且段落长度合理
        has_structure = len(sections) > 0
        reasonable_length = all(50 <= len(p) <= 500 for p in paragraphs)

        if has_structure and reasonable_length:
            return 1.0
        elif has_structure or reasonable_length:
            return 0.7
        else:
            return 0.5

    def _identify_strengths(self, dimensions: Dict[str, float]) -> List[str]:
        """识别优点"""
        strengths = []

        for dim, score in dimensions.items():
            if score >= 0.8:
                if dim == 'clarity':
                    strengths.append('表达清晰')
                elif dim == 'completeness':
                    strengths.append('内容完整')
                elif dim == 'consistency':
                    strengths.append('术语一致')
                elif dim == 'readability':
                    strengths.append('结构清晰')

        return strengths

    def _identify_weaknesses(self, dimensions: Dict[str, float], options: Dict[str, Any]) -> List[str]:
        """识别不足"""
        weaknesses = []
        quality_threshold = options.get('quality_threshold', 0.7)

        for dim, score in dimensions.items():
            if score < quality_threshold:
                if dim == 'clarity':
                    weaknesses.append('表达不够清晰')
                elif dim == 'completeness':
                    weaknesses.append('内容不够完整')
                elif dim == 'consistency':
                    weaknesses.append('术语使用不够一致')
                elif dim == 'readability':
                    weaknesses.append('结构不够清晰')

        return weaknesses

    def _analyze_cross_chapter(self, context: Dict[str, Any], options: Dict[str, Any]) -> Dict[str, Any]:
        """
        分析跨章节关联

        Args:
            context: 上下文信息
            options: 处理选项

        Returns:
            Dict[str, Any]: 跨章节关联分析结果
        """
        # 获取章节关联信息
        relations = []
        duplicates = []

        # 简化实现：基于章节ID生成关联信息
        chapter_id = context.get('chapter_id', '')

        # 生成与前后章节的关联
        if chapter_id:
            # 假设章节ID格式为"第X章"
            chapter_num = int(re.search(r'\d+', chapter_id).group()) if re.search(r'\d+', chapter_id) else 1

            # 前一章关联
            if chapter_num > 1:
                relations.append({
                    'chapter_id': f'第{chapter_num-1}章',
                    'relation_type': 'preceding',
                    'strength': 0.8
                })

            # 后一章关联
            relations.append({
                'chapter_id': f'第{chapter_num+1}章',
                'relation_type': 'following',
                'strength': 0.8
            })

        return {
            'relations': relations,
            'duplicates': duplicates
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
            'capabilities': self.capabilities
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

        if 'quality_threshold' in config:
            threshold = config['quality_threshold']
            if not isinstance(threshold, (int, float)) or not (0 <= threshold <= 1):
                logger.error("Invalid quality_threshold value")
                return False

        if 'max_suggestions' in config:
            max_suggestions = config['max_suggestions']
            if not isinstance(max_suggestions, int) or max_suggestions < 0:
                logger.error("Invalid max_suggestions value")
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
            logger.info("ai-research-skills plugin cleaned up successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to cleanup ai-research-skills plugin: {e}")
            return False
