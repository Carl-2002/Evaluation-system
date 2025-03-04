import requests
import time
import re

# API的URL
url = 'http://127.0.0.1:11434/api/chat'

def choose_qwen(query, A, B, C, D):
    history = [
        {"role": "system",
         "content": "你的任务是对给定问题判断四个选项中哪一个是对的。你的选择只能是大写字母A、B、C、D中的一个。你的理由不能超过100字。请按以下格式输出：(A/B/C/D)：阐述你的理由。"
         }]
    
    history.append({
        "role": "user",
        "content": "问题是:[" + str(query) + "] 选项A:[" + str(A) + "] 选项B:[" + str(B) + "] 选项C:[" + str(C) + "] 选项D:[" + str(D) + "] 请回答："
    })

    response = requests.post(
        url,
        json={
            "model": "qwen2.5:3b",  
            "messages": history,
            "stream": False,
            "keep_alive": 10
        }
    )
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
        result = result.replace('\n', '')
    else:
        result = f"Error: {response.status_code} - {response.text}"

    history.clear()

    return result

def choose_deepseek(query, A, B, C, D):
    history = [
        {"role": "system",
         "content": "你的任务是对给定问题判断四个选项中哪一个是对的。你的选择只能是大写字母A、B、C、D中的一个。你的理由不能超过100字。请按以下格式输出：(你的选择)：阐述你的理由。"
         }]
    
    history.append({
        "role": "user",
        "content":"问题是:[" + str(query) + "] 选项A:[" + str(A) + "] 选项B:[" + str(B) + "] 选项C:[" + str(C) + "] 选项D:[" + str(D) + "] 请回答："
    })

    response = requests.post(
        url,
        json={
            "model": "deepseek-r1:1.5b",  
            "messages": history,
            "stream": False,
            "keep_alive": 10
        }
    )
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
        result = result.replace('\n', '')
        content_after_think = re.split(r'</think>\s*', result, maxsplit=1)[1]
    else:
        result = f"Error: {response.status_code} - {response.text}"

    history.clear()

    return content_after_think

def chat_deepseek(query):
    history = [
        {"role": "system",
         "content": "你的任务是对以下问题作出回答。你的答案限制在100字以内，但需要超过20字。"}
    ]
    
    history.append({
        "role": "user",
        "content": "我的问题是:[" + query + "] 请回答。"
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
    time.sleep(1)
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
        result = result.replace('\n', '')
        content_after_think = re.split(r'</think>\s*', result, maxsplit=1)[1]
    else:
        result = f"Error: {response.status_code} - {response.text}"
    
    history.clear()

    return content_after_think

def chat_qwen(query):
    history = [
        {"role": "system",
         "content": "你的任务是对以下问题作出回答。你的答案限制在100字以内，但需要超过20字。"}
    ]
    
    history.append({
        "role": "user",
        "content": "我的问题是:[" + query + "] 请回答。"
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
    time.sleep(1)
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
        result = result.replace('\n', '')
    else:
        result = f"Error: {response.status_code} - {response.text}"
    
    history.clear()

    return result

def extract_mark(response):
    # 找到第一个字母
    letter_match = re.search(r'[A-Z]', response)
    if letter_match:
        letter = letter_match.group()
        print(letter)
        stop = 0
    else:
        letter = '-FFFF'
        print("未找到字母")
        stop = 1
    
    # 找到结构 ":" 或 "：" 并提取其后面的内容直到字符串结束
    reason_match = re.search(r'[：:]\s*(.*)', response)
    if reason_match:
        reason = reason_match.group(1)
        print(reason)
        stop = 0
    else:
        reason = "-FFFF"
        print("未找到内容")
        stop = 1
        
    
    return letter, reason, stop
