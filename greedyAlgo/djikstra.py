from pyvis.network import Network

# Define Dijkstra's algorithm function to find the shortest path tree
def dijkstra(graph, source):
    # Initialize data structures
    num_nodes = len(graph)
    distance = [float('inf')] * num_nodes
    parent = [-1] * num_nodes
    visited = [False] * num_nodes

    distance[source] = 0

    for _ in range(num_nodes):
        # Find the node with the minimum distance
        min_dist = float('inf')
        min_index = -1
        for i in range(num_nodes):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        visited[min_index] = True

        # Update distances to adjacent nodes
        for i in range(num_nodes):
            if not visited[i] and graph[min_index][i] > 0:
                if distance[min_index] + graph[min_index][i] < distance[i]:
                    distance[i] = distance[min_index] + graph[min_index][i]
                    parent[i] = min_index

    return parent

# Example graph represented as an adjacency matrix
original_graph = [
    [0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0],
    [0, 0, 12, 0, 22, 0, 18],
    [0, 0, 0, 22, 0, 25, 24],
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 24, 0, 0]
]

# Create a Pyvis graph for the original graph
G_original = Network(directed=False)
for i in range(len(original_graph)):
    G_original.add_node(i, label=str(i), font={'size': 60})
    for j in range(i + 1, len(original_graph)):
        weight = original_graph[i][j]
        if weight > 0:
            G_original.add_node(j, label=str(j), font={'size': 60})
            G_original.add_edge(i, j, title=str(weight), label=str(weight), font={'size': 60})

# Set node positions using Barnes-Hut layout
G_original.barnes_hut()

# Display the original graph
G_original.show("original_graph.html", notebook=False)

# Prompt the user for the starting and ending nodes
start_node = int(input("Enter the starting node: "))
end_node = int(input("Enter the ending node: "))

# Perform Dijkstra's algorithm to find the shortest path tree
shortest_path_tree_parents = dijkstra(original_graph, start_node)

# Create a Pyvis graph for the shortest path
G_shortest_path = Network(directed=False)

# Trace the path from the end_node to the start_node using the parents array
current_node = end_node
while current_node != start_node:
    parent = shortest_path_tree_parents[current_node]
    G_shortest_path.add_node(current_node, label=str(current_node), font={'size': 60})
    G_shortest_path.add_node(parent, label=str(parent), font={'size': 60})
    weight = original_graph[current_node][parent]
    G_shortest_path.add_edge(parent, current_node, color='red', label=str(weight), font={'size': 60})
    current_node = parent

# Add the starting node to the graph
G_shortest_path.add_node(start_node, label=str(start_node), font={'size': 60})

# Set node positions using Barnes-Hut layout
G_shortest_path.barnes_hut()

# Display the shortest path
G_shortest_path.show("shortest_path.html", notebook=False)
