'''Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать.
Далее считывает nn строк с числами x_ix
i
​
 , по одному числу в каждой строке. Итого будет n+1n+1 строк.

При считывании числа x_ix
i
​
  программа должна на отдельной строке вывести значение f(x_i)f(x
i
​
 ). Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента xx. Для того, чтобы уложиться в ограничение по времени,
нужно избежать повторного вычисления значений.'''
d={}
k=[]
n=int(input())
for i in range(n):
    x = int(input())
    k.append(x)
for j in range(0,len(k)):
    key=k[j]
    if  key in d:
        print(d[key])
    elif key not in d:
        p = k[j]
        d[key]=f(p)
        print(d.get(key))