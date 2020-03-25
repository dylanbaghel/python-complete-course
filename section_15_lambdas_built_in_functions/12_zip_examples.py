# zip() Example

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['Abhishek', 'Bittu', 'Dylan']

# Using Comprehension
final_grades = {pair[0]: max(pair[1], pair[2])
                for pair in zip(students, midterms, finals)}
print(final_grades)


# Using map function and lambda
average_marks = zip(
    students,
    map(
        lambda pair: ((pair[0] + pair[1]) / 2),
        zip(midterms, finals)
    )

)
print(dict(average_marks))
