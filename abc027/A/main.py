#!/usr/bin/env python3
import sys


def solve(l: "List[int]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    l = [ int(next(tokens)) for _ in range(3) ]  # type: "List[int]"
    solve(l)

if __name__ == '__main__':
    main()
