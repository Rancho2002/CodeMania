import os
from math import log10

files=os.listdir(".")

files.sort(key=lambda x: os.path.getmtime(x))
# print(files) # list index 0 hold the oldest file
digits=int(log10(len(files)))+1

rename=0

hidden=0
for i in range(len(files)-1):
    if(files[i][0]=="."):
        hidden+=1
        continue

    if "_" in files[i] and files[i][0]!="_":
        index=files[i].find("_")
        isNum=files[index-1]
    
        if(isNum >="0" and isNum<="9"):
            oldName=files[i][index+1:]
        else:
            oldName=files[i]
    else:
        oldName=files[i]


    if(hidden>0):
        print(f"Hidden files lead to non-consecutive renaming. Move or delete files/folder that start with '.' to gain consecutive naming. \nor Want to proceed anyway? ('y'/'Y' or any key to quit)")
        n=input()
        if(n=="y" or n=="Y"):
            newfile_name=f"{str(i+1).zfill(digits)}_{oldName}"
        else:
            print("File renaming cancel.")
            exit(0)

    
    newfile_name=f"{str(i+1).zfill(digits)}_{oldName}"
    # os.rename(oldName,newfile_name)
    # print(newfile_name)
    # print(oldName)
    

