#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (M)  # type: "List[int]"
    D = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, A, B, C, D)

if __name__ == '__main__':
    main()