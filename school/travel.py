#https://school.programmers.co.kr/learn/courses/30/lessons/43164
import sys

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

def solution_bk(tickets):
    answer = []

    #print(len(tickets))

    start=[]
    ticket_map={}
    for idx in range(0,len(tickets)):
        #ticket_map[tickets[idx][0]]=tickets[idx][1]
        ticket_map[tickets[idx][0]]=[]


    for idx in range(0,len(tickets)):
        #ticket_map[tickets[idx][0]]=tickets[idx][1]
        arry=ticket_map[tickets[idx][0]]
        arry.append(tickets[idx][1])
    
    
    
    # print(start)
    # start_sort=sorted(start)
    # print(start_sort)
    #print(ticket_map)

    stack=[]
    stack.append("ICN")
    
    while(len(stack)>0):
        city=stack.pop()

        # print(ticket_map)
        answer.append(city)

        if city not in ticket_map:
            break

        if len(ticket_map[city]) >0 :

            destinations = sorted(ticket_map[city])
            stack.append(destinations[0])
            #del destinations[0]
            ticket_map[city]=destinations
            del ticket_map[city][0]

        

    print(answer)

        



    # for key in ticket_map.keys():
    #     print(ticket_map[key])
    

    return answer

def solution(tickets):

    answer = 0

    

    return answer

for tc_case in range(0,T):
    read_line=int(input())

    tickets=[]
    for line in range(0,read_line):
        ticket=list(map(str,input().split(",")))
        tickets.append(ticket)
    
    solution(tickets)