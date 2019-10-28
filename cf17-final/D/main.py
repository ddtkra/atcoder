#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, H: "List[int]", P: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        H[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, H, P)

if __name__ == '__main__':
    main()
