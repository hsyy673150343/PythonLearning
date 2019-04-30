#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 18:02
# @Author   : 洪松
# @File     : built_in.py
'''

	    Built-in Functions(内置函数)
abs()	delattr()	hash()	memoryview()	set()
all()	dict()	help()	min()	setattr()
any()	dir()	hex()	next()	slice()
ascii()	divmod()	id()	object()	sorted()
bin()	enumerate()	input()	oct()	staticmethod()
bool()	eval()	int()	open()	str()
breakpoint()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	__import__()
complex()	hasattr()	max()	round()

'''


'''
重要的内置函数 filter()
    """
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
'''

str_1 = ['test_before','b','c','d']

def fun_1(s):
    if s != 'test_before':
        return s

result_1 = filter(fun_1,str_1)
print(list(result_1))

'''
重要的内置函数 map()
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
'''
str_2 = ['test_before','b','c']

def fun_2(s):
    return s +'hongsong'

result_2 = map(fun_2,str_2)
print(list(result_2))

'''
重要的内置函数 reduce()
    """
    reduce(function, sequence[, initial]) -> value
    
    Apply test_before function of two arguments cumulatively to the items of test_before sequence,
    from left to right, so as to reduce the sequence to test_before single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as test_before default when the
    sequence is empty.
    """
'''
from functools import reduce

def add_1(x,y):
    return x + y

print(reduce(add_1,range(1,6)))

'''
匿名函数lambda 
'''

add = lambda a,b : a+b
print(add(2,3))