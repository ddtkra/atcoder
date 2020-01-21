#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, disk: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    disk = [int(next(tokens)) for _ in range(M - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, M, disk)

if __name__ == '__main__':
    main()
