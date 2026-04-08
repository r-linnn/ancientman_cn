"""
Ancientman Mode - 使用示例

演示如何使用古代人模式进行文本压缩
"""

from ancientman import AncientmanCompressor, ClassicalCompressor


def demo_basic():
    """基础使用示例"""
    print("=" * 60)
    print("🗿 Ancientman Mode - 基础示例")
    print("=" * 60)
    
    text = "数据库连接超时通常是因为网络连接不稳定或服务器负载过高。"
    
    print(f"\n原始文本: {text}")
    print(f"字符数: {len(text)}\n")
    
    # 轻度压缩
    compressor = AncientmanCompressor("lite")
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"轻度模式: {compressed}")
    print(f"字符数: {stats['compressed_length']}, 节省: {stats['save_ratio']}%\n")
    
    # 标准压缩
    compressor = AncientmanCompressor("standard")
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"标准模式: {compressed}")
    print(f"字符数: {stats['compressed_length']}, 节省: {stats['save_ratio']}%\n")
    
    # 极致压缩
    compressor = AncientmanCompressor("ultra")
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"极致模式: {compressed}")
    print(f"字符数: {stats['compressed_length']}, 节省: {stats['save_ratio']}%\n")


def demo_react():
    """React场景示例"""
    print("=" * 60)
    print("⚛️  React性能优化场景")
    print("=" * 60)
    
    text = """好的，这个问题可能是因为你在组件内部创建了新的对象或函数。
每次渲染都会产生新的引用，导致React认为属性发生了变化，
从而触发子组件的重新渲染。你可以尝试使用useMemo来记忆化这个值，
或者使用useCallback来记忆化函数。"""
    
    print(f"\n原始文本:\n{text}")
    print(f"字符数: {len(text)}\n")
    
    # 标准压缩
    compressor = AncientmanCompressor("standard")
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"标准模式: {compressed}")
    print(f"字符数: {stats['compressed_length']}, 节省: {stats['save_ratio']}%\n")
    
    # 极致压缩
    compressor = AncientmanCompressor("ultra")
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"极致模式: {compressed}")
    print(f"字符数: {stats['compressed_length']}, 节省: {stats['save_ratio']}%\n")


def demo_classical():
    """古风模式示例"""
    print("=" * 60)
    print("📜 古风模式示例")
    print("=" * 60)
    
    text = "数据库连接超时通常是因为网络连接不稳定或服务器负载过高。"
    
    print(f"\n原始文本: {text}")
    print(f"字符数: {len(text)}\n")
    
    compressor = ClassicalCompressor()
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"古风模式: {compressed}")
    print(f"字符数: {stats['compressed_length']}, 节省: {stats['save_ratio']}%\n")


def demo_comparison():
    """全模式对比示例"""
    print("=" * 60)
    print("📊 全模式对比")
    print("=" * 60)
    
    scenarios = [
        "数据库连接超时通常是因为网络连接不稳定或服务器负载过高。",
        "React组件重复渲染通常是因为在组件内部创建了新的对象或函数引用。",
        "API接口返回404错误可能是因为请求的资源不存在或URL路径错误。",
    ]
    
    print("\n场景1: 数据库连接问题")
    print("-" * 40)
    text = scenarios[0]
    print(f"原始: {text} ({len(text)}字符)")
    
    for mode in ["lite", "standard", "ultra"]:
        compressor = AncientmanCompressor(mode)
        compressed = compressor.compress(text)
        stats = compressor.get_stats(text, compressed)
        print(f"{mode:8}: {compressed} ({stats['compressed_length']}字符, -{stats['save_ratio']}%)")
    
    compressor = ClassicalCompressor()
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"{'classical':8}: {compressed} ({stats['compressed_length']}字符, -{stats['save_ratio']}%)")
    
    print("\n场景2: React性能问题")
    print("-" * 40)
    text = scenarios[1]
    print(f"原始: {text} ({len(text)}字符)")
    
    for mode in ["lite", "standard", "ultra"]:
        compressor = AncientmanCompressor(mode)
        compressed = compressor.compress(text)
        stats = compressor.get_stats(text, compressed)
        print(f"{mode:8}: {compressed} ({stats['compressed_length']}字符, -{stats['save_ratio']}%)")
    
    compressor = ClassicalCompressor()
    compressed = compressor.compress(text)
    stats = compressor.get_stats(text, compressed)
    print(f"{'classical':8}: {compressed} ({stats['compressed_length']}字符, -{stats['save_ratio']}%)")


def demo_quick_functions():
    """便捷函数示例"""
    print("=" * 60)
    print("⚡ 便捷函数")
    print("=" * 60)
    
    from ancientman.compressor import compress_lite, compress_standard, compress_ultra
    from ancientman.classical_compressor import compress_classical
    
    text = "使用useMemo来记忆化这个值，避免每次渲染都创建新的引用。"
    
    print(f"\n原始: {text}\n")
    print(f"轻度: {compress_lite(text)}")
    print(f"标准: {compress_standard(text)}")
    print(f"极致: {compress_ultra(text)}")
    print(f"古风: {compress_classical(text)}")


if __name__ == "__main__":
    demo_basic()
    print("\n")
    
    demo_react()
    print("\n")
    
    demo_classical()
    print("\n")
    
    demo_comparison()
    print("\n")
    
    demo_quick_functions()
    
    print("\n" + "=" * 60)
    print("✅ 示例运行完成！")
    print("=" * 60)
