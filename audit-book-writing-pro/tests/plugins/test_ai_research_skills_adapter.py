"""
ai-research-skills适配器单元测试
"""

import unittest
import sys
import os

# 添加src目录到Python路径
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.plugins.ai_research_skills_adapter import AIResearchSkillsAdapter


class TestAIResearchSkillsAdapter(unittest.TestCase):
    """ai-research-skills适配器测试"""

    def setUp(self):
        """测试前准备"""
        self.adapter = AIResearchSkillsAdapter()

    def test_initialize(self):
        """测试初始化"""
        config = {
            'timeout': 60,
            'max_retries': 3
        }

        result = self.adapter.initialize(config)

        self.assertTrue(result)
        self.assertTrue(self.adapter.is_initialized)
        self.assertEqual(self.adapter.timeout, 60)

    def test_validate_config(self):
        """测试配置验证"""
        # 有效配置
        valid_config = {
            'timeout': 60,
            'max_retries': 3,
            'quality_threshold': 0.7,
            'max_suggestions': 5
        }
        self.assertTrue(self.adapter.validate_config(valid_config))

        # 无效的timeout
        invalid_config = {
            'timeout': -1
        }
        self.assertFalse(self.adapter.validate_config(invalid_config))

        # 无效的quality_threshold
        invalid_config = {
            'quality_threshold': 1.5
        }
        self.assertFalse(self.adapter.validate_config(invalid_config))

    def test_process(self):
        """测试处理"""
        # 初始化适配器
        config = {
            'timeout': 60
        }
        self.adapter.initialize(config)

        # 准备输入数据
        input_data = {
            'content': '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

## 审计的目标

根据《审计准则第1101号》的规定，审计的目标是对财务报表是否不存在重大错报提供合理保证。

## 审计的原则

因此，审计应当遵循独立性、客观性、公正性的原则。

此外，审计人员还应当保持职业怀疑态度。

综上，审计是保证财务信息质量的重要手段。
            '''.strip(),
            'chapter_type': 'theoretical',
            'context': {
                'chapter_id': '第1章',
                'book_title': '审计基础理论'
            },
            'options': {
                'strict_mode': False,
                'quality_threshold': 0.7,
                'max_suggestions': 5
            }
        }

        # 处理
        result = self.adapter.process(input_data)

        # 验证结果
        self.assertIn('structure_analysis', result)
        self.assertIn('logic_analysis', result)
        self.assertIn('quality_assessment', result)
        self.assertIn('metadata', result)

    def test_structure_analysis(self):
        """测试章节结构分析"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备测试内容
        content = '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

## 审计的目标

根据《审计准则第1101号》的规定，审计的目标是对财务报表是否不存在重大错报提供合理保证。

## 审计的原则

因此，审计应当遵循独立性、客观性、公正性的原则。

此外，审计人员还应当保持职业怀疑态度。

综上，审计是保证财务信息质量的重要手段。
        '''.strip()

        # 分析结构
        result = self.adapter._analyze_structure(content, {}, {})

        # 验证结果
        self.assertIn('detected_type', result)
        self.assertIn('confidence', result)
        self.assertIn('features', result)
        self.assertIn('suggestions', result)

    def test_extract_structure_features(self):
        """测试提取结构特征"""
        content = '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

## 审计的目标

根据《审计准则第1101号》的规定，审计的目标是对财务报表是否不存在重大错报提供合理保证。
        '''.strip()

        features = self.adapter._extract_structure_features(content)

        self.assertIn('total_paragraphs', features)
        self.assertIn('total_sections', features)
        self.assertIn('has_theory', features)
        self.assertIn('has_clear_structure', features)
        self.assertTrue(features['has_theory'])
        self.assertTrue(features['has_clear_structure'])

    def test_classify_chapter_type(self):
        """测试识别章节类型"""
        features = {
            'has_theory': True,
            'has_guidance': False,
            'has_case_study': False,
            'avg_paragraph_length': 150,
            'has_clear_structure': True
        }

        chapter_type, confidence = self.adapter._classify_chapter_type(features)

        self.assertIn(chapter_type, ['theoretical', 'practical', 'case_study', 'mixed'])
        self.assertGreaterEqual(confidence, 0.0)
        self.assertLessEqual(confidence, 1.0)

    def test_logic_analysis(self):
        """测试逻辑连贯性分析"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备测试内容
        content = '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

## 审计的目标

根据《审计准则第1101号》的规定，审计的目标是对财务报表是否不存在重大错报提供合理保证。

## 审计的原则

因此，审计应当遵循独立性、客观性、公正性的原则。

此外，审计人员还应当保持职业怀疑态度。

综上，审计是保证财务信息质量的重要手段。
        '''.strip()

        # 分析逻辑
        result = self.adapter._analyze_logic(content, {}, {})

        # 验证结果
        self.assertIn('coherence_score', result)
        self.assertIn('total_paragraphs', result)
        self.assertIn('issues', result)
        self.assertIn('improvements', result)

    def test_calculate_coherence_score(self):
        """测试计算逻辑连贯性得分"""
        paragraphs = [
            '审计是指独立的第三方对被审计单位进行检查的活动。',
            '因此，审计应当遵循独立性、客观性、公正性的原则。',
            '此外，审计人员还应当保持职业怀疑态度。'
        ]

        score = self.adapter._calculate_coherence_score(paragraphs)

        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_identify_logic_issues(self):
        """测试识别逻辑问题"""
        paragraphs = [
            '审计是指独立的第三方对被审计单位进行检查的活动。',
            '审计是指独立的第三方对被审计单位进行检查的活动。',
            '审计是指独立的第三方对被审计单位进行检查的非常长的活动，非常长的内容。'
        ]

        issues = self.adapter._identify_logic_issues(paragraphs, {})

        self.assertIsInstance(issues, list)
        self.assertTrue(any(i['type'] == 'duplicate_content' for i in issues))

    def test_quality_assessment(self):
        """测试内容质量评估"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备测试内容
        content = '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

## 审计的目标

根据《审计准则第1101号》的规定，审计的目标是对财务报表是否不存在重大错报提供合理保证。

## 审计的原则

因此，审计应当遵循独立性、客观性、公正性的原则。

此外，审计人员还应当保持职业怀疑态度。

综上，审计是保证财务信息质量的重要手段。
        '''.strip()

        # 评估质量
        result = self.adapter._assess_quality(content, {}, {})

        # 验证结果
        self.assertIn('overall_score', result)
        self.assertIn('dimensions', result)
        self.assertIn('strengths', result)
        self.assertIn('weaknesses', result)

    def test_assess_clarity(self):
        """测试评估清晰度"""
        content = '审计是指独立的第三方对被审计单位进行检查的活动。'
        score = self.adapter._assess_clarity(content)

        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_assess_completeness(self):
        """测试评估完整性"""
        content = '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

## 审计的目标

根据《审计准则第1101号》的规定，审计的目标是对财务报表是否不存在重大错报提供合理保证。
        '''.strip()

        score = self.adapter._assess_completeness(content)

        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_assess_readability(self):
        """测试评估可读性"""
        content = '''
# 审计的基本理论

## 审计的定义

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。
        '''.strip()

        score = self.adapter._assess_readability(content)

        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_cross_chapter_analysis(self):
        """测试跨章节关联分析"""
        context = {
            'chapter_id': '第3章'
        }

        result = self.adapter._analyze_cross_chapter(context, {})

        self.assertIn('relations', result)
        self.assertIn('duplicates', result)
        self.assertIsInstance(result['relations'], list)

    def test_get_metadata(self):
        """测试获取元数据"""
        metadata = self.adapter.get_metadata()

        self.assertEqual(metadata['name'], 'ai-research-skills')
        self.assertEqual(metadata['version'], '1.0.0')
        self.assertIn('capabilities', metadata)

    def test_health_check(self):
        """测试健康检查"""
        health = self.adapter.health_check()

        self.assertIn('name', health)
        self.assertIn('status', health)
        self.assertIn('initialized', health)

    def test_practical_chapter_type(self):
        """测试实务操作型章节识别"""
        content = '''
# 现金审计实务

## 审计目标

现金审计的目标是验证现金余额的真实性、完整性和准确性。

## 审计程序

首先，审计人员应当核对现金日记账与总账余额。

其次，应当进行盘点。

最后，编制审计工作底稿。

## 审计要点

注意事项：1. 盘点时应当在场
2. 应当注意现金保管措施
        '''.strip()

        features = self.adapter._extract_structure_features(content)
        chapter_type, confidence = self.adapter._classify_chapter_type(features)

        self.assertEqual(chapter_type, 'practical')

    def test_case_study_chapter_type(self):
        """测试案例分析型章节识别"""
        content = '''
# 某上市公司审计案例分析

## 案例背景

某上市公司2023年度财务报表审计案例。

## 案例分析

经审计发现，该公司存在以下问题：

1. 收入确认不规范
2. 存货计价方法不当

## 审计启示

因此，审计人员应当重点关注收入确认和存货计价。

此外，还应当加强内部控制审计。
        '''.strip()

        features = self.adapter._extract_structure_features(content)
        chapter_type, confidence = self.adapter._classify_chapter_type(features)

        self.assertEqual(chapter_type, 'case_study')


if __name__ == '__main__':
    unittest.main()
