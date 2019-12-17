#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(N: int, X: int, Y: int, c: "List[int]", w: "List[int]"):
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
    c = [int()] * (N)  # type: "List[int]"
    w = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        c[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, X, Y, c, w)

if __name__ == '__main__':
    main()
