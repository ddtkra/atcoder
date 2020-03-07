#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, A: "List[int]", B: "List[int]", D: "List[int]", S: "List[int]", E: "List[int]", C: "List[int]", X: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    D = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        D[i] = int(next(tokens))
    S = [int()] * (M)  # type: "List[int]"
    E = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    X = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        S[i] = int(next(tokens))
        E[i] = int(next(tokens))
        C[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, M, A, B, D, S, E, C, X)

if __name__ == '__main__':
    main()
