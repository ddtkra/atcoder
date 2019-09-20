#!/usr/bin/env python3
import sys
import itertools

def solve(S: int):
    se = ('+', '_')
    S = list(str(S))

    ans = 0
    for i in itertools.product(se,repeat=(len(S)-1)):
        t =[]
        t.append(S[0])
        for j,x in enumerate(i):
            t.append(x) 
            t.append(S[j+1])

        t = [x for x in t if(x != '_')]
        ts = ''.join(t)
        
        ans += sum(list(map(int,ts.split('+'))))
        
    print(ans)

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()