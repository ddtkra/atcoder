#!/usr/bin/env python3
import sys


def solve(s: str, K: int):
    sl = set()

    for i in range(len(s)):
        for j in range(i,min(i+K,len(s))):
            sl.add(s[i:j+1])

    sl = list(sorted(sl))   
    # print(sl)
    print(sl[K-1])

    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(s, K)

if __name__ == '__main__':
    main()