#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int):
    sn = str(N)
    if sn[1:] == '9'*(len(sn)-1):
        print(int(sn[0])+9*(len(sn)-1))
    else:
        print(int(sn[0])+9*(len(sn)-1)-1)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
