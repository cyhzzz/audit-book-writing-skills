"""
ChatLaw适配器单元测试（本地检索版本）
"""

import unittest
import sys
import os

# 添加src目录到Python路径
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.plugins.chatlaw_adapter import ChatLawAdapter


class TestChatLawAdapter(unittest.TestCase):
    """ChatLaw适配器测试（本地检索版本）"""

    def setUp(self):
        """测试前准备"""
        self.adapter = ChatLawAdapter()

    def test_initialize(self):
        """测试初始化"""
        # 获取默认法规库路径
        default_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            'references', 'laws-database'
        )

        config = {
            'timeout': 30,
            'max_retries': 3
        }

        result = self.adapter.initialize(config)

        self.assertTrue(result)
        self.assertTrue(self.adapter.is_initialized)
        self.assertEqual(self.adapter.timeout, 30)
        self.assertIsNotNone(self.adapter.laws_database_path)

    def test_initialize_with_custom_path(self):
        """测试初始化（自定义法规库路径）"""
        # 获取默认法规库路径
        default_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            'references', 'laws-database'
        )

        config = {
            'laws_database_path': default_path,
            'timeout': 30,
            'max_retries': 3
        }

        result = self.adapter.initialize(config)

        self.assertTrue(result)
        self.assertTrue(self.adapter.is_initialized)
        self.assertEqual(self.adapter.laws_database_path, default_path)

    def test_initialize_invalid_path(self):
        """测试初始化（无效路径）"""
        config = {
            'laws_database_path': '/invalid/path'
        }

        with self.assertRaises(Exception) as context:
            self.adapter.initialize(config)

        self.assertTrue('not found' in str(context.exception))

    def test_validate_config(self):
        """测试配置验证"""
        # 有效配置
        valid_config = {
            'timeout': 30,
            'max_retries': 3
        }
        self.assertTrue(self.adapter.validate_config(valid_config))

        # 无效的timeout
        invalid_config = {
            'timeout': -1
        }
        self.assertFalse(self.adapter.validate_config(invalid_config))

    def test_process(self):
        """测试处理"""
        # 初始化适配器
        config = {
            'timeout': 30
        }
        self.adapter.initialize(config)

        # 准备输入数据
        input_data = {
            'citations': [
                {
                    'law_name': '《中华人民共和国文物保护法》',
                    'year': '2024',
                    'article': '第10条'
                },
                {
                    'law_name': '《中华人民共和国审计法》',
                    'year': '2021',
                    'article': '第5条'
                }
            ],
            'options': {
                'strict_mode': True
            }
        }

        # 处理
        result = self.adapter.process(input_data)

        # 验证结果
        self.assertIn('validation_results', result)
        self.assertIn('details', result)
        self.assertIn('metadata', result)

        # 验证验证结果
        self.assertIn('total_count', result['validation_results'])
        self.assertEqual(result['validation_results']['total_count'], 2)

    def test_get_metadata(self):
        """测试获取元数据"""
        metadata = self.adapter.get_metadata()

        self.assertEqual(metadata['name'], 'ChatLaw')
        self.assertEqual(metadata['version'], '1.0.0')
        self.assertIn('capabilities', metadata)
        self.assertEqual(metadata['mode'], 'local_database')

    def test_health_check(self):
        """测试健康检查"""
        health = self.adapter.health_check()

        self.assertIn('name', health)
        self.assertIn('status', health)
        self.assertIn('initialized', health)

    def test_extract_keywords(self):
        """测试提取关键词"""
        law_name = '《中华人民共和国文物保护法》'
        keywords = self.adapter._extract_keywords(law_name)

        self.assertIsInstance(keywords, list)
        self.assertTrue(len(keywords) > 0)
        self.assertIn('文物保护法', keywords)

    def test_validate_effectiveness(self):
        """测试验证时效性"""
        matched_law = {'file': 'test.md'}

        status, issues = self.adapter._validate_effectiveness(
            '《中华人民共和国文物保护法》',
            '2024',
            matched_law
        )

        self.assertIn(status, ['valid', 'warning'])
        self.assertIsInstance(issues, list)

    def test_validate_article(self):
        """测试验证条款号"""
        matched_law = {'file': 'test.md'}

        result = self.adapter._validate_article(
            '《中华人民共和国文物保护法》',
            '第10条',
            matched_law
        )

        self.assertIn('status', result)
        self.assertIn('issues', result)

    def test_generate_summary(self):
        """测试生成验证总结"""
        validation_results = [
            {
                'validation': {'status': 'valid'},
                'issues': []
            },
            {
                'validation': {'status': 'invalid'},
                'issues': [{'severity': 'error'}]
            },
            {
                'validation': {'status': 'valid'},
                'issues': [{'severity': 'warning'}]
            }
        ]

        summary = self.adapter._generate_summary(validation_results)

        self.assertEqual(summary['total_count'], 3)
        self.assertEqual(summary['valid_count'], 2)
        self.assertEqual(summary['invalid_count'], 1)
        self.assertEqual(summary['warning_count'], 1)
        self.assertAlmostEqual(summary['success_rate'], 2/3, places=2)


if __name__ == '__main__':
    unittest.main()
