"""
lexnlp适配器单元测试
"""

import unittest
import sys
import os

# 添加src目录到Python路径
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.plugins.lexnlp_adapter import LexNLPAdapter


class TestLexNLPAdapter(unittest.TestCase):
    """lexnlp适配器测试"""

    def setUp(self):
        """测试前准备"""
        self.adapter = LexNLPAdapter()

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
            'consistency_threshold': 0.8
        }
        self.assertTrue(self.adapter.validate_config(valid_config))

        # 无效的timeout
        invalid_config = {
            'timeout': -1
        }
        self.assertFalse(self.adapter.validate_config(invalid_config))

        # 无效的consistency_threshold
        invalid_config = {
            'consistency_threshold': 1.5
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
# 审计的基本概念

审计是指独立的第三方对被审计单位的财务报表、内部控制等进行检查和评价的活动。

根据《中华人民共和国审计法》第二条规定：国家实行审计监督制度。

审计师应当按照审计准则执行审计程序，获取充分的审计证据。

注册会计师应当保持职业怀疑态度。
            '''.strip(),
            'domain': 'audit',
            'context': {
                'chapter_id': '第1章',
                'book_title': '审计基础理论'
            },
            'options': {
                'strict_mode': False,
                'consistency_threshold': 0.8,
                'extract_articles': True,
                'extract_entities': True
            }
        }

        # 处理
        result = self.adapter.process(input_data)

        # 验证结果
        self.assertIn('terminology_check', result)
        self.assertIn('legal_analysis', result)
        self.assertIn('article_extraction', result)
        self.assertIn('metadata', result)

    def test_check_terminology(self):
        """测试术语校对"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备测试内容
        content = '''
审计师应当执行审计程序，获取充分的审计证据。

审计人员应当保持职业怀疑态度。

注册会计师应当遵守审计准则。
        '''.strip()

        # 检查术语
        result = self.adapter._check_terminology(content, 'audit', {})

        # 验证结果
        self.assertIn('terms', result)
        self.assertIn('overall_consistency', result)
        self.assertIn('consistency_issues', result)
        self.assertIn('suggestions', result)

    def test_extract_terms(self):
        """测试提取术语"""
        content = '''
审计师应当执行审计程序，获取充分的审计证据。

审计人员应当保持职业怀疑态度。

注册会计师应当遵守审计准则。
        '''.strip()

        terms = self.adapter._extract_terms(content, 'audit')

        self.assertIsInstance(terms, list)
        self.assertTrue(len(terms) > 0)
        self.assertTrue(any(t['term'] == '审计师' for t in terms))
        self.assertTrue(any(t['term'] == '审计程序' for t in terms))

    def test_check_consistency(self):
        """测试术语统一性检查"""
        terms = [
            {'term': '审计师', 'position': 0, 'length': 3, 'context': '审计师应当执行审计程序'},
            {'term': '审计人员', 'position': 20, 'length': 4, 'context': '审计人员应当保持职业怀疑态度'},
            {'term': '注册会计师', 'position': 40, 'length': 5, 'context': '注册会计师应当遵守审计准则'}
        ]

        issues = self.adapter._check_consistency(terms, {'enable_synonym_check': True})

        self.assertIsInstance(issues, list)
        self.assertTrue(any(i['type'] == 'inconsistent_synonyms' for i in issues))

    def test_detect_synonyms(self):
        """测试同义词检测"""
        terms = [
            {'term': '审计师', 'position': 0, 'length': 3, 'context': '审计师应当执行审计程序'},
            {'term': '审计人员', 'position': 20, 'length': 4, 'context': '审计人员应当保持职业怀疑态度'},
            {'term': '注册会计师', 'position': 40, 'length': 5, 'context': '注册会计师应当遵守审计准则'}
        ]

        synonym_groups = self.adapter._detect_synonyms(terms)

        self.assertIsInstance(synonym_groups, list)
        self.assertTrue(len(synonym_groups) > 0)

    def test_detect_ambiguity(self):
        """测试歧义检测"""
        terms = [
            {'term': '审计', 'position': 0, 'length': 2, 'context': '审计师应当执行审计程序'},
            {'term': '审计', 'position': 100, 'length': 2, 'context': '审计报告应当准确'},
            {'term': '审计', 'position': 200, 'length': 2, 'context': '审计风险需要评估'}
        ]

        ambiguity_issues = self.adapter._detect_ambiguity(terms)

        self.assertIsInstance(ambiguity_issues, list)

    def test_calculate_overall_consistency(self):
        """测试计算整体一致性得分"""
        terms = [
            {'term': '审计师', 'position': 0, 'length': 3, 'context': '审计师应当执行审计程序'},
            {'term': '审计人员', 'position': 20, 'length': 4, 'context': '审计人员应当保持职业怀疑态度'}
        ]

        consistency_issues = [
            {'type': 'inconsistent_synonyms', 'message': '同一概念使用了不同术语'}
        ]

        score = self.adapter._calculate_overall_consistency(terms, consistency_issues)

        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_generate_terminology_suggestions(self):
        """测试生成术语修正建议"""
        terms = [
            {'term': '审计师', 'position': 0, 'length': 3, 'context': '审计师应当执行审计程序'},
            {'term': '审计人员', 'position': 20, 'length': 4, 'context': '审计人员应当保持职业怀疑态度'}
        ]

        consistency_issues = [
            {
                'type': 'inconsistent_synonyms',
                'message': '同一概念使用了不同术语',
                'terms': ['审计师', '审计人员']
            }
        ]

        suggestions = self.adapter._generate_terminology_suggestions(terms, consistency_issues, {})

        self.assertIsInstance(suggestions, list)
        self.assertTrue(len(suggestions) > 0)

    def test_analyze_legal(self):
        """测试法律分析"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备测试内容
        content = '''
根据《中华人民共和国审计法》第二条规定：国家实行审计监督制度。

审计师应当遵守《审计准则第1101号》的规定。

注册会计师应当获取充分的审计证据。
        '''.strip()

        # 分析法律
        result = self.adapter._analyze_legal(content, 'audit', {})

        # 验证结果
        self.assertIn('entities', result)
        self.assertIn('sentences', result)

    def test_extract_legal_entities(self):
        """测试提取法律实体"""
        content = '''
根据《中华人民共和国审计法》第二条规定：国家实行审计监督制度。

审计师应当遵守《审计准则第1101号》的规定。

注册会计师应当获取充分的审计证据。

第十二条审计师应当保持独立性。
        '''.strip()

        entities = self.adapter._extract_legal_entities(content, 'audit')

        self.assertIsInstance(entities, list)
        self.assertTrue(len(entities) > 0)

        # 检查是否识别出法规
        self.assertTrue(any(e['type'] == 'law' for e in entities))

        # 检查是否识别出条款号
        self.assertTrue(any(e['type'] == 'article' for e in entities))

        # 检查是否识别出审计主体
        self.assertTrue(any(e['type'] == 'audit_subject' for e in entities))

    def test_analyze_sentences(self):
        """测试句子分析"""
        content = '''
审计师应当执行审计程序。

审计人员应当保持职业怀疑态度。

注册会计师应当遵守审计准则。
        '''.strip()

        sentences = self.adapter._analyze_sentences(content)

        self.assertIsInstance(sentences, list)
        self.assertTrue(len(sentences) == 3)
        self.assertTrue(all('index' in s for s in sentences))
        self.assertTrue(all('text' in s for s in sentences))

    def test_extract_articles(self):
        """测试抽取法律条文"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备测试内容
        content = '''
根据《中华人民共和国审计法》第二条规定：国家实行审计监督制度。

第三十五条规定：审计机关对被审计单位的财务收支进行审计监督。

第十八条：审计机关有权要求被审计单位提供有关资料。
        '''.strip()

        # 抽取条文
        result = self.adapter._extract_articles(content, 'audit', {})

        # 验证结果
        self.assertIn('articles', result)
        self.assertIn('summary', result)

    def test_extract_articles_from_text(self):
        """测试从文本中抽取法律条文"""
        content = '''
根据《中华人民共和国审计法》第二条规定：国家实行审计监督制度。

第三十五条规定：审计机关对被审计单位的财务收支进行审计监督。

第十八条：审计机关有权要求被审计单位提供有关资料。
        '''.strip()

        articles = self.adapter._extract_articles_from_text(content, 'audit')

        self.assertIsInstance(articles, list)
        self.assertTrue(len(articles) > 0)

    def test_generate_article_summary(self):
        """测试生成条文摘要"""
        articles = [
            {'reference': '第二条规定：', 'content': '国家实行审计监督制度。', 'position': 0},
            {'reference': '第三十五条规定：', 'content': '审计机关对被审计单位的财务收支进行审计监督。', 'position': 50}
        ]

        summary = self.adapter._generate_article_summary(articles)

        self.assertEqual(summary['total_count'], 2)
        self.assertGreater(summary['average_length'], 0)

    def test_get_metadata(self):
        """测试获取元数据"""
        metadata = self.adapter.get_metadata()

        self.assertEqual(metadata['name'], 'lexnlp')
        self.assertEqual(metadata['version'], '1.0.0')
        self.assertIn('capabilities', metadata)

    def test_health_check(self):
        """测试健康检查"""
        health = self.adapter.health_check()

        self.assertIn('name', health)
        self.assertIn('status', health)
        self.assertIn('initialized', health)

    def test_audit_domain_terms(self):
        """测试审计领域术语提取"""
        content = '''
审计师应当执行审计程序，获取充分的审计证据。

内部控制是审计的重要组成部分。

注册会计师应当遵守审计准则。
        '''.strip()

        terms = self.adapter._extract_terms(content, 'audit')

        self.assertTrue(any(t['term'] == '审计师' for t in terms))
        self.assertTrue(any(t['term'] == '审计程序' for t in terms))
        self.assertTrue(any(t['term'] == '内部控制' for t in terms))

    def test_legal_domain_terms(self):
        """测试法律领域术语提取"""
        content = '''
根据《中华人民共和国民法典》的规定，合同双方应当遵守诚实信用原则。

最高人民法院发布了相关司法解释。

司法部制定了相关管理办法。
        '''.strip()

        terms = self.adapter._extract_terms(content, 'legal')

        self.assertTrue(any(t['term'] == '民法典' for t in terms) or any('民法典' in t['context'] for t in terms))


if __name__ == '__main__':
    unittest.main()
