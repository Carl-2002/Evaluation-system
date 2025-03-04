from rouge_chinese import Rouge

def calculate_rouge_scores(df, hyps_col_index=2, refs_col_index=3):
    # 提取预测文本和参考文本
    hyps = df.iloc[:, hyps_col_index].tolist()
    refs = df.iloc[:, refs_col_index].tolist()

    # 确保 hyps 和 refs 的长度一致
    if len(hyps) != len(refs):
        raise ValueError("预测文本和参考文本的数量不一致！")

    # 计算 ROUGE 分数
    rouge = Rouge()
    scores = rouge.get_scores(hyps, refs, avg=True)  # 计算平均分数
    
    for key in scores:  # 遍历外层字典的键（如 'rouge-1', 'rouge-2', 'rouge-l'）
        for sub_key in scores[key]:  # 遍历内层字典的键（如 'r', 'p', 'f'）
            if scores[key][sub_key] < 0.001:  # 检查值是否小于 0.001
                scores[key][sub_key] = 0.001  # 如果小于 0.001，则赋值为 0.001(避免出错)

    print(scores)
    
    return scores