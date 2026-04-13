#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COBOL Coding Agent

一个基于Claude和Ollama的COBOL代码生成和处理工具
"""

import os
import click
import anthropic
import ollama
from dotenv import load_dotenv
from pygments import highlight
from pygments.lexers import CobolLexer
from pygments.formatters import TerminalFormatter

# 加载配置
load_dotenv()

class CobolAgent:
    def __init__(self):
        """初始化COBOL代理"""
        self.claude_client = None
        self.ollama_client = None
        self._initialize_clients()
    
    def _initialize_clients(self):
        """初始化API客户端"""
        # 初始化Claude客户端
        claude_api_key = os.getenv('ANTHROPIC_API_KEY')
        if claude_api_key:
            self.claude_client = anthropic.Anthropic(api_key=claude_api_key)
        
        # 初始化Ollama客户端
        try:
            self.ollama_client = ollama.Client()
        except Exception as e:
            print(f"警告: 无法连接到Ollama: {e}")
    
    def generate_cobol_code(self, prompt, model="claude-3-sonnet-20240229", temperature=0.7):
        """生成COBOL代码"""
        if self.claude_client:
            return self._generate_with_claude(prompt, model, temperature)
        elif self.ollama_client:
            return self._generate_with_ollama(prompt, model, temperature)
        else:
            raise Exception("没有可用的AI模型客户端")
    
    def _generate_with_claude(self, prompt, model, temperature):
        """使用Claude生成COBOL代码"""
        message = self.claude_client.messages.create(
            model=model,
            max_tokens=4096,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": f"作为COBOL编程专家，请根据以下需求生成COBOL代码:\n{prompt}"
                }
            ]
        )
        return message.content[0].text
    
    def _generate_with_ollama(self, prompt, model, temperature):
        """使用Ollama生成COBOL代码"""
        response = self.ollama_client.generate(
            model=model,
            prompt=f"作为COBOL编程专家，请根据以下需求生成COBOL代码:\n{prompt}",
            options={"temperature": temperature}
        )
        return response["response"]
    
    def analyze_cobol_code(self, code, model="claude-3-sonnet-20240229"):
        """分析COBOL代码"""
        if self.claude_client:
            message = self.claude_client.messages.create(
                model=model,
                max_tokens=4096,
                temperature=0.3,
                messages=[
                    {
                        "role": "user",
                        "content": f"作为COBOL编程专家，请分析以下COBOL代码，指出潜在问题并提供改进建议:\n{code}"
                    }
                ]
            )
            return message.content[0].text
        elif self.ollama_client:
            response = self.ollama_client.generate(
                model=model,
                prompt=f"作为COBOL编程专家，请分析以下COBOL代码，指出潜在问题并提供改进建议:\n{code}"
            )
            return response["response"]
        else:
            raise Exception("没有可用的AI模型客户端")
    
    def format_cobol_code(self, code):
        """格式化COBOL代码"""
        # 这里可以实现更复杂的COBOL代码格式化逻辑
        return code
    
    def highlight_cobol_code(self, code):
        """高亮显示COBOL代码"""
        return highlight(code, CobolLexer(), TerminalFormatter())

@click.group()
def cli():
    """COBOL Coding Agent命令行工具"""
    pass

@cli.command()
@click.option('--prompt', '-p', required=True, help='生成COBOL代码的提示')
@click.option('--model', '-m', default='claude-3-sonnet-20240229', help='使用的模型')
@click.option('--temperature', '-t', default=0.7, help='生成温度')
@click.option('--output', '-o', help='输出文件')
def generate(prompt, model, temperature, output):
    """生成COBOL代码"""
    agent = CobolAgent()
    try:
        code = agent.generate_cobol_code(prompt, model, temperature)
        
        # 高亮显示代码
        highlighted_code = agent.highlight_cobol_code(code)
        print(highlighted_code)
        
        # 保存到文件
        if output:
            with open(output, 'w') as f:
                f.write(code)
            print(f"代码已保存到: {output}")
    except Exception as e:
        click.echo(f"错误: {e}", err=True)

@cli.command()
@click.option('--file', '-f', required=True, help='COBOL代码文件')
@click.option('--model', '-m', default='claude-3-sonnet-20240229', help='使用的模型')
def analyze(file, model):
    """分析COBOL代码"""
    agent = CobolAgent()
    try:
        with open(file, 'r') as f:
            code = f.read()
        
        analysis = agent.analyze_cobol_code(code, model)
        print(analysis)
    except Exception as e:
        click.echo(f"错误: {e}", err=True)

@cli.command()
@click.option('--file', '-f', required=True, help='COBOL代码文件')
@click.option('--output', '-o', help='输出文件')
def format(file, output):
    """格式化COBOL代码"""
    agent = CobolAgent()
    try:
        with open(file, 'r') as f:
            code = f.read()
        
        formatted_code = agent.format_cobol_code(code)
        highlighted_code = agent.highlight_cobol_code(formatted_code)
        print(highlighted_code)
        
        if output:
            with open(output, 'w') as f:
                f.write(formatted_code)
            print(f"格式化后的代码已保存到: {output}")
    except Exception as e:
        click.echo(f"错误: {e}", err=True)

if __name__ == '__main__':
    cli()
