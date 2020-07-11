"""
テキストデータ（英⽂）の総単語数及び上位20単語の出現数をカウントし，
表⽰するスクリプトを書いてください。
"""
import sys

# with open("/Users/yanliling/ssp-lesson/ssp/pg19033.txt", "rU") as file:
file = sys.stdin
if len(sys.argv) > 1:
    file = open(sys.argv[1], "r")
else:
    print("ファイル指定されない")

strs = file.read()
words = strs.split()
print("文字数：", len(words))
wc_d = {}
# 単語の抽出及びカウント
for w in words:
    if w in wc_d:
        wc_d[w] += 1
    else:
        wc_d[w] = 1
# 出現頻度
sorted_words = sorted(wc_d.items(), key=lambda x: x[1], reverse=True)

i = 0
for (k, v) in sorted_words:
    if i == 20:
        break
    print("{}: {}".format(k, v))
    i += 1
    