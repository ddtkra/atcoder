#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(T: "List[int]", A: "List[int]", B: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    A = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    solve(T, A, B)

if __name__ == '__main__':
    main()
