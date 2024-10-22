import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = [22, 24, 26, 28, 29, 31, 35, 37, 41, 53, 64]
sort_data = np.sort(data)
print(sort_data)

# Median
Q2 = statistics.median(data)
print('Median : ', Q2)

# Lower Half
Lower_half = [x for x in data if x < Q2]
print('Lower Half:', Lower_half)
Q1 = statistics.median(Lower_half)
print('Q1 : ', Q1)

# Upper Half
Upper_half = [x for x in data if x > Q2]
print('Upper Half:', Upper_half)
Q3 = statistics.median(Upper_half)
print('Q3 : ', Q3)

# Interquartile Range (IQR)
IQR = Q3 - Q1
print('IQR : ', IQR)

# Boundaries
low_boundary = Q1 - 1.5 * IQR
print('Lower boundary is ', low_boundary)
upper_boundary = Q3 + 1.5 * IQR
print('Upper boundary is ', upper_boundary)

# Outliers
outlier = [x for x in data if x > upper_boundary or x < low_boundary]
print('Outliers in the dataset:', outlier)

# Plotting the Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.title('Box Plot of the Dataset')
plt.xlabel('Data')
plt.ylabel('Values')
plt.show()
