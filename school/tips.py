import sys

sys.stdin = open('./tips.txt','r')
# 2
# 3
# 110
# 110
# 001
# 3
# 110
# 111
# 011
T = int(input())

for tc_case in range(0,T):
    row = int(input())
    maps=[]
    for r in range(0,row):
        maps.append(list(map(int,input()))) #공백이 없을때, input().split() 이 아님
    
    print(maps)
        
# arr 초기화시
#visited = [[0] * col] * row 
# 위 방법으로 하면, visited[i][j]=value 로 바꾸면 visited[*][j] 가 다 바껴버림
#=> 아래방법으로 ...
    # visited =[]
    # for r in range(1,row+1):
    #     visited.append([0]*col)

#deep copy
import copy
ticket_map = [] # 이중 arry
tmp_ticket_map=copy.deepcopy(ticket_map)

answer=[] # 단일 arry
ret=answer.copy()

#ICN,KUL
#ICN,NRT
#NRT,ICN
# to -> {"ICN":[KUL,NRT],"NRT":[ICN]}
ticket_map={}
for idx in range(0,len(tickets)):
    #ticket_map[tickets[idx][0]]=tickets[idx][1]
    ticket_map[tickets[idx][0]]=[]

for idx in range(0,len(tickets)):
    #ticket_map[tickets[idx][0]]=tickets[idx][1]
    arry=ticket_map[tickets[idx][0]]
    arry.append(tickets[idx][1])

for key in ticket_map.keys():
    arr=ticket_map[key]
    ticket_map[key]=sorted(arr)  #!!!!!!!!중요 sorted(arr)

#GET dictonary element
res_ticket_map.get(start)
#delete dictionary element
del res_ticket_map.get(start)[idx]


from collections import defaultdict
graph = defaultdict(list)
for ticket in tickets:
    graph[ticket[0]].append(ticket[1])
    graph[ticket[0]].sort()

#{"ICN":[KUL,NRT],"NRT":[ICN]}
key="ICN"
for idx, country in enumerate(graph[key]):
    (0, 'KUL')
    (1, 'NRT')