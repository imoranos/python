my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            #print(node, distance)
            if distance + distances[current] < distances[node]:
                print(distance , distances[current] , distances[node],node)
                distances[node] = distance + distances[current]
                print(distance , distances[current] , distances[node],node)
        return 1
    #print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    
shortest_path(my_graph, 'A')