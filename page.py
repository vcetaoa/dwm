import numpy as np

def page_rank(graph, teleportation_factor=0.8, num_iterations=2):
    
    num_nodes = len(graph)

    rank = np.ones(num_nodes) / num_nodes
    
    
    adjacency_matrix = np.zeros((num_nodes, num_nodes))
    for i, links in enumerate(graph):
        if links:
            for link in links:
                adjacency_matrix[link, i] = 1
        else:
          
            adjacency_matrix[:, i] = 1
    
    column_sums = adjacency_matrix.sum(axis=0)
    column_sums[column_sums == 0] = 1  
    adjacency_matrix = adjacency_matrix / column_sums
      
    for _ in range(num_iterations):
        rank = teleportation_factor * adjacency_matrix @ rank + (1 - teleportation_factor) / num_nodes * np.ones(num_nodes)
    
    return rank

graph = [
    [1, 2],       
    [2],          
    [0]        
]

pagerank_scores = page_rank(graph, teleportation_factor=0.8, num_iterations=2)
print("PageRank scores after 2 iterations:", pagerank_scores)

