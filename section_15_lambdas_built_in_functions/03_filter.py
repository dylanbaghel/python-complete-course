# filter() Function

"""
filter:
    --> Filter The Iterable Using a condition, if true means included else excluded.
"""

data = [
    {
        'id': '1',
        'name': 'Abhishek'
    },
    {
        'id': '2',
        'name': 'Dylan'
    },
    {
        'id': '3',
        'name': 'Bittu'
    }
]

found = list(filter(lambda d: d['id'] == '1', data))
print(found)
