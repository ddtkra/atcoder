#!/usr/bin/env python3
import sys


def solve(N: int, M: int, l: "List[int]", r: "List[int]", s: "List[int]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]" 
    r = [int()] * (N)  # type: "List[int]" 
    s = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
        s[i] = int(next(tokens))
    solve(N, M, l, r, s)

if __name__ == '__main__':
    main()