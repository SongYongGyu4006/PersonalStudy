graph = {
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['D','F'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

def topological_sort(graph) :
    inDeg = {}
    for v in graph : #inDeg에 graph의 노드 저장
        inDeg[v] = 0
    for v in graph : #inDeg 각 노드의 진입차수를 저장
        for u in graph[v]:
            inDeg[u] += 1
    vlist = []
    for v in graph :
        if inDeg[v] == 0 :
            vlist.append(v) #graph 노드의 진입차수가 0이면 vlist에 노드 추가

    while vlist :
        v = vlist.pop() #진입차수가 0인 노드 v에 빼기
        print(v, end=' ')

        for u in graph[v] :
            inDeg[u] -= 1 #연결된 노드의 진입차수 감소
            if inDeg[u] == 0 :
                vlist.append(u) #진입차수가 0이면 vlist에 추가
topological_sort(graph)
