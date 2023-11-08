from pyvis.network import Network

# Define Dial's algorithm function to find the shortest path tree
def dial(graph, source):
    # Initialize data structures
    num_nodes = len(graph)
    distance = [float('inf')] * num_nodes
    parent = [-1] * num_nodes
    visited = [False] * num_nodes

    distance[source] = 0
    max_weight = max(max(row) for row in graph)  # Find the maximum weight in the graph

    # Create a list of buckets for each possible distance
    buckets = [set() for _ in range(max_weight + 1)]
    buckets[0].add(source)

    for _ in range(num_nodes):
        # Find the first non-empty bucket
        current_distance = 0
        while not buckets[current_distance]:
            current_distance += 1

        # Get the node with the minimum distance in the current bucket
        min_dist_node = buckets[current_distance].pop()

        for i in range(num_nodes):
            if not visited[i] and graph[min_dist_node][i] > 0:
                if distance[min_dist_node] + graph[min_dist_node][i] < distance[i]:
                    new_distance = distance[min_dist_node] + graph[min_dist_node][i]

                    # Extend the buckets list if necessary
                    if new_distance > max_weight:
                        buckets.extend([set() for _ in range(new_distance - max_weight)])

                    old_bucket = distance[i]
                    distance[i] = new_distance
                    new_bucket = distance[i]
                    parent[i] = min_dist_node

                    # Move the node to the new bucket
                    buckets[new_bucket].add(i)

        visited[min_dist_node] = True

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

# Perform Dial's algorithm to find the shortest path tree
shortest_path_tree_parents = dial(original_graph, start_node)

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

