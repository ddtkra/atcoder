#!/usr/bin/env python3




def main():
    N = int(input())
    s = input()

    print((s.count('A')*4+s.count('B')*3+s.count('C')*2+s.count('D'))/N)
    

if __name__ == '__main__':
    main()
