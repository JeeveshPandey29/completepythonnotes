#Representation of undirected graph as adjacency matrix 

def create_graph(v, edges):
    mat = [[0 for _ in range(v)] for _ in range(v)]
    for it in edges:
        u = it[0]
        w = it[1]
        mat[u][w] = 1
        mat[w][u] = 1
    return mat

def print_graph(mat):
    for row in mat:
        print(row)

if __name__ == "__main__":
    v = 4
    edges = [(0, 1), (0, 2), (1, 3)]
    graph = create_graph(v, edges)
    print("Adjacency Matrix Representation:")
    print_graph(graph)


#Representation of directed graph as adjacency matrix 

def create_graph(v, edges):
    mat = [[0 for _ in range(v)] for _ in range(v)]

    for it in edges:
        u = it[0]
        w = it[1]
        mat[u][w] = 1
    
    return mat


def print_graph(mat):
    for row in mat:
        print(row)

if __name__ == "__main__":
    v = 4
    edges = [(0, 1), (0, 2), (1, 3)]
    graph = create_graph(v, edges)
    print("Adjacency Matrix Representation of Directed Graph:")
    print_graph(graph)



# Representation of undirected graph as adjacency list

def create_graph(v, edges):
    graph = [[] for _ in range(v)]

    for (u, w) in edges:
        graph[u].append(w)
        graph[w].append(u)

    return graph


def print_graph(graph):
    for i in range(len(graph)):
        print(f"{i}: {graph[i]}")


if __name__ == "__main__":
    v = 4
    edges = [(0, 1), (0, 2), (1, 3)]

    graph = create_graph(v, edges)

    print("Adjacency List Representation:")
    print_graph(graph)
