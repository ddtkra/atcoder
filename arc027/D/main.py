#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(N: int, h: "List[int]", D: int, s: "List[int]", t: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    D = int(next(tokens))  # type: int
    s = [int()] * (D)  # type: "List[int]"
    t = [int()] * (D)  # type: "List[int]"
    for i in range(D):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, h, D, s, t)

if __name__ == '__main__':
    main()
