#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(s: str):
    rs = s[::-1]
    if all([s[i] == rs[i] for i in range(len(s)) if s[i] != '*' and rs[i] != '*']):
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
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
