'''Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):'''
n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])