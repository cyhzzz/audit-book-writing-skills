"""
法规引用提取器单元测试
"""

import unittest
import sys
import os

# 添加src目录到Python路径
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.utils.citation_extractor import (
    LawCitation,
    CitationExtractor,
    get_extractor,
    extract_citations
)


class TestCitationExtractor(unittest.TestCase):
    """法规引用提取器测试"""

    def setUp(self):
        """测试前准备"""
        self.extractor = CitationExtractor()

    def test_extract_law_citation(self):
        """测试提取法规引用"""
        text = "根据《审计准则第1101号——财务报表审计的目标和总体要求》第5条规定，..."

        citations = self.extractor.extract_citations(text)

        self.assertEqual(len(citations), 1)
        self.assertIn('审计准则第1101号——财务报表审计的目标和总体要求', citations[0].law_name)
        self.assertEqual(citations[0].year, '2022')
        self.assertEqual(citations[0].article, '5')

    def test_extract_multiple_citations(self):
        """测试提取多个法规引用"""
        text = """
        根据《审计准则第1101号——财务报表审计的目标和总体要求》第5条规定，
        同时参考《中华人民共和国审计法》第10条的要求，
        以及《内部控制基本规范》第12条的规定。
        """

        citations = self.extractor.extract_citations(text)

        self.assertEqual(len(citations), 3)
        self.assertIn('审计准则第1101号', citations[0].law_name)
        self.assertIn('审计法', citations[1].law_name)
        self.assertIn('内部控制基本规范', citations[2].law_name)

    def test_extract_citation_with_location(self):
        """测试提取法规引用（包含位置信息）"""
        text = "根据《审计准则第1101号》第5条规定，..."

        citations = self.extractor.extract_citations(text)

        self.assertEqual(len(citations), 1)
        self.assertIsNotNone(citations[0].location)
        self.assertIn('line', citations[0].location)
        self.assertIn('column', citations[0].location)

    def test_filter_by_keyword(self):
        """测试关键词过滤"""
        text = "根据《审计准则第1101号》第5条规定，同时参考《普通法律文件》第3条。"

        citations = self.extractor.extract_citations(text)

        # 应该只提取包含关键词的引用
        self.assertEqual(len(citations), 1)
        self.assertIn('审计准则', citations[0].law_name)

    def test_extract_article_after_citation(self):
        """测试提取法规引用后面的条款号"""
        text = "根据《审计准则第1101号》第5条规定，审计人员应当..."

        citations = self.extractor.extract_citations(text)

        self.assertEqual(len(citations), 1)
        self.assertEqual(citations[0].article, '5')

    def test_chinese_number_to_arabic(self):
        """测试中文数字转阿拉伯数字"""
        self.assertEqual(self.extractor._chinese_number_to_arabic('一'), '1')
        self.assertEqual(self.extractor._chinese_number_to_arabic('十'), '10')
        self.assertEqual(self.extractor._chinese_number_to_arabic('五'), '5')
        self.assertEqual(self.extractor._chinese_number_to_arabic('123'), '123')

    def test_extract_citation_with_context(self):
        """测试从指定位置提取法规引用（包含上下文）"""
        text = "根据《审计准则第1101号》第5条规定，审计人员应当..."
        span = (3, 19)  # 《审计准则第1101号》的位置

        citation = self.extractor.extract_citation_with_context(text, span)

        self.assertIn('审计准则第1101号', citation.law_name)
        self.assertEqual(citation.source_text, '《审计准则第1101号》')

    def test_to_dict(self):
        """测试转换为字典"""
        citation = LawCitation(
            law_name='《审计准则第1101号》',
            year='2022',
            article='5'
        )

        citation_dict = self.extractor.to_dict(citation)

        self.assertEqual(citation_dict['law_name'], '《审计准则第1101号》')
        self.assertEqual(citation_dict['year'], '2022')
        self.assertEqual(citation_dict['article'], '5')

    def test_to_dict_list(self):
        """测试转换为字典列表"""
        citations = [
            LawCitation(law_name='《审计准则第1101号》', year='2022'),
            LawCitation(law_name='《审计法》', year='2021')
        ]

        citation_dicts = self.extractor.to_dict_list(citations)

        self.assertEqual(len(citation_dicts), 2)
        self.assertEqual(citation_dicts[0]['law_name'], '《审计准则第1101号》')
        self.assertEqual(citation_dicts[1]['law_name'], '《审计法》')

    def test_get_extractor(self):
        """测试获取全局提取器"""
        extractor1 = get_extractor()
        extractor2 = get_extractor()

        # 应该返回同一个实例
        self.assertIs(extractor1, extractor2)

    def test_extract_citations_convenience_function(self):
        """测试便捷函数"""
        text = "根据《审计准则第1101号》第5条规定，..."

        citations = extract_citations(text)

        self.assertEqual(len(citations), 1)
        self.assertIn('law_name', citations[0])
        self.assertIn('year', citations[0])
        self.assertIn('article', citations[0])


if __name__ == '__main__':
    unittest.main()
