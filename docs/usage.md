# 使用指南

## 目录

- [快速开始](#快速开始)
- [压缩模式](#压缩模式)
- [API参考](#api参考)
- [使用示例](#使用示例)
- [最佳实践](#最佳实践)

---

## 快速开始

### 安装

```bash
pip install ancientman-cn
```

### 基础使用

```python
from ancientman import AncientmanCompressor

# 创建压缩器
compressor = AncientmanCompressor(mode="standard")

# 压缩文本
text = "数据库连接超时通常是因为网络连接不稳定。"
compressed = compressor.compress(text)
print(compressed)  # 输出: 库连超时→网不稳
```

---

## 压缩模式

### 轻度模式 (lite)

**节省率:** ~52%

**特点:**
- 去除填充词
- 保留完整句子结构
- 适合快速参考

**示例:**
```python
compressor = AncientmanCompressor("lite")
text = "数据库连接超时通常是因为网络连接不稳定。"
result = compressor.compress(text)
# 输出: "数据库连接超时原因:网络不稳定"
```

### 标准模式 (standard) - 默认

**节省率:** ~66%

**特点:**
- 片段化句子
- 省略助词
- 使用→表示因果
- 适合日常开发

**示例:**
```python
compressor = AncientmanCompressor("standard")
text = "数据库连接超时通常是因为网络连接不稳定。"
result = compressor.compress(text)
# 输出: "库连超时→网不稳"
```

### 极致模式 (ultra)

**节省率:** ~74%

**特点:**
- 最大化缩写
- 符号表示因果关系
- 适合专家快速查阅

**示例:**
```python
compressor = AncientmanCompressor("ultra")
text = "数据库连接超时通常是因为网络连接不稳定。"
result = compressor.compress(text)
# 输出: "库连逾→网不稳"
```

### 古风模式 (classical)

**节省率:** ~73%

**特点:**
- 极简文言风格
- 无典故
- 独特的压缩体验

**示例:**
```python
from ancientman import ClassicalCompressor

compressor = ClassicalCompressor()
text = "数据库连接超时通常是因为网络连接不稳定。"
result = compressor.compress(text)
# 输出: "库连逾→网不稳"
```

---

## API参考

### AncientmanCompressor

主压缩器类。

```python
class AncientmanCompressor:
    def __init__(self, mode: str = "standard")
    def compress(self, text: str) -> str
    def get_stats(self, original: str, compressed: str) -> Dict[str, float]
```

**参数:**
- `mode`: 压缩模式，可选 `"lite"`, `"standard"`, `"ultra"`

**方法:**
- `compress(text)`: 压缩文本
- `get_stats(original, compressed)`: 获取压缩统计

### ClassicalCompressor

古风压缩器类。

```python
class ClassicalCompressor:
    def compress(self, text: str) -> str
    def get_stats(self, original: str, compressed: str) -> Dict[str, float]
```

### 便捷函数

```python
from ancientman.compressor import (
    compress_lite,      # 轻度压缩
    compress_standard,  # 标准压缩
    compress_ultra,     # 极致压缩
)
from ancientman.classical_compressor import (
    compress_classical, # 古风压缩
)
```

---

## 使用示例

### 示例1: React性能优化

```python
from ancientman import AncientmanCompressor

text = """
好的，这个问题可能是因为你在组件内部创建了新的对象或函数。
每次渲染都会产生新的引用，导致React认为属性发生了变化。
"""

compressor = AncientmanCompressor("standard")
result = compressor.compress(text)
print(result)
# 输出: 组件重渲染→内部新对象/函数→新引用→React属性变化
```

### 示例2: 获取压缩统计

```python
from ancientman import AncientmanCompressor

compressor = AncientmanCompressor("ultra")
text = "数据库连接超时通常是因为网络连接不稳定。"
compressed = compressor.compress(text)
stats = compressor.get_stats(text, compressed)

print(f"原始长度: {stats['original_length']}")
print(f"压缩后: {stats['compressed_length']}")
print(f"节省: {stats['saved_chars']} 字符")
print(f"节省率: {stats['save_ratio']}%")
```

### 示例3: 批量压缩

```python
from ancientman import AncientmanCompressor

texts = [
    "数据库连接超时。",
    "React组件重复渲染。",
    "API接口返回404错误。",
]

compressor = AncientmanCompressor("standard")

for text in texts:
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"{text} -> {compressed} (-{stats['save_ratio']}%)")
```

---

## 最佳实践

### 1. 选择合适的模式

- **初学者**: 使用 `lite` 模式
- **日常开发**: 使用 `standard` 模式（默认）
- **快速查阅**: 使用 `ultra` 模式
- **追求风格**: 使用 `classical` 模式

### 2. 注意可读性

虽然压缩可以节省token，但也要确保压缩后的内容仍然可读。如果压缩后的内容难以理解，建议：
- 降低压缩强度
- 分段压缩
- 保留关键术语

### 3. 技术术语处理

压缩器会自动处理常见的技术术语：
- `数据库` → `库`
- `服务器` → `服`
- `配置` → `配`
- `连接` → `连`

对于专业术语，压缩器会尽量保留其可识别性。

### 4. 与LLM配合使用

古代人模式最适合与中文大模型配合使用：

```
用户: /古代人 标准
AI: 已切换到标准压缩模式

用户: 为什么我的React组件一直在重新渲染？
AI: 组件重渲染→内部新对象/函数→新引用→React属性变化→子组件重渲。用useMemo/useCallback。查依赖。
```

### 5. 命令行使用

在支持古代人模式的平台上：

```
/古代人 [轻度|标准|极致|古风]
/ancientman [lite|standard|ultra|classical]
```

---

## 常见问题

**Q: 压缩后的内容还能理解吗？**

A: 可以。古代人模式在压缩的同时保持了技术准确性。轻度模式几乎不影响理解，极致模式需要一些适应。

**Q: 支持英文吗？**

A: 主要针对中文优化，但也可以处理中英混合文本。

**Q: 可以自定义词汇映射吗？**

A: 目前不支持自定义映射，未来版本可能会添加此功能。

**Q: 压缩率是固定的吗？**

A: 不是。压缩率取决于原文的冗余程度，通常在50%-75%之间。

---

## 更多资源

- [GitHub仓库](https://github.com/yourusername/ancientman-cn)
- [测试报告](../ancientman-cn-大模型对比测试报告.md)
- [示例代码](../examples/demo.py)
