# Imports should usually be on separate lines(importは一行づつ書くべきです)
# import time, random
import time
import random

# sum はpythonのbuilt-in関数、他の変数名に変更することに推奨する
# sum = 0
counter = 0

# "="のサイドにスペースを入れないです
# before=time.perf_counter()
before = time.perf_counter()

# Immediately before a comma, semicolon, or colon(”:”の左側はスペースがいらないです)
# for i in range(1000000) :
for i in range(1000000):
    # Use 4 spaces per indentation level.
    # 一つのインデントが４つのスペースが推奨です。この行のインデントが深すぎる
    # Immediately before a comma, semicolon, or colon
    # (1 , 100) カンマの直前に空白を入れるの方が推奨です。左側の空白はいらない
    # sum = sum + random.randint(1 , 100)
    counter = counter + random.randint(1, 100)
gaptime = time.perf_counter() - before
# "("の右のスペースがいらないです、")"の左のスペースがいらないです
# ","の左のスペースがいらないです
# "flush = True"キーワード引数や、デフォルトパラメータを示す = の両側にスペースを入れてはいけません
# print( "gaptime:" , gaptime , flush = True )
print("gaptime:", gaptime, flush=True)
