# cook your dish here
a=int(input())
for i in range(a):
    count=0
    limit=int(input())
    for i in range(limit):
        for j in range(limit):
            if((i+j)%2 !=0):
               count+=1
    print(count)
