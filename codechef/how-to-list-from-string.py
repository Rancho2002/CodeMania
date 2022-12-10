# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=input()
c=list(b.strip())
print(c)
new=[]
for i in range(len(c)):
    if(c.count(c[i])>1):
        new.append(c[i])
        
# print(new)
if(len(new)<3):
    # print("me here 1")
    print(3)
elif(len(new)%3==0):
    # print("me here 2")
    print(len(new))
else:
    # print("me here 3")
    print(len(new)+1)