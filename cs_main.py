import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import sqlite3
from datetime import datetime

# ========= 模型路径，确认这个文件存在 =========
MODEL_PATH = r"C:\Users\fovik\Desktop\task-main\model\model.pkl"
DB_PATH = "cs_history.db"

# 加载训练好的模型
model = joblib.load(MODEL_PATH)

# 初始化数据库
def init_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operate_time TEXT,
        pressure REAL,
        temperature REAL,
        speed REAL,
        thickness REAL,
        result TEXT
    )
    """
    cur.execute(sql)
    conn.commit()
    conn.close()

def do_predict():
    """执行预测并保存记录"""
    try:
        p = float(var_pressure.get())
        t = float(var_temp.get())
        s = float(var_speed.get())
        th = float(var_thickness.get())
    except ValueError:
        messagebox.showwarning("输入错误", "请输入有效的数字！")
        return

    # 经验阈值判定，四个条件必须同时满足才合格
    if 122.0 <= p <= 126.0 and 214.5 <= t <= 218.0 and 23.0 <= s <= 25.0 and 4.80 <= th <= 5.00:
        res = "合格"
    else:
        res = "不合格"

    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO history(operate_time,pressure,temperature,speed,thickness,result) VALUES (?,?,?,?,?,?)",
        (now_time, p, t, s, th, res)
    )
    conn.commit()
    conn.close()

    label_result.config(text=f"✅ 预测结果：{res}")
    refresh_table()

def refresh_table():
    """刷新历史表格"""
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM history ORDER BY id DESC")
    data_list = cur.fetchall()
    conn.close()
    for row in data_list:
        tree.insert("", tk.END, values=(row[1], row[2], row[3], row[4], row[5], row[6]))


if __name__ == "__main__":
    init_database()

    root = tk.Tk()
    root.title("工件质量预测系统(C/S桌面版）")
    root.geometry("750x460")

    var_pressure = tk.StringVar()
    var_temp = tk.StringVar()
    var_speed = tk.StringVar()
    var_thickness = tk.StringVar()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(main_frame, text="压力：").grid(row=0, column=0, sticky="w", pady=7)
    ttk.Entry(main_frame, textvariable=var_pressure, width=24).grid(row=0, column=1, padx=10)

    ttk.Label(main_frame, text="温度：").grid(row=1, column=0, sticky="w", pady=7)
    ttk.Entry(main_frame, textvariable=var_temp, width=24).grid(row=1, column=1, padx=10)

    ttk.Label(main_frame, text="速度：").grid(row=2, column=0, sticky="w", pady=7)
    ttk.Entry(main_frame, textvariable=var_speed, width=24).grid(row=2, column=1, padx=10)

    ttk.Label(main_frame, text="厚度：").grid(row=3, column=0, sticky="w", pady=7)
    ttk.Entry(main_frame, textvariable=var_thickness, width=24).grid(row=3, column=1, padx=10)

    btn_frame = ttk.Frame(main_frame)
    btn_frame.grid(row=4, column=0, columnspan=2, pady=15)
    ttk.Button(btn_frame, text="开始预测", command=do_predict).pack(side="left", padx=8)
    ttk.Button(btn_frame, text="刷新历史", command=refresh_table).pack(side="left", padx=8)

    label_result = ttk.Label(main_frame, text="预测结果：", font=("微软雅黑", 13, "bold"))
    label_result.grid(row=5, column=0, columnspan=2, pady=10)

    columns = ["time", "pressure", "temp", "speed", "thickness", "res"]
    tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=9)
    tree.heading("time", text="时间")
    tree.heading("pressure", text="压力")
    tree.heading("temp", text="温度")
    tree.heading("speed", text="速度")
    tree.heading("thickness", text="厚度")
    tree.heading("res", text="预测结果")

    tree.column("time", width=150)
    tree.column("pressure", width=90)
    tree.column("temp", width=90)
    tree.column("speed", width=90)
    tree.column("thickness", width=90)
    tree.column("res", width=90)

    tree.grid(row=6, column=0, columnspan=2)

    refresh_table()
    root.mainloop()