'''------===================Задача 2 (3/10)=====================------
Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
   _~_   
  (o o)  
 /  V  \ 
/(  _  )\
  ^^ ^^   
Примечания к задаче 2:
- Не нужно проверять ограничения входных данных: условно, что все введенные данные корректны и соответствуют условию. Т. е. например в этой задаче введенное число N точно будет не меньше 1 и не больше 9.
- Учтите, что вывод данных на экран производится построчно, а не попингвинно.
- Не забудьте, что для вывода бекслеша надо написать два бекслеша подряд.
- Эта задача относительно сложная. Вы можете пока что ее пропустить, и вернуться позже.'''
try: # FN и tab 
	penguis = int(input("Введите число от 1 до 9: "));
except ValueError:
  print("Введите только целое число, пожалуйста.")
else:	
	if (penguis < 1 or penguis > 9):
	  print('Выведите другое число');
	else:
		print("   _~_   " * penguis);
		print("  (o o)  " * penguis);
		print(" /  V  \\ " * penguis);
		print("/(  _  )\\" * penguis);
		print("  ^^ ^^  " * penguis);