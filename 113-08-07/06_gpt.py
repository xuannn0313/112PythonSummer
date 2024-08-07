import tkinter as tk
from tkinter import ttk

# 模擬的觀測數據
data = {
    "StationA": {
        "Location": "Location A",
        "Time": "2024-08-07 10:00:00",
        "Temperature": "25°C",
        "Weather": "Sunny"
    },
    "StationB": {
        "Location": "Location B",
        "Time": "2024-08-07 11:00:00",
        "Temperature": "22°C",
        "Weather": "Cloudy"
    },
    "StationC": {
        "Location": "Location C",
        "Time": "2024-08-07 12:00:00",
        "Temperature": "28°C",
        "Weather": "Rainy"
    }
}

def update_info(event):
    station = station_var.get()
    info = data.get(station, {})
    
    location_var.set(info.get("Location", "N/A"))
    time_var.set(info.get("Time", "N/A"))
    temperature_var.set(info.get("Temperature", "N/A"))
    weather_var.set(info.get("Weather", "N/A"))

# 建立主視窗
root = tk.Tk()
root.title("Weather Information")

# StationName 下拉選單
station_var = tk.StringVar(value=list(data.keys())[0])
station_menu = ttk.OptionMenu(root, station_var, *data.keys())
station_menu.pack(pady=10)

# 綁定選單變化事件
station_var.trace("w", update_info)

# 顯示信息的標籤
location_var = tk.StringVar(value="N/A")
time_var = tk.StringVar(value="N/A")
temperature_var = tk.StringVar(value="N/A")
weather_var = tk.StringVar(value="N/A")

tk.Label(root, text="Location:").pack()
tk.Label(root, textvariable=location_var).pack()

tk.Label(root, text="Time:").pack()
tk.Label(root, textvariable=time_var).pack()

tk.Label(root, text="Temperature:").pack()
tk.Label(root, textvariable=temperature_var).pack()

tk.Label(root, text="Weather:").pack()
tk.Label(root, textvariable=weather_var).pack()

# 啟動主循環
root.mainloop()