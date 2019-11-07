#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

from re import findall

def solve(S: str):
    if S.count('*') == S.count('+')-1:
        print(S.count('*')-cd )
    else:
        print(S.count('+')-S.count('+0+')+S.count('*'))
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
