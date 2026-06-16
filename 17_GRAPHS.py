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


# Representation of directed graph as adjacency list

def create_graph(v, edges):
    graph = [[] for _ in range(v)]
    for (u, w) in edges:
        graph[u].append(w)  

    return graph


def print_graph(graph):
    for i in range(len(graph)):
        print(f"{i}: {graph[i]}")


if __name__ == "__main__":
    v = 4
    edges = [(0, 1), (0, 2), (1, 3)]
    graph = create_graph(v, edges)
    print("Adjacency List Representation of Directed Graph:")
    print_graph(graph)

# BFS
from collections import deque

def bfs(adj, src=0):
    v = len(adj)               
    visited = [False] * v
    res = []

    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)  

if __name__ == '__main__':
    v = 5
    adj = [[] for _ in range(v)]

    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)

    res = bfs(adj, 0)

    print("BFS Traversal:")
    for node in res:
        print(node, end='  ')

# DFS for single connected component
def dfs(adj, src, visited, res):
    visited[src] = True     
    res.append(src)             

    for x in adj[src]:          
        if not visited[x]:       
            dfs(adj, x, visited, res)  

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)             

if __name__ == "__main__":
    v = 5
    adj = [[] for _ in range(v)]

    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)

    visited = [False] * v
    res = []
    dfs(adj, 0, visited, res)

    print("DFS Traversal:")
    for node in res:
        print(node, end='  ')


#DFS Traversal
from collections import defaultdict

def dfsRec(adj, visited , s , res):
    visited[s] = True
    res.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj,visited, i ,res)
        
def dfs(adj):
    visited=[False]*len(adj)
    res = []
    for i in range(len(adj)):
        if not visited[i]:
            dfsRec(adj, visited ,i , res)
    return res

def addEdge(adj , u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__=='__main__':
    v = 6
    adj = []
    for i in range(v):
        adj.append([])
    addEdge(adj , 1, 2)
    addEdge(adj , 2, 4)
    addEdge(adj , 0, 3)
    addEdge(adj , 5, 4)  

    res = dfs(adj)
    print(*res)