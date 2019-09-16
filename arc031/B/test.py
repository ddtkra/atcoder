#!/usr/bin/env python3

YES = "YES"  # type: str
NO = "NO"  # type: str

from collections import deque
import sys


def isfullmaze(maze):
    # if(not maze):
    #     return True
    ans = 0
    for i in maze:
        if(i.count(maze[0][0]) == len(i)):
            ans += i.count(maze[0][0])
            continue
        else:

            return False
        
    print(ans)
    return True


def main():
    maze = [list('xxxx'), list('xxxx'), list('xxxx'), list('xxax')]
    if(isfullmaze(maze)):
        print('YES')
    else:
        print('NO')



if __name__ == '__main__':
    main()
