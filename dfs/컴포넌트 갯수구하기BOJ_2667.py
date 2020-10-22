def dfs(x,y):
    check[x][y]=True
    count=1
    for i in range(len(dx)):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and maps[nx][ny]==1 and check[nx][ny]==False:
            count+=dfs(nx,ny)
    return count
            
    
    
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n= int(input())

check=[[False]*n for _ in range(n)]
maps=[]
for i in range(n):
    maps.append([int(i) for i in list(str(input()))])
count=0
q=[]
for i in range(n):
    for j in range(n):
        if maps[i][j]==1 and check[i][j]==False:
            q.append(dfs(i,j))
            count+=1
print(count)
for i in sorted(q):
    print(i)
