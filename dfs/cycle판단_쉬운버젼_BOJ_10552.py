def dfs(p):
    global count
    count+=1
    visited[p]=True
    if len(edge[p])>0:
        next_=edge[p][0]
        if visited[next_]==True:
            return False
        else:
            return dfs(next_)
            
            
    
        
    else:
        return True
count=0
n,m,p=map(int,input().split())
visited=[False]*(m+1)
finish=[False]*(m+1)
q=[]
from collections import defaultdict
edge=defaultdict(list)
for i in range(n):
    fav,hate=map(int,input().split())
    #print(fav,hate)
    edge[hate].append(fav)
#print(edge)
if dfs(p):
    print(count-1)
else:
    print(-1)
