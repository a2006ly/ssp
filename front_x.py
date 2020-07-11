"""
受け取った⽂字列のリストの要素を、'x'で始まる⽂字列と、
'x'以外で始まる⽂字列に分類し、
整列（ソート）したリスト を返すfront_x関数を書いてください。
"""


def front_x(x):
    list_x = []
    for str1 in x:
        if str1.startswith("x"):
            list_x.append(str1)
        list_x.sort(reverse=True)

    for str2 in list_x:
        x.remove(str2)
        x.insert(0, str2)
    return x


print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
