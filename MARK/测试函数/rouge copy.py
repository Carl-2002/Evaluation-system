import pandas as pd
from rouge_chinese import Rouge

# 读取 Excel 文件
file_path = 'D:/BIT/MARK/uploads/2_result.xlsx'  # 替换为你的 Excel 文件路径
sheet_name = 'Sheet1'  # 替换为你的工作表名称

# 使用 pandas 读取 Excel 文件
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 假设预测文本在第1列，参考文本在第2列
# 如果列有标题，可以通过列名访问；如果没有标题，可以通过列索引访问
hyps = df.iloc[:, 2].tolist()  # 提取第1列（预测文本）
refs = df.iloc[:, 3].tolist()  # 提取第2列（参考文本）

# 确保 hyps 和 refs 的长度一致
if len(hyps) != len(refs):
    raise ValueError("预测文本和参考文本的数量不一致！")

# 计算 ROUGE 分数
rouge = Rouge()
scores1 = rouge.get_scores(hyps, refs, avg=True)  # 计算平均分数
print(scores1)

