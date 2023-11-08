# Prompt the user to input the number of vertices
num_vertices = int(input("Enter the number of vertices: "))

# Initialize an empty adjacency matrix with zeros
adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

# Get vertex labels from the user
vertex_labels = [input(f"Enter label for vertex {i + 1}: ") for i in range(num_vertices)]

# Fill in the adjacency matrix based on user input
for i in range(num_vertices):
    for j in range(num_vertices):
        if i != j:
            weight = int(input(f"Enter the weight from {vertex_labels[i]} to {vertex_labels[j]} (or 0 if no connection): "))
            adjacency_matrix[i][j] = weight

# Print the adjacency matrix
for row in adjacency_matrix:
    print(row, ",")
#copy the matrix from the terminal and paste it in the file