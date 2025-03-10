
def YY (a,arr,i):
    if a in arr:
        if arr[i]==a:
            return 2
        else:
            return 1
    else:
        return 0

import random
# c=[0,1,2,3,4,5,6,7,8,9]
# random.shuffle(c)
# c1=c[0:4]
##print(c1)
c1=random.sample([1,2,3,4,5,6,7,8,9,0],4)
print("我选了四个数，你猜一猜")
while True:
    e=[]
    count1=0
    count2=0
    d=list(map(int,list(input("请输入四个数:\n"))))
    if len(d)!=4:
        print("请输入四个数")
        continue
    if len(set(d))!=len(d):
        print("不可重复")
        continue
    for i in range(4):
        f=YY(d[i],c1,i)
        if f==1:
            count1=count1+1
        elif f==2:
            count2=count2+1
        e=e+[f]
    print(count2,"阳",count1,"阴")
    if count2==4:
        print("你赢了")
        break
    
##b=int(input())
##brr=list(map(int,input().split()))
##print(brr)
##print(YY(b, brr,2))
##    
