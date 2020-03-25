# sorted() Function

"""
sorted():
    --> Returns a new sorted list from the items in iterable.
    --> Returns a new list {not in-place}
"""

# List
nums = [4, 6, 1, 30, 55, 23]
nums_asc_order = sorted(nums)
print(nums_asc_order)
nums_desc_order = sorted(nums, reverse=True)
print(nums_desc_order)

# Tuple
numbers = (55, 85, 23, 55, 21, 1, 55)
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# Complex Data Sorting
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
print(users)

sorted_users_asc = sorted(users, key=lambda user: user['username'])
print(sorted_users_asc)

sorted_users_tweets_length_asc = sorted(users, key=lambda user: len(user['tweets']))
print(sorted_users_tweets_length_asc)