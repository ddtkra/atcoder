#!/usr/bin/env python3
import sys


def solve(N: int, s: "List[str]"):
    ans = []
    for j in range(N):
        su = []
        for i in s:
            su.append(i[j])
        ans.append(su[::-1])

    for i in ans:
        print(''.join(i))

    return


# Generated by 1.1.3 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()