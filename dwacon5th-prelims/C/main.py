#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, S: str, Q: int, k: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    Q = int(next(tokens))  # type: int
    k = [int(next(tokens)) for _ in range(Q - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, S, Q, k)

if __name__ == '__main__':
    main()
