def lookAndSequence(n):
    if n == 1:
        return "1"
    s = "1"  # Initialize the sequence with "1"
    for _ in range(1, n):
        ans = ""
        x = 0
        while x < len(s):
            cnt = 1
            for i in range(x, len(s) - 1):
                if s[i] != s[i + 1]:
                    break
                cnt += 1
            ans += str(cnt) + s[x]
            x += cnt
        s = ans
    return s

# Test the function
print(lookAndSequence(5))  # Generate the sequence up to the 5th term
