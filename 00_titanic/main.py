# what sorts of people were more likely to survive?を解く
# testデータにはtest.csvを使う
# trainデータにはtrain.csvを使う
# このファイルはmain.py
# このファイルはtrain.csvを使って学習させる
# このファイルはtest.csvを使って予測させる
# gender_submission.csvはtest.csvの回答を示す
# このファイルはgender_submission.csvを使って正解率を測る

#%%
# 0. ライブラリのインポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.linear_model import LinearRegression


#%%
# 1. データの読み込み
test = pd.read_csv("test.csv") # testデータの読み込み
train = pd.read_csv("train.csv") #  trainデータの読み込み

#%%
train["Title"] = train["Name"].apply(lambda x: x.split(',')[1].split('.')[0].strip()) # 敬称を抽出
test["Title"] = test["Name"].apply(lambda x: x.split(',')[1].split('.')[0].strip()) # 敬称を抽出

#%%
titleGroups = {
    'Mr': 'Mr', 'Mrs': 'Mrs', 'Miss': 'Miss', 'Master': 'Master',
    'Don': 'Mr', 'Rev' : 'Rev', 'Dr' : 'Dr', 'Mme': 'Mrs',
    'Ms': 'Miss', 'Major': 'Mr', 'Lady': 'Mrs', 'Sir': 'Mr', 
    'Mlle': 'Miss', 'Col': 'Mr', 'Capt': 'Mr', 
    'the Countess': 'Mrs','Jonkheer': 'Mr'
} # 敬称をグループ分け

# %%
