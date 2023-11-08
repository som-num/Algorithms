from pyvis.network import Network

# Define the Boruvka's algorithm function to find the minimum spanning tree
def boruvka(graph):
    # Initialize a list to store edges and sort them by weight
    edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            weight = graph[i][j]
            if weight > 0:
                edges.append((i, j, weight))
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight

    # Create a list to store the cheapest edge for each component
    cheapest = [-1] * len(graph)

    # Create a list to store the component for each vertex
    component = [i for i in range(len(graph))]

    # Initialize the number of components
    num_components = len(graph)

    # Initialize a list to store the selected edges for the minimum spanning tree
    minimum_spanning_tree = []

    # Iterate through sorted edges
    for edge in edges:
        source, target, weight = edge
        source_component = component[source]
        target_component = component[target]

        # Check if the source and target are in different components
        if source_component != target_component:
            minimum_spanning_tree.append(edge)
            # Merge the components
            for i in range(len(graph)):
                if component[i] == target_component:
                    component[i] = source_component

        # Update the cheapest edge for the component
        if cheapest[source_component] == -1 or weight < cheapest[source_component][2]:
            cheapest[source_component] = edge

    # Remove -1 values from the cheapest list
    cheapest = [edge for edge in cheapest if edge != -1]

    # Repeat the process until there's only one component
    while num_components > 1:
        # Initialize a list to store the new cheapest edges
        new_cheapest = [-1] * num_components

        # Iterate through the cheapest edges
        for edge in cheapest:
            source, target, weight = edge
            source_component = component[source]
            target_component = component[target]

            # Check if the source and target are in different components
            if source_component != target_component:
                minimum_spanning_tree.append(edge)
                # Merge the components
                for i in range(len(graph)):
                    if component[i] == target_component:
                        component[i] = source_component

            # Update the new cheapest edge for the component
            if new_cheapest[source_component] == -1 or weight < new_cheapest[source_component][2]:
                new_cheapest[source_component] = edge

        # Remove -1 values from the new cheapest list
        new_cheapest = [edge for edge in new_cheapest if edge != -1]

        # Update the cheapest list
        cheapest = new_cheapest

        # Update the number of components
        num_components = len(cheapest)

    return minimum_spanning_tree

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
    G_original.add_node(i, label=str(i), font={'size': 60})  # Add nodes with labels and font size
    for j in range(i + 1, len(original_graph)):
        weight = original_graph[i][j]
        if weight > 0:
            G_original.add_node(j, label=str(j), font={'size': 60})  # Ensure both nodes exist
            G_original.add_edge(i, j, title=str(weight), label=str(weight), font={'size': 60})  # Add edges with labels and font size

# Set node positions using Barnes-Hut layout
G_original.barnes_hut()

# Display the original graph
G_original.show("original_graph.html", notebook=False)

# Perform Boruvka's algorithm to find the minimum spanning tree
minimum_spanning_tree_edges = boruvka(original_graph)
print(minimum_spanning_tree_edges)
total_weight = sum(edge[2] for edge in minimum_spanning_tree_edges)
print(f"Total weight of the minimum spanning tree: {total_weight}")

# Create a Pyvis graph for the minimum spanning tree
G_mst = Network(directed=False)
for edge in minimum_spanning_tree_edges:
    source, target, weight = edge
    G_mst.add_node(source, label=str(source), font={'size': 60}, color='red')  # Add nodes with labels, font size, and red color
    G_mst.add_node(target, label=str(target), font={'size': 60}, color='red')  # Add nodes with labels, font size, and red color
    G_mst.add_edge(source, target, title=str(weight), label=str(weight), color='red', font={'size': 60})  # Add edges with labels, font size, and red color

# Set node positions using Barnes-Hut layout
G_mst.barnes_hut()

# Display the minimum spanning tree
G_mst.show("minimum_spanning_tree.html", notebook=False)
