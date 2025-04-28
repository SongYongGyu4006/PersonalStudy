vertex = ['A','B','C','D','E','F','G','H']
adjMat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
def dfs(A, visited=None):
    if visited is None:
        visited = []

    visited.append(A)
    print(A, end=' ')

    A = vertex.index(A)
    
    for i in range(len(adjMat[A])):
        if adjMat[A][i] == 1 and vertex[i] not in visited:
            dfs(vertex[i], visited)

dfs('A')
