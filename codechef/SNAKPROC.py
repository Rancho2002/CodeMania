# https://www.codechef.com/submit/SNAKPROC
for i in range(int(input())):
    a=int(input())
    b=input()
    b=b.replace(".","")
    b=b.replace("HT","")
    if(len(b)==0):
        print("Valid")
    else:
        print("Invalid")