import sys

print(sys.argv[0])
print(sys.argv[1])
print("Enter a line: ")
line = sys.stdin.readline()     # 读取一行（包括换行符）
print("Line: [%s]\n%s" % (line, "-"*20))