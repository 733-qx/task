import pandas as pd
from sklearn.model_selection import train_test_split

# 直接把数据集写进代码，不再读取csv，就不会解析报错
data_list = [
    [1,"铝合金6061",121.3,215.2,23.5,4.82,"合格"],
    [2,"铝合金6061",124.5,216.1,24.1,4.91,"合格"],
    [3,"铝合金6061",119.8,214.7,22.8,4.75,"合格"],
    [4,"铝合金6061",125.2,217.3,25.2,5.03,"合格"],
    [5,"铝合金6061",122.7,215.8,23.9,4.88,"合格"],
    [6,"铝合金6061",120.5,214.2,22.4,4.71,"合格"],
    [7,"铝合金6061",123.9,216.5,24.6,4.96,"合格"],
    [8,"铝合金6061",118.6,213.9,21.9,4.65,"不合格"],
    [9,"铝合金6061",126.1,217.8,25.7,5.12,"合格"],
    [10,"铝合金6061",121.9,215.5,23.7,4.85,"合格"],
    [11,"铝合金6061",123.2,216.2,24.3,4.92,"合格"],
    [12,"铝合金6061",120.1,214.5,22.6,4.73,"合格"],
    [13,"铝合金6061",124.8,216.9,24.9,4.99,"合格"],
    [14,"铝合金6061",119.2,214.1,22.1,4.68,"不合格"],
    [15,"铝合金6061",122.4,215.7,23.8,4.86,"合格"],
    [16,"铝合金6061",125.7,217.5,25.4,5.07,"合格"],
    [17,"铝合金6061",121.1,215.0,23.2,4.79,"合格"],
    [18,"铝合金6061",123.5,216.4,24.4,4.94,"合格"],
    [19,"铝合金6061",118.9,213.7,22.0,4.66,"不合格"],
    [20,"铝合金6061",124.2,216.6,24.7,4.97,"合格"],
    [21,"铝合金6061",122.1,215.3,23.6,4.83,"合格"],
    [22,"铝合金6061",120.8,214.8,22.9,4.76,"合格"],
    [23,"铝合金6061",126.3,218.0,25.9,5.15,"合格"],
    [24,"铝合金6061",119.5,214.3,22.3,4.70,"不合格"],
    [25,"铝合金6061",123.7,216.3,24.5,4.93,"合格"]
]
columns_name = ["编号","材料","压力","温度","速度","厚度","是否合格"]
df = pd.DataFrame(data_list, columns=columns_name)

print("✅ 数据集读取成功！共 {} 行，{} 列".format(len(df), len(df.columns)))
print("列名：", df.columns.tolist())
print("\n前5行数据预览：")
print(df.head())

# 1. 删除缺失值
df = df.dropna()

# 2. 3σ准则剔除异常值
for col in df.select_dtypes(include=["int", "float"]).columns:
    col_mean = df[col].mean()
    col_std = df[col].std()
    if col_std != 0:
        df = df[(df[col] >= col_mean - 3 * col_std) & (df[col] <= col_mean + 3 * col_std)]

# 3. 8:2划分训练集、测试集
train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

# 保存到data文件夹
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
train_set.to_csv(os.path.join(DATA_DIR, "train.csv"), index=False, encoding="utf-8-sig")
test_set.to_csv(os.path.join(DATA_DIR, "test.csv"), index=False, encoding="utf-8-sig")

print("\n✅ 预处理全部完成！")
print(f"训练集：{len(train_set)} 行，已保存为 train.csv")
print(f"测试集：{len(test_set)} 行，已保存为 test.csv")