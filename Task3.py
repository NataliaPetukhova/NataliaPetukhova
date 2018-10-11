
#Problem1
def squares(a):
	for i in a:
		yield iter(i)**2


#Problem2
def repeatntimes(elems, n):
	it=itertools.tee(elems,n)
	for i in it:
		yield from i


#Problem3
def evens(x):
	if x%2:
	   x=+1
	while True:
		x+=2
		yield x


#Problem4
def digitsumdiv(p):
	for i in itertolls.count(1):
		if not sum(map(int,str(i)))%p:
			yield i

			
#Problem5
def extractnumbers(s):
	return filter(lambda x: x.isdigit(),s)


 
#Problem#6
def changecase(s):
	return map(lambda x: x.swapcase() if x.isalpha() else x,s)


>>> 
