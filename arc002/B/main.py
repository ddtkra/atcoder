#!/usr/bin/env python3




def main():
    y,m,d = input().split('/')
    from datetime import datetime, timedelta
    now = datetime(int(y),int(m),int(d))
    while True:
        y,m,d = now.year, now.month, now.day
        if y%(m*d) == 0:
            print(now.strftime("%Y/%m/%d"))
            exit()
        now += timedelta(days=1)



if __name__ == '__main__':
    main()
