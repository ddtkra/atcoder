#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int):
    A = list(str(A))
    B = list(str(B))
    for i in range(3):
        if A[i] == '9' and ((i != 0 and B[i] == '0') or (i == 0 and B[i] == '1')):
            continue
        else:
            if i == 0:
                if abs(int(A[i])-9) < abs(int(B[i])-1):
                    B[i] = '1'
                else:
                    A[i] = '9'
            else:
                if abs(int(A[i])-9) < abs(int(B[i])):
                    B[i] = '0'
                else:
                    A[i] = '9'
        break

    print(int(''.join(A))-int(''.join(B)))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
