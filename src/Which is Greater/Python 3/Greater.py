list = []
item = input().split()
for i in item:
  list.append(int(i))
a = list[0]
b = list[1]
if a > b:
    print(1)
else:
    print(0)
