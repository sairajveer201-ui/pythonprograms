import sys
sys.path.append("./code")

from largest_number import largest

assert largest(10, 20, 30) == 30
assert largest(50, 20, 10) == 50
assert largest(10, 40, 20) == 40
assert largest(5, 5, 2) == 5

print("All test cases passed")