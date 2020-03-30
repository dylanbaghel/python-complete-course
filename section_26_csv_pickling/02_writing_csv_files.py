"""
Writing CSV Files:
    --> Can Write Using Lists or Dictionaries.
"""

from csv import writer, reader

"""
Using List:
    --> 'writer' - creates a writer object for writing to CSV.
    --> 'writerow' - method on a writer to write a row to the CSV.
"""
with open("reviews.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["review", "from", "to"])
    csv_writer.writerow(["Nice Post Man", "Abhishek", "Dylan"])
    csv_writer.writerow(
        ["Amazing Article on this tough topic, thanks", "Jonas", "Kora"])

# Reading Data Then Writing Data Using List

# Approach 1
with open('users.csv') as file:
    csv_reader = reader(file)
    with open('users_approach_1.csv', 'w') as file:
        csv_writer = writer(file)
        for user in csv_reader:
            csv_writer.writerow([u.upper() for u in user])

# Approach 2
with open('users.csv') as file:
    csv_reader = reader(file)
    users_list = [user for user in csv_reader]

with open('users_approach_2.csv', 'w') as file:
    csv_writer = writer(file)
    for user in users_list:
        csv_writer.writerow([u.lower() for u in user])


"""
Using Dictionaries:
    --> 'DictWriter' - Creaters a writer object for writing using dictionaries.
    --> 'fieldnames' - kwarg for the DictWriter specifying headers.
    --> 'writeheader' - method on a writer to write header row
    --> 'writerow' - method on a writer to write a row based on a dictionary.
"""
from csv import DictWriter, DictReader

with open('pets.csv', 'w') as file:
    headers = ['Name', 'Species']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        'Name': 'Blue',
        'Species': 'Cat'
    })
    csv_writer.writerow({
        'Name': 'Hop',
        'Species': 'Rabbit'
    })


# Reading Data Then Writing Using Dictionaries
with open('temp_in_c.csv') as file:
    csv_reader = DictReader(file)
    temps = list(csv_reader)

with open('temp_in_k.csv', 'w') as file:
    headers = ('city', 'temp(in k)')
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for temp in temps:
        csv_writer.writerow({ 
            'city': temp['city'], 
            'temp(in k)': float(temp['temp(in c)']) + 273.15 
        })
