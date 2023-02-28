string = "The other day I went over there"
string=string.lower()
count = string.count("the")
print(count)

import re

pattern=re.compile(r"the")
matches=re.finditer(pattern,string)
string = "The other day I went over there"
string=string.lower()

l=[]
for match in matches:
    l.append(match.span())
print(l)
print(l[1][0])
#changing to check