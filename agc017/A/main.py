#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 2  # type: int

def solve(N: int, P: int, A: "List[int]"):
    
    if all([(A[i]%2==0) for i in range(N)]):
        if P == 0:
            print(2**N)
        else:
            print(0)
        exit()

    
            


    ans = 0
    for i in range(1<<N):
        s = 0
        for j in range(N):
            if (i>>j) & 1:
                s += A[j]

        if s%2 == P:
            ans += 1

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, A)

if __name__ == '__main__':
    main()
