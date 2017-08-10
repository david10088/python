#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Liang'



f = open('number.txt', 'r')
f1 = open('test.txt', 'w')
#print(f.read())
s = set()
for line in f.readlines():

	s.add(line[4::])
	#print(line[4::])
for k in s:
	f1.write(k)
	print(k)

f.close()
#print(s)