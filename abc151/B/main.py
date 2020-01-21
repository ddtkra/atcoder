#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int, M: int, A: "List[int]"):
    s = sum([M-A[i] for i in range(N-1)])
    if s >= 0 and s+M > K:
        print(-1)
    else:
        print(max(0, s+M))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, K, M, A)

if __name__ == '__main__':
    main()
