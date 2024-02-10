import sys
import ast
from collections import deque

#https://school.programmers.co.kr/learn/courses/30/lessons/1844
#keypoint
# arr 초기화시
#visited = [[0] * col] * row 
# 위 방법으로 하면, visited[i][j]=value 로 바꾸면 visited[*][j] 가 다 바껴버림
#=> 아래방법으로 ...
    # visited =[]
    # for r in range(1,row+1):
    #     visited.append([0]*col)

#

#sys.stdin = open("./shortest_1844.txt",'r')
sys.stdin = open("./shortest_1844copy.txt",'r')

T = int(input())

def print_doublearr(arr):
    for i in range(0 , len(arr)):
        print(arr[i])
    print("##########")
    
    

def solution(maps):
    answer = -1


    row = len(maps)
    col = len(maps[0])
    print(f"row / col : {row} / {col}")

    #visited = [[0] * col] * row
    visited =[]
    for r in range(1,row+1):
        visited.append([0]*col)

    # print_doublearr(maps)

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    que=deque()
    que.append([0,0])

    while(que):
        x,y=que.popleft()
        #print(f"x/y : {x} / {y}")
        for i in range(0,4):
            
            cx=x+dx[i]
            cy=y+dy[i]

            
            if (cx<0 or cy<0 or cx>=row or cy>=col):
                continue
            # print(f"cx/cy : {cx} / {cy}")
            # print_doublearr(visited)

            if visited[cx][cy] == 0 and maps[cx][cy]!=0:
                # print(f"{cx}/{cy} enterd..{visited[cx][cy]}")
                que.append([cx,cy])
                visited[cx][cy] = 1
                # print_doublearr(visited)
                #print(f"value..:{maps[cx][cy]}/{maps[x][y]}")
                maps[cx][cy]=maps[x][y]+1
                #print(maps)
        # print(que)
        # print("map.........")
        # print_doublearr(maps)

        # 1,0,1,1,1
        # 1,0,1,0,1
        # 1,0,1,1,1
        # 1,1,1,0,1
        # 0,0,0,0,1
    print_doublearr(maps)
    print("visited....")
    print_doublearr(visited)
    if maps[row-1][col-1]>1:
        answer=maps[row-1][col-1]




    return answer


for test_case in range(1, T+1):
    # tc_map = input()
    # tc_map_chage=ast.literal_eval(tc_map)
    # solution(tc_map_chage)
    
    n, m = map(int, input().split())
    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    for i in range(0,n):
        graph.append(list(map(int, input())))
    print_doublearr(graph)        
    print(solution(graph))