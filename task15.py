'''------==================Задача 15 (1/10)====================------
Дано целое число N. Выведите следующее за ним четное число.
>*водится целое положительное число, не превышающее 1000.'''


x = int(input("Введите целое число:"));
if(x < 0 or x >1000):
  print("Введите целое положительное число, не превышающее 1000.");
else:
  print(x + 1)