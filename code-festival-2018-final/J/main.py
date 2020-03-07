#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, S: "List[List[int]]", T: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [[int(next(tokens)) for _ in range(N)] for _ in range(0 - 0 + 1)]  # type: "List[List[int]]"
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, T)

if __name__ == '__main__':
    main()
