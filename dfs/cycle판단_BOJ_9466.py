def dfs(curr):
    global count
    check[curr]=True
    next_=arr[curr]
   # print(next_,"next",curr,"curr")
    if check[next_]==True:
        if not finish[next_]:
            temp=next_
            counts=1
            while temp!=curr:
              #  print(temp,curr)
                temp=arr[temp]
                counts+=1
            count+=counts
    else:
        dfs(next_)
    finish[curr]=True
   
N=int(input())
arr=[0]+list(map(int,input().split()))
check=[True]+[False]*N
finish=[True]+[False]*N
count=0

for i in range(1,N+1):
    if check[i]==False:
        dfs(i)
print(N-count)
