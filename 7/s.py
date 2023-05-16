from bisect import bisect_left as bl, bisect_right as br, insort_left, insort_right
from collections import deque, Counter as counter, defaultdict as dd
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce, partial
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge, nlargest, nsmallest
from itertools import count, cycle, repeat, accumulate, chain, groupby, starmap, product, permutations, combinations, combinations_with_replacement, zip_longest, islice
from math import ceil, comb, factorial, floor, gcd, lcm, prod, log, sqrt, acos, asin, atan, dist, sin, cos, tan, degrees, radians, pi, e, inf
from operator import add, sub, mul, truediv, floordiv, mod, xor, and_, or_, eq, ne, neg, concat, contains
from random import randint, choice, shuffle, sample
from string import ascii_lowercase as lowers, ascii_uppercase as uppers, ascii_letters as all_letters, digits
from sys import stdin, argv, setrecursionlimit

def lmap(function, iterable): return list(map(function, iterable))
def line(): return stdin.readline().strip()
def rd(converter): return converter(line())
def rl(converter, delimeter = None): return lmap(converter, line().split(delimeter))
def rls(num_lines, converter): return [rd(converter) for i in range(num_lines)]
def rg(num_lines, converter, delimeter = None): return [rl(converter,delimeter) for i in range(num_lines)]

MOD = 10**9+7
EPS = 10**-6
MULTIPLE_CASES = 0

def main():
    grid = "XXXX.X....X..X..X.X.XX.XX"
    grid = [list(grid[i:i+5]) for i in range(0,len(grid),5)]
    seen = set()

    while True:
        grid2 = [["."]*5 for i in range(5)]

        for r in range(5):
            for c in range(5):
                x = sum(grid[r2][c2] == "X" for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]] if 0 <= r2 < 5 and 0 <= c2 < 5)

                if grid[r][c] == "X":
                    if x == 1: grid2[r][c] = "X"
                else:
                    if x in [1,2]: grid2[r][c] = "X"

        grid = grid2

        if "".join("".join(row) for row in grid) in seen:
            break
        else:
            seen.add("".join("".join(row) for row in grid))

    print(sum(2**(r*5+c) for r in range(5) for c in range(5)))

for i in range(rd(int) if MULTIPLE_CASES else 1): main()