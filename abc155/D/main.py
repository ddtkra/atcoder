#!/usr/bin/env python3



def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    am = sorted([i for i in a if i < 0])
    ap = sorted([i for i in a if i >= 0])


    def f(x: int):
        # xが与えられたとき、x以下のai*ajの数が個以上か？
        ans = 0
        if x < 0:
            

        else:


        if ans >= k:
            return True
        else:
            return False
    
    def binary_search(left: int, right: int):
        while right-left > 1:
            mid = (left+right)//2
            if f(mid):
                left = mid
            else:
                right = mid
        return left

    
    ans = 0
    if len(am)*len(ap) > k:
        # minus
        ans =  binary_search(-10**9, 0)

    else:
        # plus
        ans = binary_search(0, 10**9)
    
    print(ans)


if __name__ == '__main__':
    main()
