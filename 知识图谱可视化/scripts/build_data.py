#!/usr/bin/env python3
"""
从仓库实际目录结构生成知识图谱可视化所需的 data.js 文件。

用法：
    python 知识图谱可视化/scripts/build_data.py

该脚本会扫描 00_高中复习 ~ 04_持续研究 五个阶段目录，生成包含完整
目录树、跨阶段桥接关系、跨模块依赖关系和知识衔接关系的 data.js。
"""

import json
import os
import re
import textwrap

# ---------------------------------------------------------------------------
# 路径配置
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, "..", ".."))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "..", "data.js")

STAGES = [
    "00_高中复习",
    "01_基础能力",
    "02_核心原理",
    "03_工程落地",
    "04_持续研究",
]

SKIP_DIRS = {
    "assets", "code", "exercises", ".git", "__pycache__",
    "node_modules", "知识图谱可视化", ".github",
}

# ---------------------------------------------------------------------------
# 跨阶段桥接关系（AGENTS.MD §3.2）
# ---------------------------------------------------------------------------

CROSS_LINKS = [
    # 桥接关系
    {"source": "00-01", "target": "01-02", "type": "bridge", "label": "桥接数学"},
    {"source": "00-02", "target": "01-01", "type": "bridge", "label": "桥接技术阅读"},
    {"source": "00-03", "target": "01-03", "type": "bridge", "label": "桥接工具使用"},
    {"source": "00-04", "target": "01-05", "type": "bridge", "label": "桥接实验思维"},

    # 跨模块依赖（AGENTS.MD §3.3）
    {"source": "01-02", "target": "02-01", "type": "dependency",
     "label": "概率统计支撑不确定性推理，最优化支撑计算智能"},
    {"source": "01-03", "target": "02-01", "type": "dependency",
     "label": "数据结构与算法支撑搜索策略与计算智能实现"},
    {"source": "02-01", "target": "02-02", "type": "dependency",
     "label": "搜索、推理、知识表示为机器学习提供方法论背景"},
    {"source": "01-02", "target": "02-02", "type": "dependency",
     "label": "线性代数、概率统计支撑模型理解"},
    {"source": "01-02", "target": "02-03", "type": "dependency",
     "label": "微积分、最优化支撑梯度训练"},
    {"source": "01-03", "target": "01-04", "type": "dependency",
     "label": "编程能力支撑数值工具使用"},
    {"source": "01-04", "target": "01-05", "type": "dependency",
     "label": "NumPy/Pandas 支撑数据处理"},
    {"source": "01-05", "target": "02-02", "type": "dependency",
     "label": "数据工程支撑建模实践"},
    {"source": "01-05", "target": "02-03", "type": "dependency",
     "label": "数据预处理支撑深度学习训练"},
    {"source": "02-02", "target": "02-03", "type": "dependency",
     "label": "模型评估与正则化概念传递"},
    {"source": "02-03", "target": "02-04", "type": "dependency",
     "label": "神经网络支撑深度强化学习"},
    {"source": "02-03", "target": "02-05", "type": "dependency",
     "label": "自注意力架构支撑大模型理解"},
    {"source": "02-04", "target": "02-05", "type": "dependency",
     "label": "对齐、智能体与序列决策的前置知识"},
    {"source": "02-01", "target": "02-05", "type": "dependency",
     "label": "知识表示与推理支撑知识图谱、智能体规划"},
    {"source": "02-05", "target": "03-01", "type": "dependency",
     "label": "模型原理到工程部署"},
    {"source": "02-05", "target": "03-02", "type": "dependency",
     "label": "大模型原理到应用工程"},
    {"source": "02-05", "target": "04-01", "type": "dependency",
     "label": "原理理解支撑论文阅读与趋势判断"},
    {"source": "02-05", "target": "04-02", "type": "dependency",
     "label": "大模型引发伦理与安全议题"},
    {"source": "03-01", "target": "04-01", "type": "dependency",
     "label": "工程实践反馈研究方向"},
    {"source": "03-01", "target": "04-02", "type": "dependency",
     "label": "部署经验支撑安全合规判断"},
]

