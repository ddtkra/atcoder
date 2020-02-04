#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: "List[int]"):

    def lis(A: "List[int]"):
        import bisect

        LIS = [A[0]]
        uLIS = []
        for i in range(len(A)):
            if A[i] > LIS[-1]:
                LIS.append(A[i])
            else:
                LIS[bisect.bisect_left(LIS, A[i])] = A[i]
                uLIS.append(A[i])

        return [len(LIS), uLIS, LIS]

    print(A, lis(A))
    # cn, aA, b = lis(A)
    # c = cn
    # c = 1
    # while c < N:
    #     print(A, aA, b)
    #     cn, aA, b = lis(aA)
    #     c += cn
    #     c += 1

    # print(c)




def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
