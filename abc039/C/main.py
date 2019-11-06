#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(S: str):
    S = S
    try:
        i = S.index('WBWBWWBWBWBW')
    
        if i == 0:
            print('Do')
        elif i == 1:
            print('Si')
        elif i == 3:
            print('La')
        elif i == 5:
            print('So')
        elif i == 7:
            print('Fa')
        elif i == 8:
            print('Mi')
        elif i == 10:
            print('Re')
        else:
            print('Do')
    except:
        print('Re')
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
