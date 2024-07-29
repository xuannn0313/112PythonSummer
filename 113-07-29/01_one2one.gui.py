import tkinter as tk
from tkinter import messagebox
import requests

# 輸入你的 LINE Notify 存取權杖
ACCESS_TOKEN = '3dMhDEbEzaee9HSeZ8F7Br11IxI7FomZiG7BIJCS6f4'

def send_message():
    # 取得用戶輸入的訊息
    message = message_entry.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning("警告", "訊息內容不能為空！")
        return

    # LINE Notify API 的 URL
    url = 'https://notify-api.line.me/api/notify'

    # 設置請求頭和資料
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    data = {
        'message': message
    }

    # 發送 POST 請求
    response = requests.post(url, headers=headers, data=data)

    # 檢查請求是否成功
    if response.status_code == 200:
        messagebox.showinfo("成功", "訊息已成功發送到 LINE！")
    else:
        messagebox.showerror("錯誤", f"發送訊息失敗，錯誤代碼：{response.status_code}")

# 建立 GUI 應用程式
root = tk.Tk()
root.title("LINE Notify 發送器")

# 設置訊息輸入框
message_label = tk.Label(root, text="請輸入：")
message_label.pack(pady=5)

message_entry = tk.Text(root, height=10, width=40)
message_entry.pack(pady=5)

# 設置送出按鈕
send_button = tk.Button(root, text="送出", command=send_message)
send_button.pack(pady=10)

# 啟動主循環
root.mainloop()