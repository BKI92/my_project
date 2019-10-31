#!/usr/bin/env python
# coding: utf-8

# In[282]:


# Импортируем необходимые библиотеки и наборы данных, размечаем данные.
import sklearn
import numpy as np
import pandas as pd
money = pd.read_csv('USD_CURRENCY_HISTORY.csv', sep=',')
past= 7 * 4
future = 7
values = money['curs']
start = past
end = len(values) - future
raw_df = []
for i in range(start, end):
    past_and_future_value = values[(i - past):(i + future)]
    raw_df.append(list(past_and_future_value))
past_columns =[f'past_{i}' for i in range(past)]
future_columns =[f'future_{i}' for i in range(future)]    


# In[283]:


# Подготавливаем данные для обучения и проверки точности предсказания моделей.
df = pd.DataFrame(raw_df, columns=(past_columns+future_columns))
X = df[past_columns][:-1]
y = df[future_columns][:-1]
X_test = df[past_columns][-1:]
y_test = df[future_columns][-1:]


# In[284]:


# 1) Предсказания на основе алгоритм линейной регрессии.
from sklearn.linear_model import LinearRegression 
import numpy as np
import matplotlib.pyplot as plt
LinReg = LinearRegression()
LinReg.fit(X, y)
# Анализ предсказанных данных.
prediction = LinReg.predict(X_test)[0]
plt.plot(prediction, label='prediction')
plt.plot(y_test.iloc[0], label='real')
plt.legend()
mean_abs_error =sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
linalg_norm = np.linalg.norm(y_test - prediction)
print(f'mean absolute error = {mean_abs_error}')
print(f'linalg norm = {linalg_norm}')


# In[285]:


# 2) Прогноз курса доллара на основе алгоритма К ближайших соседей.
from sklearn.neighbors import KNeighborsRegressor
KNN = KNeighborsRegressor(n_neighbors=2)
KNN.fit(X, y)
# Анализ предсказанных данных.
prediction = KNN.predict(X_test)[0]
plt.plot(prediction, label='prediction')
plt.plot(y_test.iloc[0], label='real')
plt.legend()
mean_abs_error =sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
linalg_norm = np.linalg.norm(y_test - prediction)
print(f'mean absolute error = {mean_abs_error}')
print(f'linalg norm = {linalg_norm}')


# In[286]:


# 3) Предсказание курса доллара на основе нейронной сети. 
from sklearn.neural_network import MLPRegressor
MLP = MLPRegressor(max_iter=2000, hidden_layer_sizes=200, random_state=40)
MLP.fit(X, y)
# Анализ предсказанных данных.
prediction = MLP.predict(X_test)[0]
plt.plot(prediction, label='prediction')
plt.plot(y_test.iloc[0], label='real')
plt.legend()
mean_abs_error =sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
linalg_norm = np.linalg.norm(y_test - prediction)
print(f'mean absolute error = {mean_abs_error}')
print(f'linalg norm = {linalg_norm}')


# In[287]:


# 4) Предсказание курса доллара на основе деревьев решений.
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=10, min_samples_split=20, min_weight_fraction_leaf=0.13)
regressor.fit(X, y)
# Анализ предсказанных данных.
prediction = regressor.predict(X_test)[0]
plt.plot(prediction, label='prediction')
plt.plot(y_test.iloc[0], label='real')
plt.legend()
mean_abs_error =sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
linalg_norm = np.linalg.norm(y_test - prediction)
print(f'mean absolute error = {mean_abs_error}')
print(f'linalg norm = {linalg_norm}')    


# In[288]:


regressor


# In[289]:


# 5) Предсказание курса доллара на основе случайного леса.
from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=300, random_state=40, n_estimators=500, min_samples_leaf=78)
regr.fit(X, y)
# Анализ предсказанных данных.
prediction = regr.predict(X_test)[0]
plt.plot(prediction, label='prediction')
plt.plot(y_test.iloc[0], label='real')
plt.legend()
mean_abs_error =sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
linalg_norm = np.linalg.norm(y_test - prediction)
print(f'mean absolute error = {mean_abs_error}')
print(f'linalg norm = {linalg_norm}')    


# In[214]:


regr


# In[293]:


from sklearn.preprocessing import PolynomialFeatures
PF = PolynomialFeatures()
PF.fit(X, y)
prediction = PF.predict(X_test)[0]
plt.plot(prediction, label='prediction')
plt.plot(y_test.iloc[0], label='real')
plt.legend()
mean_abs_error =sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
linalg_norm = np.linalg.norm(y_test - prediction)
print(f'mean absolute error = {mean_abs_error}')
print(f'linalg norm = {linalg_norm}')    


# In[ ]:




