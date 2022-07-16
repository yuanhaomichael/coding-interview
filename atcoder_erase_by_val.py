

# Prompt:
# Given is a sequence of N integers
# Snuke now chooses a value in A. Let x be the value chosen. Then, he makes an integer sequence a by lining up all elements of A that are not x without changing the order.
# Find the lexicographically smallest sequence that can be obtained as a.

class solution:
    def erase_value():
        x=a[-1]
        for i in range(n-1):
            if a[i]>a[i+1]:
                x=a[i]
                break
        
        a=[v for v in a if v!=x]
        print(*a)