#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]", b: "List[int]"):
    g = [[] for i in range(N+1)]
    for i in range(N-1):
        g[a[i]].append(b[i])
        g[b[i]].append(a[i])


    gcc = [len(i) for i in g]
    k = max(gcc)
    gc = [[j for j in range(1,k+1)] for i in g]
    
    ans = []

    for i in range(N-1):
        idx = 0
        if gc[a[i]][0] == gc[b[i]][0]:
            idx = 0
        else:
            idx = -1 
        x = gc[a[i]][idx]
        # print(x, gc[a[i]], gc[b[i]])
        ans.append(x)
        if idx == -1:
            gc[a[i]].pop(-1)
            gc[b[i]].pop(-1)
        else:
            gc[a[i]].pop(0)
            gc[b[i]].pop(0)


    print(k)
    for i in ans:
        print(i)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()
