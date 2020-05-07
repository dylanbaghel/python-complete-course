import requests

url = 'http://jsonplaceholder.typicode.com/todos'

response = requests.get(
    url,
    headers={'Content-Type': 'application/json'}
)

print(response.text)
print(response.json())

data = response.json()

for todo in data:
    print(f"id: {todo['id']}")
    print(f"Title: {todo['title']}")
    print(f"Completed: {todo['completed']}\n")