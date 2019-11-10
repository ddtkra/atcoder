#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    '''
    Warshall-Floyd
    input:  c[|V|][|V|]
            input example to from cost
            (c[i][i] == 0)
    Output: Minimun cost of all paths in the inputed graph 
    '''

    

    V = N+1
    INF = 1<<32
    
    g = [[INF] * (V) for i in range(V)]
    for i in range(M):
        g[A[i]][B[i]] = 1
        g[B[i]][A[i]] = 1

    for k in range(V):
        for i in range(V):
            if g[i][k] == INF : continue
            for j in range(V):
                if g[k][j] == INF: continue
                g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    
    for i in range(V):
        g[i][i] = INF
    
    for i in range(1,V):
        print(g[i].count(2))
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
