Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def unique(e):
	return sorted([el for el in set(e)])

>>> unique([1,2,1,3])
[1, 2, 3]
>>> unique({5, 1, 3})
[1, 3, 5]
>>> unique('adsfasdf')
['a', 'd', 'f', 's']
>>> 
>>> #Problem1
>>> def unique(e):
	return sorted([el for el in set(e)])

>>> unique([1,2,1,3])
[1, 2, 3]
>>> unique({5, 1, 3})
[1, 3, 5]
>>> unique('adsfasdf')
['a', 'd', 'f', 's']
>>> 
>>> 
>>> #Problem2
>>> def transposeDict(d):
	return{d[key]: key for key in d.keys()}

>>> transposeDict({1: 'a', 2: 'b'})
{'a': 1, 'b': 2}
>>> transposeDict({1: 1})
{1: 1}
>>> transposeDict({}) = {}
SyntaxError: can't assign to function call
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Problem3
>>> def mex(e):
	return next(x for x in range(1, len(e)+2) if x not in set(e))

>>> mex([1, 2, 3])
4
>>> mex(['asdf', 123])
1
>>> mex([0, 0, 1, 0])
2
>>> 
>>> 
>>> #Problem4
>>> def frequencyDict(s):
	return{symdict: s.count(symdict) for symdict in set(s)}

>>> frequencyDict('')
{}
>>> frequencyDict('abacaba')
{'c': 1, 'b': 2, 'a': 4}
>>> 
