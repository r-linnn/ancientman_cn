"""
Ancientman Mode - 工具函数

提供一些实用的辅助函数
"""

import re
from typing import List, Tuple


def calculate_token_savings(original: str, compressed: str) -> Tuple[int, float]:
    """
    计算token节省量和节省率
    
    Args:
        original: 原始文本
        compressed: 压缩后文本
        
    Returns:
        (节省字符数, 节省率百分比)
    """
    saved = len(original) - len(compressed)
    ratio = (saved / len(original) * 100) if len(original) > 0 else 0
    return saved, round(ratio, 1)


def split_sentences(text: str) -> List[str]:
    """
    将文本分割成句子
    
    Args:
        text: 输入文本
        
    Returns:
        句子列表
    """
    # 使用中文和英文标点分割
    sentences = re.split(r'[。；;！!？?\n]+', text)
    return [s.strip() for s in sentences if s.strip()]


def remove_filler_words(text: str, filler_words: List[str]) -> str:
    """
    删除填充词
    
    Args:
        text: 输入文本
        filler_words: 要删除的填充词列表
        
    Returns:
        处理后的文本
    """
    result = text
    for word in filler_words:
        result = result.replace(word, "")
    return result


def replace_words(text: str, word_map: dict) -> str:
    """
    批量替换词汇
    
    Args:
        text: 输入文本
        word_map: 词汇映射字典 {原词: 新词}
        
    Returns:
        处理后的文本
    """
    result = text
    for old, new in word_map.items():
        if old in result:
            result = result.replace(old, new)
    return result


def clean_whitespace(text: str) -> str:
    """
    清理多余空白字符
    
    Args:
        text: 输入文本
        
    Returns:
        清理后的文本
    """
    # 将多个空格替换为单个空格
    result = re.sub(r'\s+', ' ', text)
    # 去除首尾空白
    return result.strip()


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    截断文本到指定长度
    
    Args:
        text: 输入文本
        max_length: 最大长度
        suffix: 截断后缀
        
    Returns:
        截断后的文本
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def format_stats(original: str, compressed: str) -> str:
    """
    格式化统计信息为可读字符串
    
    Args:
        original: 原始文本
        compressed: 压缩后文本
        
    Returns:
        格式化的统计信息
    """
    saved, ratio = calculate_token_savings(original, compressed)
    return (
        f"原始: {len(original)}字符 | "
        f"压缩: {len(compressed)}字符 | "
        f"节省: {saved}字符 ({ratio}%)"
    )


def is_chinese_text(text: str) -> bool:
    """
    检查文本是否主要为中文
    
    Args:
        text: 输入文本
        
    Returns:
        是否主要为中文
    """
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    total_chars = len(text.replace(' ', ''))
    if total_chars == 0:
        return False
    return (chinese_chars / total_chars) > 0.3


def extract_keywords(text: str, min_length: int = 2) -> List[str]:
    """
    提取文本中的关键词（简单实现）
    
    Args:
        text: 输入文本
        min_length: 最小词长度
        
    Returns:
        关键词列表
    """
    # 简单的基于标点的分词
    words = re.split(r'[，,。；;！!？?\s]+', text)
    # 过滤短词和空词
    return [w for w in words if len(w) >= min_length]


# 常用填充词列表
COMMON_FILLER_WORDS = [
    "的", "地", "得",
    "了", "着", "过",
    "啊", "呢", "吧", "吗", "嘛",
    "嗯", "哦", "哈",
    "这个", "那个", "就是", "其实",
    "那么", "这样", "那样",
    "可能", "大概", "应该",
    "我觉得", "我认为", "我想",
    "你好", "您好",
    "请问", "麻烦", "谢谢", "感谢",
    "请", "能否", "是否可以",
    "好的", "明白了", "了解了", "清楚了",
    "没问题", "不客气", "没关系",
]


# 常用礼貌用语列表
COMMON_POLITE_PHRASES = [
    "你好", "您好",
    "请问", "麻烦", "谢谢", "感谢",
    "好的", "明白了", "了解了", "清楚了",
    "没问题", "不客气", "没关系",
]
