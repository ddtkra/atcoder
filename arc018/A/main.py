#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(Height: float, BMI: float):
    print(BMI*((Height/100)**2))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Height = float(next(tokens))  # type: float
    BMI = float(next(tokens))  # type: float
    solve(Height, BMI)

if __name__ == '__main__':
    main()
