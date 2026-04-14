#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COBOL Coding Agent 测试用例
"""

import os
import unittest
from unittest.mock import Mock, patch
from cobol_agent import CobolAgent

class TestCobolAgent(unittest.TestCase):
    """测试COBOL Coding Agent"""
    
    def setUp(self):
        """设置测试环境"""
        # 保存原始环境变量
        self.original_api_key = os.getenv('MODELSCOPE_API_KEY')
        # 设置测试用的API密钥
        os.environ['MODELSCOPE_API_KEY'] = 'test_api_key'
    
    def tearDown(self):
        """清理测试环境"""
        # 恢复原始环境变量
        if self.original_api_key:
            os.environ['MODELSCOPE_API_KEY'] = self.original_api_key
        elif 'MODELSCOPE_API_KEY' in os.environ:
            del os.environ['MODELSCOPE_API_KEY']
    
    def test_initialization(self):
        """测试初始化功能"""
        agent = CobolAgent()
        self.assertIsNotNone(agent.openai_client)
    
    @patch('cobol_agent.OpenAI')
    def test_generate_cobol_code(self, mock_openai):
        """测试代码生成功能"""
        # 模拟OpenAI客户端
        mock_response = Mock()
        mock_message = Mock()
        mock_message.content = "COBOL代码测试"
        mock_choice = Mock()
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        agent = CobolAgent()
        code = agent.generate_cobol_code("创建一个简单的COBOL程序")
        self.assertEqual(code, "COBOL代码测试")
    
    @patch('cobol_agent.OpenAI')
    def test_analyze_cobol_code(self, mock_openai):
        """测试代码分析功能"""
        # 模拟OpenAI客户端
        mock_response = Mock()
        mock_message = Mock()
        mock_message.content = "分析结果测试"
        mock_choice = Mock()
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        agent = CobolAgent()
        analysis = agent.analyze_cobol_code("COBOL代码")
        self.assertEqual(analysis, "分析结果测试")
    
    def test_format_cobol_code(self):
        """测试代码格式化功能"""
        agent = CobolAgent()
        code = "IDENTIFICATION DIVISION."
        formatted_code = agent.format_cobol_code(code)
        self.assertEqual(formatted_code, code)
    
    def test_highlight_cobol_code(self):
        """测试代码高亮功能"""
        agent = CobolAgent()
        code = "IDENTIFICATION DIVISION."
        highlighted_code = agent.highlight_cobol_code(code)
        self.assertIsInstance(highlighted_code, str)
    
    def test_initialization_without_api_key(self):
        """测试没有API密钥时的初始化"""
        # 删除API密钥
        del os.environ['MODELSCOPE_API_KEY']
        
        agent = CobolAgent()
        self.assertIsNone(agent.openai_client)

if __name__ == '__main__':
    unittest.main()
