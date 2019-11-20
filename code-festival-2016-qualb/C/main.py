#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(W: int, H: int, p: "List[int]", q: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(W - 1 - 0 + 1)]  # type: "List[int]"
    q = [int(next(tokens)) for _ in range(H - 1 - 0 + 1)]  # type: "List[int]"
    solve(W, H, p, q)

if __name__ == '__main__':
    main()
