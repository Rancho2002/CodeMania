# Your code here : https://my.newtonschool.co/playground/code/avn11386h0s9
dt=input().split("/")
yr,mon,day=int(dt[0]),int(dt[1]),int(dt[2])

if(yr>=2022):
    if(yr==2022):
        if(mon>=6):
            if(mon==6):
                if(day>=20):
                    print("After")
                else:
                    print("Before")
            else:
                print("After")
        else:
            print("Before")
    else:
        print("After")
else:
    print("Before")