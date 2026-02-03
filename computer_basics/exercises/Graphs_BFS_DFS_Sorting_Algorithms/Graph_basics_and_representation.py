class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  # remove this line for directed

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

g.print_graph()


class GraphMatrix:
    def __init__(self):
        # List to store vertex names in order of insertion
        self.vertices = []
        # Dictionary to map vertex names to indices in the matrix
        self.vertex_indices = {}
        # The adjacency matrix (2D list), initially empty
        self.adj_matrix = []

    def add_vertex(self, vertex):
        # Only add vertex if it's not already present
        if vertex not in self.vertex_indices:
            # Map vertex to the next available index
            self.vertex_indices[vertex] = len(self.vertices)
            # Add vertex to the list
            self.vertices.append(vertex)
            
            # Expand each existing row to account for the new vertex
            for row in self.adj_matrix:
                row.append(0)  # new column initialized to 0
            
            # Add a new row for the new vertex, all 0s initially
            self.adj_matrix.append([0] * len(self.vertices))

    def add_edge(self, v1, v2):
        # Make sure both vertices exist in the graph
        for v in (v1, v2):
            if v not in self.vertex_indices:
                self.add_vertex(v)
        
        # Get the matrix indices for these vertices
        idx1 = self.vertex_indices[v1]
        idx2 = self.vertex_indices[v2]
        
        # Set the matrix cell to 1 to indicate an edge
        self.adj_matrix[idx1][idx2] = 1
        self.adj_matrix[idx2][idx1] = 1  # for undirected graphs

    def print_graph(self):
        # Print the header row with vertex names
        print("  ", " ".join(self.vertices))
        # Print each row with the corresponding vertex name
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], row)


g = GraphMatrix()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

g.print_graph()
