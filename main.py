from cmath import sin
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


# Add data to a list
sinet_list = []
for vertex in range(len(D)):
    assign = sinet_list.append(D[vertex])
sinet_list.append(assign)
sinet_list.pop()

print("=================================================================================================")


# Yuki distance

y = Graph(16)

y.add_edge(0, 1, 5)
y.add_edge(0, 11, 6)
y.add_edge(1, 2, 2)
y.add_edge(1, 15, 2)
y.add_edge(1, 0, 5)
y.add_edge(2, 1, 2)
y.add_edge(2, 3, 5)
y.add_edge(2, 15, 3)
y.add_edge(3, 2, 5)
y.add_edge(3, 4, 10)
y.add_edge(3, 12, 9)
y.add_edge(4, 3, 10)
y.add_edge(4, 5, 5)
y.add_edge(5, 4, 5)
y.add_edge(5, 6, 6)
y.add_edge(6, 5, 6)
y.add_edge(6, 7, 8) 
y.add_edge(6, 14, 5) 
y.add_edge(7, 6, 8) 
y.add_edge(7, 8, 2) 
y.add_edge(8, 7, 2) 
y.add_edge(8, 9, 6) 
y.add_edge(8, 14, 4) 
y.add_edge(9, 8, 6) 
y.add_edge(9, 10, 5) 
y.add_edge(9, 12, 5) 
y.add_edge(10, 9, 5) 
y.add_edge(10, 11, 4) 
y.add_edge(10, 12, 4) 
y.add_edge(11, 10, 4) 
y.add_edge(11, 0, 6) 
y.add_edge(11, 12, 5) 
y.add_edge(11, 15, 9) 
y.add_edge(12, 13, 6) 
y.add_edge(12, 9, 5) 
y.add_edge(12, 10, 4) 
y.add_edge(12, 11, 5) 
y.add_edge(13, 12, 6) 
y.add_edge(13, 14, 6) 
y.add_edge(13, 15, 7) 
y.add_edge(14, 6, 5) 
y.add_edge(14, 8, 4) 
y.add_edge(14, 3, 9) 
y.add_edge(14, 13, 6) 
y.add_edge(15, 11, 9) 
y.add_edge(15, 2, 3) 
y.add_edge(15, 1, 2) 
y.add_edge(15, 13, 7) 

yuki_place = ["His House", "AEON1", "Wat Phnom", "Daro House", "AEON2", "Sensok", "Airport", "Sinet house", "Stoeng MeanChey", "K-mall", "ISPP", "AEON3", "Wat Sonsomkosal", "Spar ToulTompong", "Toul Kork", "Boeng KengKong"]

D = y.dijkstra(0)

for vertex in range(len(D)):
    print("From Teacher Yuki house to ", yuki_place[vertex], "is", D[vertex])


print("=================================================================================================")

# Daro distance

r = Graph(16)

r.add_edge(0, 1, 10)
r.add_edge(0, 11, 5)
r.add_edge(0, 15, 9)
r.add_edge(1, 0, 10)
r.add_edge(1, 2, 5)
r.add_edge(2, 1, 5)
r.add_edge(2, 3, 6)
r.add_edge(3, 2, 6)
r.add_edge(3, 4, 8)
r.add_edge(3, 15, 5)
r.add_edge(4, 3, 8)
r.add_edge(4, 5, 2)
r.add_edge(5, 4, 2)
r.add_edge(5, 6, 6)
r.add_edge(5, 15, 4)
r.add_edge(6, 5, 6)
r.add_edge(6, 7, 5) 
r.add_edge(6, 13, 5) 
r.add_edge(7, 6, 5) 
r.add_edge(7, 8, 4) 
r.add_edge(7, 13, 4) 
r.add_edge(8, 7, 4) 
r.add_edge(8, 9, 6) 
r.add_edge(8, 13, 5) 
r.add_edge(8, 12, 9) 
r.add_edge(9, 8, 6) 
r.add_edge(9, 10, 5) 
r.add_edge(10, 9, 5) 
r.add_edge(10, 11, 2) 
r.add_edge(10, 12, 2) 
r.add_edge(11, 10, 2) 
r.add_edge(11, 0, 5) 
r.add_edge(11, 12, 3) 
r.add_edge(12, 11, 3) 
r.add_edge(12, 10, 2) 
r.add_edge(12, 8, 9) 
r.add_edge(12, 14, 7) 
r.add_edge(13, 8, 5) 
r.add_edge(13, 7, 4) 
r.add_edge(13, 6, 5) 
r.add_edge(13, 14, 6) 
r.add_edge(14, 12, 7) 
r.add_edge(14, 13, 6) 
r.add_edge(14, 15, 6) 
r.add_edge(15, 3, 5) 
r.add_edge(15, 0, 9) 
r.add_edge(15, 14, 6) 
r.add_edge(15, 5, 4) 

daro_place = ["His house", "AEON2", "Sensok", "Airport", "Sinet house", "Stoeng Meanchey", "K-Mall", "ISPP", "AEON3", "Yuki house", "AEON1", "Wat Phnom", "Boeng KengKong", "Wat Sonsom Kosal", "Spar Toul Tompong", "Toul Kok"]

D = r.dijkstra(0)

for vertex in range(len(D)):
    print("From Teacher Daro house to ", daro_place[vertex], "is", D[vertex])
print("=================================================================================================")

# organize List is the list I take to compare all the three list with the same place t 
organize_place = ["Teacher Sinet House", "Airport", "Sensok", "AEON2", "Teacher Daro House", "WatPhnom", "AEON1", "Teacher Yuki House", "AEON3", "ISPP", "K-Mall", "StoengMeanchey", "ToulKok", "Spar Toul Tompong", "Wat SonSomKosal", "BoengKengKong"]
sinet_organize_list = sinet_list
yuki_organize_list = [23,25,27,22,12,7,5,0,6,10,15,21,20,14,11,7]
daro_organize_list = [15,14,15,10,0,5,7,12,17,21,19,13,9,15,21,8]



# Ref: https://stackoverflow.com/questions/16326853/enumerate-two-python-lists-simultaneously
print("Based on the information teacher can have a party less than 16mn of commute time at: \n")

for index, value in enumerate(zip(sinet_organize_list, yuki_organize_list, daro_organize_list)):
    if((value[0]<=15) and (value[1]<=15) and (value[2]<=15)):
        print(organize_place[index])
        print(f" Teacher Sinet drive {value[0]}mn\n Teacher yuki drive {value[1]}mn\n Teacher Daro drive {value[2]}mn")
print("=================================================================================================")

