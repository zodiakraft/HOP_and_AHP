import tkinter as tk
import os

def sign(a):
    if a>0:
        return '+'
    elif a<0:
        return '-'
    else:
        return '+'

def gcd(a,b): # обычный алгоритм Евклида
    return(a if b==0 else gcd(b, a%b))

def cases(A,B,C): # проверка на особые случаи
    if A == B == 0:
        if C == 0: #0x + 0y = 0
            print('ок...')
        else: # 0x + 0y = x; x!=0
            print('x,y - принадлежит пустое множество')
    elif A == 0: # By = C
        print('y =', C/B)
    elif B == 0: # Ax = C
        print('x =', C/A)
    elif C==0: # Ax + By = 0
        print('x = 0',sign(B), abs(B),'*k\ny= 0',sign(-A), abs(A),'*k')
        result(0,0,A,B)
    elif C%gcd(A,B) == 0: # Евклид
        main(A,B)
    else: # алгебраический метод
        print('x = 1',sign(B), abs(B) ,'*k\ny = ',(C-A),'/',B,sign(-A),abs(A),'*k', sep='')

def main(a,b): # расширенный алгоритм Евклида
    print('Расширенный алгоритм Евклида:')
    A, B = a, b
    x, xr, y, yr = 1, 0, 0, 1
    while b:
        q = a//b
        a, b=b, a%b
        x, xr = xr, x - xr*q
        y, yr = yr, y - yr*q
    x, y,A,B = x*(C/gcd(A,B)), y*(C/gcd(A,B)),A/gcd(A,B),B/gcd(A,B)
    print('x=', x, sign(B), abs(B) ,'*k;')
    print('y=', y, sign(-A), abs(A) ,'*k')
    result(x,y,A,B)

def result(x, y, A, B, i=1): # вывод решений
    print('Пары решений для k[-1; 1]:\n')
    for k in range(-i,i+1):
          print('x=',x+(B*k),';\ny=',y-(A*k),';\n','k=',k, '\n', sep='');
    print('где k - это любое целое число')

def testcases():
    """прошу не обращать на это внимание, это нужно было для траблшутинга
        пометка себе: если два случая похожи то проверка прошла успешно"""
    if (cases(2,0,1)==0.5)==(cases(0,2,1)==0.5)==(cases(0,0,1)==False)==(cases(2,0,0)==0)==(cases(0,0,0)=='ок...'):
        print('passed')
    else:
        print('error')

print('Введитие коеффиценты для \nAx + By = C')
try:
    A, B, C = int(input('A = ')), int(input('B = ')), int(input('C = '))
    print(A,'x + ',B,'y = ',C, sep='')
    cases(A,B,C)
except ValueError:
    print('только цифры, попробуй снова.')
    
os.system('pause')