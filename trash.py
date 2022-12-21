my = ['M', 'D', 'Z', 'J', 'W', 'F', 'B', 'V']
my_new = []

for i in range(3):
    my_new.append(my.pop())
my_new.reverse()
print(f"my: {my}")
print(f"my_new: {my_new}")

my.extend(my_new)
print(my)