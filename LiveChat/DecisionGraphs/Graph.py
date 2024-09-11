class GraphTraversal:
    def __init__(self):
        self.graph = {}
        self.current_node = None
        
    def setup(self, graph_dict):
        self.graph = graph_dict.copy()  # Create a copy to avoid modifying the original dictionary
        print("Graph setup complete.")
        
        # Set current_node to the first node in the graph if it's not already set
        if self.current_node is None and self.graph:
            self.current_node = next(iter(self.graph))
            print(f"Current node set to {self.current_node}")

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append(to_node)

    def forward(self):
        if self.current_node is None:
            raise ValueError("No current node set. Use 'arrive_at' first.")
        
        neighbors = self.graph.get(self.current_node, [])
        if not neighbors:
            print(f"No forward nodes from {self.current_node}")
            return None
        
        next_node = neighbors[0]  # For simplicity, we'll always choose the first neighbor
        print(f"Moving forward from {self.current_node} to {next_node}")
        self.current_node = next_node
        return next_node

    def backwards(self):
        if self.current_node is None:
            raise ValueError("No current node set. Use 'arrive_at' first.")
        
        previous_node = None
        for node, neighbors in self.graph.items():
            if self.current_node in neighbors:
                previous_node = node
                break
        
        if previous_node is None:
            print(f"No backward nodes from {self.current_node}")
            return None
        
        print(f"Moving backward from {self.current_node} to {previous_node}")
        self.current_node = previous_node
        return previous_node

    def arrive_at(self, node):
        if node not in self.graph:
            raise ValueError(f"Node {node} does not exist in the graph")
        
        self.current_node = node
        print(f"Arrived at node {node}")
        return node