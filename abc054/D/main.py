#!/usr/bin/env python3
import sys


def solve(N: int, M_a: int, M_b: int, a: "List[int]", b: "List[int]", c: "List[int]"):    
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M_a = int(next(tokens))  # type: int
    M_b = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]" 
    b = [int()] * (N)  # type: "List[int]" 
    c = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M_a, M_b, a, b, c)

if __name__ == '__main__':
    main()
