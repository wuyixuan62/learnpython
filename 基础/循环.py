n=int(input())
m=0
while True:
    s=2**m
    if 2**m>=n:
        break
    m=m+2
print(m-2)
