import numpy as np
import pandas as pd
import json
 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#function, assuming dataset is processed according above workbook

def model_logistic_regression(df):
    #adding collumns
    df['Open-close'] = df['Open'] - df['Close']
    df['Low-high'] = df['Low'] - df['High']
    # Shift stock prices forward one day, so we're predicting tomorrow's stock prices from today's prices.
    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)
    #defining X and Y
    features = df[['Open-close', 'Low-high']]
    target = df['Target']
    #normalization
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    #splitting the data
    X_train, X_valid, Y_train, Y_valid = train_test_split(features, target, test_size=0.1, random_state=2022)
    #modeling 
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    accuracy = metrics.roc_auc_score(target, model.predict_proba(features)[:, 1])
    print(accuracy)

with open("sp500_index.json") as f:
    stock_data = json.load(f) 

df = pd.DataFrame(stock_data)

model_logistic_regression(df)

#OUTPUT with sp500_index.json
# 0.530811636846621