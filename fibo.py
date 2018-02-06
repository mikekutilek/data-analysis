from math import sqrt

def fibo1(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibo1(n-1) + fibo1(n-2)

def fibo2(n):
	return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))



