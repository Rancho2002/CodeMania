def stringReverse(S: str) -> str:
    S = bytearray(S, 'utf-8')
    s = 0
    e = len(S) - 1
    
    while s < e:
        S[s], S[e] = S[e], S[s]
        s += 1
        e -= 1
    
    return S.decode('utf-8')

input_string = "hello"
reversed_string = stringReverse(input_string)
print(reversed_string)  # Output: "olleh"
