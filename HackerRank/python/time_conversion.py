# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
def timeConversion(s):
    indi=s[-2]
    form=s[0:2]
    ans=form + s[2:-2]

    # Write your code here
    if(indi=='A' and form!='12'):
        # print("i returned 1")
        return ans
    elif(indi=='A' and form=='12'):
        # print("i returned 2")
        form=int(form) - 12
        form=str(form)+'0'
        return form + s[2:-2]
    elif(indi=='P' and form!='12'):
        # print("i returned 3")
        form=(int(form)+12)
        form=str(form)
        # print(form)
        return form + s[2:-2]
    elif(indi=='P' and form=='12'):
        # print("i returned 4")
        return ans
print(timeConversion("01:00:00PM"))
