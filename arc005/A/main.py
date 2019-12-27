#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, w: "List[str]"):
    w = [i.lower() for i in w]
    # print(w)
    from collections import Counter
    c = Counter(w)
    ans = c['takahashikun']
    
    if w[-1]  == 'takahashikun.':
        print(ans+1)
    else:
        print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    w = [next(tokens) for _ in range(N - 1 - 0 + 1)]  # type: "List[str]"
    solve(N, w)

if __name__ == '__main__':
    main()
