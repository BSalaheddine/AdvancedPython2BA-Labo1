# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

from scipy.integrate import quad

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	res = 1
	if n == 0:
		return 1
	for i in range(1,n+1):
		res *= i
	return res

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = (b**2)-(4*a*b)
	x1 = (-b+(delta**(1/2)))/2*a
	x2 = (-b-(delta**(1/2)))/2*a
	return (x1, x2)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))

import unittest
import utils

class Test(unittest.TestCase):
	def test_fact(self):
		self.assertEqual(utils.fact(0), 1)
		self.assertEqual(utils.fact(2), 2)
		with self.assertRaises(ValueError):
			utils.fact(-1)
	def test_root(self):
		self.assertAlmostEqual(utils.roots(0, 0, 0), (0, 0))
		self.assertAlmostEqual(utils.roots(1, 4, 2), (-2, -2))
		self.assertAlmostEqual(utils.roots(1, 5, 6), (-2, -3))

	#def test_integrate(self):
			#self.assertEqual(utils.integrate(x**2, -1, 1), 0.666)
			#self.assertEqual(utils.integrate(x**4, -3, 2), 55)
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
runner = unittest.TextTestRunner()
print(runner.run(suite))