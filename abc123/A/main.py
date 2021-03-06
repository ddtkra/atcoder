#!/usr/bin/env python3
import sys


def solve(a: int, b: int, c: int, d: int, e: int, k: int):
    ans = k
    for i,v in enumerate([a,b,c,d,e]):
        for j,x in enumerate([a,b,c,d,e],i+1):
            if(abs(v-x)):
                ans = max(ans,abs(v-x))

    if(ans > k):
        print(':(')
    else:
        print('Yay!')
    return


# Generated by 1.1.3 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    e = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(a, b, c, d, e, k)

if __name__ == '__main__':
    main()
