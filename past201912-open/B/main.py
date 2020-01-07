#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: "List[int]"):
    for i in range(1, N):
        if A[i-1] == A[i]:
            print('stay')
        elif A[i-1] < A[i]:
            print('up', abs(A[i]-A[i-1]))
        else:
            print('down', abs(A[i]-A[i-1]))
            
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
