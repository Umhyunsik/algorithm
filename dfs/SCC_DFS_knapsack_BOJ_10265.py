def scc(x):
    global id_
    id_+=1
    stack.append(x)
    d[x]=id_
    parent=d[x]
    #print(id_,d)
    for i in a[x]:
        if d[i]==0:
            parent=min(parent,scc(i))
        elif finished[i]==False:
            parent=min(d[i],parent)
            
    if parent==d[x]:
        t=[]
        while True:
            tmp=stack.pop()
            t.append(tmp)
            home[d[x]].append(tmp)
            
            finished[tmp]=True
            if tmp==x:
                break
        SCC.append(t)
        
    return parent
def dfs(now):
    tmp=1
    if visited[now]==True:
        return 0
    visited[now]=True
    for i in rev_a[now]:
       # print(now,i)
        tmp+=dfs(i)
    return tmp
    
    

stack=[]
SCC=[]
id_=0
itemlist=[]
N,K=map(int,input().split())
finished=[False]*(N+1)
visited=[False]*(N+1)
d=[0]*(N+1)

arr=[0]+list(map(int,input().split()))
a=[[] for _ in range(N+1)]
from collections import defaultdict
home=defaultdict(list)
countlist=[0]*(N+1)
rev_a=[[] for _ in range(N+1)]
for i in range(1,N+1):
    a[i].append(arr[i])
    rev_a[arr[i]].append(i)
stack=[]

for i in range(1,N+1):
    if d[i]==0:
        scc(i)

visited=[False]*(N+1)
min_max=[[0,0]]

for i in SCC:
    root=i[-1]
    min_component_length=len(i)
    if visited[root]==False:
        min_max.append([min_component_length,dfs(root)])


dp = [[0 for j in range(0, K+1)] for i in range(0, len(min_max))]
for i in range(1,len(min_max)):
    for j in range(K+1):
        dp[i][j]=dp[i-1][j]
        for w in range(min_max[i][0],min_max[i][1]+1):
            if j-w>=0:
                dp[i][j]=max(dp[i][j],dp[i-1][j-w]+w)

                
print(dp[-1][-1])

