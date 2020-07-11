s1 = "The quick brown fox jumps over a lazy dog."
s2 = s1[:3]
print(s2)

s2 = s1[16:20]
print(s2)

s2 = s1[4:10] + s1[37:-1]
print(s2)

#スペースで分割されたs1の要素をs1_listに格納
s1_list = s1.split()

#The Lazy brown fox.
s2 = s1_list[0] + " " + s1_list[7] + " " + s1_list[2] + " " + s1_list[3] + s1[-1]
print(s2)
