'''------===================Задача 9 (3/10)=====================------
Дано трехзначное число. Найдите сумму его цифр.
>*Вводится целое положительное число. Гарантируется, что оно соответствует условию задачи.'''


x = int(input("Введіть трьохзначне число:"));
if( x > 99 and x <1000):
	m = (x // 100) + ((x // 10) % 10) + (x % 10);
	print(m);