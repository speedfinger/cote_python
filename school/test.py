visited = [[0] * 3]*3


graph = []
graph.append([0]*3)
graph.append([0]*3)
graph.append([0]*3)
#graph.append([0,0,0])
#graph.append([0,0,0])


def print_doublearr(arr):
    for i in range(0 , len(arr)):
        print(arr[i])
    print("##########")
    
visited[1][1]=5
graph[1][1]=5
print_doublearr(visited)
print_doublearr(graph)