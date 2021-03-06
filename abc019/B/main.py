#!/usr/bin/env python3
import sys


def solve(s: str):
    ans = []
    c = 1
    b = s[0]
    for i in range(1,len(s)):
        if(s[i] == b):
            c += 1
        else:
            ans += [b, str(c)]
            b = s[i]
            c = 1
    ans += [b, str(c)]
    print(''.join(ans))    

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
