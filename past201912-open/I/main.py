#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, S: "List[str]", C: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [str()] * (M)  # type: "List[str]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        S[i] = next(tokens)
        C[i] = int(next(tokens))
    solve(N, M, S, C)

if __name__ == '__main__':
    main()
