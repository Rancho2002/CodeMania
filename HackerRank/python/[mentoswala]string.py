# # print(type("{0:d}".format(10)))
# def print_formatted(number):
#     # your code goes here
#     for i in range(1,number+1):
#         l=len("{0:b}".format(number))
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=l))

# print_formatted(17)

# a=0o3
# b=0o7
# a=int(input(),8)
# print(a+b)

# a=int(input(),2)
# print(a)
# a=0b1010 #a is now in binary
# print(a) # convert a to decimal and print the value

# Taking user input in binary
a=int(input(),2) # valid only 0,1
print(a) # convert 'a' to decimal and print the value

# Declare a value as binary
a=0b10101 # a is now in binary
print(a) # convert 'a' to decimal and print the value

# Addition and so on...
a,b= 0b10, 0b10 #(10)₂ = (2)₁₀
print(a+b) # Answer is 4

# Convert decimal to binary
a= 10
print(bin(a)) # 0b1010, here 0b represents the number in base 'b' i.e binary

