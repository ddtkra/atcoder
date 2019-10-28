#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(S: str):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
