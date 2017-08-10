#!/usr/bin/env python3
# -*- coding: utf-8 _*_

import math

def move(x,y,step,angle = 0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx, ny


x, y = move(100, 100, 60, math.pi/6)
print(x, y)
r = move(100, 100, 60, math.pi/6)
print(r[0])
print(r[1])
print(r)

def power(x):
	return x*x

print(power(3.14))

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

# a = int(input('Plesase input a number:'))
# print(fact(a))

# def a(n):
# 	return  b(n, 1)

# def b(num, sum1):
# 	if num == 1:
# 		return sum1
# 	return b(num - 1 ,num * sum1)

# def fact1(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

# b1 = int(input('Please input b:'))
# print(a(b1))

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key, ':', d[key])

L = [x * x  for x in range(3, 15)]
print(L)
print(L[2:8:])

LL = [x * x for x in range(3, 30) if x % 3 == 0]
print(LL)

LLL = [x + y for x in 'ABC' for y in '123456']
print(LLL)