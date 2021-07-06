'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки
 сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.'''
a = int(input())
b = int(input())
c = int(input())

if a>=b and a>=c:
  print(a)
  if b>=c:
    print(c)
    print(b)
  else :
    print(b)
    print(c)
elif b>=c and b>=a:
  print(b)
  if a>=c:
    print(c)
    print(a)
  else:
    print(a)
    print(c)
else:
  print(c)
  if b>=a:
    print(a)
    print(b)
  else:
    print(b)
    print(a)