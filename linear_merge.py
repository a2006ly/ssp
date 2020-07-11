"""
昇順（⼩さい順） の2個のリストを受け取って、
マージして、 要素の値で昇順で整列したリストを返す関数linear_mergeを書 いてください
"""


def linear_merge(li1, li2):
    # li1 と　li2 マージする
    li1.extend(li2)
    list_new = sorted(li1)
    return list_new


print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