# ---------------------------------------------------------------------------
# 知识衔接关系（AGENTS.MD §3.3 阶段内依赖）
#
# ID 格式：阶段-模块-主题  或  阶段-模块-主题-知识点
# 例如：00-01-06 = 00_高中复习/01_数学基础/06_向量
#       01-02-01 = 01_基础能力/02_数学基础/01_线性代数
# ---------------------------------------------------------------------------

KNOWLEDGE_LINKS = [
    # 高中 → 基础能力桥接（主题级）
    {"source": "00-01-06", "target": "01-02-01",
     "label": "向量运算是线性代数的基础操作"},
    {"source": "00-01-12", "target": "01-02-02",
     "label": "导数初步为微积分提供入门概念"},
    {"source": "00-01-09", "target": "01-02-03",
     "label": "概率基础为概率论提供直觉"},
    {"source": "00-01-08", "target": "01-02-03",
     "label": "排列组合支撑概率计数"},
    {"source": "00-01-11", "target": "02-01-03",
     "label": "集合与逻辑支撑谓词逻辑与推理"},

    # 基础能力内部衔接
    {"source": "01-02-02", "target": "01-02-04",
     "label": "梯度计算是优化算法的核心"},
    {"source": "01-02-03", "target": "01-02-05",
     "label": "概率分布是信息论的前置概念"},
    {"source": "01-02-01", "target": "01-02-04",
     "label": "矩阵运算用于高维优化"},
    {"source": "01-03-01", "target": "01-04-01",
     "label": "数据结构影响 NumPy 数组实现"},
    {"source": "01-03-06", "target": "01-05-01",
     "label": "数据库知识直接应用于查询语言"},
    {"source": "01-03-07", "target": "01-05-05",
     "label": "软件工程规范指导实验设计"},

    # 基础能力 → 核心原理（经典AI）
    {"source": "01-02-03", "target": "02-01-05",
     "label": "概率推断是不确定性推理的基石"},
    {"source": "01-03-01", "target": "02-01-02",
     "label": "数据结构支撑搜索策略的实现"},

    # 基础能力 → 核心原理（经典机器学习）
    {"source": "01-05-03", "target": "02-02-01",
     "label": "特征工程为回归提供输入"},
    {"source": "01-05-02", "target": "02-02-16",
     "label": "数据清洗中发现的异常驱动检测方法选择"},
    {"source": "01-05-06", "target": "02-02-07",
     "label": "采样策略影响集成方法的性能"},
    {"source": "01-02-04", "target": "02-02-13",
     "label": "最优化中的惩罚项即正则化"},
    {"source": "01-02-03", "target": "02-02-03",
     "label": "条件概率是朴素贝叶斯的理论基础"},
    {"source": "01-02-01", "target": "02-02-09",
     "label": "线性变换与特征分解是降维的数学核心"},
    {"source": "01-02-03", "target": "02-02-15",
     "label": "概率推断是概率图模型的基石"},

    # 经典机器学习内部衔接
    {"source": "02-02-01", "target": "02-02-02",
     "label": "回归到分类是输出空间从连续到离散的推广"},
    {"source": "02-02-02", "target": "02-02-06",
     "label": "非线性分类催生核方法"},
    {"source": "02-02-05", "target": "02-02-07",
     "label": "单棵树组合为集成学习"},
    {"source": "02-02-10", "target": "02-02-14",
     "label": "偏差方差权衡指导模型选择"},
    {"source": "02-02-17", "target": "02-02-18",
     "label": "可解释性为因果推理提供动机与应用场景"},

    # 基础能力 → 核心原理（深度学习）
    {"source": "01-02-02", "target": "02-03-02",
     "label": "链式法则是反向传播的数学基础"},
    {"source": "01-02-04", "target": "02-03-03",
     "label": "优化器是最优化理论在神经网络中的实现"},
    {"source": "01-02-05", "target": "02-03-07",
     "label": "交叉熵等损失函数源于信息论"},

    # 深度学习内部衔接
    {"source": "02-03-01", "target": "02-03-02",
     "label": "前向传播定义计算图，反向传播沿图求梯度"},
    {"source": "02-03-02", "target": "02-03-03",
     "label": "梯度计算后由优化器执行参数更新"},
    {"source": "02-03-03", "target": "02-03-19",
     "label": "优化器选择直接决定训练效果与调参策略"},
    {"source": "02-03-09", "target": "02-03-08",
     "label": "深层卷积网络退化问题催生残差连接"},
    {"source": "02-03-11", "target": "02-03-13",
     "label": "序列建模的瓶颈推动注意力机制诞生"},
    {"source": "02-03-13", "target": "02-03-14",
     "label": "自注意力是 Transformer 架构的核心算子"},
    {"source": "02-03-14", "target": "02-03-15",
     "label": "Transformer 理解后对比学习 SSM 替代架构"},
    {"source": "02-03-11", "target": "02-03-15",
     "label": "RNN/LSTM 序列建模基础支撑 SSM 理解"},
    {"source": "02-03-16", "target": "02-03-17",
     "label": "自编码器的解码能力引出生成模型"},
    {"source": "02-03-06", "target": "02-03-01",
     "label": "合理的初始化保证网络训练稳定启动"},

    # 深度学习 → 大模型
    {"source": "02-03-14", "target": "02-05-03",
     "label": "Transformer 架构是预训练的基础模型"},
    {"source": "02-03-14", "target": "02-05-01",
     "label": "自注意力架构产出高质量上下文表示"},
    {"source": "02-03-17", "target": "02-05-16",
     "label": "生成模型的知识可通过蒸馏迁移到小模型"},

    # 大模型内部衔接
    {"source": "02-05-01", "target": "02-05-02",
     "label": "表示学习产出的向量即嵌入表示"},
    {"source": "02-05-03", "target": "02-05-04",
     "label": "预训练模型通过微调适配下游任务"},
    {"source": "02-05-04", "target": "02-05-05",
     "label": "LoRA 是参数高效微调的主流方法"},
    {"source": "02-05-02", "target": "02-05-06",
     "label": "嵌入表示用于检索增强生成的语义索引"},
    {"source": "02-05-04", "target": "02-05-07",
     "label": "微调后通过对齐使模型符合人类偏好"},
    {"source": "02-05-07", "target": "02-05-11",
     "label": "对齐后的模型才能安全地作为智能体核心"},
    {"source": "02-05-10", "target": "02-05-11",
     "label": "提示工程是智能体编排的基础技能"},
    {"source": "02-05-10", "target": "02-05-18",
     "label": "提示工程用于驱动合成数据生成"},
    {"source": "02-05-08", "target": "02-05-09",
     "label": "推理效率与推理时扩展互为对偶"},
    {"source": "02-05-21", "target": "02-05-22",
     "label": "视频理解支撑 3D 重建与生成"},
    {"source": "02-05-23", "target": "02-05-24",
     "label": "世界模型为具身智能提供环境预测能力"},
    {"source": "02-01-03", "target": "02-05-25",
     "label": "符号知识表示支撑神经符号融合"},

    # 强化学习 → 大模型
    {"source": "02-04-04", "target": "02-05-07",
     "label": "策略梯度为 RLHF 对齐提供训练算法"},
    {"source": "02-04-06", "target": "02-05-24",
     "label": "深度强化学习支撑机器人学习与决策"},

    # 工程落地内部衔接
    {"source": "03-01-01", "target": "03-01-02",
     "label": "框架训练循环产出需要实验管理来追踪"},
    {"source": "03-01-05", "target": "03-01-10",
     "label": "在线服务需要配套监控"},
    {"source": "03-01-06", "target": "03-01-15",
     "label": "容器化能力延伸到边缘部署"},
]

