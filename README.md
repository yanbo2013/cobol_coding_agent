# COBOL Coding Agent

一个基于Claude和Ollama的COBOL代码生成和处理工具

## 项目简介

COBOL Coding Agent 是一个命令行工具，利用AI模型（Claude或Ollama）来生成、分析和处理COBOL代码。它可以帮助开发者快速生成COBOL代码模板、分析现有代码的问题，并提供改进建议。

## 功能特性

- ✅ COBOL代码生成：根据自然语言描述生成COBOL代码
- ✅ 代码分析：分析COBOL代码，指出潜在问题并提供改进建议
- ✅ 代码格式化：格式化COBOL代码，提高代码可读性
- ✅ 代码高亮：在终端中高亮显示COBOL代码
- ✅ 多模型支持：支持Claude和Ollama模型

## 安装指南

### 前提条件

- Python 3.9+
- 虚拟环境（推荐）
- Claude API密钥（可选，用于使用Claude模型）
- Ollama（可选，用于使用本地模型）

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/yourusername/cobol_coding_agent.git
cd cobol_coding_agent
```

2. **创建并激活虚拟环境**

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux
source venv/bin/activate
# Windows
# venv\Scripts\activate
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **配置环境变量**

如果使用Claude模型，需要设置API密钥：

```bash
# 创建.env文件
echo "ANTHROPIC_API_KEY=your_api_key" > .env
```

## 使用方法

### 生成COBOL代码

```bash
python cobol_agent.py generate --prompt "创建一个简单的COBOL程序，读取输入文件并计算总和" --output output.cob
```

### 分析COBOL代码

```bash
python cobol_agent.py analyze --file input.cob
```

### 格式化COBOL代码

```bash
python cobol_agent.py format --file input.cob --output formatted.cob
```

## 命令行参数

### generate 命令

- `--prompt, -p`：生成COBOL代码的提示（必填）
- `--model, -m`：使用的模型（默认：claude-3-sonnet-20240229）
- `--temperature, -t`：生成温度（默认：0.7）
- `--output, -o`：输出文件路径

### analyze 命令

- `--file, -f`：要分析的COBOL代码文件（必填）
- `--model, -m`：使用的模型（默认：claude-3-sonnet-20240229）

### format 命令

- `--file, -f`：要格式化的COBOL代码文件（必填）
- `--output, -o`：输出文件路径

## 示例

### 生成示例

```bash
python cobol_agent.py generate --prompt "创建一个COBOL程序，计算1到100的和并输出结果" --output sum.cob
```

### 分析示例

```bash
python cobol_agent.py analyze --file sum.cob
```

## 项目结构

```
cobol_coding_agent/
├── cobol_agent.py        # 主入口脚本
├── requirements.txt      # 依赖文件
├── README.md             # 项目文档
├── src/                  # 源代码目录
├── config/               # 配置文件目录
├── examples/             # 示例代码
└── tests/                # 测试文件
```

## 注意事项

1. 使用Claude模型需要有效的API密钥
2. 使用Ollama需要本地安装并运行Ollama服务
3. 生成的代码可能需要根据具体环境进行调整
4. 分析功能仅提供参考建议，最终决策权在开发者

## 许可证

MIT License
