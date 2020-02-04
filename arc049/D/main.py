#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, Q: int, t: "List[int]", a: "List[int]", b: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    t = [int()] * (Q)  # type: "List[int]"
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        t[i] = int(next(tokens))
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, Q, t, a, b)

if __name__ == '__main__':
    main()
