#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, a: "List[int]", b: "List[int]", Q: int, v: "List[int]", d: "List[int]", c: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    v = [int()] * (Q)  # type: "List[int]"
    d = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        v[i] = int(next(tokens))
        d[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, a, b, Q, v, d, c)

if __name__ == '__main__':
    main()
