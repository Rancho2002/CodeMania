import re
# pattern=re.compile(r"is*")
# pattern=re.compile(r"is+")
# pattern=re.compile(r"is{2}")
pattern=re.compile(r"ve+|is{2}")
string="Hi this iss me. I love to code. Teaching is my hobby and love to do."
matches=re.finditer(pattern,string)
for match in matches:
    print(match)



