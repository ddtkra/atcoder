#!/usr/bin/env python3




def main():
    n = int(input())
    r = input()
    ans = (4*r.count('A')+3*r.count('B')+2*r.count('C')+1*r.count('D'))/n
    print(ans)



if __name__ == '__main__':
    main()
