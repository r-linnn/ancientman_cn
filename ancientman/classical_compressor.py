"""
Classical Compressor - 古风压缩器

无典故版本，专注于极致token压缩
使用极简文言文风格
"""

import re
from typing import Dict


class ClassicalCompressor:
    """
    古风压缩器 - 无典故版本
    
    特点：
    - 绝不使用成语、诗句、历史典故
    - 单字词最大化压缩
    - 符号替代因果关系
    """
    
    def __init__(self):
        """初始化古风压缩器"""
        self._init_mappings()
    
    def _init_mappings(self):
        """初始化词汇映射表"""
        
        # 极致文言词汇映射（最高压缩率）
        self.classical_map = {
            # 技术词汇
            "数据库": "库",
            "服务器": "服",
            "网络": "网",
            "配置": "配",
            "连接": "连",
            "超时": "逾",
            "错误": "谬",
            "问题": "疑",
            "解决": "解",
            "检查": "检",
            "使用": "用",
            "设置": "置",
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
            "性能": "效",
            "优化": "优",
            "测试": "测",
            "调试": "校",
            "运行": "行",
            "启动": "启",
            "停止": "止",
            "创建": "创",
            "删除": "删",
            "修改": "改",
            "更新": "更",
            "查询": "询",
            "添加": "增",
            "移除": "去",
            "打开": "开",
            "关闭": "闭",
            "读取": "读",
            "写入": "写",
            "显示": "显",
            "隐藏": "藏",
            "成功": "成",
            "失败": "败",
            "完成": "毕",
            "开始": "始",
            "结束": "终",
            "等待": "候",
            "继续": "续",
            "取消": "废",
            "确认": "认",
            "选择": "择",
            "输入": "入",
            "输出": "出",
            
            # 前端/React词汇
            "组件": "件",
            "渲染": "绘",
            "引用": "引",
            "属性": "性",
            "变化": "变",
            "状态": "态",
            "异步": "异",
            "同步": "同",
            "请求": "请",
            "响应": "应",
            "接口": "口",
            "方法": "法",
            "对象": "象",
            "数组": "列",
            "字符串": "文",
            "数字": "数",
            "布尔": "逻",
            "循环": "环",
            "条件": "条",
            "判断": "断",
            "异常": "异",
            "抛出": "投",
            "捕获": "捉",
            "处理": "理",
            "调用": "召",
            "执行": "施",
            "生成": "生",
            "实例": "例",
            "类": "类",
            "继承": "继",
            "封装": "包",
            "多态": "多",
            "抽象": "抽",
            "实现": "现",
            "定义": "定",
            "声明": "宣",
            "初始化": "初",
            "赋值": "赋",
            "比较": "较",
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
            "平台": "台",
            "环境": "境",
            "依赖": "赖",
            "版本": "版",
            "兼容": "容",
            "扩展": "展",
            "插件": "插",
            "工具": "具",
            "命令": "令",
            "脚本": "脚",
            "选项": "项",
            "特性": "特",
            "功能": "能",
            "优势": "长",
            "缺点": "短",
            "建议": "议",
            "推荐": "荐",
            "注意": "慎",
            "警告": "警",
            "原因": "因",
        }
        
        # 删除词列表
        self.remove_words = [
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
    
    def compress(self, text: str) -> str:
        """
        压缩文本为古风格式
        
        Args:
            text: 原始文本
            
        Returns:
            压缩后的古风文本
        """
        result = text
        
        # 删除无用词汇
        for word in self.remove_words:
            result = result.replace(word, "")
        
        # 替换为文言词汇
        for old, new in self.classical_map.items():
            if old in result:
                result = result.replace(old, new)
        
        # 替换因果词为→
        causal_words = ["因为", "由于", "所以", "因此", "导致", "引起", "造成", "使得"]
        for word in causal_words:
            result = result.replace(word, "→")
        
        # 替换并列词为/
        conj_words = ["和", "与", "以及", "还有", "或者", "或是"]
        for word in conj_words:
            result = result.replace(word, "/")
        
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
def compress_classical(text: str) -> str:
    """
    快速古风压缩
    
    Args:
        text: 原始文本
        
    Returns:
        压缩后的古风文本
    """
    compressor = ClassicalCompressor()
    return compressor.compress(text)
