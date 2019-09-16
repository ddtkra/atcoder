#!/usr/bin/env python3
import sys
import bisect 

def solve(N: int, L: int):
    li = [i for i in range(L,L+N)]

    # print(li)
    if(L < 0 and L+N-1 <= 0):
        print(sum(li)-li[-1])
    elif(L < 0 and L+N-1 > 0):
        print(sum(li))
    elif(L >= 0):
        print(sum(li) - li[0])

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)

if __name__ == '__main__':
    main()
