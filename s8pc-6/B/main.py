#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    from bisect import bisect_left, bisect_right
    
    A.sort()
    B.sort()
    ans = 0
    x = A[N//2]
    y = B[N//2]
    for i in range(N):
        ans += y-x
        if A[i] < x:
            ans += 2*(x-A[i])
        if B[i] > y:
            ans += 2*(B[i]-y)

    print(ans)
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]" 
    B = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
