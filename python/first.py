import requests
import pyperclip
import time

def send_post_request(name, message):
    url = "https://eell.pro/api/chat/"
    data = {"name": name, "chat": message}
    response = requests.post(url, data=data)
    return response

# 获取用户输入的名字
name = input("Please enter your name: ")

# 每秒检查剪贴板内容是否变化
last_clipboard_content = None
while True:
    current_clipboard_content = pyperclip.paste()
    if current_clipboard_content != last_clipboard_content:
        print(f"Copied content: {current_clipboard_content}")  # 打印复制的内容
        send_post_request(name, current_clipboard_content)
        last_clipboard_content = current_clipboard_content
    time.sleep(1)
