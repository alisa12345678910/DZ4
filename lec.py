# # 1.Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

# n = int(input('Введите точность: '))
# pi = 0
# for a in range(n):
#     pi += (1 / 16 ** a) * (4 / (8 * a + 1) - 2 / (8 * a + 4) - 1 / (8 * a + 5) - 1 / (8 * a + 6))
# print('Число ПИ: ', round(pi, n))


# # 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# # number=int(input("Введите число: "))
# for i in range(1, number+1):
#     if(number%i==0):
#         print(i)

# # 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# #  элементов исходной последовательности.

# A = [1, 2, 3, 2, 5, 1]
# found = set()
# found_again = set()

# for a in A:
#     if a in found_again:
#         continue
#     if a in found:
#         found.remove(a)
#         found_again.add(a)
#     else:
#         found.add(a)

# print(list(found))

# # 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# # (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# # *Пример:* 

# # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint as rd

# k = int(input('Введите K: '))
# for i in range(k, 0, -1):
#     x = rd(-100, 100)
#     if x > 0:
#         print(f"+{x}x^{i}", end=' ')
#     else:
#         print(f"{x}x^{i}", end=' ')

# print(rd(-100,100), end='')
