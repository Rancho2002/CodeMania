if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        s=input()
        if(s=="print"):
            print(l)
        else: 
            a=int(input())
            b=int(input())
            if(s=="insert"):
                l.insert(a)
                l.insert(b)
            if(s=="remove"):
                l.remove(a)
                l.remove(b)
            if(s=="sort"):
                l.sort()
            if(s=="append"):
                l.append(a)
                l.append(b)
            
        
        