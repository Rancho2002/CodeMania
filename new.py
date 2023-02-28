import re

string_to_search = "Hi this is me. I love to code. Teaching is my hobby."

# re.search() returns a match object if there is a match anywhere in the string
# pattern = re.compile(r".is")
# pattern = re.compile(r"^Hi")
pattern = re.compile(r"bby.$")
matches = re.finditer(pattern, string_to_search)

l=[]
for match in matches:
    print(match.span(),end=" ")

