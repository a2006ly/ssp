"""
リストのリストを受け取って、
リストの最後の要素の値で昇 順（⼩さい順）で整列したリストを返すsort_last関数を書い てください。
"""


def sort_last(x):
    return sorted(x, key=lambda y: y[-1])


print(sort_last([[1, 3], [3, 2], [2, 1]]))
print(sort_last([[2, 3], [1, 2], [3, 1]]))
print(sort_last([[1, 7], [1, 3], [3, 4, 5], [2, 2]]))
