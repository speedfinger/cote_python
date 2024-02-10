from collections import defaultdict 
import sys

sys.stdin=open('./travel.txt','r')

T = int(input())

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer



for tc_case in range(0,T):
    read_line=int(input())

    tickets=[]
    for line in range(0,read_line):
        ticket=list(map(str,input().split(",")))
        tickets.append(ticket)
    
    solution(tickets)