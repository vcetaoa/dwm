# Function to convert an adjacency matrix to an adjacency list
def adjacency_matrix_to_list(adj_matrix):
    graph = {}
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        graph[chr(65 + i)] = []  # Using letters A, B, C, ... for node names
        for j in range(num_nodes):
            if adj_matrix[i][j] == 1:  # There is a link from node i to node j
                graph[chr(65 + i)].append(chr(65 + j))
    return graph


# Function to calculate PageRank
def calculate_pagerank(graph, beta, iterations):
    num_nodes = len(graph)
    pagerank = {node: 1 / num_nodes for node in graph}  # Initialize PageRank values

    for it in range(iterations):
        new_pagerank = {}
        for node in graph:
            inbound_links = [n for n in graph if node in graph[n]]
            inbound_sum = sum(
                pagerank[in_link] / len(graph[in_link]) for in_link in inbound_links
            )

            # Calculate new PageRank
            new_pagerank[node] = (1 - beta) + beta * inbound_sum

        # Output the results for the iteration
        print(f"Iteration {it + 1}:")
        for node, pr in new_pagerank.items():
            print(f"PR({node}) = {pr:.4f}")

        # Update pagerank for the next iteration
        pagerank = new_pagerank


# Predefined adjacency matrix (example for 4 nodes)
adj_matrix = [
    [0, 1, 1, 0],  # A -> B, A -> C
    [0, 0, 0, 1],  # B -> D
    [1, 0, 0, 1],  # C -> A, C -> D
    [0, 0, 0, 0],  # D has no outbound links
]

# Convert adjacency matrix to graph
graph = adjacency_matrix_to_list(adj_matrix)

# Initialize constants
beta = 0.8

# Perform PageRank calculation for 2 iterations
calculate_pagerank(graph, beta, 2)


"""
Output:

Iteration 1:
PR(A) = 0.3000
PR(B) = 0.3000
PR(C) = 0.3000
PR(D) = 0.5000
Iteration 2:
PR(A) = 0.3200
PR(B) = 0.3200
PR(C) = 0.3200
PR(D) = 0.5600
"""
