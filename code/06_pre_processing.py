import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# Creating the DataFrame
data = {
    "Country": [
        "France",
        "Spain",
        "Germany",
        "Spain",
        "Germany",
        "France",
        "Spain",
        "France",
        "Germany",
        "France",
    ],
    "Age": [44, 27, 30, 38, np.nan, 35, np.nan, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"],
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Filling missing values with the mean
df[["Age", "Salary"]] = df[["Age", "Salary"]].fillna(df[["Age", "Salary"]].mean())
print("\nData after filling missing values:")
print(df)

# Binning the data
bins_age = pd.cut(df["Age"], bins=3, labels=False)
bins_salary = pd.cut(df["Salary"], bins=3, labels=False)
df["Age_Binned"] = bins_age
df["Salary_Binned"] = bins_salary
print("\nData after binning:")
print(df[["Age", "Salary", "Age_Binned", "Salary_Binned"]])

# Z-score normalization
scaler = StandardScaler()
df[["Age_Normalized", "Salary_Normalized"]] = scaler.fit_transform(
    df[["Age", "Salary"]]
)
print("\nData after Z-score normalization:")
print(df[["Age", "Salary", "Age_Normalized", "Salary_Normalized"]])


"""
Output:

Original Data:
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany   NaN      NaN       Yes
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes

Data after filling missing values:
   Country     Age        Salary Purchased
0   France  44.000  72000.000000        No
1    Spain  27.000  48000.000000       Yes
2  Germany  30.000  54000.000000        No
3    Spain  38.000  61000.000000        No
4  Germany  38.625  63777.777778       Yes
5   France  35.000  58000.000000       Yes
6    Spain  38.625  52000.000000        No
7   France  48.000  79000.000000       Yes
8  Germany  50.000  83000.000000        No
9   France  37.000  67000.000000       Yes

Data after binning:
      Age        Salary  Age_Binned  Salary_Binned
0  44.000  72000.000000           2              2
1  27.000  48000.000000           0              0
2  30.000  54000.000000           0              0
3  38.000  61000.000000           1              1
4  38.625  63777.777778           1              1
5  35.000  58000.000000           1              0
6  38.625  52000.000000           1              0
7  48.000  79000.000000           2              2
8  50.000  83000.000000           2              2
9  37.000  67000.000000           1              1

Data after Z-score normalization:
      Age        Salary  Age_Normalized  Salary_Normalized
0  44.000  72000.000000        0.782465       7.494733e-01
1  27.000  48000.000000       -1.692308      -1.438178e+00
2  30.000  54000.000000       -1.255584      -8.912655e-01
3  38.000  61000.000000       -0.090984      -2.532004e-01
4  38.625  63777.777778        0.000000       6.632192e-16
5  35.000  58000.000000       -0.527709      -5.266569e-01
6  38.625  52000.000000        0.000000      -1.073570e+00
7  48.000  79000.000000        1.364765       1.387538e+00
8  50.000  83000.000000        1.655915       1.752147e+00
9  37.000  67000.000000       -0.236559       2.937125e-01
"""
