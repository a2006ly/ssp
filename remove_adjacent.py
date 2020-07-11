"""
リストを受け取って、
隣接した同じ要素を削除したリストを返すremove_adjacent関数を書いてください。
"""


def remove_adjacent(li):
    if li:
        foo = li[0]
        for x in li[1:]:
            if foo == x:
                foo = x
                li.remove(x)
            else:
                foo = x
    else:
        return li

    # 重複の要素を削除すれば
    # list_new = sorted(set(li),key= li.index)

    return li


print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([]))
