l,m=map(int,input().split())
ltree=[1]*(l+1)
count=0
for i in range(m):
    ai,bi=map(int,input().split())
    for j in range(ai,bi+1):
        ltree[j]=0
for i in range(len(ltree)):
    if ltree[i]==1:
        count=count+1
print(count)


    
