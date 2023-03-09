import pandas as pd
import numpy as np
import pickle

df = pd.read_csv("../../data/processed/obdelani_podatki.csv", sep="," , decimal=".", index_col=False)

# print(df.head().columns)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score

df_vhod = df.drop('pm10', axis = 1)
df_izhod = df['pm10']

# print(df_vhod.head().columns)

X_train, X_test, y_train, y_test = train_test_split(df_vhod, df_izhod, test_size=0.3, random_state=1234)

reg = LinearRegression()
reg.fit(X_train,y_train)

y_pred = reg.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

var = explained_variance_score(y_test, y_pred)

metrike = 'mean_absolute_error: ' + str(mae) + '\nmean_squared_error: ' + str(mse) + '\nexplained_variance_score: ' + str(var)
with open('../../reports/train_metrics.txt', 'w') as f:
    f.write(metrike)

with open("../../models/model.pkl", "wb") as f:
    pickle.dump(reg, f)