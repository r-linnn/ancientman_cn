"""
Ancientman Compressor - 古代人模式压缩器

三级强度压缩：lite / standard / ultra
"""

import re
from typing import Dict, List, Optional


class AncientmanCompressor:
    """
    古代人模式压缩器
    
    通过极简表达将token使用量减少约75%
    """
    
    MODES = ["lite", "standard", "ultra"]
    
    def __init__(self, mode: str = "standard"):
        """
        初始化压缩器
        
        Args:
            mode: 压缩模式 - "lite", "standard", "ultra"
        """
        if mode not in self.MODES:
            raise ValueError(f"Invalid mode: {mode}. Choose from {self.MODES}")
        
        self.mode = mode
        self._init_mappings()
    
    def _init_mappings(self):
        """初始化词汇映射表"""
        
        # 单字词压缩映射
        self.word_map = {
            "数据库": "库",
            "服务器": "服",
            "网络": "网",
            "配置": "配",
            "连接": "连",
            "超时": "超时",
            "错误": "错",
            "问题": "题",
            "解决": "解",
            "检查": "查",
            "使用": "用",
            "设置": "设",
            "系统": "系",
            "程序": "程",
            "代码": "码",
            "函数": "函",
            "变量": "量",
            "参数": "参",
            "返回": "返",
            "结果": "果",
            "数据": "数",
            "文件": "档",
            "目录": "目",
            "路径": "径",
            "用户": "户",
            "权限": "权",
            "安全": "安",
            "性能": "性",
            "优化": "优",
            "测试": "测",
            "调试": "调",
            "运行": "运",
            "启动": "启",
            "停止": "停",
            "创建": "创",
            "删除": "删",
            "修改": "改",
            "更新": "更",
            "查询": "询",
            "添加": "加",
            "移除": "除",
            "打开": "开",
            "关闭": "关",
            "读取": "读",
            "写入": "写",
            "显示": "显",
            "隐藏": "隐",
            "成功": "成",
            "失败": "败",
            "完成": "完",
            "开始": "始",
            "结束": "终",
            "等待": "等",
            "继续": "续",
            "取消": "消",
            "确认": "认",
            "选择": "选",
            "输入": "入",
            "输出": "出",
        }
        
        # 因果连接词映射
        self.causal_map = {
            "因为": "→",
            "由于": "→",
            "所以": "→",
            "因此": "→",
            "导致": "→",
            "引起": "→",
            "造成": "→",
            "使得": "→",
        }
        
        # 并列连接词映射
        self.conjunction_map = {
            "和": "/",
            "与": "/",
            "以及": "/",
            "还有": "/",
            "或者": "/",
            "或是": "/",
        }
        
        # 填充词列表（删除）
        self.filler_words = [
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
        ]
        
        # 礼貌用语（lite模式保留，其他模式删除）
        self.polite_phrases = [
            "好的", "明白了", "了解了", "清楚了",
            "没问题", "不客气", "没关系",
        ]
    
    def compress(self, text: str) -> str:
        """
        压缩文本
        
        Args:
            text: 原始文本
            
        Returns:
            压缩后的文本
        """
        if self.mode == "lite":
            return self._compress_lite(text)
        elif self.mode == "standard":
            return self._compress_standard(text)
        else:  # ultra
            return self._compress_ultra(text)
    
    def _compress_lite(self, text: str) -> str:
        """轻度压缩 - 去除填充词，保留完整句子"""
        result = text
        
        # 删除填充词
        for word in self.filler_words:
            result = result.replace(word, "")
        
        # 简化部分词汇
        for old, new in self.word_map.items():
            if old in result:
                result = result.replace(old, new)
        
        # 清理多余空格
        result = re.sub(r'\s+', ' ', result).strip()
        
        return result
    
    def _compress_standard(self, text: str) -> str:
        """标准压缩 - 片段化句子，省略助词"""
        result = text
        
        # 删除填充词和礼貌用语
        for word in self.filler_words + self.polite_phrases:
            result = result.replace(word, "")
        
        # 替换因果连接词
        for old, new in self.causal_map.items():
            result = result.replace(old, new)
        
        # 替换并列连接词
        for old, new in self.conjunction_map.items():
            result = result.replace(old, new)
        
        # 简化词汇
        for old, new in self.word_map.items():
            if old in result:
                result = result.replace(old, new)
        
        # 将句子分段，用→连接
        sentences = re.split(r'[。；;！!？?\n]', result)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(sentences) > 1:
            result = "→".join(sentences)
        else:
            result = sentences[0] if sentences else ""
        
        # 清理多余空格
        result = re.sub(r'\s+', '', result).strip()
        
        return result
    
    def _compress_ultra(self, text: str) -> str:
        """极致压缩 - 使用缩写，符号表示因果关系"""
        result = self._compress_standard(text)
        
        # 进一步压缩常见词组
        ultra_map = {
            "组件": "件",
            "渲染": "渲",
            "引用": "引",
            "属性": "属",
            "变化": "变",
            "状态": "态",
            "异步": "异",
            "同步": "同",
            "请求": "请",
            "响应": "响",
            "接口": "口",
            "方法": "法",
            "对象": "象",
            "数组": "组",
            "字符串": "串",
            "数字": "数",
            "布尔": "布",
            "循环": "环",
            "条件": "条",
            "判断": "判",
            "异常": "异",
            "抛出": "抛",
            "捕获": "捕",
            "处理": "理",
            "调用": "调",
            "执行": "执",
            "生成": "生",
            "实例": "例",
            "类": "类",
            "继承": "继",
            "封装": "封",
            "多态": "多",
            "抽象": "抽",
            "接口": "口",
            "实现": "现",
            "定义": "定",
            "声明": "声",
            "初始化": "初",
            "赋值": "赋",
            "比较": "比",
            "运算": "算",
            "表达式": "式",
            "语句": "句",
            "块": "块",
            "作用域": "域",
            "命名空间": "间",
            "模块": "模",
            "包": "包",
            "库": "库",
            "框架": "架",
            "平台": "平",
            "环境": "环",
            "依赖": "赖",
            "版本": "版",
            "兼容": "兼",
            "扩展": "扩",
            "插件": "插",
            "工具": "具",
            "命令": "令",
            "脚本": "脚",
            "配置": "配",
            "设置": "设",
            "选项": "项",
            "参数": "参",
            "属性": "属",
            "特性": "特",
            "功能": "功",
            "特性": "特",
            "优势": "优",
            "缺点": "缺",
            "问题": "题",
            "解决方案": "案",
            "建议": "议",
            "推荐": "推",
            "注意": "注",
            "警告": "警",
            "错误": "错",
            "失败": "败",
            "成功": "成",
            "完成": "完",
            "结果": "果",
            "效果": "效",
            "影响": "影",
            "原因": "因",
            "结果": "果",
        }
        
        for old, new in ultra_map.items():
            if old in result:
                result = result.replace(old, new)
        
        return result
    
    def get_stats(self, original: str, compressed: str) -> Dict[str, float]:
        """
        获取压缩统计信息
        
        Args:
            original: 原始文本
            compressed: 压缩后文本
            
        Returns:
            统计信息字典
        """
        original_len = len(original)
        compressed_len = len(compressed)
        saved = original_len - compressed_len
        ratio = (saved / original_len * 100) if original_len > 0 else 0
        
        return {
            "original_length": original_len,
            "compressed_length": compressed_len,
            "saved_chars": saved,
            "save_ratio": round(ratio, 1),
        }


# 便捷函数
def compress(text: str, mode: str = "standard") -> str:
    """
    快速压缩文本
    
    Args:
        text: 原始文本
        mode: 压缩模式
        
    Returns:
        压缩后的文本
    """
    compressor = AncientmanCompressor(mode)
    return compressor.compress(text)


def compress_lite(text: str) -> str:
    """轻度压缩"""
    return compress(text, "lite")


def compress_standard(text: str) -> str:
    """标准压缩"""
    return compress(text, "standard")


def compress_ultra(text: str) -> str:
    """极致压缩"""
    return compress(text, "ultra")
