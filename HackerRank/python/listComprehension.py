if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                col=[]
                if(i+j+k!=n):
                   col.append(i)
                   col.append(j)
                   col.append(k)
                   l.append(col)
         
    print(l)