import time
import random


def addList():
    list1 = []
    # 開始ミリ秒
    before = int(time.time() * 1000)
    for i in range(100000):
        list1.append(i)
    # 時間コスト
    gapTime = int(time.time() * 1000) - before
    return gapTime


def readList():
    list2 = [i for i in range(100000)]
    # 開始ミリ秒
    before = int(time.time() * 1000)
    for i in list2:
        index = random.randint(1, 99999)
        list2[index]

    # 時間コスト
    gapTime = int(time.time() * 1000) - before

    return gapTime


print("100000個要素を追加する時間(ms）", addList(), flush=True)
print("100000個要素をランダム参照する時間(ms）", readList(), flush=True)
