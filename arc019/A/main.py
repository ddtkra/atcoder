#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(S: str):
    ls = list(S)
    for i in range(len(ls)):
        if ls[i] == 'O' or ls[i] == 'D':
            ls[i] = '0'
        elif ls[i] == 'I':
            ls[i] = '1'
        elif ls[i] == 'Z':
            ls[i] = '2'
        elif ls[i] == 'S':
            ls[i] = '5'
        elif ls[i] == 'B':
            ls[i] = '8'

    print(''.join(ls))
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
