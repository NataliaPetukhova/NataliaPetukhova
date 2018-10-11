
#Problem1
def listToString(a):
	assert type(a)==list
	return str(a)

 
#Problem2
def addBorder(a):
	assert type(a)==list
	assert len(a)>0
	length=len(a[0])
	equal_strings=True
	for string in a:
		if len(string)!=length:
			equal_string=False
	hBorder="+"
	for i in range(length):
		hBorder+="-"
	hBorder+="+"
	for i in range(len(a)):
		a[i]="|"+a[i]+"|"
	return [hBorder]+a+[hBorder]


#Problem3
def shorting(e):
	assert type(e)==list
	for x in range(len(e)):
		if len(e[x])>10:
			e[x]=e[x][0]+str(len(e[x])-2)+e[x][len(e[x])-1]
	return e


#Problem4
def competition(e, k):
	assert type(e)==list
	adv_cont=0
	for i in range(len(e)):
		if e[i]>=e[k] and e[i]>0:
			adv_cont+=1
	return adv_cont


#Problem5
def goodPairs(a, b):
	result=[]
	result_set=set()
	for i in a:
		for j in b:
			if (i*j)%(i+j)==0:
				s = (i ** 2 + j ** 2)
				if s not in result_set:
					result.append(s)
					result_set.add(s)
	result.sort()
	return result

 
#Problem6
def makeShell(n):
	result=[]
	for a in range(n):
		result+=[[0]*(a+1)]
	for a in range(n-1,0,-1):
		result+=[[0]*a]
	return result
