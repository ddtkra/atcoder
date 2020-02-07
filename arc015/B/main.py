#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, MT: "List[float]", mT: "List[float]"):
    ans = [0] * 6
    for i in range(N):
        if MT[i] >= 35:
            ans[0] += 1
        elif 30 <= MT[i] < 35:
            ans[1] += 1
        elif 25 <= MT[i] < 30:
            ans[2] += 1

        if mT[i] >= 25:
            ans[3] += 1
        
        if mT[i] < 0 and MT[i] >= 0:
            ans[4] += 1
        elif MT[i] < 0:
            ans[5] += 1

        
    print(' '.join(map(str, ans)))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    MT = [float()] * (N)  # type: "List[float]"
    mT = [float()] * (N)  # type: "List[float]"
    for i in range(N):
        MT[i] = float(next(tokens))
        mT[i] = float(next(tokens))
    solve(N, MT, mT)

if __name__ == '__main__':
    main()
