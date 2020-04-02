def data_merge(lst,mergeby,initV,func):
    c=[(lst[0][i],initV)[i in mergeby]for i in range(len(lst[0]))]
    for y in mergeby:
       for x in lst:
          c[y]=func(c[y],x[y])
    return c

def GroupBy(lst,index, filterby=lambda x : True):
    c=[]
    i=0
    b=[]
    while i<len(lst):
        if filterby(lst[i]):
            if i<len(lst)-1 and lst[i][index]==lst[i+1][index]:
                b.append(lst[i])
            elif lst[i][index]==lst[i-1][index]:
                b.append(lst[i])
                c.append(b)
                b=[]
            else:
                c.append([lst[i]])
            
        i =i+1
    return c     
        
groups=GroupBy(a,0)
result=[data_merge(x,[1,2,3],0,lambda a,b:a+b)for x in groups]


