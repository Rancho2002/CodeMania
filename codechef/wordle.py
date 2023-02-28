# cook your dish here
# https://www.codechef.com/submit/WORDLE #![Solved]
a=int(input())

for i in range(a):
    s="AAAAA"
    s=list(s)
    l=input()
    r=input()
    for i in range(5):
        if(l[i]==r[i]):
            s[i]="G"
        else:
            s[i]="B"
    s="".join(s)
    print(s)