"""
ファイルを読み込んで、
指定された⽂字列が存在する⾏だけ表⽰するプログラムを書いてください。
⼤⽂字⼩⽂字を無視するように⼯夫してください。
"""
with open("/Users/yanliling/ssp-lesson/ssp/Football Coach.txt", "rU") as file_object:
    opt = "but"
    lines = file_object.readlines()
    for line in lines:
        lower_line = line.lower()
        if lower_line.find(opt) != -1:
            print(line)

