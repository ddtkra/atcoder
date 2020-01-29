#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(n: int, c: int, a: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, c, a)

if __name__ == '__main__':
    main()
