#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

from re import findall

def solve(S: str):

    l = S.split('+')
    ans = 0
    for i in l:
        il = i.split('*')
        if '0' not in il:
            ans += 1
    
    print(ans)
    
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
