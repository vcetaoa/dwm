import pandas as pd
import numpy as np


class DecisionTreeNode:
    def __init__(self, attribute=None, value=None, label=None):
        self.attribute = attribute
        self.value = value
        self.label = label
        self.children = {}


def entropy(data):
    labels = data.iloc[:, -1]
    probabilities = labels.value_counts(normalize=True)
    return -sum(probabilities * np.log2(probabilities + 1e-9))


def information_gain(data, attribute):
    total_entropy = entropy(data)
    weighted_entropy = sum(
        (len(subset) / len(data)) * entropy(subset)
        for value, subset in data.groupby(attribute)
    )
    return total_entropy - weighted_entropy


def best_split(data):
    return max(data.columns[:-1], key=lambda attr: information_gain(data, attr))


def build_tree(data):
    if len(data.iloc[:, -1].unique()) == 1:
        return DecisionTreeNode(label=data.iloc[0, -1])
    if len(data.columns) == 1:
        return DecisionTreeNode(label=data.iloc[:, -1].mode()[0])

    best_attr = best_split(data)
    root = DecisionTreeNode(attribute=best_attr)

    for value, subset in data.groupby(best_attr):
        root.children[value] = build_tree(subset.drop(columns=[best_attr]))
    return root


def predict(tree, instance):
    if tree.label is not None:
        return tree.label
    return predict(tree.children.get(instance[tree.attribute]), instance)


# Create a simple weather dataset
data = {
    "Outlook": [
        "Sunny",
        "Sunny",
        "Overcast",
        "Rain",
        "Rain",
        "Rain",
        "Overcast",
        "Sunny",
        "Sunny",
        "Rain",
        "Sunny",
        "Overcast",
        "Overcast",
        "Rain",
    ],
    "Temperature": [
        "Hot",
        "Hot",
        "Hot",
        "Mild",
        "Cool",
        "Cool",
        "Cool",
        "Mild",
        "Cool",
        "Mild",
        "Mild",
        "Mild",
        "Hot",
        "Mild",
    ],
    "Play": [
        "No",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "No",
    ],
}

df = pd.DataFrame(data)

# Build decision tree
tree = build_tree(df)

# User input for prediction
user_outlook = input("Enter Outlook (Sunny, Overcast, Rain): ")
user_temperature = input("Enter Temperature (Hot, Mild, Cool): ")

# Prepare the instance for prediction
instance = {"Outlook": user_outlook, "Temperature": user_temperature}

instance_series = pd.Series(instance)
result = predict(tree, instance_series)
print(f"Predicted label for {instance}: {result}")
