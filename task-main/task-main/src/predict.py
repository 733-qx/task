import os
import joblib
import pandas as pd

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, "model", "model.pkl")
model = joblib.load(model_path)

# 示例：一条待测数据 压力、温度、速度、厚度
sample_data = pd.DataFrame([[122.0, 215.0, 23.0, 4.80]],
                          columns=["压力","温度","速度","厚度"])

pred = model.predict(sample_data)
print("输入样本：", sample_data.to_dict(orient="records")[0])
print("预测结果：", pred[0])