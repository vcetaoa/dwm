import numpy as np


def detect_outliers(data):
    # Ensure the data is a numpy array for convenience
    data = np.array(data)

    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)

    # Calculate Interquartile Range (IQR)
    IQR = Q3 - Q1

    # Define boundaries
    upper_boundary = Q3 + 1.5 * IQR
    lower_boundary = Q1 - 1.5 * IQR

    # Find outliers
    outliers = data[(data > upper_boundary) | (data < lower_boundary)]

    return outliers


# Example usage
data = [22, 24, 26, 28, 29, 31, 35, 37, 41, 53, 64]  # Example dataset
print("Outliers:", detect_outliers(data))



'''
Output:

Outliers: [64]
'''
