'''------===================Задача 3 (1/10)=====================------
N школьников делят K яблок поровну, не делящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
>* Программа получает на вход числа N и K — натуральные, не превышают 10000.
1)
'''

children = int(input("Ввелите количество школьников:"));
apples = int(input("Введите количество яблок:"));
if(children > 10000 or apples > 10000):
	print("Максимальное значение - 1000");
	exit();
apple_count = apples // children;
print("Всем детям достанется по %i яблок" % apple_count);



# if(children and apples > 10000):
#   print("Ви ввели забагато тексту, макс. кількість символів - 10000 ");
# elif(children and apples <1):
#   print("Дію виконати не можливо(");
# elif(children > apples):
#   print("Поровну яблок невозможно поделить поровну на детей(");
# elif (apples // children == 0):
#   print("");
#   print("Корзина - пусто");
# else:
#   print("");


#  if(children > 10000 or apples > 10000):
#  	print("Максимальное значение - 1000");
#  	exit();
#  apple_count = apples // children;
#  print("Всем детям достанется по %i яблок" % apple_count);
  