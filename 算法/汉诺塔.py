##def AtoC(A,B,C):
##    print(A+"=>"+B)
##    print(A+"=>"+C)
##    print(B+"=>"+C)      
##
##def hanoi(n,f,t,m):
##    if n==1:
##        print("over")
##    else:
##        print(hanoi(hanoi(n-1,),f,t))


# han  表示把n个圆盘从f移到t, 以m为过度
def han(n,f,t,m):
    if n==1:
        print(f + "=>" +t)
    else:
        han(n-1,f,m,t)
        print(f+"=>"+t)
        han(n-1,m,t,f)

han(4,"A","C","B")        
##print(input(han(n,f,t,m)))

       
