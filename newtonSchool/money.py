# https://my.newtonschool.co/playground/code/tfzuufcxzt0i
init=0
for i in range(int(input())):
    a=input()
    if(a[-3:]=="JPY"):
        init+=float(a[0:-4])
    
    elif(a[-3:]=="BTC"):
        init+=float(a[0:-4])*380000

print(format(init,".8f"))