#!/usr/bin/env python3
import sys


def solve(X: str, Y: str):
    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = next(tokens)  # type: str
    Y = next(tokens)  # type: str
    solve(X, Y)

if __name__ == '__main__':
    main()
