#!/usr/bin/env python3
import sys


def solve(M: int, D: int):
    ans = 0

    for i in range(1,M+1):
        for j in range(22, D+1):
            d10 = j//10
            d1 = j%10
            if d10 >= 2 and d1 >= 2 and d10*d1 == i:
                ans += 1

    print(ans)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(M, D)

if __name__ == '__main__':
    main()
