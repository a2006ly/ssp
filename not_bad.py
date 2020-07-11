"""
⽂字列を受け取って、'not'の後に'bad'が表れたら、
'not'〜'bad'を'good'で置換するnot_bad関数を書いてください。
"""


def not_bad(s):
    not_index = s.find("not")
    bad_index = s.find("bad")
    if not_index < bad_index:
        replace_area = s[not_index:(bad_index + len("bad"))]
        return_str = s.replace(replace_area, "good")
    else:
        return_str = s

    return return_str


print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad!'))
print(not_bad('This tea is not hot'))
print(not_bad("It's bad yet not"))
