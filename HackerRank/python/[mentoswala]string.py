# print(type("{0:d}".format(10)))
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        l=len("{0:b}".format(number))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=l))

print_formatted(17)