from kimi_copy import chat
import os

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 调用kimi.py中的chat函数
    response = chat(content)

    # 生成新的文件名
    base_name, ext = os.path.splitext(file_path)
    result_file_path = base_name + "_result.txt"

    # 将输入内容和生成的内容保存到新的文件中
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        result_file.write(f"输入内容:\n{content}\n\n生成内容:\n{response}")

    return response