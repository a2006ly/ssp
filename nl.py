"""
課題1-2: nl.py
Unixのnlコマンドの基本機能相当のnl.pyを書いてください。
os.system()等でOS標準のnlコマンドを起動する実装は期待されていません。
テキストデータは、ファイル名が指定されればファイルから、ファイル名が無ければstdinから読み込んでください。
ファイル名が不正であればエラー処理をしてください。
"""
import sys

# 引数チェック
if len(sys.argv) > 1:
    file_in = sys.argv[1]
else:
    file_in = sys.stdin.readline()

# ファイルチェック
try:
    file = open('file_in', 'r')
except IOError:
    print("ファイル[" + file_in + "]開くエラー")
    exit(1)

# メイン処理
lines = file.readlines()
i = 1
for line in lines:
    if line.strip() == '':  # 空行を判定する、行番号つけない
        print('{}'.format(line))
    else:
        # 行番号：５文字長さ、左揃え:< （右揃え：>）
        # 余剰桁はデフォルトspaceで充填。充填文字指定する場合は{:*<5}：”*”で充填
        print('{:<5}{}'.format(i, line))
        i += 1

file.close()
