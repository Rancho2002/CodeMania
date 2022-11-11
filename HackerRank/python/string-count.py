def count_substring(string, sub_string):
    c=[]
    for i in range(0,len(string)):
        c.append(string[i:len(sub_string)+i])
    return c.count(sub_string)

count_substring("ABCDCDC","CDC")




