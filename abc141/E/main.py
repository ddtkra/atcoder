#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    
    ans = 0
    x = []
    for i in range(N):
        x.append(S[i])
        xj = ''.join(x)
        if(S[i+1:].count(xj)):
            ans = max(ans, len(xj))
        else:
            x.pop(0)

    print(ans)
    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()