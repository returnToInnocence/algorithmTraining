import sys
import re


def addDir(dir, str):
    if str not in dir:
        dir[str] = {}
    return dir[str]


def printDir(dir, depth):
    for s in sorted(dir):
        print(' ' * depth + s)
        printDir(dir[s], depth + 1)


N = int(sys.stdin.readline())
dirs = {}
for i in range(N):
    str = sys.stdin.readline()
    dir = dirs
    for dirstr in re.split(r"\\", str):
        dir = addDir(dir, dirstr.rstrip())
printDir(dirs, 0)
