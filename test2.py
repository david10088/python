#!/usr/bin/env python
# -*- coding: utf-8 _*_
from functools import reduce
import os

print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L1 if isinstance(s,str)])

def prod(L):
	def f(x, y):
		return x*y
	return reduce(f, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def normalize(name):
    return name[0].upper()+name[1:].lower()
print(list(map(normalize,['ardm','LiLa','TKLA'])))

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n >0

def primes():
	yield 2
	it = _odd_iter() #初始序列cla	
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primes():
	if(n < 1000):
		print(n)

	else:
		break

#print(list(primes()))

def is_palindrome(n):
	m = str(n)[::-1]
	return int(m) == n

output = filter(is_palindrome, range(1, 100))
print(list(output))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return -t[1]

L2 = sorted(L, key=by_name)
print(L2)