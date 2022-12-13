# https://my.newtonschool.co/playground/code/ivfg9mx69lbk
# Your code here
family=int(input())
l=list(map(int,input().split()))
for i in range(1,family+1):
    print(l.count(i))