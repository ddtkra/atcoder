#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, p: "List[int]", a: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    a = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, p, a)

if __name__ == '__main__':
    main()
