'''------===================Задача 5 (1/10)=====================------
Напишите программу, которая будет возводить 2-ку в степень, которая была введена пользователем:
>* Вводится целое неотрицательное число N (N≤100).
Вывод: 2 в степени N
1)надо ввести число
2)не писать отрицательное
'''

try:   
  n = int(input("Введіть число щоб ми віднесли 2 до степеня: "));
except ValueError:
  print("Пишите только число!");
else:
  if (n >= 0):
    print(2 ** n);
  elif(n < 0):
    print("Число должно быть больше 0");