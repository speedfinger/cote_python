#https://school.programmers.co.kr/learn/courses/30/lessons/43163
import sys
from collections import deque

sys.stdin=open("./word_change.txt",'r')

T = int(input())

def link(left,right):
    #print(f"{left}/{right}")
    cnt = 0 
    for idx in range(0,len(left)):

        if left[idx]==right[idx]:
            #print(f"{left[idx]} / {right[idx]} .....")
            cnt+=1

    if cnt==len(left)-1:
        return True
    return False

def solution(begin, target, words):
    answer = 0

    que=deque()
    que.append(begin)
    
    next_que=deque()
    while(que):        
        left=que.popleft()
        if left==target:
            return answer
        
        next_words=words.copy()

        for idx in range(0,len(words)):
            right=words[idx]

            isLinked=link(left,right)
            if isLinked:
                #print(f"linked...{right} with {left}")
                next_que.append(right)
                next_words.remove(right)
        if not que:
            #print(f"next_que!! : {next_que} with {left}")
            que=next_que.copy()
            next_que=deque()
            answer=answer+1

        #print(next_words)
        #print(que)
        
        words=next_words.copy()
        # if not que:
        #     print("que is empty, replace next que...")
        #     print(next_que)
        #     que=next_que
        #     answer=answer+1

            
    answer=0


    return answer


for i in range(0,T):
    begin=input()
    target=input()
    words= list(map(str,input().split(",")))

    # print(f"{begin} / {target}")
    print(f"{begin} / {words}")
    print(solution(begin,target,words))