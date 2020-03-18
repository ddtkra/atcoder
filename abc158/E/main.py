#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, P: int, S: str):
    
    ans = 0
    n = 0
    while n <= int(S):
        ans += S.count(str(n))
        # print(ans)
        n += P

    print(ans)


    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = str(next(tokens))  # type: int
    solve(N, P, S)

if __name__ == '__main__':
    main()
