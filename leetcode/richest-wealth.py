l=[]
accounts=[[1,2],[12,34],[3,9]]
for i in range(len(accounts)):
    l.append(sum(accounts[i]))
print(max(l))