# a=[]

def route(x,y):
    if x==0 and y==0:
        a=[[(0,0)]]
        return a
    else:
        e3=[]
        f3=[]
        if x>0:
            e1=route(x-1,y)
            
            for i in range(len(e1)):
                e2=e1[i]
                e2.insert(0,(x,y))
                e3.append(e2)
            
        
        if y>0:
            f1=route(x,y-1)
            
            for j in range(len(f1)):
                f2=f1[j]            
                f2.insert(0,(x,y))
                f3.append(f2)
        return e3+f3
            
    # elif x>0 and y>0:
    #     c=(x,y)+route(x-1,y)
    #     d=(x,y)+route(x,y-1)
    #     return [c,d]
    #     a.append(c)
    #     a.append(d)


a=list(map(int,list(input())))
r = route(a[0],a[1])
for b in r:
    print(b)


