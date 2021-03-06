#!/usr/bin/env python3
import sys


def solve(N: int, x: int, a: "List[int]"):
    ans = 0
    a.sort()
    for i in a:
        if(x-i >= 0):
            ans += 1
            x -= i
        else:
            break
    else:
        if(x > 0):
            print(ans-1)
            exit()

    print(ans)
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, x, a)

if __name__ == '__main__':
    main()
