"""
課題1-1：fizz_buzz.py
以下のスクリプトから呼び出す関数fbを書いてください。
関 数fbは、3で割切れるときはFizz、5で割切れるときはBuzz、両者で割切れるときはFizzBuzzと返してください。
ただし、if、 while、for構⽂及び==等の⽐較演算⼦を使ってはいけません。
"""

import math


def fb(x):
    msg = {3: 'Fizz', 5: 'Buzz', 15: 'FizzBuzz', 1: ''}
    rs = math.gcd(x, 3)
    rs = math.gcd(x, 5)
    rs = math.gcd(x, 15)
    return msg[rs]


i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1
