
#Problem1
def unique(e):
	return sorted([el for el in set(e)])



#Problem2
def transposeDict(d):
	return{d[key]: key for key in d.keys()}


#Problem3
def mex(e):
	return next(x for x in range(1, len(e)+2) if x not in set(e))


#Problem4
def frequencyDict(s):
	return{symdict: s.count(symdict) for symdict in set(s)}


