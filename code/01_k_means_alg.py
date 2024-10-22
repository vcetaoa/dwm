import numpy as np

# Predefined dataset that is likely to require multiple iterations
D = np.array([10, 12, 14, 50, 52, 54, 80, 82, 84, 90])
print(f"Dataset D: {D}")

# Input for number of clusters
k = int(input("Enter the number of clusters (k): "))

# Step 1: Initialize cluster means randomly from the dataset
means = np.random.choice(D, k, replace=False)
print(f"Initial means (k={k}): {means}")

# Step 2: Assign remaining elements to clusters randomly
clusters = np.random.randint(0, k, size=D.shape)
print("Initial random cluster assignments:")
for i in range(k):
    cluster_elements = D[clusters == i]
    print(f"  Cluster {i+1} initial elements: {cluster_elements}")


# Function to calculate distance
def calculate_distance(data, means):
    return np.abs(data[:, np.newaxis] - means)


# K-Means Iteration
iteration = 0
previous_means = np.zeros_like(means)

while not np.array_equal(previous_means, means):
    iteration += 1
    previous_means = means.copy()

    # Step 3: Update means based on the assigned clusters
    means = np.array(
        [
            D[clusters == i].mean() if np.any(clusters == i) else means[i]
            for i in range(k)
        ]
    )

    # Step 4: Calculate distances from means to elements
    distances = calculate_distance(D, means)

    # Step 5: Reassign clusters based on the closest mean
    clusters = np.argmin(distances, axis=1)

    # Output for this iteration
    print(f"Iteration {iteration}:")
    for i in range(k):
        cluster_elements = D[clusters == i]
        print(f"  Cluster {i+1}: Elements = {cluster_elements}, Mean = {means[i]}")
    print()

# Final result
print("Final clusters:")
for i in range(k):
    cluster_elements = D[clusters == i]
    print(f"Cluster {i+1}: Elements = {cluster_elements}, Mean = {means[i]}")


"""
Output:

Dataset D: [10 12 14 50 52 54 80 82 84 90]
Enter the number of clusters (k): 2
Initial means (k=2): [84 82]
Initial random cluster assignments:
  Cluster 1 initial elements: [12 14 50 52 80 82 84]
  Cluster 2 initial elements: [10 54 90]
Iteration 1:
  Cluster 1: Elements = [54 80 82 84 90], Mean = 53.42857142857143
  Cluster 2: Elements = [10 12 14 50 52], Mean = 51.333333333333336

Iteration 2:
  Cluster 1: Elements = [54 80 82 84 90], Mean = 78.0
  Cluster 2: Elements = [10 12 14 50 52], Mean = 27.6

Iteration 3:
  Cluster 1: Elements = [54 80 82 84 90], Mean = 78.0
  Cluster 2: Elements = [10 12 14 50 52], Mean = 27.6

Final clusters:
Cluster 1: Elements = [54 80 82 84 90], Mean = 78.0
Cluster 2: Elements = [10 12 14 50 52], Mean = 27.6
"""
