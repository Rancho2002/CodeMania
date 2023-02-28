def DecimalToOctal(n):
    s=""
    while(n>0):
        s+=str(n%8)
        n=n//8
    s=s[::-1]
    return int(s)

def DecimalToHexa(n):
    s=""
    while(n>0):
        toAdd=n%16
        match toAdd:
            case 10: toAdd="A"
            case 11: toAdd="B"
            case 12: toAdd="C"
            case 13: toAdd="D"
            case 14: toAdd="E"
            case 15: toAdd="F" 
        s+=str(toAdd)
        n=n//16
    s=s[::-1]
    return (s)

def DecimalToBin(n):
    s=""
    while(n>0):
        s+=str(n%2)
        n=n//2
    s=s[::-1]
    return int(s)
        

# print(DecimalToOctal(1))
# print(DecimalToHexa(1))
# print(DecimalToBin(1))

#! WTF code below
for i in range(11):
    print("{0:4d}".format(i))
print('{0:x}'.format(10))

# if(toAdd==10): toAdd="A"
# elif(toAdd==11): toAdd="B"
# elif(toAdd==12): toAdd="C"
# elif(toAdd==13): toAdd="D"
# elif(toAdd==14): toAdd="E"
# elif(toAdd==15): toAdd="F"
