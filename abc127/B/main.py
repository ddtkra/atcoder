#!/usr/bin/env python3



# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    r,d,x = map(int, input().split())

    for i in range(10):
        x = r*x-d
        print(x)
    

if __name__ == '__main__':
    main()
