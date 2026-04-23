import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
import time
import json

# 1. Load Data
print("--- Đang load dữ liệu ---")
start_load = time.time()
df = pd.read_csv('creditcard.csv')
load_time = time.time() - start_load

# 2. Preprocessing
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Training
print("--- Đang bắt đầu training LightGBM ---")
train_data = lgb.Dataset(X_train, label=y_train)
params = {
    'objective': 'binary',
    'metric': 'auc',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'verbose': -1
}

start_train = time.time()
model = lgb.train(params, train_data, num_boost_round=100)
train_time = time.time() - start_train

# 4. Evaluation
print("--- Đang đánh giá mô hình ---")
y_pred_prob = model.predict(X_test)
y_pred = [1 if x > 0.5 else 0 for x in y_pred_prob]

# 5. Inference Latency (Đo tốc độ dự đoán)
start_inf = time.time()
_ = model.predict(X_test.iloc[:1000]) # Dự đoán 1000 dòng
inf_latency_1000 = (time.time() - start_inf) / 1000

# Tổng hợp kết quả
results = {
    "Thời gian load data (s)": round(load_time, 4),
    "Thời gian training (s)": round(train_time, 4),
    "AUC-ROC": round(roc_auc_score(y_test, y_pred_prob), 4),
    "Accuracy": round(accuracy_score(y_test, y_pred), 4),
    "F1-Score": round(f1_score(y_test, y_pred), 4),
    "Precision": round(precision_score(y_test, y_pred), 4),
    "Recall": round(recall_score(y_test, y_pred), 4),
    "Inference latency (per row - s)": f"{inf_latency_1000:.6f}"
}

print("\n========== KẾT QUẢ BENCHMARK ==========")
print(json.dumps(results, indent=4, ensure_ascii=False))

# Lưu kết quả ra file để nộp bài
with open('benchmark_result.json', 'w') as f:
    json.dump(results, f, indent=4)
print("\nKết quả đã được lưu vào file benchmark_result.json")
