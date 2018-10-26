# coding: utf-8

# Комментарий

print("Привет в нашем саду!")
print("So lucky!")
name = input("yout name: ")

print (name, ", welcome!")

answer = input ("go to work? Y/N")

if answer == 'Y':
    print("активировать функцию 1")   
    print("не посылать всех в поход? 2")
    answer = int(input "какой вариант? (1,2)")
    if answer == '1' :
        print("Ну и правильно!")
    if answer == '2' :
         print("тоже верно")
elif answer == 'N':
    print("чао!")




else:
    print("неизвестный выбор")
input()