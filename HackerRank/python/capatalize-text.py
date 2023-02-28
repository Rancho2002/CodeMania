'''
test="hello   world  lol"
test=test.split()

for i in range(len(test)):
    test[i]=test[i].capitalize()

print(" ".join(test)) #this is wrong due to mismatching spaces

'''

test="hello   world  lol"


for i in test.split():
    test=test.replace(i,i.capitalize())

print(test)
