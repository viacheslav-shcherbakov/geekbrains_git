print("Домашнее задание: посчитать сумму чисел в последовательности от А до B, где B>A")
A = int(input("Введите начальное число: "))
B = int(input("Введите конечное число: "))
sum = 0
if A > B:
    print("Вы ошиблись с числами!((")
else:
    if A == B:
        print("Сумма всех чисел = ", A)
        print("А Вы, батенька, хитрец!")
    else:
        while B - A != 0:
            sum += A
            A +=1
        else:
            sum += B
        print("Сумма всех чисел = ", sum)