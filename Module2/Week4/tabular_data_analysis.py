import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("D:/AIO/AIO2024/AIO2024-Exercise/Module2/Week4/advertising.csv")

def correlation(x, y):
  x_mean = np.mean(x)
  y_mean = np.mean(y)

  numerator = np.sum((x - x_mean) * (y - y_mean))
  denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

  if denominator == 0:
    return 0  # Handle cases where the denominator is zero

  return numerator / denominator

x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)
print("Correlation between TV and Radio: ", round(corr_xy, 2))

features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
  for feature_2 in features:
      correlation_value = correlation(data[feature_1], data[feature_2])
      print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
result1 = correlation(x, y)
print(result)
print("\nCorrelation (x,y):", round(result1, 8))

# Calculate the correlation matrix
data_corr_coef = data.corr()

plt.figure(figsize=(10,8))
sns.heatmap(data_corr_coef, annot=True, fmt=".2f", linewidth=.5)
plt.show()









