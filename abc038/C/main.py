#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]"):
    ans = N
    i = 0
    di = 1
    while i+di < N:
        if a[i+di] > a[i+di-1]:
            di += 1
            if i+di == N:
                ans += (di)*(di-1)//2
                
        else:
            if di > 1:
                ans += (di)*(di-1)//2
                i += di
            else:
                i += 1
            di = 1

    print(ans) 

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
