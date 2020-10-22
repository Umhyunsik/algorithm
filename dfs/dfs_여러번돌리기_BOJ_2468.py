
def dfs(x,y,k):
    count=1
    check[x][y]=True
    for i in range(len(dx)):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and check[nx][ny]==False and maps[nx][ny]>k:
            count+=dfs(nx,ny,k)
    return count

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
maps=[]
for i in range(n):
    maps.append(list(map(int,input().split())))

min_=float('inf')
max_=-1
for i in range(n):
    min_=min(min_,min(maps[i]))
    max_=max(max_,max(maps[i]))
            
max_plant=0
for k in range(min_,max_+1):
    check=[[False]*n for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if maps[i][j]>k and check[i][j]==False:
                dfs(i,j,k)
                count+=1
    max_plant=max(max_plant,count)
                
print(max_plant)
