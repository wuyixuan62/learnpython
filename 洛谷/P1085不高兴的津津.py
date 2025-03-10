d=[]
max=-1
pos=0
for i in range(7):
    ai,bi=map(int,input().split())
    ci=ai+bi
    if ci>max:
        max=int(ci)
        pos=i

if max<=8:
    print(0)
else:
    print(pos+1)
