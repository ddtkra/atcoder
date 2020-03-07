#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, R: "List[int]", H: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    R = [int()] * (N)  # type: "List[int]"
    H = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        R[i] = int(next(tokens))
        H[i] = int(next(tokens))
    solve(N, R, H)

if __name__ == '__main__':
    main()
