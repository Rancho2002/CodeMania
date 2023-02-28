# https://www.codechef.com/submit/SUMNEQ
# cook your dish here
a=int(input())
count=0
for i in range(a):
    for j in range(a):
        if(i+j==a):
            count+=1
print(count)