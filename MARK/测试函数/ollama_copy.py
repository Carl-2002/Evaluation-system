import requests
import time
import re

# API的URL
url = 'http://127.0.0.1:11434/api/chat'

def chat(query, A, B, C, D):
    history = [
        {"role": "system",
         "content": "你的任务是对给定问题判断四个选项中哪一个是对的。你的选项只能是A、B、C、D中的一个。你的理由不能超过100字。请按以下格式输出：(A/B/C/D)：理由。"
         }]
    
    history.append({
        "role": "user",
        "content": "问题是：" + str(query) + "选项A:" + str(A) + "选项B:" + str(B) + "选项C:" + str(C) + "选项D:" + str(D) + "请回答："
    })

    response = requests.post(
        url,
        json={
            "model": "qwen2.5:3b",  
            "messages": history,
            "stream": False,
            "keep_alive":-1
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

# 示例调用
if __name__ == "__main__":
    query = "1+2=？"
    A = "1"
    B = "2"
    C = "3"
    D = "4"
    result = chat(query, A, B, C, D)
    print(result)

'''
import requests
import time
import re

# API的URL
url = 'http://127.0.0.1:11434/api/chat'

def chat(query):
    history = [
        {"role": "system",
         "content": "你的任务是对以下问题作出回答。"}
    ]
    
    history.append({
        "role": "user",
        "content": "我的问题是：" + query + "请回答："
    })

    response = requests.post(
        url,
        json={
            "model": "deepseek-r1:1.5b",  
            "messages": history,
            "stream": False,
            "keep_alive":-1
        }
    )
    time.sleep(1)
    if response.status_code == 200:
        result = response.json().get('message', {}).get('content', '')
        content_after_think = re.split(r'</think>\s*', result, maxsplit=1)[1]
    else:
        result = f"Error: {response.status_code} - {response.text}"

    history.clear()

    return content_after_think

# 示例调用
if __name__ == "__main__":
    query = "给我几个复分解反应化学式？"
    result= chat(query)
    print(result)
    print("")

    result = result.replace('\n', '')
    print(result)
'''