#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, Q: int, A: "List[int]", B: "List[int]", S: int, s: "List[int]", t: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    S = int(next(tokens))  # type: int
    s = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, Q, A, B, S, s, t)

if __name__ == '__main__':
    main()
