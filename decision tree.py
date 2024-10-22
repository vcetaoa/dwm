import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics 
import matplotlib.pyplot as plt 
from sklearn import tree 
# Load the dataset from a CSV file 
df = pd.read_csv('play_tennis.csv') 
# Assuming 'target' is the column you want to predict, and the rest are features 
X = df.drop('play', axis=1) 
y = df['play'] 
# Convert categorical features to numeric if needed 
X = pd.get_dummies(X)  # One-hot encode categorical features 
# Split the dataset into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
# Create and train the decision tree classifier 
clf = DecisionTreeClassifier() 
clf.fit(X_train, y_train) 
# Make predictions 
y_pred = clf.predict(X_test) 
# Evaluate the classifier 
accuracy = metrics.accuracy_score(y_test, y_pred) 
print(f'Accuracy: {accuracy:.2f}') 
# Plot the decision tree 
plt.figure(figsize=(12,8)) 
tree.plot_tree(clf, feature_names=X.columns, class_names=list(map(str, y.unique())), filled=True) 
plt.show()
