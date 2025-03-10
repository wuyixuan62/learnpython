a=input()
b=input()
d=[]
a=a.split()
b=int(b)+30
for i in range(10):
    c=int(a[i])
    if c<=b:
        d=d+[c]
print(len(d))
