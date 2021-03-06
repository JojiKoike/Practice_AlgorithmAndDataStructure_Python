import heapq
from enum import Enum
from typing import List, Tuple

INFTY: int = 1000000000


class Color(Enum):
    WHITE: int = 1
    GRAY: int = 2
    BLACK: int = 3


class Edge(object):
    def __init__(self, v: int, c: int):
        self.v = v
        self.c = c


def dijkstra() -> None:
    pq: List[Tuple[int, int]] = []
    d[0] = 0
    color[0] = Color.GRAY
    heapq.heappush(pq, (0, 0))
    while len(pq) > 0:
        u: int
        dx: int
        dx, u = heapq.heappop(pq)
        color[u] = Color.BLACK
        print("d[{0}] = {1} dx = {2}".format(u, d[u], dx))
        if d[u] < dx:
            continue
        for i in range(len(adjs[u])):
            e: Edge = adjs[u][i]
            if color[e.v] == Color.BLACK:
                continue
            if d[u] + e.c < d[e.v]:
                d[e.v] = d[u] + e.c
                print("d[{0}] = {1}".format(e.v, d[e.v]))
                heapq.heappush(pq, (d[e.v], e.v))
                color[e.v] = Color.GRAY
    for i in range(n):
        print("{0} {1}".format(i, -1 if d[i] == INFTY else d[i]))


n: int = int(input())
adjs: List[List[Edge]] = [[] for i in range(n)]
color: List[Color] = [Color.WHITE for i in range(n)]
d: List[int] = [INFTY for i in range(n)]
for i in range(n):
    g: List[int] = list(map(int, input().split()))
    h: List[Edge] = []
    for j in range(1, g[1] + 1):
        edge: Edge = Edge(g[2 * j], g[2 * j + 1])
        h.append(edge)
    adjs[i] = h
dijkstra()
