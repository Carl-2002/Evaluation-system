import requests
import time
import re

# API的URL
url = 'http://127.0.0.1:11434/api/chat'

def chat_qwen(query, answer):
    history = [
        {"role": "system",
         "content": "你的任务是对我提供对问题的回复进行质量评分。评分采取5档制（1-5），5分意味着答案非常好，1分意味着答案非常差。请输出你的打分和超过20字的理由。格式例子：[(分数)：理由。]"}
    ]
    
    history.append({
        "role": "user",
        "content": "我的问题是:[" + query + "] 回复是:[" + answer + "] 请评判这个回答。"
    })

    response = requests.post(
        url,
        json={
            "model": "qwen2.5:3b",  
            "messages": history,
            "stream": False,
            "keep_alive":10
        }
    )
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
    else:
        result = f"Error: {response.status_code} - {response.text}"
    
    history.clear()

    return result

def chat_deepseek(query, answer):
    history = [
        {"role": "system",
         "content": "你的任务是对我提供的对问题的回复进行质量评分。评分采取5档制（1-5），5分意味着答案非常好，1分意味着答案非常差。例子：(3)：这个回答一般，解释得不是非常清晰。"}
    ]
    
    history.append({
        "role": "user",
        "content": "我的问题是:[" + query + "] 回复是:[" + answer + "] 请评判这个回答。"
    })

    response = requests.post(
        url,
        json={
            "model": "deepseek-r1:1.5b",  
            "messages": history,
            "stream": False,
            "keep_alive":10
        }
    )
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
        content_after_think = re.split(r'</think>\s*', result, maxsplit=1)[1]
    else:
        result = f"Error: {response.status_code} - {response.text}"
    
    history.clear()

    return content_after_think

def extract_score_and_reason(response):
    # 找到第一个阿拉伯数字
    score_match = re.search(r'\d+', response)
    if score_match:
        score = int(score_match.group())
        print(score)
        stop = 0
    else:
        score = -9999
        print("未找到数字")
        stop = 1
    
    # 找到结构 ":" 或 "：" 并提取其后面的内容直到字符串结束
    reason_match = re.search(r'[：:]\s*(.*)', response)
    if reason_match:
        reason = reason_match.group(1)
        print(reason)
        stop = 0
    else:
        reason = "-9999"
        print("未找到内容")
        stop = 1
    
    return score, reason, stop
