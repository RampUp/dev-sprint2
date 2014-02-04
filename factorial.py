# practice - Sidd Tewari 
# Page 56 - Think Python - Factorial function

def factorial(n):
	if not isinstance(n, int):
		print 'Factorial is only defined for integers'
		return None
	elif n < 0:
		print 'Factorial is not defined for negative integers'
		return None
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)

def func_call():
	x = factorial(3)
	print 'x is ', x
	y = factorial(2)
	print y
	z = factorial(0)
	print z
	l = factorial(1.5)
	#print l
	m = factorial('Sidd')
	#print m
	n = factorial(60-85)
	#print n

func_call()

def fun_factorial(n):
	space = ' ' * (4 * n)
	print space, 'factorial', n
	if n == 0:
		print space, 'returning 1'
		return 1
	else:
		recurse = fun_factorial(n-1)
		result = n * recurse
		print space, 'returning', result
		return result

def func_call_fun():
	print '\n --------------------------------------------------'
	fun_factorial(10)

func_call_fun()

