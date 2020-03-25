"""
Generators:
    --> Generators are iterators.
    --> Every Generator is an iterator but not vice-versa.
    --> Generators Can be created with generator functions. Generator functions use the yield keyword.
    --> Generators can be created with generator expressions.
"""

"""
Normal Functions v/s Generator Functions:

# Functions                            | Generator Functions
-----------------------------------------------------------------------------
  1. Uses Return                       | 1. Uses yield
  2. return once                       | 2. can yield multiple times
  3. When invoked, returns the return  | 3. When invoked, returns a generator          
     value                             |
                                       |
"""

def count_up_to(maximum):
   count = 0
   while count < maximum:
     yield count
     count += 1

counter_generator = count_up_to(10)
print(counter_generator)

for num in counter_generator:
  print(num)


def current_beat():
  nums = (1, 2, 3, 4)
  i = 0
  while True:
    if i >= len(nums): i = 0
    yield nums[i]
    i += 1

print("******** BEATS *********")
beat = current_beat()
print(next(beat)) 
print(next(beat))
print(next(beat))


print('***** Fibonacci List ********')
# Normal List Way
def fib_list(maximum):
  nums = []
  a, b = 0, 1
  while len(nums) < maximum:
    nums.append(b)
    a, b = b, a + b
  return nums

print(fib_list(10))

# Generator Way
def fib_gen(maximum):
  x, y = 0, 1
  count = 0
  while count < maximum:
    yield y
    x, y = y, x + y
    count += 1

for fib in fib_gen(20):
  print(fib)
