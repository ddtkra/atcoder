#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int):
    def isPrime(x :int):
        if(x == 1):
            return False
        for i in range(2, int(x**0.5)+1):
            if(x%i == 0):
                return False
        return True

    print(YES if isPrime(N) else NO)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
