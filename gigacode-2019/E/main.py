#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

NO = "impossible"  # type: str

def solve(N: int, L: int, V_S: int, D_S: int, X: "List[int]", V: "List[int]", D: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    V_S = int(next(tokens))  # type: int
    D_S = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    V = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        V[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, L, V_S, D_S, X, V, D)

if __name__ == '__main__':
    main()
