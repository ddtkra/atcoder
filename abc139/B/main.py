#!/usr/bin/env python3
import sys
from math import ceil


def solve(A: int, B: int):
    n = 1
    c = 0
    while(n < B):
        n += (A-1)
        c += 1

    print(c)
    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()