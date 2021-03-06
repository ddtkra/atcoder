#!/usr/bin/env python3
import sys
import math

def solve(N: int, S: str):
    if(N%2 == 1 and S[int(N/2)] == 'b'):
        for i in range(1,N):
            if((S[i] == 'a' and S[i-1] == 'c') or \
                (S[i] == 'b' and S[i-1] == 'a') or \
                (S[i] == 'c' and S[i-1] == 'b')):
                continue
            else:
                print(-1)
                sys.exit()
        print(int((N-1)/2))
        sys.exit()
    else:
        print(-1)

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
