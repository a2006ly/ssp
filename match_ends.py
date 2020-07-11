"""
受け取った⽂字列のリストの要素のうち、
2⽂字以上で、最初と最後が同じ⽂字の⽂字列の数を返す関数match_endsを書いてください。
"""

def match_ends(li):
    first_end = 0
    for str in li:
        if len(str) >= 2:
            if str[0] == str[-1]:
                first_end += 1
    return first_end


print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))