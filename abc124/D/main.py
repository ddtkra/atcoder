#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: str):
    seq = []
    if(S[0] == '0'): seq.append(0)
    f = S[0]
    c = 1
    for i in range(1, N):
        if(S[i] == f):
            c += 1
        else:
            seq.append(c)
            f = S[i]
            c = 1
    seq.append(c)
    
    rseq = [0] * (len(seq)+1)
    for i in range(1,len(seq)+1):
        rseq[i] = rseq[i-1] + seq[i-1]

    ans = 0
    # cumulative sum
    for i in range(len(rseq)):
        # print(ans, rseq[min(len(rseq)-1,i*2+2*K+2)], rseq[min(len(rseq)-1, i*2)])
        ans = max(ans, rseq[min(len(rseq)-1,i*2+2*K+1)] - rseq[min(len(rseq)-1, i*2)])


    # naive
    # for i in range(len(seq)):
    #     for j in range(K):
    #         # print(seq[i*2:i*2+2*K+1])
    #         ans = max(ans, sum(seq[i*2:i*2+2*K+1]))

    print(ans)

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = str(next(tokens))  # type: str
    solve(N, K, S)

if __name__ == '__main__':
    main()
