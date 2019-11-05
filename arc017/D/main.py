#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]", M: int, t: "List[int]", l: "List[int]", r: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    t = [int()] * (M)  # type: "List[int]"
    l = [int()] * (M)  # type: "List[int]"
    r = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        t[i] = int(next(tokens))
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, a, M, t, l, r)

if __name__ == '__main__':
    main()
