#https://school.programmers.co.kr/learn/courses/30/lessons/84021
import sys


def show(arr):
    for i in range(0,len(arr)):
        print(arr[i])

def solution(game_board, table):
    answer = -1

    

    return answer

sys.stdin = open("./puzzle.txt",'r')

T = int(input())

for tc_case in range(0,T):
    n,m = map(int,input().split())

    board=[]
    for i in range(0,n):
        board.append(list(map(int,input())))
    table=[]
    for i in range(0,n):
        table.append(list(map(int,input())))
    
    # print("board.......")
    # show(board)
    # print("table.......")
    # show(table)
    solution(board,table)