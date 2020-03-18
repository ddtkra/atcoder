#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(L: int, R: int, l: "List[int]", r: "List[int]"):
    al = [0] * 41
    bl = [0] * 41

    for i in range(L):
        al[l[i]] += 1

    for i in range(R):
        bl[r[i]] += 1

    ans = 0
    for i in range(10, 41):
        ans += min(al[i], bl[i])

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    l = [int(next(tokens)) for _ in range(L)]  # type: "List[int]"
    r = [int(next(tokens)) for _ in range(R)]  # type: "List[int]"
    solve(L, R, l, r)

if __name__ == '__main__':
    main()
