#!/usr/bin/env python3
import sys


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    lm = max(L)
    rm = min(R)
    print(max(0,rm-lm+1))

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]" 
    R = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, L, R)

if __name__ == '__main__':
    main()