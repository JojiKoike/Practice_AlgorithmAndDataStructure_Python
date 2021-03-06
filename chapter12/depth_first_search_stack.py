from typing import List
from enum import Enum


class Color(Enum):
    WHITE: int = 1
    GRAY: int = 2
    BLACK: int = 3


time: int = 0


def dfs() -> None:
    # Solve
    for i in range(n):
        if color[i] == Color.WHITE:
            dfs_visit(i)

    # Print Results
    for i in range(n):
        print("{0} {1} {2}".format(i + 1, d[i], f[i]))


def dfs_visit(k: int) -> None:
    global time
    nt = [0 for i in range(n)]

    stack: List[int] = []
    stack.append(k)
    color[k] = Color.GRAY
    time += 1
    d[k] = time

    while len(stack) > 0:
        u: int = stack[len(stack) - 1]
        v: int = next(u)
        if v != -1:
            if color[v] == Color.WHITE:
                color[v] = Color.GRAY
                time += 1
                d[v] = time
                stack.append(v)
        else:
            stack.pop()
            color[u] = Color.BLACK
            time += 1
            f[u] = time


def next(u: int) -> int:
    for i in range(nt[u], n):
        nt[u] = i + 1
        if m[u][i]:
            return i
    return -1


n: int = int(input())
d: List[int] = [0 for i in range(n)]
f: List[int] = [0 for i in range(n)]
color: List[Color] = [Color.WHITE for i in range(n)]
time = 0
adjs: List[List[int]] = [list(map(int, input().split())) for i in range(n)]
m: List[List[bool]] = [[False for j in range(n)] for i in range(n)]
color: List[Color] = [Color.WHITE for i in range(n)]
nt: List[int] = [0 for i in range(n)]
for adj in adjs:
    for i in range(2, 2 + adj[1]):
        m[adj[0] - 1][adj[i] - 1] = True
dfs()
