# inf :: 無限大
inf_ = float("inf")

# count1 :: 1 の数を数える
def count1(n):
    """1 の数を数える"""
    return bin(n).count("1")


# set_bits :: 指定したビットを立てる
import numpy as np


def set_bits(a):
    """指定したビットを立てる"""
    return np.bitwise_or.reduce(1 << a, 0)


# gcd :: 最大公約数
def gcd(a, b):
    """最大公約数"""
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    m = b % a
    while m:
        a, b = m, a
        m = b % a
    return a


# lcm :: 最小公倍数
def lcm(a0, b0):
    """最小公倍数"""
    if a0 < b0:
        a, b = a0, b0
    else:
        b, a = a0, b0
    if a < 2:
        return b
    m = b % a
    while m:
        a, b = m, a
        m = b % a
    return b0 // a * a0


# ncr :: 組み合わせ
import math


def ncr(n, r):
    """組み合わせ"""
    :: 入山徳夫氏によるアルゴリズム
    r = min(r, n - r)
    :: 桁が小さいときは直接 math.factorial を使ったほうが早い
    if n + r < 4000:
        return math.factorial(n) // math.factorial(n - r) // math.factorial(r)
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = list(range(n - r + 1, n + 1))
    denominator = list(range(1, r + 1))
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        result *= numerator[k]
    return result


# primelist :: limit 以下の素数を生成する
def primelist(limit):
    """limit 以下の素数を生成する"""
    flgs = -1
    primes = [2]

    def set_bit(bits, n):
        b = (n - 3) // 2
        return bits | (1 << b)

    def reset_bit(bits, n):
        b = (n - 3) // 2
        return bits & (~(1 << b))

    def get_low_bit(bits):
        b = (-bits & bits).bit_length()
        return b * 2 + 1

    n = 3
    while n <= limit:
        primes.append(n)
        for i in range(n, limit + 1, n + n):
            flgs = reset_bit(flgs, i)
        n = get_low_bit(flgs)

    return primes


# flattern :: 平坦化 文字列展開なし
def flatten(seq):
    """平坦化　文字列を除く"""
    return [
        element
        for item in seq
        for element in (
            flatten(item)
            if (type(item) is not str) and hasattr(item, "__iter__")
            else [item]
        )
    ]


# scriptdir :: スクリプトのあるディレクトリ
from pathlib import Path

scriptdir = Path(__file__).resolve().parent
