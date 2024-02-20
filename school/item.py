import sys
from collections import deque


sys.stdin = open('./item.txt','r')

def map_print(maps):

    # x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

    for idx in range(0,20):
        print(f"{19-idx}\t:{maps[19-idx][:20]}")
    # print(x)

def bfs(maps, characterX, characterY, item_x, item_y,dis):

    
    
    map_size=len(maps)

    # 좌 하 상 우
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]

    que=deque()
    que.append([characterX,characterY])

    while(que):

        x,y=que.popleft()

        
    
        if x==item_x and y==item_y:
            # print("reached!!!")
            break

    

        for i in range(0,4):        

            mx=x+dx[i]
            my=y+dy[i]
            if (mx<0 or mx>map_size):
                break        
            if (my<0 or my>map_size):
                break

            

            if maps[my][mx]==1:
                # print(f"{x},{y} => {mx}, {my}  /// {maps[y][x]}")
                #print(f"{characterX},{characterY} => {mx}, {my}  /// {dis}")
                maps[my][mx]=maps[y][x]+0.5
                que.append([mx,my])

    # map_print(maps)
    return maps[item_y][item_x]

def dfs(maps, characterX, characterY, item_x, item_y,dis):

    print(f"{characterX},{characterY} => {item_x}, {item_y}  /// {dis}")
    
    if characterX==item_x and characterY==item_y:
        print("??????????????")
        return dis
    
    map_size=len(maps)

    # 좌 하 상 우
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]

    

    for i in range(0,4):        

        mx=characterX+dx[i]
        my=characterY+dy[i]
        if (mx<0 or mx>map_size):
            break        
        if (my<0 or my>map_size):
            break

        

        if maps[my][mx]==1:
            #print(f"{characterX},{characterY} => {mx}, {my}  /// {dis}")
            maps[my][mx]=0
            dfs(maps,mx,my,item_x,item_y,dis+0.5)


    return dis

def solution(rectangle, characterX, characterY, itemX, itemY):
    

    multiple=2

    maps=[]
    for idx in range(0,50*multiple):
        map = [0]*50*multiple
        maps.append(map)

    #map_print(maps)
    
    #map_print(rectangle)

    # map_print(maps)
        
    for idx in range(0,len(rectangle)):
        #print(rectangle[x])
        x1=rectangle[idx][0]*multiple
        x2=rectangle[idx][2]*multiple
        y1=rectangle[idx][1]*multiple
        y2=rectangle[idx][3]*multiple
        # print(f"{x1}~{x2}, {y1}~{y2}")

    for x in range(0,50*multiple):
        for y in range(0,50*multiple):
            cnt=0
            x_hit=0
            y_hit=0
            is_line=0
            

            for idx in range(0,len(rectangle)):
                #print(rectangle[x])
                x1=rectangle[idx][0]*multiple
                x2=rectangle[idx][2]*multiple
                y1=rectangle[idx][1]*multiple
                y2=rectangle[idx][3]*multiple
                #print(f"{x1}~{x2}, {y1}~{y2}")
                if x>x1 and x<x2 and y>y1 and y<y2 :
                    cnt=cnt+1
                    #print(f"x:{x}/{x1}~{x2} y:{y}/{y1}~{y2}")
                if (x==x1 or x==x2) and (y>=y1 and y<=y2):
                    is_line=is_line+1

                    # if x==6 and y==4 :
                    #     print(f"x,x1,x2:{x},{x1},{x2} / y,y1,y2:{y},{y1},{y2}")
                    
                if (y==y1 or y==y2) and (x>=x1 and x<=x2):
                    is_line=is_line+1
                    # if x==6 and y==4 :
                    #     print(f"x,x1,x2:{x},{x1},{x2} / y,y1,y2:{y},{y1},{y2}")

            
            #if (cnt==1 and is_line>=1) or (cnt>1 and is_line==2):
            #if (cnt==1 and is_line>=1):
            if is_line>=1 and cnt<1:
                maps[y][x]=1
            # if x==6 and y==4 :
            #     print(f"why>>{cnt} / {is_line} / map value : {maps[y][x]}")
                

    # map_print(maps)
    
    # print(f"x,y,itemx,itemy : {characterX*multiple},{characterY*multiple},{itemX*multiple},{itemY*multiple}")

    #return dfs(maps, characterX*multiple, characterY*multiple, itemX*multiple, itemY*multiple,0)
    return int(bfs(maps, characterX*multiple, characterY*multiple, itemX*multiple, itemY*multiple,0)-1)


def solution_bk(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    multiple=2

    maps=[]
    for idx in range(0,50*multiple):
        map = [0]*50*multiple
        maps.append(map)

    #map_print(maps)
    
    #map_print(rectangle)

    # map_print(maps)
        
    for idx in range(0,len(rectangle)):
        #print(rectangle[x])
        x1=rectangle[idx][0]*multiple
        x2=rectangle[idx][2]*multiple
        y1=rectangle[idx][1]*multiple
        y2=rectangle[idx][3]*multiple
        print(f"{x1}~{x2}, {y1}~{y2}")

    for x in range(0,50*multiple):
        for y in range(0,50*multiple):
            cnt=0
            x_hit=0
            y_hit=0
            is_line=0
            

            for idx in range(0,len(rectangle)):
                #print(rectangle[x])
                x1=rectangle[idx][0]*multiple
                x2=rectangle[idx][2]*multiple
                y1=rectangle[idx][1]*multiple
                y2=rectangle[idx][3]*multiple
                #print(f"{x1}~{x2}, {y1}~{y2}")
                if x>=x1 and x<=x2 and y>=y1 and y<=y2 :
                    cnt=cnt+1
                    #print(f"x:{x}/{x1}~{x2} y:{y}/{y1}~{y2}")
                if (x==x1 or x==x2) and (y>=y1 and y<=y2):
                    is_line=is_line+1

                    if x==6 and y==4 :
                        print(f"x,x1,x2:{x},{x1},{x2} / y,y1,y2:{y},{y1},{y2}")
                    
                if (y==y1 or y==y2) and (x>=x1 and x<=x2):
                    is_line=is_line+1
                    if x==6 and y==4 :
                        print(f"x,x1,x2:{x},{x1},{x2} / y,y1,y2:{y},{y1},{y2}")

            
            #if (cnt==1 and is_line>=1) or (cnt>1 and is_line==2):
            if (cnt==1 and is_line>=1):
                maps[y][x]=1
            if x==6 and y==4 :
                print(f"why>>{cnt} / {is_line} / map value : {maps[y][x]}")
                

    map_print(maps)

    return answer

T = int(input())

for tc_case in range(0,T):
    box_case = int(input())

    box_arr=[]
    for idx in range(0,box_case):        
        box_arr.append(list(map(int,input().split(','))))
    chr_x,chr_y,item_x,item_y = map(int,input().split())
    # print(box_arr)
    #print(f"{chr_x} / {chr_y} / {item_x} / {item_y}")

    print(f"tc_case : {tc_case} : {solution(box_arr,chr_x,chr_y,item_x,item_y)}")


