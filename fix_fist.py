"""
⽂字列を受け取って、最初の⽂字と同じ⽂字を'*'に変更し て返すfix_first関数を書いてください。
ただし、最初の⽂字は 変更しないでください。
"""


def fix_first(s):
    first_char = s[0]
    str_arr = s.split(first_char)
    replaced_str = first_char + "*".join(str_arr[1:])
    return replaced_str


print(fix_first("babble"))
print(fix_first("google"))
print(fix_first("apple"))
print(fix_first("orange"))
