#!/usr/bin/env python3
import sys


def solve(b: "List[List[int]]", c: "List[List[int]]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    b = [ [ int(next(tokens)) for _ in range(3) ] for _ in range(2) ]  # type: "List[List[int]]"
    c = [ [ int(next(tokens)) for _ in range(2) ] for _ in range(3) ]  # type: "List[List[int]]"
    solve(b, c)

if __name__ == '__main__':
    main()
