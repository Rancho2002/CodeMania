def finLength(N, color, radius):
    st = []
    for i in range(N):
        if st and st[-1] == (color[i], radius[i]):
            print("st, st[-1] ",st,st[-1])
            st.pop()
        else:
            st.append((color[i], radius[i]))
    return len(st)

print(finLength(3,[2,5,2],[3,4,3]))

# https://practice.geeksforgeeks.org/problems/546ea68f97be7283a04ddcc8057e09b46a686471/1