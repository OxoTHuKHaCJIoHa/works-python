# Буду рад если укажите на ошибки!!


#1 Задание
lst_1 = [1, 2, 4, 0]
lst_2 = []
i = lst_1
x = lambda el: i ** i
lst_2.append(x)
print(lst_2)


lst_1 = [1, 2, 4, 0]
lst_2 = []
for i in lst_1:
    if i == lst_1:
        i ** i
        lst_2.append(i)
print(lst_2)

# 2 Задание
c = []
a = ["Арбуз", "Помидоры", "Авокадо"]
print(a)
b = ["Арбуз", "Лук", "Свекла", "Авокадо"]
print(b)
print("Общий список, {1} {0}".format(a,b))
for i in b:
    if i == a:
        c.append(i)
print(c)


# 3 Задание


import random
lst = []
lst2 = []
for _ in range(10):
    lst.append(random.randint(-10,10))
print(lst)
for i in lst:
    if i>0:
        lst2.append(i)
    if i%3:
        lst2.append(i)
    if i%4:
        lst2.append(i)
else:
    lst.append(i)
print(lst)
print(lst2)
