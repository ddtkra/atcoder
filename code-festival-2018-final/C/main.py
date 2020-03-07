#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: "List[int]", B: "List[int]", M: int, T: "List[int]"):
    return



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
    M = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, A, B, M, T)

if __name__ == '__main__':
    main()
