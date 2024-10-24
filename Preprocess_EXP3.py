import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer, OneHotEncoder
from sklearn.impute import SimpleImputer

# Sample data
data = {
    'Country': ['France', 'Spain', 'Germany', 'Spain', 'Germany', 'France', 'Spain', 'France', 'Germany', 'France'],
    'Age': [44, 27, 30, 38, np.nan, 35, np.nan, 48, 50, 37],
    'Salary': [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    'Purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

# 1) Fill up missing values
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])

# 2) Remove duplicates
df.drop_duplicates(inplace=True)

# 3) Handle noisy data
df.loc[df['Age'] < 0, 'Age'] = df['Age'].mean()
df.loc[df['Age'] > 100, 'Age'] = df['Age'].mean()

# 4) Handle outliers
def handle_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lb = Q1 - 1.5 * IQR
    ub = Q3 + 1.5 * IQR
    df[col] = np.where((df[col] < lb) | (df[col] > ub), df[col].median(), df[col])

handle_outliers('Age')
handle_outliers('Salary')

# 5) Binning
binner = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
df[['Age', 'Salary']] = binner.fit_transform(df[['Age', 'Salary']])

# 6) Z-score normalization
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# 7) Encoding of text data
encoder = OneHotEncoder(sparse=False)
encoded_cols = encoder.fit_transform(df[['Country', 'Purchased']])
encoded_col_names = encoder.get_feature_names_out(['Country', 'Purchased'])
df = df.join(pd.DataFrame(encoded_cols, columns=encoded_col_names))

# Drop the original categorical columns
df.drop(['Country', 'Purchased'], axis=1, inplace=True)

# Save the cleaned and processed data to a new CSV
df.to_csv('cleaned_data.csv', index=False)

print("Data preprocessing complete. Cleaned data saved to 'cleaned_data.csv'.")
print("\nCleaned Data:")
print(df)
