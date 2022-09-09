# cook your dish here
total=int(input())
st=0
lt=0
for i in range(total):
    int(input())
    l=list(input().split())
    print(l)
    for i in range(len(l)):
        if("START38" in l[i]):
            st+=1 
        elif("LTIME108" in l[i]):
            lt+=1
    l=[]
    print(st,lt)
    st=0 
    lt=0
            