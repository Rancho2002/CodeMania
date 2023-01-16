from typing import List

def main():
    # Your code here
    N, K, X = map(int, input().split())
    arr = list(map(int,input().split()))
    
    arr.sort(reverse=True)
    for i in range(N):
        req = arr[i] // X
        if req <= K:
            arr[i] = arr[i] % X
            K -= req
        else:
            if K == 0:
                break
            else:
                arr[i] = arr[i] - (K * X)
                K = 0
    arr.sort(reverse=True)
    ans = 0
    for i in range(K, N):
        ans += arr[i]
    print(ans)

if __name__ == "__main__":
    main()