#https://school.programmers.co.kr/learn/courses/30/lessons/43162
import sys
from collections import deque

sys.stdin = open("./network.txt","r")


T = int(input())

def show(arr):
    for i in range(0,len(arr)):
        print(arr[i])



def solution(n, computers):
    answer = 0

    visited=[False]*n
    visit_chk=[]


    que=deque()  
    

    while(len(visit_chk)<n):
        for index in range(0,len(visited)):
            if visited[index]==0:
                answer=answer+1
                que.append(index)


            while(que):
                x=que.popleft()
                #print(f"que..{x}")
                visit_chk.append(x)
                visited[x]=True

                for i in range(0,n):
                    if computers[x][i]==1 and visited[i]==False:
                        que.append(i)
                # print(que)


            # print("visited....")
            # print(visited)
            # print(visit_chk)
            
    return answer

for tc_case in range(0,T):
    computerNumber=int(input())

    maps=[]
    for i in range(0,computerNumber):        
        maps.append(list(map(int,input())))
    #print(f"tc ..{tc_case}")
    show(maps)
    print(f"tc..{tc_case} : {solution(computerNumber,maps)}")
