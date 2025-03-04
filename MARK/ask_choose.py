import pandas as pd
import time
import model_ask as model

def process_file(file_path, dropdown, socketio, filename):
    # 读取Excel文件，假设文件从第二行开始有数据
    df = pd.read_excel(file_path, header=0)  # header=0 表示第一行为列名

    if '模型答案' not in df.columns:
        df['模型答案'] = None
    if '标准答案' not in df.columns:
        df['标准答案'] = None
    if '结果' not in df.columns:
        df['结果'] = None
    if '理由' not in df.columns:
        df['理由'] = None

    if dropdown == 'qwen2.5:3b':
        chat = model.choose_qwen
        moxing = 'qwen2.5_3b'
    else:
        chat = model.choose_deepseek
        moxing = 'deepseek-r1_1.5b'
    print(moxing)
    
    total_questions = len(df)
    stop_1 = 0
    for index, row in df.iterrows():
        if pd.notna(row[1]) and pd.notna(row[2]) and pd.notna(row[3]) and pd.notna(row[4]) and pd.notna(row[5]) and pd.isna(row[6]):  
            question = row[1]
            A = row[2]
            B = row[3]
            C = row[4]
            D = row[5]
            time.sleep(1)
            response = chat(question, A, B, C, D)
            print("")
            xuanxiang, liyou, stop = model.extract_mark(response)
            if stop == 1:
                stop_1 = 1

            df.at[index, '模型答案'] = xuanxiang
            df.at[index, '理由'] = liyou
            
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

    result_file_path = file_path.replace('.xlsx', '_' + moxing + '_c_a.xlsx') 
    df.to_excel(result_file_path, sheet_name='数据', index=False)
    
    if stop_1 == 1:  # 如果有停止标志，则发送停止信号
        socketio.emit('status', {'message': '回答中有错误，请检查结果！(-FFFF)'})
    else:
        socketio.emit('status', {'message': '回答成功!'})