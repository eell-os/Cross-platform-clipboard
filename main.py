import requests
import pyperclip
import time

def send_post_request(name, message):
    url = "https://eell.pro/api/chat/"
    data = {"name": name, "chat": message}
    response = requests.post(url, data=data)
    return response

url = "https://eell.pro/api/chat/receive.php"

# 获取用户输入的名字
name = input("创建/加入房间号: ")
print("-------------------------------------------------------------------------------")  # 打印分割线

# 每秒检查剪贴板内容是否变化
last_clipboard_content = None
last_text_content = None
while True:
    current_clipboard_content = pyperclip.paste()
    if current_clipboard_content != last_clipboard_content:
        send_post_request(name, current_clipboard_content)
        last_clipboard_content = current_clipboard_content

    # 使用POST请求发送name字段
    response = requests.post(url, data={"name": name})
    data = response.json()

    # 如果数据为空，将剪贴板的内容设置为空
    if not data:
        pyperclip.copy("")
    else:
        # 获取并打印最后一个text字段的内容
        last_item = data[-1]
        name = last_item.get('name')
        text = last_item.get('text')
        if text != last_text_content:
            print(f"用户: {name} - 文本: {text}")
            print("-------------------------------------------------------------------------------")  # 打印分割线
            last_text_content = text

        # 将最后一个text字段的内容复制到剪贴板
        pyperclip.copy(text)

    time.sleep(1)
