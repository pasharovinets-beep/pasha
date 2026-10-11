from math import *
def mean(a,n):
    return sum(a)/n
def sem(a,n,sr):
    if n<2:
        return 0
    rkv=[] #(xi-sr(x))^2
    for i in range(n):
        rkv.append((a[i]-sr)**2)
    return (sum(rkv)/(n*(n-1)))**0.5


data=[float(i) for i in input("Введите данные через пробел: ").split()]
n=len(data)
sr=mean(data,n)
sa=sem(data,n,sr)
print(f'Среднее: {sr}')
print(f'Стандартная ошибка: {sa}')
