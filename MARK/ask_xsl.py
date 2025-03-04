import pandas as pd
import time
import model_ask as model

def process_file(file_path, dropdown, socketio, filename):
    df = pd.read_excel(file_path, header=0)  # header=0 表示第一行为列名

    if '模型答案' not in df.columns:
        df['模型答案'] = None
    if '标准答案' not in df.columns:
        df['标准答案'] = None 

    if dropdown == 'qwen2.5:3b':
        chat = model.chat_qwen
        moxing = 'qwen2.5_3b'
    else:
        chat = model.chat_deepseek
        moxing = 'deepseek-r1_1.5b'
    print(moxing)
    
    total_questions = len(df)
    for index, row in df.iterrows():
        if pd.notna(row[1]) and pd.isna(row[2]):  
            question = row[1]
            time.sleep(1)
            response = chat(question)
            print("")
            print(response)
            
            df.at[index, '模型答案'] = response
            
            # 更新进度
            progress = (index + 1) / total_questions * 100
            socketio.emit('progress', {'filename': filename, 'progress': progress})
        else:
            if index == 0:
                error_message = f"文件格式！您所选择的操作与您的文件格式不匹配。"
            else:
                error_message = f"文件格式: 第 {index + 1} 行数据不完整。"
            
            socketio.emit('error', {'message': error_message})
            raise ValueError(error_message)  # 抛出异常以停止程序

    result_file_path = file_path.replace('.xlsx', '_'+moxing+'_t_a.xlsx') 
    df.to_excel(result_file_path, sheet_name='数据', index=False)
    
    socketio.emit('status', {'message': '回答成功!'})