# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a,b=input().split()
    try:
        a,b=int(a),int(b)
        print(a//b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:",v)