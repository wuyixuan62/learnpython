##def fabonacci(n):
##    if n==1 or n==2:
##        return 1
##    else:
##        return fabonacci(n-1)+fabonacci(n-2)
##while True:
##    n=int(input("位数"))
##    print(fabonacci(n))

##def hanoi(n1,n2,f,t,m):
##    if n1==n2:
##        print(n1,"%s=>%s"%(f,t))
##    else:
##        hanoi(n1,n2-1,f,m,t)
##        print(n2,"%s=>%s"%(f,t))
##        hanoi(n1,n2-1,m,t,f)
##while True:
##    n1,n2=list(map(int,input("请输入n1,n2").split()))
##    hanoi(n1,n2,"A","C","B")


def route(x,y):
    if x==0 or y==0:
        return 1
    else:
        return route(x-1,y)+route(x,y-1)

while True:
    a,b=list(map(int,input().split()))
    print(route(a,b))
        
