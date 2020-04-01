#Функція, яка приймає 2 числові аргументи, які задають довжину масиву
##Функція повертає числа з цього проміжку, які мають таку властивість 135 = 1^1 + 3^2 + 5^3
###Якщо таких чисел немає в цьому проміжку - вона повертає пустий список
from math import pow
def func(num1, num2):
    list = [] #створюємо пустий список, в який будемо закидувати вибрані числа
    for i in range(num1, num2+1): #наш рендж чисел
        list1 = [int(j) for j in str(i)] #розбиваємо число
        counter = 1 #counter для порядковості в множенні
        sum = 0
        for n in list1: #ітерюємось по числам та перемножуємо їх
            sum += (pow(n, counter))
            counter+=1
        if i == sum:
            list.append(i)
    return list
print(func(10,89))
