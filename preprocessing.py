import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.impute import SimpleImputer
data = {
    'Country': ['France', 'Spain', 'Germany', 'Spain', 'Germany', 'France', 'Spain', 'France', 'Germany', 'France'],
    'Age': [44, 27, 30, 38, np.nan, 35, np.nan, 48, 50, 37],
    'Salary': [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    'Purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])
print("\nData after filling missing values:")
print(df)
binner = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
df_binned = df.copy()
df_binned[['Age', 'Salary']] = binner.fit_transform(df[['Age', 'Salary']])
print("\nData after binning:")
print(df_binned)
scaler = StandardScaler()
df_normalized = df_binned.copy()
df_normalized[['Age', 'Salary']] = scaler.fit_transform(df_binned[['Age', 'Salary']])
print("\nData after Z-score normalization:")
print(df_normalized)
