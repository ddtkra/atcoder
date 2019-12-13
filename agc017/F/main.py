#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (K)  # type: "List[int]"
    B = [int()] * (K)  # type: "List[int]"
    C = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, K, A, B, C)

if __name__ == '__main__':
    main()
