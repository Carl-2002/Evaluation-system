import pandas as pd
from openpyxl import load_workbook

def evaluate_answers(file_path):
    df = pd.read_excel(file_path, header=0)
    
    # 初始化一个新的列用于存储结果，并将其插入到第三列
    if '结果' not in df.columns:
        df['结果'] = None
    
    # 处理前10行的结果
    for index in range(0, 10):
        df.at[index, '结果'] = 1

    result_file_path = file_path.replace('.xlsx', '_c_r.xlsx')
    
    with pd.ExcelWriter(result_file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='数据', index=False)

file_path = "C:/Users/16211/Desktop/bababa_c_r.xlsx"
evaluate_answers(file_path)


'''
 rouge_data = {
            'rouge-1': {'r': df3.iloc[0, 0], 'p': df3.iloc[0, 1], 'f': df3.iloc[0, 2]},
            'rouge-2': {'r': df3.iloc[1, 0], 'p': df3.iloc[1, 1], 'f': df3.iloc[1, 2]},
            'rouge-l': {'r': df3.iloc[2, 0], 'p': df3.iloc[2, 1], 'f': df3.iloc[2, 2]},
                    }
        print(rouge_data)
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Buttons</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .button-container {
            display: flex;
            flex-direction: column; /* 按列排列 */
            align-items: flex-start; /* 靠左对齐 */
            margin-top: 20px; /* 根据需要调整 */
        }
        .button-container button {
            margin: 20px 0; /* 调整按钮之间的间距 */
            padding: 20px 40px; /* 调整按钮的内边距 */
            font-size: 30px; /* 调整字体大小 */
            cursor: pointer;
            border: none;
            border-radius: 15px; /* 增加圆角 */
            background-color: #007bff;
            color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
            transition: background-color 0.3s ease, transform 0.3s ease; /* 添加过渡效果 */
        }
        .button-container button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="button-container">
        <button onclick="location.href='/file'">文件</button>
        <button onclick="location.href='/evaluation'">评测</button>
        <button onclick="location.href='/result'">结果</button>
        <button onclick="location.href='/answer'">回答</button>
        <button onclick="location.href='/list'">列表</button>
    </div>

    <script>
        function exitSystem() {
            // 这里可以添加退出系统的逻辑，例如重定向到登录页面或关闭窗口
            alert('系统已退出');
            window.location.href = '/login';
        }
    </script>
</body>
</html>


import jieba
from nltk.translate.bleu_score import sentence_bleu

target = '我是一个人。我非常善良'  # target
inference = '我是一个人。我非常邪恶。'  # inference

target_fenci = ' '.join(jieba.cut(target))
inference_fenci = ' '.join(jieba.cut(inference))

print(target_fenci)
print(inference_fenci)

reference = []  
candidate = [] 

reference.append(target_fenci.split())
candidate = (inference_fenci.split())
print(candidate)
print(reference)
score1 = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
score2 = sentence_bleu(reference, candidate, weights=(0, 1, 0, 0))
score3 = sentence_bleu(reference, candidate, weights=(0, 0, 1, 0))
score4 = sentence_bleu(reference, candidate, weights=(0, 0, 0, 1))
reference.clear()
print(score1)
print(score2)  
print(score3)
print(score4)   

import pandas as pd

def evaluate_answers(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)
    
    # 初始化一个新的列用于存储结果
    df['结果'] = 0  # 默认值为0，表示错误
    
    # 判断模型答案和标准答案是否一致
    for index, row in df.iterrows():
        if row['模型答案'] == row['标准答案']:
            df.at[index, '结果'] = 1  # 如果一致，设置为1
    
    # 将结果写回 Excel 文件
    df.to_excel(file_path, index=False)

# 调用函数
file_path = 'C:/Users/16211/Desktop/3_choose.xlsx'
evaluate_answers(file_path)

import re

def extract_score_and_reason(response):
    # 找到第一个阿拉伯数字
    score_match = re.search(r'\d+', response)
    if score_match:
        score = int(score_match.group())
    else:
        score = -1
        print("未找到数字")
    
    # 找到结构 ":" 或 "：" 并提取其后面的内容直到字符串结束
    reason_match = re.search(r'[：:]\s*(.*)', response)
    if reason_match:
        reason = reason_match.group(1)
    else:
        reason = "格式错误"
        print("未找到内容")
    
    return score, reason

response = "1啦啦啦啦\n啦啦:啦啦啦啦"
score, reason = extract_score_and_reason(response)
print(score)
print(reason)
'''