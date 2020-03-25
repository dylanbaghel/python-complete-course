# abs(), sum() & round() Functions

"""
abs(x):
    --> Returns the absolute value of a number. The argument may be an integer or a floating point number.
sum(iterable):
    --> Takes an iterable and an optional start.
    --> Returns the sum of start and the items of an iterable from left to right and returns the total.
    --> start defaults to 0
round(x):
    --> Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nerest integer to its input.
"""
# abs
print(abs(-55))
print(abs(11))

# sum
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 10))

# round
print(round(10.2))
print(round(1.212121, 2))
print(round(3.51325125, 4))