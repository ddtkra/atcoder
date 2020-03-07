#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, X: int, Y: int, Z: int, A: "List[int]", B: "List[int]"):
    ans = 0
    for i in range(N):
        if A[i] >= X and B[i] >= Y and A[i]+B[i] >= Z:
            ans += 1

    print(ans)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, X, Y, Z, A, B)

if __name__ == '__main__':
    main()
