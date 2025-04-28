import queue

def bfs(graph, start):
    visited = { start }
    que = queue.Queue()
    que.put(start)

    while not que.empty():
        v = que.get()
        print(v, end=' ')
        nbr = set(graph[v]) - visited  # 집합 사용해 미방문 노드 찾기
        for u in nbr:
            visited.add(u)
            que.put(u)

# 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # BFS 실행
