#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(x: "List[List[int]]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [ [ int(next(tokens)) for _ in range(5) ] for _ in range(5) ]  # type: "List[List[int]]"
    solve(x)

if __name__ == '__main__':
    main()