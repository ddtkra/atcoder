#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(n: int, x: int, h: "List[int]", a: "List[int]", b: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    a = [int()] * (n - 1)  # type: "List[int]"
    b = [int()] * (n - 1)  # type: "List[int]"
    for i in range(n - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(n, x, h, a, b)

if __name__ == '__main__':
    main()
