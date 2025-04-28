vertex = {"A" : {'B','D','E'}
          ,'B' : {'C','E','F'}
          ,'C' : {'G'}
          ,'D' : {'E'}
          ,'E' : {}
          ,'F' : {'G'}
          ,'G' : {}
          }

#def topological_dfs(graph):
#    inDeg = {}
#    for v in graph:
#        inDeg[v] = 0
#    for v in graph:
#        for u in graph[v]:
#            inDeg[u] += 1
#    vlist = []
#    for v in graph :
#        if inDeg[v] == 0 :
#            vlist.append(v)
#   while vlist :
#        v = vlist.pop()
#        print(v, end=' ')
#       for u in graph[v]:
#            inDeg[u] -= 1
#           if inDeg[u] == 0:
#                vlist.append(u)

def topological_dfs(graph):
    inDeg = {}
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1
    vlist = []
    for v in graph:
        if inDeg[v] == 0:
            vlist.append(v)
    while vlist:
        v = vlist.pop()
        print(v,end=' ')
        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vlist.append(u)
topological_dfs(vertex)
        
        
