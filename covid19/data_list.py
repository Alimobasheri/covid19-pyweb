def dataMerge(lst,mergeBy,initV,func):
    c=[(lst[0][i],initV)[i in mergeBy]for i in range(len(lst[0]))]
    for y in mergeBy:
       for x in lst:
          c[y]=func(c[y],x[y])
    return c

def groupBy(lst,index, filterBy=lambda x : True):
    c=[]
    i=0
    b=[]
    while i<len(lst):
        if filterBy(lst[i]):
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
        


