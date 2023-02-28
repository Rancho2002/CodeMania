# Your code here
# This question says I have to give N and in the output I have to calculate how many possible M such that M*d(M)=N, where d(M) is sum of digit, that mean I N=36 then the possiblities are 2 i.e 6 because d(6)=6*6 =36 and 12 because d(12)=3 and 12*3=36
def sumDigit(n):
     
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)

for i in range(int(input())):
    count=0
    a=int(input())
    l=[]
    for j in range(1,a+1):
        if(a%j==0):
            l.append(j)
    for j in range(len(l)):
        if(l[j]*sumDigit(l[j])==a):
            count+=1
    print(count)

#! Runtime Error :(