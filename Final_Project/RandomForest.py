import numpy as np
import pandas as pd
import json
 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

def random_forest_regression(df):
    #setting Date as index
    df.set_index("Date", inplace=True)
    df.dropna(inplace=True)
    #defining features and predictors
    x = df.iloc[:, 0:5].values
    y = df.iloc[:, 4].values
    #train, test, split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1,  random_state=0)
    #scaling
    scale = StandardScaler()
    x_train = scale.fit_transform(x_train)
    x_test = scale.transform(x_test)
    #modeling
    model = RandomForestRegressor(n_estimators=500, random_state=42, min_samples_split=2, min_samples_leaf=1, max_depth=12, bootstrap=False)
    model.fit(x_train, y_train)
    predict = model.predict(x_test)
    #model evaluation
    print("Mean Absolute Error:", round(metrics.mean_absolute_error(y_test, predict), 4))
    print("Mean Squared Error:", round(metrics.mean_squared_error(y_test, predict), 4))
    print("Root Mean Squared Error:", round(np.sqrt(metrics.mean_squared_error(y_test, predict)), 4))
    print("(R^2) Score:", round(metrics.r2_score(y_test, predict), 4))
    print(f'Train Score : {model.score(x_train, y_train) * 100:.2f}% and Test Score : {model.score(x_test, y_test) * 100:.2f}% using Random Tree Regressor.')
    errors = abs(predict - y_test)
    mape = 100 * (errors / y_test)
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')


stock_data = pd.read_csv("sp500_data.csv")

df = pd.DataFrame(stock_data)

random_forest_regression(df)

#OUTPUT with sp500_data.csv: 
#Mean Absolute Error: 0.7311
#Mean Squared Error: 2.451
#Root Mean Squared Error: 1.5656
#(R^2) Score: 1.0
#Train Score : 100.00% and Test Score : 100.00% using Random Tree Regressor.
#Accuracy: 99.96 %.
