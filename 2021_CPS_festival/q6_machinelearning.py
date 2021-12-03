# A modest machine learning question to build a model
# that implements a linear regression model using simple x-y values

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# 주어진 데이터셋
x = [5, -15, 7, -7, -11, 3, -9, 1, -1, 11, 9, -13, 13, -3, -5]
y = [18, -82, 28, -42, -62, 8, -52, -2, -12, 48, 38, -72, 58, -22, -32]

# 머신러닝 모델로 예측 값을 얻어야하는 데이터셋
x_not = [-11, -4, -9, 2, -10, -2, 0, -3, 1, -6, -7, -5, -8, -1]

# sklearn 리그레션 모델에 적용시키기 위해 reshape이 필요함 (2차원 배열)
x_rs = np.array(x).reshape(-1,1)
x_not_rs = np.array(x_not).reshape(-1,1)

# 트레이닝, 테스트 셋으로 분할
x_train = x_rs[:-3]     # 80:20 ratio
y_train = y[:-3]
x_test = x_rs[-3:]      
y_test = y[-3:]         

# sklearn linear regression 모델 사용
regr = linear_model.LinearRegression()

# 모델 훈련 
regr.fit(x_train, y_train)

# 예측값 도출
y_test_pred = regr.predict(x_test)
y_not_pred = regr.predict(x_not_rs)

# 여기에서 만약 y_pred 에서 y 값이 그대로 예측 되었다면 성공이다.
print("x 값: \n", list(map(int,x_test)))
print("y 예상값: \n", list(map(int,y_test_pred)))
print("y 실제값: \n", y_test)

# 결과 디스플레이
print("x_not 값: \n", x_not)
print("y_not 예상값: \n", list(map(int,y_not_pred)))
print("y_not 함수 대입값: \n", [5*val-7 for val in x_not])

# 차트 디스플레이
plt.scatter(x_not, y_not_pred, color='black')
plt.plot(x_not, y_not_pred, color='blue')

plt.xticks(())
plt.yticks(())
plt.show()
