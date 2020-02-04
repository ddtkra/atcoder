#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: "List[List[int]]"):
    N = len(A)
    for i in range(N):
        for j in range(N):
            for x, y in [[-1,0], [0, -1], [1, 0], [0, 1]]:
                if 0 <= i+x < N and 0 <= j+y < N and A[i][j] == A[i+x][j+y]:
                    print('CONTINUE')
                    exit()
    
    print('GAMEOVER')

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(4)] for _ in range(4)]  # type: "List[List[int]]"
    solve(A)

if __name__ == '__main__':
    main()
