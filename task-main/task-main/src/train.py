import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")

# 读取划分好的数据
train_df = pd.read_csv(os.path.join(data_dir, "train.csv"), encoding="utf-8-sig")
test_df = pd.read_csv(os.path.join(data_dir, "test.csv"), encoding="utf-8-sig")

# 选特征列，标签列
feature_cols = ["压力","温度","速度","厚度"]
X_train = train_df[feature_cols]
y_train = train_df["是否合格"]
X_test = test_df[feature_cols]
y_test = test_df["是否合格"]

# 训练逻辑回归模型
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 预测评估
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("===== 模型训练完成 =====")
print(f"测试集准确率：{acc:.4f}")
print("\n分类报告：")
print(classification_report(y_test, y_pred, zero_division=0))

# 保存模型
import joblib
model_dir = os.path.join(base_dir, "model")
os.makedirs(model_dir, exist_ok=True)
joblib.dump(model, os.path.join(model_dir, "model.pkl"))
print(f"\n模型已保存到 model/model.pkl")

