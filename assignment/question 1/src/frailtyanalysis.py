# -*- coding: utf-8 -*-
"""frailtyanalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1boWxDTMxm1rXUnPIHr8dxZJN3Q0O8sP4
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

import io
data = pd.read_csv(io.BytesIO(uploaded['fraility (3).csv']))

print(data.isnull().sum())

data['Grip Strength'] = pd.to_numeric(data['Grip Strength'], errors='coerce')

data.dropna(inplace=True)

# Example: Scatter plot of grip strength vs frailty
sns.scatterplot(x='Grip Strength', y='Frailty', data=data)
plt.title('Grip Strength vs Frailty')
plt.xlabel('Grip Strength (kg)')
plt.ylabel('Frailty')
plt.show()