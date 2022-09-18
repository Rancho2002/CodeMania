# cook your dish here
a=int(input())
for i in range(a):
    b,c,d,e=map(int,input().split())
    alice=c/b #0.3
    bob=e/d #0.25
    if(bob>alice):
        print("Alice")
    elif(bob==alice):
        print("Equal")
    else:
        print("Bob")