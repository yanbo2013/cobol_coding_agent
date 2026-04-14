#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COBOL Coding Agent 安装配置
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cobol-coding-agent',
    version='0.1.0',
    description='一个基于ModelScope的COBOL代码生成和处理工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='COBOL Coding Agent Team',
    author_email='contact@example.com',
    url='https://github.com/yourusername/cobol_coding_agent',
    packages=find_packages(),
    py_modules=['cobol_agent'],
    include_package_data=True,
    install_requires=[
        'openai',
        'click',
        'python-dotenv',
        'pygments'
    ],
    entry_points={
        'console_scripts': [
            'cobol-agent=cobol_agent:cli'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Quality Assurance'
    ],
    python_requires='>=3.9'
)
