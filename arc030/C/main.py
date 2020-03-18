#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(n: int, m: int, k: int, c: "List[str]", a: "List[int]", b: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    c = [next(tokens) for _ in range(n)]  # type: "List[str]"
    a = [int()] * (m)  # type: "List[int]"
    b = [int()] * (m)  # type: "List[int]"
    for i in range(m):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(n, m, k, c, a, b)

if __name__ == '__main__':
    main()
