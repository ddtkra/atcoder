#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, K: int):
    c = 0
    n = A
    l = 2 * pow(10,12)
    if K == 0:
        print(l-A)
        exit()
        
    while n < l:
        n += 1 + K*n
        c += 1
    print(c)
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, K)

if __name__ == '__main__':
    main()
