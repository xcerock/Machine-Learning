import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/HappinessAlcoholConsumption.csv')
print(df.head())
plt.plot(df('YearsExperience'), df('Salary'))
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
