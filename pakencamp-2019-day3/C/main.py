#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, A: "List[List[int]]"):

    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            tans = 0
            for k in range(N):
                tans += max(A[k][i], A[k][j])

            ans = max(ans, tans)

    print(ans)
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(M)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
