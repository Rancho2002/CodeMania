num,length=4,5
num=str(num)
len1=len(str(num))
if(len1!=length):
    num="0"*abs(length-len1)+num
print(num)

num=str(num)
print(num.zfill(length))
