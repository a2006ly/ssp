#你的比萨和我的比萨
my_pizza = ["マルゲリータ", "シーフードピザ", "ベーコン"]
your_pizza = my_pizza[:]
your_pizza.append("照り焼きチキンピザ")
print("My pizza:")
for pizza in my_pizza:
    print(pizza)
print("Your pizza:")
for pizza in your_pizza:
    print(pizza)