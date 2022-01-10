memo = {}

def fibonacci(n: int):
	# Check if we've encountered this input before.
	if n in memo:
		return memo[n]

	# Base cases
	if n == 0 or n == 1:
		return n

	# Recursive step
	output = fibonacci(n-2) + fibonacci(n-1)

	# Memoize the solution before returning
	memo[n] = output
	return output