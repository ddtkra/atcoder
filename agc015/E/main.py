#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(N: int, X: "List[int]", V: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    V = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, X, V)

if __name__ == '__main__':
    main()
