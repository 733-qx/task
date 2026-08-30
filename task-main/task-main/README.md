# task
# 铝合金工件质量预测项目
## 项目结构
- data：存放预处理后的训练集、测试集
- src：源代码
  - data_preprocess.py：数据预处理、缺失值删除、3σ异常值剔除、8:2数据集划分
  - train.py：模型训练与评估
  - predict.py：模型预测
- model：保存训练完成的模型文件
- prompt：任务记录文件夹
  - record.json：项目任务信息记录文件

## 项目简介
# 铝合金工件质量预测项目
## 项目简介
本项目基于铝合金加工的压力、温度、速度、厚度四项工艺参数，构建机器学习二分类模型，用来预测工件最终质量是否合格。
项目完整包含：数据预处理、缺失值处理、3σ准则异常值剔除、数据集划分、模型训练、模型评估、单样本预测全流程，完整复现了一个小型机器学习项目的标准开发流程。

## 项目结构
      task‑main
      ├─ data                 # 数据集文件夹
      │  ├─ train.csv         # 训练集（80%数据）
      │  └─ test.csv          # 测试集（20%数据）
      ├─ model                # 模型保存文件夹
      │  └─ model.pkl         # 训练完成的模型文件
      ├─ prompt               # 任务记录文件夹
      │  └─ record.json       # 项目任务信息记录文件
      ├─ src                  # 源代码文件夹
      │  ├─ data_preprocess.py  # 数据预处理脚本
      │  ├─ train.py           # 模型训练与评估脚本
      │  └─ predict.py         # 模型单样本预测脚本
      └─ README.md            # 项目说明文档
## 运行顺序
1. 运行 src/data_preprocess.py 生成train.csv、test.csv
2. 运行 src/train.py 训练模型，保存模型
3. 运行 src/predict.py 进行样本预测

