import requests
import pyperclip
import time

url = "https://eell.pro/api/chat/receive.php"

while True:
    # 获取JSON数据
    response = requests.get(url)
    data = response.json()

    # 解析并打印name和text字段的内容
    for item in data:
        name = item.get('name')
        text = item.get('text')
        print(f"Name: {name}, Text: {text}")

    # 将最后一个text字段的内容复制到剪贴板
    last_text = data[-1].get('text')
    pyperclip.copy(last_text)

    # 每1秒请求一次数据
    time.sleep(1)
