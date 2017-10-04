#factorial problem
'''The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion. '''

startNum = "e"
while str.isalpha(startNum):
	startNum = input("Loop Method: \nWhat number would you like to find the factorial for? \nEnter a whole number : ")
startNum = int(startNum)

factorial = 1

if startNum != 0:
	for i in range (startNum,0,-1):
		factorial = factorial * i

print (factorial,"\n")



startNum = "e"
while str.isalpha(startNum):
	startNum = input("Recursion Method: \nWhat number would you like to find the factorial for? \nEnter a whole number : ")

def recur_factorial(n):
   """https://www.programiz.com/python-programming/examples/factorial-recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

print("ans = ",recur_factorial(int(startNum)))