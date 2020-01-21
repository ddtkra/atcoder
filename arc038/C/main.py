#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, C: "List[int]", A: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N - 1)  # type: "List[int]"
    A = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        C[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, C, A)

if __name__ == '__main__':
    main()
