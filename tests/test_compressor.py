"""
Ancientman Mode - 单元测试

测试压缩器的各项功能
"""

import pytest
from ancientman import AncientmanCompressor, ClassicalCompressor
from ancientman.compressor import compress_lite, compress_standard, compress_ultra
from ancientman.classical_compressor import compress_classical


class TestAncientmanCompressor:
    """测试AncientmanCompressor类"""
    
    def test_init_valid_modes(self):
        """测试有效的初始化模式"""
        for mode in ["lite", "standard", "ultra"]:
            compressor = AncientmanCompressor(mode)
            assert compressor.mode == mode
    
    def test_init_invalid_mode(self):
        """测试无效的初始化模式"""
        with pytest.raises(ValueError):
            AncientmanCompressor("invalid")
    
    def test_compress_lite(self):
        """测试轻度压缩"""
        compressor = AncientmanCompressor("lite")
        text = "数据库连接超时通常是因为网络连接不稳定。"
        result = compressor.compress(text)
        assert len(result) < len(text)
        assert "数据库" not in result or "库" in result
    
    def test_compress_standard(self):
        """测试标准压缩"""
        compressor = AncientmanCompressor("standard")
        text = "数据库连接超时通常是因为网络连接不稳定。"
        result = compressor.compress(text)
        assert len(result) < len(text)
        assert "→" in result or "因为" not in result
    
    def test_compress_ultra(self):
        """测试极致压缩"""
        compressor = AncientmanCompressor("ultra")
        text = "数据库连接超时通常是因为网络连接不稳定。"
        result = compressor.compress(text)
        assert len(result) < len(text)
    
    def test_get_stats(self):
        """测试统计信息"""
        compressor = AncientmanCompressor("standard")
        original = "数据库连接超时。"
        compressed = compressor.compress(original)
        stats = compressor.get_stats(original, compressed)
        
        assert "original_length" in stats
        assert "compressed_length" in stats
        assert "saved_chars" in stats
        assert "save_ratio" in stats
        assert stats["original_length"] == len(original)
        assert stats["compressed_length"] == len(compressed)
        assert stats["saved_chars"] == len(original) - len(compressed)


class TestClassicalCompressor:
    """测试ClassicalCompressor类"""
    
    def test_compress(self):
        """测试古风压缩"""
        compressor = ClassicalCompressor()
        text = "数据库连接超时通常是因为网络连接不稳定。"
        result = compressor.compress(text)
        assert len(result) < len(text)
    
    def test_get_stats(self):
        """测试统计信息"""
        compressor = ClassicalCompressor()
        original = "数据库连接超时。"
        compressed = compressor.compress(original)
        stats = compressor.get_stats(original, compressed)
        
        assert stats["original_length"] == len(original)
        assert stats["compressed_length"] == len(compressed)


class TestQuickFunctions:
    """测试便捷函数"""
    
    def test_compress_lite(self):
        """测试compress_lite函数"""
        text = "数据库连接超时。"
        result = compress_lite(text)
        assert len(result) < len(text)
    
    def test_compress_standard(self):
        """测试compress_standard函数"""
        text = "数据库连接超时。"
        result = compress_standard(text)
        assert len(result) < len(text)
    
    def test_compress_ultra(self):
        """测试compress_ultra函数"""
        text = "数据库连接超时。"
        result = compress_ultra(text)
        assert len(result) < len(text)
    
    def test_compress_classical(self):
        """测试compress_classical函数"""
        text = "数据库连接超时。"
        result = compress_classical(text)
        assert len(result) < len(text)


class TestCompressionScenarios:
    """测试具体场景"""
    
    def test_react_scenario(self):
        """测试React场景"""
        text = "React组件重复渲染通常是因为在组件内部创建了新的对象或函数引用。"
        compressor = AncientmanCompressor("standard")
        result = compressor.compress(text)
        assert len(result) < len(text)
        stats = compressor.get_stats(text, result)
        assert stats["save_ratio"] > 30  # 至少节省30%
    
    def test_database_scenario(self):
        """测试数据库场景"""
        text = "数据库连接超时通常是因为网络连接不稳定或服务器负载过高。"
        compressor = AncientmanCompressor("standard")
        result = compressor.compress(text)
        assert len(result) < len(text)
        stats = compressor.get_stats(text, result)
        assert stats["save_ratio"] > 30
    
    def test_api_scenario(self):
        """测试API场景"""
        text = "API接口返回404错误可能是因为请求的资源不存在或URL路径错误。"
        compressor = AncientmanCompressor("ultra")
        result = compressor.compress(text)
        assert len(result) < len(text)


class TestEdgeCases:
    """测试边界情况"""
    
    def test_empty_string(self):
        """测试空字符串"""
        compressor = AncientmanCompressor("standard")
        result = compressor.compress("")
        assert result == ""
    
    def test_single_char(self):
        """测试单字符"""
        compressor = AncientmanCompressor("standard")
        result = compressor.compress("a")
        assert result == "a"
    
    def test_no_compressible_content(self):
        """测试无可压缩内容"""
        compressor = AncientmanCompressor("lite")
        text = "abc"
        result = compressor.compress(text)
        assert result == "abc"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
