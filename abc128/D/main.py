#!/usr/bin/env python3
import sys
from collections import deque
import heapq

sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, K: int, V: "List[int]"):
    hq = []
    heapq.heapify(hq)

    d = deque(V)

    cnt = K
    while cnt > 0:
        if len(d) > 0:
            if d[0] < d[-1]:
                t = d.pop()
            else:
                t = d.popleft()
            if t < 0:
                cnt += 1
            print(t)
            heapq.heappush(hq, t)
            cnt -= 1
        else:
            break

    print(hq)

    while K > 0:
        t = heapq.heappop(hq)
        print(t)
        if t > 0:
            heapq.heappush(hq, t)
            break;
        K -= 1

    print(hq)

    print(sum(hq))




    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, V)

if __name__ == '__main__':
    main()
