#!/usr/bin/env python3
import sys


def solve(E: "List[int]", B: int, L: "List[int]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    E = [ int(next(tokens)) for _ in range(5-0+1) ]  # type: "List[int]"
    B = int(next(tokens))  # type: int
    L = [ int(next(tokens)) for _ in range(5-0+1) ]  # type: "List[int]"
    solve(E, B, L)

if __name__ == '__main__':
    main()
