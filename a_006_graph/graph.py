# a simple implementation of graph using adjacency list (dictionary)
# each key corresponds to a vertex
# value is a list of the vertices each vertex has an edge with

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True

        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

            return True
        
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass

            return True
        
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)

            del self.adj_list[vertex]
            return True
        
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.print_graph()
print()

g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")

g.print_graph()
print()

g.remove_edge("C", "E")
g.remove_edge("A", "E")
g.print_graph()
print()

g.remove_vertex("C")
g.remove_vertex("B")
g.remove_vertex("X")
g.print_graph()
