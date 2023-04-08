# cook your dish here
for i in range(int(input())):
    t,n,sumN=map(int,input().split())
    
    temp=0
    l=[]
    for i in range(t):
        if(n<=sumN):
            l.append(n)
        else:
            l.append(sumN)
            break
        sumN=sumN-n 
    
    for j in l:
        temp=temp+pow(j,2)
        
    print(temp)