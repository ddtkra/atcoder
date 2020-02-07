#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, H: int, f: "List[int]", t: "List[int]", D: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    f = [int()] * (M)  # type: "List[int]"
    t = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        f[i] = int(next(tokens))
        t[i] = int(next(tokens))
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, H, f, t, D)

if __name__ == '__main__':
    main()
