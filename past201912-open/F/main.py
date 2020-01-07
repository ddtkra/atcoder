#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(S: str):
    N = len(S)
    sl = []
    idx = 0
    for i in range(1, N):
        if S[i-1].isupper() and S[i].isupper() and i-idx > 1:
            sl.append(S[idx:i])
            idx = i

    sl.append(S[idx:])
    sl = sorted(sl, key=lambda x: x.upper())

    # from collections import OrderedDict
    # od = OrderedDict()
    # for i in range(len(sl)):
    #     od[i] = sl[i]

    # for k,v in od.items():
    #     print(k, v)
    
    print(''.join(sl))


    return



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
