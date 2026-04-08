"""
Ancientman Mode - 中文超压缩通信模式

将大模型响应token使用量减少约75%，同时保持完整技术准确性。
"""

__version__ = "1.0.0"
__author__ = "Ancientman Mode Contributors"
__license__ = "MIT"

from .compressor import AncientmanCompressor
from .classical_compressor import ClassicalCompressor

__all__ = [
    "AncientmanCompressor",
    "ClassicalCompressor",
]
