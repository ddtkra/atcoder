#!/usr/bin/env python3



# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    S = input().replace('?', '.')
    T = input()

    import re
    import sys

    for i in range(len(S)-len(T),-1,-1):
        if(re.match(S[i:i+len(T)],T)):
            S = S.replace('.', 'a')
            print(S[:i]+T+S[i+len(T):])
            exit()
    else:
        print("UNRESTORABLE")
    
if __name__ == '__main__':
    main()
