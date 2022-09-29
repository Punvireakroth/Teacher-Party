from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    
    def dijkstra(graph, start_vertex):
        D = {v:float('inf') for v in range(graph.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        
        return D


g = Graph(16)
# លេខរៀង / ទៅណា / មានweightប៉ុន្មាន 
g.add_edge(0, 1, 8)
g.add_edge(0, 11, 2)
g.add_edge(1, 2, 6)
g.add_edge(1, 12, 5)
g.add_edge(1, 0, 8)
g.add_edge(2, 1, 6)
g.add_edge(2, 3, 5)
g.add_edge(3, 2, 5)
g.add_edge(3, 4, 10)
g.add_edge(4, 3, 10)
g.add_edge(4, 5, 5)
g.add_edge(4, 12, 9)
g.add_edge(5, 4, 5)
g.add_edge(5, 15, 3)
g.add_edge(5, 6, 2)
g.add_edge(6, 5, 2)
g.add_edge(6, 7, 5) 
g.add_edge(6, 15, 2) 
g.add_edge(7, 6, 5) 
g.add_edge(7, 8, 6) 
g.add_edge(8, 7, 6) 
g.add_edge(8, 9, 4) 
g.add_edge(8, 14, 5) 
g.add_edge(8, 15, 9) 
g.add_edge(9, 8, 4) 
g.add_edge(9, 10, 5) 
g.add_edge(9, 14, 4) 
g.add_edge(10, 9, 5) 
g.add_edge(10, 11, 6) 
g.add_edge(10, 14, 5) 
g.add_edge(11, 10, 6) 
g.add_edge(11, 0, 2) 
g.add_edge(11, 12, 4) 
g.add_edge(12, 11, 4) 
g.add_edge(12, 1, 5) 
g.add_edge(12, 4, 9) 
g.add_edge(12, 13, 6) 
g.add_edge(13, 12, 6) 
g.add_edge(13, 14, 6) 
g.add_edge(13, 15, 7) 
g.add_edge(14, 13, 6) 
g.add_edge(14, 8, 5) 
g.add_edge(14, 9, 4) 
g.add_edge(14, 10, 5) 
g.add_edge(15, 5, 3) 
g.add_edge(15, 6, 2) 
g.add_edge(15, 8, 9) 
g.add_edge(15, 13, 7) 



sinet_place = ["His House", "Airport", "Sensok", "AEON2", "Daro House", "Wat Phnom", "AEON1", "BTP", "AEON3", "ISPP", "K-Mall", "Stoeng Meanchey", "Toul Kok", "Spar Toul Tompong", "Wat SonSomKosal", "Boeng KengKong"]

D = g.dijkstra(0)

for vertex in range(len(D)):
    print("From Teacher Sinet house to ", sinet_place[vertex], "is", D[vertex])

