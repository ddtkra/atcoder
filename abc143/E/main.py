#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)


def solve(N: int, M: int, L: int, A: "List[int]", B: "List[int]", C: "List[int]", Q: int, s: "List[int]", t: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    s = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, M, L, A, B, C, Q, s, t)

if __name__ == '__main__':
    main()
