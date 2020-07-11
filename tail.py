"""
ファイルを読み込んで、後ろの⾏から表⽰するためのコード (a)を書いてください。
"""
# 关键字with 在不再需要访问文件后将其关闭
with open("/Users/yanliling/ssp-lesson/ssp/Football Coach.txt", "rU") as file_object:
    lines = file_object.readlines()
    new_lines = reversed(sorted(lines, key=lines.index))
    for line in new_lines:
        print(line)
