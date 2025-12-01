import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import random

# Train an ML model for linear regression

def train_model(X, y) :
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)    
    print(f"测试集平均绝对误差: {mae:.2f}")
    print(f"测试集R²分数: {r2:.4f}")
    feature_names = [
        '0', '1', '2', '3','4', '5',
        '6', '7', '8', '9', '10','11'
    ]
    print("\n=== 模型学到的权重分析 ===")
    for i, (name, weight) in enumerate(zip(feature_names, model.coef_)):
        print(f"{name:8}: {weight:8.1f}")
    print(f"偏置项: {model.intercept_:.1f}")
    return model

def main() :
    tot = 6683
    X = []
    y = []
    list = []
    for i in range(tot) :
        tmp = eval(input())
        list.append(tmp)
    las = 0
    for i in range(tot) :
        if i == tot - 1 or list[i][-2] != list[i + 1][-2] :
            round = i - las + 1
            base = 5000
            if round % 2 == 0 :
                base = -base
            for j in range(las, i + 1) :
                list[j][12] += base * (list[j][-1] // round)
                base = -base
            las = i + 1
    for i in range(tot) :
        y.append(list[i][12])
        X.append(list[i][:12])
    train_model(np.array(X),np.array(y))

if __name__ == "__main__":
    main()