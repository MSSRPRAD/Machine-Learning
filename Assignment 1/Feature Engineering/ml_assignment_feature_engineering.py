# -*- coding: utf-8 -*-
"""ML_Assignment_Feature_Engineering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r8s12rkDW76ix21L8upVvmOe9VmeYyjI

## FEATURE ENGINEERING TASK 1:


REPLACE MISSING DATA WITH:

*   MODE OF COLUMN IF CATEGORICAL DATA
*   MEAN OF COLUMN IF NUMERICAL DATA

Import Libraries:
"""

import pandas as pd
import numpy as np

"""Read csv file and store data as pandas dataframe:"""

df = pd.read_csv("data.csv")
df.head(20)

"""Find no of null values:"""

df.isnull().sum().sum()

"""Replace the missing value (fillna) with 1) mode if col = "diagnosis" (Categorical) and 2) mean otherwise. We don't do anything for col = "id" as it is not supposed to be filled."""

cols = list(df)
# mean = df.mean(axis=0)
# mode = df.mode(axis=0)
for col in cols:
  if col=="diagnosis":
    df[col].fillna(value=df[col].mode(), inplace = True)
  elif col != "id":
    df[col].fillna(value=df[col].mean(), inplace = True)

"""We can see that there is no missing data anymore!"""

df.isnull().sum().sum()

"""Read the data (After Feature Engineering 1)"""

df = pd.read_csv("featureEngineering1.csv")

"""Do the normalization (Except columns "id" and "diagnosis")"""

df.iloc[:,3:] =  (df.iloc[:,3:] - df.iloc[:,3:].mean())/df.iloc[:,3:].std()

"""See the normalized data:"""

df

