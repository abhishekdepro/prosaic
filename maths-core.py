def divisor_calculator(num):
	_num=num
	_div=[]
	_div.append(1)
	for i in range(2, num-1):
		if(num%i==0):
			num=num/i
			_div.append(i)
			i=i-1
	_p=[1]
	for i in range(0, len(_div)):
		q=_div[i]
		for j in range(i+1, len(_div)):
			_p.append(_div[j]*q)
	_p.append(_num)
	return _p

def primegenerator(_set):
	_set=[]
	for i in range(2,999):
		if(isPrime(i)==True):
			_set.append(i)
	return _set

def isPrime(num):
	flag=0
	for i in range(2, num-1):
		if num%i==0:
			flag=1
			break
		else:
			continue
	if flag==1:
		return False
	else:
		return True
