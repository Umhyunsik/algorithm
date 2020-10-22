

def dfs(x,y,color):
    check[x][y]=True
    count=1
    for i in range(len(dx)):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and maps[nx][ny]==color and check[nx][ny]==False:
            count+=dfs(nx,ny,color)
    return count

def differdfs(x,y,color):
    
    check[x][y]=True
    count=1
    for i in range(len(dx)):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and (maps[nx][ny]=="R" or maps[nx][ny]=="G") and check[nx][ny]==False:
            count+=differdfs(nx,ny,color)
    return count
    
from collections import defaultdict
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n= int(input())
maps=[]
for i in range(n):
    maps.append(list(str(input())))
check=[[False]*n for _ in range(n)]
color_dict=defaultdict(int)
color_dict2=defaultdict(int)
for i in range(n):
    for j in range(n):
        if check[i][j]==False:
            color_dict[maps[i][j]]+=1
            dfs(i,j,maps[i][j])
            
check=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if check[i][j]==False:
            if maps[i][j]=="R" or maps[i][j]=="G":
                color_dict2["R"]+=1
                differdfs(i,j,maps[i][j])

print(sum(color_dict.values()),color_dict2['R']+color_dict['B'])
