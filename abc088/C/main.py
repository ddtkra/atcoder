#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(c: "List[List[int]]"):

    for a1 in range(101):
        b1 = c[0][0] - a1
        b2 = c[0][1] - a1
        b3 = c[0][2] - a1
        
        a2 = c[1][0] - b1
        a3 = c[2][0] - b1

        if(a1+b1 == c[0][0] and a2+b1 == c[1][0] and a3+b1 == c[2][0] and 
        a1+b2 == c[0][1] and a2+b2 == c[1][1] and a3+b2 == c[2][1] and 
        a1+b3 == c[0][2] and a2+b3 == c[1][2] and a3+b3 == c[2][2]):
            print(YES)
            exit()

    print(NO)

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    c = [ [ int(next(tokens)) for _ in range(3) ] for _ in range(3) ]  # type: "List[List[int]]"
    solve(c)

if __name__ == '__main__':
    main()