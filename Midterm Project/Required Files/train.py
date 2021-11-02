#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pickle

df = pd.read_csv('https://raw.githubusercontent.com/gialkady/ml_zoomcamp/Homeworks/Midterm%20Project/Data/NetflixOriginals.csv',encoding='latin-1') 

df["Date"] = pd.to_datetime(df.Premiere)

df['Year'] = df['Date'].apply(lambda x:x.year)
df['Month'] = df['Date'].apply(lambda x:x.month)
df['Week Day'] = df['Date'].apply(lambda x:x.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Week Day'] = df['Week Day'].map(dmap)

mmap = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun', 7: 'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
df['Month'] = df['Month'].map(mmap)

df.rename(columns={'IMDB Score':'rating'},inplace=True)


df.columns = df.columns.str.lower().str.replace(' ', '_')

strings = list(df.dtypes[df.dtypes == 'object'].index)

for col in strings:
    df[col] = df[col].str.lower().str.replace(' ', '_')


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=11)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=11)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.rating.values
y_val = df_val.rating.values
y_test = df_test.rating.values

del df_train['rating']
del df_val['rating']
del df_test['rating']

del df_train['date']
del df_val['date']
del df_test['date']

features = ['title', 'genre', 'premiere', 'runtime', 'language',  'year', 'month', 'week_day']

train_dicts = df_train[features].to_dict(orient='records')
val_dicts = df_val[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_train = dv.fit_transform(train_dicts)
X_val = dv.transform(val_dicts)


features = dv.get_feature_names()
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)


#training

xgb_params = {
    'eta': 0.1,
    'max_depth': 6,
    'min_child_weight':1,

    'objective': 'reg:squarederror',
    'nthread': 8,

    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=100)

y_pred = model.predict(dtrain)
rmse=np.sqrt(mean_squared_error(y_train, y_pred))
#print(f'rmse_train={rmse}')



#validation

xgb_params = {
    'eta': 0.1,
    'max_depth': 6,
    'min_child_weight':1,

    'objective': 'reg:squarederror',
    'nthread': 8,

    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dval, num_boost_round=100)

y_pred = model.predict(dval)
rmse=np.sqrt(mean_squared_error(y_val, y_pred))
#print(f'rmse_val={rmse}')


# training the final model
df_full_train = df_full_train.reset_index(drop=True)
y_full_train = df_full_train.rating.astype(int).values
del df_full_train['rating']
del df_full_train['date']

dicts_full_train = df_full_train.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)

dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train,
                    feature_names=dv.get_feature_names())

dtest = xgb.DMatrix(X_test, feature_names=dv.get_feature_names())

xgb_params = {
    'eta': 0.1, 
    'max_depth': 6,
    'min_child_weight':1,

    'objective': 'reg:squarederror',
    'nthread': 8,

    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dfulltrain, num_boost_round=100)


y_pred = model.predict(dtest)
rmse=np.sqrt(mean_squared_error(y_test, y_pred))
print(f'rmse_final_train={rmse}')

# Save the model

output_file = 'film_rating_pred.bin'
output_file

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)


print(f'the model is saved to {output_file}')