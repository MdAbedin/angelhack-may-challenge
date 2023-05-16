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

def decode(encoded,codebook):
    @cache
    def solve(i):
        if i > len(encoded): return []
        if i == len(encoded): return [""]

        ans = []

        for char,code in codebook.items():
            if encoded.startswith(code,i):
                for suffix in solve(i+len(code)): ans.append(char+suffix)

        return ans[-20:]
    
    return solve(0)

def main():
    codebook = {
        'a': '00',
        'b': '01',
        'c': '10',
        'd': '1100',
        'e': '1101',
        'f': '1110',
        'g': '111100',
        'h': '111101',
        'i': '111110',
        'j': '1111110000',
        'k': '1111110001',
        'l': '1111110010',
        'm': '1111110011',
        'n': '1111110100',
        'o': '1111110101',
        'p': '1111110110',
        'q': '1111110111',
        'r': '1111111000',
        's': '1111111001',
        't': '1111111010',
        'u': '1111111011',
        'v': '1111111100',
        'w': '1111111101',
        'x': '1111111110',
        'y': '1111111111',
        'z': '11111111110000',
        ' ': '11111111110001'
    }
    encoded = "11111011111111110001111111001011111101011111111100110111111111110001001111110100111100110111111100101111010010111111000111111111110001101111110101110011011111111111000110111101001111110010111111001011011111110100111100110111111111110001011101100011111110111111111001110111111111110001111110111111101011111111110001111110111111100111111111110001111011111110111111110100111111111100010011111101001100111111111100011101111111111010111110111111101011111011111101001111001111111111000100111111010011001111111111000111111011111111110001110011111011111110011111110010111110111111000111011111111111000111111110101111011101111111111100011111111101111111010111111110001100111111111100011111111111000111111111110001111111101011110100111111101011111111110001001111110110111111011011010011111110001111111001111111111100011111101111110100111111111100011111111010111101110111111111110001111111011011110111111110000011111110011101"

    for ans in decode(encoded,codebook): print(ans)

for i in range(rd(int) if MULTIPLE_CASES else 1): main()