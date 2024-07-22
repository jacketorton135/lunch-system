from openai import OpenAI   # 引入OpenAI函式庫
import json                # 引入json模組，用於處理json格式數據
import pymysql             # 引入pymysql模組，用於操作MySQL數據庫
import pprint              # 引入pprint模組，用於美化輸出
import subprocess          # 引入subprocess模組，用於執行系統命令
from datetime import datetime  # 引入datetime模組，用於處理日期和時間

client = OpenAI()  # 初始化OpenAI客戶端
current_time = '現在時間' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 獲取當前時間並格式化為字符串

# 註釋掉的部分是打印歡迎語的程式碼
# print('================================')
# print('   歡迎使用XXX訂票系統AI客服     ')
# print('================================')

message = """請用繁體中文回答 你是 餐廳點餐客戶服務系統  
                    主要用在客戶點了什麼餐點 幾份 結帳 
                     內用 或 外帶 或 外送  
                     需要留下 1.使用者的名稱  和2.手機號碼  兩者都要
                     $付款方式 現金 line pay apple pay 要不要載具
                     如果是外送    還需要知道使用者的 3.地址(縣市/路名/門牌號碼) 如果要離開系統就要輸入 再見"""
# 定義系統消息的內容

def aichat():
    txt = ""
    file_path = 'data.txt'  # 指定文件路徑

    # 開啟文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # 讀取文件內容

    print(content)  # 打印文件內容
    txt = content

    while True: 
        user = input(f'請輸入問題: ')  # 輸入用戶問題
        # user 裡面是否有 再見 bye bye 確定 謝謝 

        if "再見" in user or "bye" in user or "確定" in user or "謝謝" in user:
            print("再見")        
            break

        messages = [ 
            {"role": "system", "content": message},  # 系統消息
            {"role": "assistant", "content": txt},  # 文件內容作為助理消息
            {"role": "user", "content": user}  # 用戶輸入的問題
        ]
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 指定使用的模型
            messages=messages,  # 傳遞消息列表
        )
        response_message = completion.choices[0].message  # 獲取回應消息
        result = response_message.content  # 提取回應消息的內容
        print("chatGPT: " + result)  # 打印回應消息

    return result

aichat()  # 調用aichat函數，開始聊天
