#https://school.programmers.co.kr/learn/courses/30/lessons/43164
import sys
import copy

sys.stdin=open('./travel.txt','r')

T = int(input())

# https://leetcode.com/problems/reconstruct-itinerary/submissions/1169435981/
# Input
# tickets =
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

# Use Testcase
# Output
# ["JFK","KUL"]
# Expected
# ["JFK","NRT","JFK","KUL"]


def dfs(answer,ticket_map,start,N):

    # print(f"len chk : {len(answer)} / {N}")

    if len(answer) == N+1:
        return answer

    arr=ticket_map.get(start)

    # print(arr)
    
    if arr :
        # print("entered...")
        
        tmp_ticket_map=copy.deepcopy(ticket_map)
    
        for next in range(0,len(arr)):
            ret=answer.copy()
            # print(arr[next])
            ret.append(arr[next])

            res_ticket_map=copy.deepcopy(tmp_ticket_map)
            del res_ticket_map.get(start)[next]

            # print(f"key : {arr[next]} / {arr}")
            # print(f"{arr[next]} / {res_ticket_map}")
            # print(ticket_map)
            res = dfs(ret,res_ticket_map,arr[next],N)
            if res:
                return res

def solution(tickets):
    answer = []

    #print(len(tickets))

    ticket_map={}
    for idx in range(0,len(tickets)):
        #ticket_map[tickets[idx][0]]=tickets[idx][1]
        ticket_map[tickets[idx][0]]=[]

    for idx in range(0,len(tickets)):
        #ticket_map[tickets[idx][0]]=tickets[idx][1]
        arry=ticket_map[tickets[idx][0]]
        arry.append(tickets[idx][1])

    # print(ticket_map)

    visited={}
    for key in ticket_map.keys():
        #print(f"??? : {ticket_map[key]}")
        arr=ticket_map[key]
        ticket_map[key]=sorted(arr)
        visited[key]=0
    
    #print(visited)
    stack=[]
    stack.append("ICN")

    #return dfs(stack,ticket_map,"ICN",len(tickets),visited)
    return dfs(stack,ticket_map,"ICN",len(tickets))

    return answer


for tc_case in range(0,T):
    read_line=int(input())

    tickets=[]
    for line in range(0,read_line):
        ticket=list(map(str,input().split(",")))
        tickets.append(ticket)
    
    print(f"sol : {solution(tickets)}")