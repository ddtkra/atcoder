#!/usr/bin/env python3
import sys


def solve(S: str):
    sl = {'A', 'C', 'G', 'T'}

    T = list(S)
    c = 0
    ans = 0
    for i in range(len(T)):
        if(T[i] in sl):
            c += 1
            continue
        else:
            ans = max(ans,c)
            c = 0
    print(max(ans,c))
    return


# Generated by 1.1.3 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
