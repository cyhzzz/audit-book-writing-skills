"""
zotero-better-bibtex适配器单元测试
"""

import unittest
import sys
import os

# 添加src目录到Python路径
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.plugins.zotero_bibtex_adapter import ZoteroBibtexAdapter


class TestZoteroBibtexAdapter(unittest.TestCase):
    """zotero-better-bibtex适配器测试"""

    def setUp(self):
        """测试前准备"""
        self.adapter = ZoteroBibtexAdapter()

    def test_initialize(self):
        """测试初始化"""
        config = {
            'format': 'APA',
            'timeout': 30
        }

        result = self.adapter.initialize(config)

        self.assertTrue(result)
        self.assertTrue(self.adapter.is_initialized)
        self.assertEqual(self.adapter.config.get('format'), 'APA')

    def test_validate_config(self):
        """测试配置验证"""
        # 有效配置
        valid_config = {
            'format': 'APA',
            'timeout': 30,
            'auto_numbering': True
        }
        self.assertTrue(self.adapter.validate_config(valid_config))

        # 无效的format
        invalid_config = {
            'format': 'INVALID'
        }
        self.assertFalse(self.adapter.validate_config(invalid_config))

        # 无效的timeout
        invalid_config = {
            'timeout': -1
        }
        self.assertFalse(self.adapter.validate_config(invalid_config))

    def test_process(self):
        """测试处理"""
        # 初始化适配器
        config = {
            'format': 'APA'
        }
        self.adapter.initialize(config)

        # 准备输入数据
        input_data = {
            'citations': [
                {
                    'id': 1,
                    'author': '张三',
                    'year': '2023',
                    'title': '审计基础理论',
                    'source': '中国审计出版社',
                    'url': 'https://example.com'
                },
                {
                    'id': 2,
                    'author': '李四',
                    'year': '2024',
                    'title': '内部审计实务',
                    'source': '经济科学出版社'
                }
            ],
            'footnotes': [
                {
                    'id': 1,
                    'text': '这是第一条脚注',
                    'references': [1]
                }
            ],
            'format': 'APA',
            'options': {
                'auto_numbering': True,
                'cross_ref_check': True,
                'include_url': True
            }
        }

        # 处理
        result = self.adapter.process(input_data)

        # 验证结果
        self.assertIn('bibliography', result)
        self.assertIn('footnotes', result)
        self.assertIn('consistency_report', result)
        self.assertEqual(len(result['bibliography']), 2)
        self.assertEqual(len(result['footnotes']), 1)

    def test_generate_bibliography(self):
        """测试生成参考文献列表"""
        # 初始化适配器
        self.adapter.initialize({'format': 'APA'})

        # 准备参考文献
        citations = [
            {
                'id': 1,
                'author': '张三',
                'year': '2023',
                'title': '审计基础理论',
                'source': '中国审计出版社'
            }
        ]

        # 生成参考文献
        bibliography = self.adapter._generate_bibliography(citations, 'APA', {})

        # 验证结果
        self.assertEqual(len(bibliography), 1)
        self.assertEqual(bibliography[0]['id'], 1)
        self.assertIn('formatted', bibliography[0])

    def test_format_apa(self):
        """测试APA格式化"""
        citation = {
            'author': '张三',
            'year': '2023',
            'title': '审计基础理论',
            'source': '中国审计出版社',
            'url': 'https://example.com'
        }

        formatted = self.adapter._format_apa(citation, {'include_url': True})

        self.assertIn('张三', formatted)
        self.assertIn('2023', formatted)
        self.assertIn('审计基础理论', formatted)
        self.assertIn('中国审计出版社', formatted)
        self.assertIn('Retrieved from', formatted)

    def test_format_mla(self):
        """测试MLA格式化"""
        citation = {
            'author': '张三',
            'year': '2023',
            'title': '审计基础理论',
            'source': '中国审计出版社',
            'url': 'https://example.com'
        }

        formatted = self.adapter._format_mla(citation, {'include_url': True})

        self.assertIn('张三', formatted)
        self.assertIn('审计基础理论', formatted)
        self.assertIn('中国审计出版社', formatted)

    def test_format_chicago(self):
        """测试Chicago格式化"""
        citation = {
            'author': '张三',
            'year': '2023',
            'title': '审计基础理论',
            'source': '中国审计出版社'
        }

        formatted = self.adapter._format_chicago(citation, {})

        self.assertIn('张三', formatted)
        self.assertIn('审计基础理论', formatted)
        self.assertIn('中国审计出版社', formatted)

    def test_format_gb7714(self):
        """测试GB/T 7714格式化"""
        citation = {
            'author': '张三',
            'year': '2023',
            'title': '审计基础理论',
            'source': '中国审计出版社'
        }

        formatted = self.adapter._format_gb7714(citation, {})

        self.assertIn('张三', formatted)
        self.assertIn('审计基础理论', formatted)
        self.assertIn('[M]', formatted)
        self.assertIn('中国审计出版社', formatted)

    def test_generate_footnotes(self):
        """测试生成脚注"""
        # 初始化适配器
        self.adapter.initialize({'format': 'APA'})

        # 准备脚注
        footnotes = [
            {
                'id': 1,
                'text': '这是第一条脚注',
                'references': [1, 2]
            }
        ]

        # 生成脚注
        footnotes_result = self.adapter._generate_footnotes(footnotes, 'APA', {})

        # 验证结果
        self.assertEqual(len(footnotes_result), 1)
        self.assertEqual(footnotes_result[0]['id'], 1)
        self.assertIn('formatted', footnotes_result[0])

    def test_format_footnote(self):
        """测试格式化脚注"""
        footnote = {
            'id': 1,
            'text': '这是第一条脚注',
            'references': [1, 2]
        }

        formatted = self.adapter._format_footnote(footnote, 'APA', {})

        self.assertIn('这是第一条脚注', formatted)
        self.assertIn('[1, 2]', formatted)

    def test_check_consistency(self):
        """测试检查一致性"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备参考文献
        bibliography = [
            {
                'id': 1,
                'original': {
                    'id': 1,
                    'author': '张三',
                    'year': '2023'
                },
                'number': 1
            }
        ]

        # 准备脚注
        footnotes = [
            {
                'id': 1,
                'original': {
                    'id': 1,
                    'text': '脚注',
                    'references': [1]
                },
                'number': 1
            }
        ]

        # 检查一致性
        consistency_report = self.adapter._check_consistency(bibliography, footnotes, [], {})

        # 验证结果
        self.assertIn('total_issues', consistency_report)
        self.assertIn('issues', consistency_report)
        self.assertIn('is_consistent', consistency_report)

    def test_check_citation_completeness(self):
        """测试检查引用完整性"""
        # 准备参考文献
        bibliography = [
            {'id': 1, 'number': 1}
        ]

        # 准备脚注（包含不存在的引用）
        footnotes = [
            {
                'id': 1,
                'original': {
                    'id': 1,
                    'references': [1, 2]  # 引用2不存在
                },
                'number': 1
            }
        ]

        # 检查引用完整性
        issues = self.adapter._check_citation_completeness(footnotes, bibliography)

        # 验证结果
        self.assertTrue(len(issues) > 0)
        self.assertTrue(any(i['type'] == 'missing_citation' for i in issues))

    def test_check_format_consistency(self):
        """测试检查格式一致性"""
        # 准备参考文献（缺少作者和年份）
        bibliography = [
            {
                'id': 1,
                'original': {
                    'id': 1,
                    'title': '无作者无年份'
                },
                'number': 1
            }
        ]

        # 检查格式一致性
        issues = self.adapter._check_format_consistency(bibliography)

        # 验证结果
        self.assertTrue(len(issues) > 0)
        self.assertTrue(any(i['type'] == 'missing_author' for i in issues))
        self.assertTrue(any(i['type'] == 'missing_year' for i in issues))

    def test_check_numbering_consistency(self):
        """测试检查编号一致性"""
        # 准备参考文献（编号不连续）
        bibliography = [
            {'id': 1, 'number': 1},
            {'id': 2, 'number': 3}  # 跳过2
        ]

        # 准备脚注（编号不连续）
        footnotes = [
            {'id': 1, 'number': 1},
            {'id': 2, 'number': 3}  # 跳过2
        ]

        # 检查编号一致性
        issues = self.adapter._check_numbering_consistency(bibliography, footnotes)

        # 验证结果
        self.assertTrue(len(issues) > 0)
        self.assertTrue(any(i['type'] == 'numbering_inconsistency' for i in issues))
        self.assertTrue(any(i['type'] == 'footnote_numbering_inconsistency' for i in issues))

    def test_sort_by_author(self):
        """测试按作者排序"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备参考文献
        citations = [
            {
                'id': 1,
                'author': '李四',
                'year': '2024',
                'title': '内部审计实务',
                'source': '经济科学出版社'
            },
            {
                'id': 2,
                'author': '张三',
                'year': '2023',
                'title': '审计基础理论',
                'source': '中国审计出版社'
            }
        ]

        # 生成参考文献（按作者排序）
        bibliography = self.adapter._generate_bibliography(citations, 'APA', {'sort_by': 'author'})

        # 验证结果
        self.assertEqual(bibliography[0]['original']['author'], '张三')
        self.assertEqual(bibliography[1]['original']['author'], '李四')

    def test_sort_by_year(self):
        """测试按年份排序"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备参考文献
        citations = [
            {
                'id': 1,
                'author': '张三',
                'year': '2024',
                'title': '内部审计实务',
                'source': '经济科学出版社'
            },
            {
                'id': 2,
                'author': '李四',
                'year': '2023',
                'title': '审计基础理论',
                'source': '中国审计出版社'
            }
        ]

        # 生成参考文献（按年份排序）
        bibliography = self.adapter._generate_bibliography(citations, 'APA', {'sort_by': 'year'})

        # 验证结果
        self.assertEqual(bibliography[0]['original']['year'], '2023')
        self.assertEqual(bibliography[1]['original']['year'], '2024')

    def test_auto_numbering(self):
        """测试自动编号"""
        # 初始化适配器
        self.adapter.initialize({})

        # 准备参考文献
        citations = [
            {
                'id': 1,
                'author': '张三',
                'year': '2023',
                'title': '审计基础理论',
                'source': '中国审计出版社'
            },
            {
                'id': 2,
                'author': '李四',
                'year': '2024',
                'title': '内部审计实务',
                'source': '经济科学出版社'
            }
        ]

        # 生成参考文献（启用自动编号）
        bibliography = self.adapter._generate_bibliography(citations, 'APA', {'auto_numbering': True})

        # 验证结果
        self.assertEqual(bibliography[0]['number'], 1)
        self.assertEqual(bibliography[1]['number'], 2)

    def test_include_url(self):
        """测试包含URL"""
        citation = {
            'author': '张三',
            'year': '2023',
            'title': '审计基础理论',
            'source': '中国审计出版社',
            'url': 'https://example.com'
        }

        # 包含URL
        formatted_with_url = self.adapter._format_apa(citation, {'include_url': True})
        self.assertIn('Retrieved from', formatted_with_url)
        self.assertIn('https://example.com', formatted_with_url)

        # 不包含URL
        formatted_without_url = self.adapter._format_apa(citation, {'include_url': False})
        self.assertNotIn('Retrieved from', formatted_without_url)

    def test_get_metadata(self):
        """测试获取元数据"""
        metadata = self.adapter.get_metadata()

        self.assertEqual(metadata['name'], 'zotero_better_bibtex')
        self.assertEqual(metadata['version'], '1.0.0')
        self.assertIn('capabilities', metadata)
        self.assertIn('supported_formats', metadata)

    def test_health_check(self):
        """测试健康检查"""
        health = self.adapter.health_check()

        self.assertIn('name', health)
        self.assertIn('status', health)
        self.assertIn('initialized', health)


if __name__ == '__main__':
    unittest.main()
