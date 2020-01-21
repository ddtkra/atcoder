#!/usr/bin/env python3




def main():
    # Failed to predict input format
    l = input().split()
    l = ['<' if i == 'Left' else i for i in l]
    l = ['>' if i == 'Right' else i for i in l]
    l = ['A' if i == 'AtCoder' else i for i in l]
    print(' '.join(l))

if __name__ == '__main__':
    main()
