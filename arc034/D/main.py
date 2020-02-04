#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int, C: int, a: "List[int]", b: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    solve(A, B, C, a, b)

if __name__ == '__main__':
    main()
