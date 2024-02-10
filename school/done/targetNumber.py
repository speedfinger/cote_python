#https://school.programmers.co.kr/learn/courses/30/lessons/43165
import os
import sys

HOME = os.environ["HOME"]
manifest_path=os.path.join(HOME,'python-for-coding-test/school/43165_targetNumber.txt')

sys.stdin = open(manifest_path,'r')

answer = 0
def solution(numbers, target,sum):
    global answer
    #print(f'{sum} / {answer}')
    #print(len(numbers))
    #print(f'{numbers} / {sum}')
    if len(numbers) ==1:
        
        if((sum+numbers[0])==target):
            answer+=1            
            #print('aswer hit')
        
        if((sum-numbers[0])==target):
            #print('aswer hit')
            answer+=1
        #print(f'last step / {sum+numbers[0]} / {sum-numbers[0]} / {target} / answer: {answer}')
        
        return answer
    else:
        solution(numbers[1:],target,sum+numbers[0])
        solution(numbers[1:],target,sum-numbers[0])

    return answer


T = int(input())

for test_case in range(1, T + 1):
    line=list(map(int,input().split()))
    target=int(input())
    answer = 0
    #print(line)
    print(solution(line,target,0))
    print("###################")



# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])