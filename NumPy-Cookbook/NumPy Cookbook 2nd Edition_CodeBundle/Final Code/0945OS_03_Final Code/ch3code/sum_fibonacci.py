import numpy as np

#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

#1. Calculate phi
phi = (1 + np.sqrt(5))/2
print("Phi", phi)

#2. Find the index below 4 million
n = np.log(4 * 10 ** 6 * np.sqrt(5) + 0.5)/np.log(phi)
print(n)

#3. Create an array of 1-n
n = np.arange(1, n)
print(n)

#4. Compute Fibonacci numbers
fib = (phi**n - (-1/phi)**n)/np.sqrt(5)
print("First 9 Fibonacci Numbers", fib[:9])

#5. Convert to integers
# optional
fib = fib.astype(int)
print("Integers", fib)

#6. Select even-valued terms
eventerms = fib[fib % 2 == 0]
print(eventerms)

#7. Sum the selected terms
print(eventerms.sum())
