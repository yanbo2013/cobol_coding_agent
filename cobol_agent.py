#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COBOL Coding Agent

一个基于Claude和Ollama的COBOL代码生成和处理工具
"""

import os
import click
from openai import OpenAI
from dotenv import load_dotenv
from pygments import highlight
from pygments.lexers import CobolLexer
from pygments.formatters import TerminalFormatter

# 加载配置
load_dotenv()

class CobolAgent:
    def __init__(self):
        """初始化COBOL代理"""
        self.openai_client = None
        self._initialize_clients()
    
    def _initialize_clients(self):
        """初始化API客户端"""
        # 初始化OpenAI兼容客户端（用于ModelScope）
        modelscope_api_key = os.getenv('MODELSCOPE_API_KEY')
        if modelscope_api_key:
            self.openai_client = OpenAI(
                api_key=modelscope_api_key,
                base_url="https://api-inference.modelscope.cn/v1"
            )
        else:
            print("警告: 未设置MODELSCOPE_API_KEY环境变量")
    
    def generate_cobol_code(self, prompt, model="Qwen/Qwen3.5-35B-A3B", temperature=0.7):
        """生成COBOL代码"""
        if self.openai_client:
            return self._generate_with_openai(prompt, model, temperature)
        else:
            raise Exception("没有可用的AI模型客户端")
    
    def _generate_with_openai(self, prompt, model, temperature):
        """使用OpenAI兼容接口（ModelScope）生成COBOL代码"""
        try:
            response = self.openai_client.chat.completions.create(
                model=model,
                max_tokens=4096,
                temperature=temperature,
                messages=[
                    {
                        "role": "user",
                        "content": f"作为COBOL编程专家，请根据以下需求生成纯COBOL代码，要求：\n1. 只输出COBOL代码，不要包含任何markdown格式或解释文字\n2. 符合COBOL编程规范和风格\n3. 包含必要的COBOL结构：IDENTIFICATION DIVISION, ENVIRONMENT DIVISION, DATA DIVISION, PROCEDURE DIVISION\n4. 代码可以直接编译和运行\n5. 适当添加注释说明\n\n需求：\n{prompt}"
                    }
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"生成代码时出错: {str(e)}")
    

    

    

    
    def analyze_cobol_code(self, code, model="Qwen/Qwen3.5-35B-A3B"):
        """分析COBOL代码"""
        if self.openai_client:
            try:
                response = self.openai_client.chat.completions.create(
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
                return response.choices[0].message.content
            except Exception as e:
                raise Exception(f"分析代码时出错: {str(e)}")
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
@click.option('--model', '-m', default='Qwen/Qwen3.5-35B-A3B', help='使用的模型')
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
@click.option('--model', '-m', default='Qwen/Qwen3.5-35B-A3B', help='使用的模型')
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