# ---------------------------------------------------------------------------
# 目录树生成
# ---------------------------------------------------------------------------

def get_sorted_subdirs(path):
    """获取按名称排序的子目录（仅包含课程相关目录）"""
    try:
        entries = sorted(os.listdir(path))
    except OSError:
        return []
    result = []
    for entry in entries:
        if entry.startswith(".") or entry in SKIP_DIRS:
            continue
        full = os.path.join(path, entry)
        if os.path.isdir(full) and re.match(r"^\d+_", entry):
            result.append(entry)
    return result


def build_raw_tree():
    """从实际目录结构构建 RAW_TREE 字符串"""
    lines = []
    for stage_name in STAGES:
        stage_path = os.path.join(REPO_ROOT, stage_name)
        if not os.path.isdir(stage_path):
            continue
        lines.append(f"- {stage_name}")
        for module_name in get_sorted_subdirs(stage_path):
            lines.append(f"\t- {module_name}")
            module_path = os.path.join(stage_path, module_name)
            for topic_name in get_sorted_subdirs(module_path):
                lines.append(f"\t\t- {topic_name}")
                topic_path = os.path.join(module_path, topic_name)
                for kp_name in get_sorted_subdirs(topic_path):
                    lines.append(f"\t\t\t- {kp_name}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# data.js 生成
# ---------------------------------------------------------------------------

def json_array(items, indent=1):
    """将列表转换为格式化的 JS 数组字符串"""
    if not items:
        return "[]"
    tab = "\t" * indent
    inner_tab = "\t" * (indent + 1)
    parts = []
    for item in items:
        entries = []
        for k, v in item.items():
            entries.append(f'{inner_tab}{k}: {json.dumps(v, ensure_ascii=False)}')
        parts.append("{\n" + ",\n".join(entries) + f"\n{tab}}}")
    joined = f",\n".join(f"{tab}{p}" for p in parts)
    return f"[\n{joined}\n{tab}]"


def build_data_js():
    raw_tree = build_raw_tree()

    # 统计信息
    lines = raw_tree.split("\n")
    counts = {"stages": 0, "modules": 0, "topics": 0, "kps": 0}
    for line in lines:
        tabs = len(line) - len(line.lstrip("\t"))
        if tabs == 0:
            counts["stages"] += 1
        elif tabs == 1:
            counts["modules"] += 1
        elif tabs == 2:
            counts["topics"] += 1
        elif tabs == 3:
            counts["kps"] += 1

    print(f"生成统计：{counts['stages']} 阶段, {counts['modules']} 模块, "
          f"{counts['topics']} 主题, {counts['kps']} 知识点")

    # 为 knowledge links 添加 type 字段
    kl_items = [dict(**link, type="knowledge-link") for link in KNOWLEDGE_LINKS]

    output = textwrap.dedent("""\
    (function () {
    \tconst RAW_TREE = String.raw`%RAW_TREE%`;

    \tconst STAGE_COLORS = {
    \t\t"00": { fill: "#f59e0b", stroke: "#92400e" },
    \t\t"01": { fill: "#10b981", stroke: "#064e3b" },
    \t\t"02": { fill: "#3b82f6", stroke: "#1e3a8a" },
    \t\t"03": { fill: "#8b5cf6", stroke: "#4c1d95" },
    \t\t"04": { fill: "#ef4444", stroke: "#7f1d1d" }
    \t};

    \tconst CROSS_LINKS = %CROSS_LINKS%;

    \tconst KNOWLEDGE_LINKS = %KNOWLEDGE_LINKS%;

    \tfunction stripPrefix(value) {
    \t\treturn value.replace(/^\\d+_/, "");
    \t}

    \tfunction parseTree(rawTree) {
    \t\tconst nodes = [];
    \t\tconst stack = [];
    \t\tconst nodeById = new Map();
    \t\tconst childBuckets = new Map();
    \t\tconst lines = rawTree
    \t\t\t.split(/\\r?\\n/)
    \t\t\t.map((line) => line.replace(/\\r/g, ""))
    \t\t\t.filter((line) => line.trim().length > 0);

    \t\tlines.forEach((line) => {
    \t\t\tconst normalizedLine = line.replace(/ {4}/g, "\\t").replace(/ {2}/g, "\\t");
    \t\t\tconst match = normalizedLine.match(/^(\\t*)- (.+)$/);

    \t\t\tif (!match) {
    \t\t\t\treturn;
    \t\t\t}

    \t\t\tconst level = match[1].length;
    \t\t\tconst rawName = match[2].trim();
    \t\t\tconst codeMatch = rawName.match(/^(\\d+)_/);
    \t\t\tconst code = codeMatch ? codeMatch[1] : rawName;
    \t\t\tconst parent = level === 0 ? null : stack[level - 1];
    \t\t\tconst stageId = level === 0 ? code : stack[0].code;
    \t\t\tconst id = parent ? `${parent.id}-${code}` : code;

    \t\t\tconst node = {
    \t\t\t\tid,
    \t\t\t\tcode,
    \t\t\t\trawName,
    \t\t\t\tlabel: stripPrefix(rawName),
    \t\t\t\tlevel,
    \t\t\t\tparentId: parent ? parent.id : null,
    \t\t\t\tstageId,
    \t\t\t\tstage: Number(stageId),
    \t\t\t\tchildCount: 0
    \t\t\t};

    \t\t\tstack[level] = node;
    \t\t\tstack.length = level + 1;
    \t\t\tnodes.push(node);
    \t\t\tnodeById.set(id, node);
    \t\t\tchildBuckets.set(id, []);
    \t\t});

    \t\tnodes.forEach((node) => {
    \t\t\tif (!node.parentId) {
    \t\t\t\treturn;
    \t\t\t}

    \t\t\tchildBuckets.get(node.parentId).push(node.id);
    \t\t\tnodeById.get(node.parentId).childCount += 1;
    \t\t});

    \t\tnodes.forEach((node) => {
    \t\t\tconst lineage = [];
    \t\t\tlet current = node;

    \t\t\twhile (current) {
    \t\t\t\tlineage.unshift(current.rawName);
    \t\t\t\tcurrent = current.parentId ? nodeById.get(current.parentId) : null;
    \t\t\t}

    \t\t\tnode.fullPath = lineage.join(" / ");
    \t\t\tnode.breadcrumb = lineage.map(stripPrefix).join(" / ");
    \t\t\tnode.children = childBuckets.get(node.id);
    \t\t});

    \t\treturn { nodes, nodeById };
    \t}

    \tconst { nodes } = parseTree(RAW_TREE);

    \tconst edges = nodes
    \t\t.filter((node) => node.parentId)
    \t\t.map((node) => ({ source: node.parentId, target: node.id, type: "parent-child" }));

    \tconst stageNodes = nodes
    \t\t.filter((node) => node.level === 0)
    \t\t.sort((left, right) => left.id.localeCompare(right.id, "zh-CN", { numeric: true }));

    \tfor (let index = 0; index < stageNodes.length - 1; index += 1) {
    \t\tedges.push({
    \t\t\tsource: stageNodes[index].id,
    \t\t\ttarget: stageNodes[index + 1].id,
    \t\t\ttype: "stage-flow"
    \t\t});
    \t}

    \tedges.push(...CROSS_LINKS);
    \tedges.push(...KNOWLEDGE_LINKS);
    \tedges.forEach((edge) => {
    \t\tedge.sourceId = edge.source;
    \t\tedge.targetId = edge.target;
    \t});

    \tconst meta = {
    \t\ttotalNodes: nodes.length,
    \t\tstageCount: nodes.filter((node) => node.level === 0).length,
    \t\tmoduleCount: nodes.filter((node) => node.level === 1).length,
    \t\ttopicCount: nodes.filter((node) => node.level === 2).length,
    \t\tknowledgePointCount: nodes.filter((node) => node.level === 3).length
    \t};

    \twindow.GRAPH_DATA = {
    \t\tnodes,
    \t\tedges,
    \t\tmeta,
    \t\tstageColors: STAGE_COLORS
    \t};
    """)

    # 替换占位符
    output = output.replace("%RAW_TREE%", raw_tree)
    output = output.replace("%CROSS_LINKS%", json_array(CROSS_LINKS))
    output = output.replace("%KNOWLEDGE_LINKS%", json_array(kl_items))

    # 确保文件以 })();\n 结尾（IIFE 自执行闭合）
    output = output.rstrip() + "\n})();\n"

    return output


def main():
    data_js = build_data_js()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(data_js)
    print(f"已写入 {os.path.relpath(OUTPUT_PATH, REPO_ROOT)}")


if __name__ == "__main__":
    main()
