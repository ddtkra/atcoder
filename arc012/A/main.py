#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(day: str):
    if day == 'Sunday' or day == 'Saturday':
        print(0)
    elif day == 'Monday':
        print(5)
    elif day == 'Tuesday':
        print(4)
    elif day == 'Wednesday':
        print(3)
    elif day == 'Thursday':
        print(2)
    elif day == 'Friday':
        print(1)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    day = next(tokens)  # type: str
    solve(day)

if __name__ == '__main__':
    main()
