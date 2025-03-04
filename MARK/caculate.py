import numpy as np
# from scipy.stats import skew

def calculate_stats(numbers):
    # 计算平均数
    mean = np.mean(numbers)
    
    # 计算中位数
    median = np.median(numbers)
    
    # 计算标准差
    std_dev = np.std(numbers, ddof=0)  # ddof=0 表示样本标准差
    
    # 计算分布偏度
    # skewness = skew(numbers)
    
    return mean, median, std_dev

