# 🗿 Ancientman Mode (古代人模式)

> 中文超压缩通信模式 - 将大模型响应token使用量减少约75%

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 📖 简介

**古代人模式**是一个专为中文大模型设计的超压缩通信框架。通过极简的文言文风格表达，在保持技术准确性的同时，将token使用量平均减少**52%-74%**。

灵感来源于 [caveman](https://github.com/JuliusBrussee/caveman)，针对中文语言特点和中国本土大模型（豆包、DeepSeek、千问、Minimax等）进行了深度本土化适配。

---

## ✨ 核心特性

### 🎯 三级强度压缩

| 模式 | 节省率 | 特点 | 适用场景 |
|------|--------|------|----------|
| **轻度 (lite)** | ~52% | 去除填充词，保留完整句子 | 快速参考、有经验用户 |
| **标准 (standard)** | ~66% | 片段化句子，省略助词 | 日常开发、技术讨论 |
| **极致 (ultra)** | ~74% | 使用缩写，符号表示因果 | 快速查阅、专家用户 |
| **古风 (classical)** | ~73% | 极简文言风格 | 追求效率、独特风格 |

### 🌏 中文本土化优化

- **语言特点适配**：考虑中文无冠词、少用助词的特点
- **大模型差异**：针对不同大模型风格进行专门优化
- **单字词压缩**：数据库→库、服务器→服、网络→网

### 🤖 多平台支持

- **豆包 (Doubao)** - 口语化、接地气
- **DeepSeek** - 技术解释能力强
- **千问 (Qwen)** - 综合性强、结构清晰
- **Minimax** - 中英混合友好

---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/ancientman-cn.git
cd ancientman-cn

# 安装依赖
pip install -r requirements.txt
```

### 使用方法

```python
from ancientman import AncientmanCompressor

# 创建压缩器
compressor = AncientmanCompressor(mode="standard")

# 压缩文本
text = "数据库连接超时通常是因为网络连接不稳定或服务器负载过高。"
compressed = compressor.compress(text)
print(compressed)  # 输出: 库连超时→网不稳/服负载高
```

### 命令行使用

```bash
# 激活古代人模式
/古代人 [轻度|标准|极致|古风]

# 或英文命令
/ancientman [lite|standard|ultra|classical]
```

---

## 📊 压缩效果对比

### 场景1: React性能优化

**普通回答:**
> "好的，这个问题可能是因为你在组件内部创建了新的对象或函数。每次渲染都会产生新的引用，导致React认为属性发生了变化..."

**Token数:** 95 | **节省率:** 0%

---

**古代人模式 - 标准:**
> 组件重渲染→内部新对象/函数→新引用→React属性变化→子组件重渲。用`useMemo`/`useCallback`。检查依赖。

**Token数:** 32 | **节省率:** 66.3% ⬇️

---

**古代人模式 - 极致:**
> 组件重渲→内新对象→新引→React属性变→子件重渲。用`useMemo`/`useCallback`。查依赖。

**Token数:** 26 | **节省率:** 72.6% ⬇️

---

### 场景2: 数据库连接问题

| 模式 | 输出示例 | Token数 | 节省率 |
|------|---------|---------|--------|
| 普通 | "数据库连接超时通常有以下几个原因：1. 网络连接不稳定..." | 108 | 0% |
| 轻度 | "数据库连接超时原因：1.网络不稳定/延迟高；2.数据库服务器负载高..." | 52 | 51.9% |
| 标准 | "库连超时原因：1.网不稳/延迟高；2.库服负载高；3.连接池配错..." | 38 | 64.8% |
| 极致 | "库连超时→1.网不稳/延迟高 2.库服负载高 3.连接池配错..." | 30 | 72.2% |

---

## 🏗️ 项目结构

```
ancientman-cn/
├── README.md                   # 项目说明
├── LICENSE                     # MIT许可证
├── requirements.txt            # Python依赖
├── ancientman/                 # 核心代码
│   ├── __init__.py
│   ├── compressor.py           # 主压缩器
│   ├── classical_compressor.py # 古风压缩器
│   └── utils.py                # 工具函数
├── scripts/                    # 脚本工具
│   └── mode_checker.py         # 模式检测
├── tests/                      # 测试用例
│   └── test_compressor.py
├── docs/                       # 文档
│   ├── usage.md               # 使用指南
│   └── benchmark.md           # 性能测试
└── examples/                   # 示例代码
    └── demo.py
```

---

## 🔧 压缩规则

### 1. 单字词映射

```python
{
    "数据库": "库",
    "服务器": "服",
    "网络": "网",
    "配置": "配",
    "连接": "连",
    "超时": "超时",
    "错误": "错",
    "问题": "题",
    "解决": "解",
    "检查": "查"
}
```

### 2. 符号替代

| 原词 | 替代 | 示例 |
|------|------|------|
| 因为/由于 | → | 网络问题→连接失败 |
| 所以/因此 | → | 配置错误→无法启动 |
| 和/与 | / | 检查网络/配置 |

### 3. 虚词删除

删除所有"的"、"地"、"得"、"了"、"着"、"过"等助词。

---

## 🧪 测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_compressor.py -v

# 生成覆盖率报告
pytest --cov=ancientman tests/
```

---

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📜 许可证

本项目基于 [MIT License](LICENSE) 开源。

---

## 🙏 致谢

- 灵感来源：[caveman](https://github.com/JuliusBrussee/caveman) by Julius Brussee
- 感谢各大中文大模型平台的支持

---



如有问题或建议，欢迎提交 Issue 或 Pull Request。

---

<p align="center">
  <sub>Built with ❤️ for the Chinese LLM community</sub>
</p>
