#!/usr/bin/env python3




def main():
    r, D, x2000 = map(int, input().split())

    x = x2000
    for i in range(1,11):
        x = r*x-D
        print(x)
        
    

if __name__ == '__main__':
    main()
