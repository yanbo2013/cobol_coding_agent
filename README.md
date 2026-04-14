# COBOL Coding Agent

一个基于ModelScope的COBOL代码生成和处理工具

## 项目简介

COBOL Coding Agent 是一个命令行工具，利用ModelScope的API来生成、分析和处理COBOL代码。它可以帮助开发者快速生成COBOL代码模板、分析现有代码的问题，并提供改进建议。

## 功能特性

- ✅ COBOL代码生成：根据自然语言描述生成COBOL代码
- ✅ 代码分析：分析COBOL代码，指出潜在问题并提供改进建议
- ✅ 代码格式化：格式化COBOL代码，提高代码可读性
- ✅ 代码高亮：在终端中高亮显示COBOL代码
- ✅ ModelScope API支持：使用ModelScope的API调用大模型，无需本地部署

## 安装指南

### 前提条件

- Python 3.9+
- 虚拟环境（推荐）
- ModelScope API密钥

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

4. **配置**

本项目使用ModelScope的API来调用大模型，需要设置API密钥：

**获取ModelScope API密钥：**
- 访问 [ModelScope官方网站](https://modelscope.cn)
- 注册并登录账号
- 进入个人中心，获取API密钥

**配置环境变量：**
```bash
# 创建.env文件
echo "MODELSCOPE_API_KEY=your_api_key" > .env
```

**支持的模型：**
- `Qwen/Qwen3.5-35B-A3B`（推荐）
- `Qwen/Qwen2.5-7B-Instruct`
- `Baichuan2/Baichuan2-13B-Chat`
- 其他支持中文的大模型

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
- `--model, -m`：使用的模型（默认：Qwen/Qwen3.5-35B-A3B）
- `--temperature, -t`：生成温度（默认：0.7）
- `--output, -o`：输出文件路径

### analyze 命令

- `--file, -f`：要分析的COBOL代码文件（必填）
- `--model, -m`：使用的模型（默认：Qwen/Qwen3.5-35B-A3B）

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

1. **ModelScope API**：需要有效的API密钥
2. **模型**：推荐使用`Qwen/Qwen3.5-35B-A3B`模型，支持中文
3. **性能**：生成速度取决于网络连接和API响应速度
4. 生成的代码可能需要根据具体环境进行调整
5. 分析功能仅提供参考建议，最终决策权在开发者

## 许可证

MIT License
