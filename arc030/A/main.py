#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(n: int, k: int):
    if k <= n//2:
        print(YES)
    else:
        print(NO)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(n, k)

if __name__ == '__main__':
    main()
