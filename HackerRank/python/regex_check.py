import re
for i in range(int(input())):
    s=input()
    try:
        if(re.compile(s)):
            print(True)
    except:
        print(False)