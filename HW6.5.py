# Сумма цифр вещественного числа
n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)