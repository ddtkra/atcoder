#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, H: "List[int]"):
    for i in reversed(range(N-1)):
        if(H[i+1] >= H[i]):
            continue
        elif(H[i]+1 == H[i+1]):
            H[i] -= 1
        else:
            print(NO)
            exit()

    print(YES)
    
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, H)

if __name__ == '__main__':
    main()
