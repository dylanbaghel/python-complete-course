import requests

limit = 5

try:
    limit = int(input('How Many Todos You Need: '))
except:
    print("Invalid Number")

url = 'http://jsonplaceholder.typicode.com/todos'

response = requests.get(
    url,
    headers={'Content-Type': 'application/json'},
    params={
        '_limit': limit
    }
)

data = response.json()

for todo in data:
    print(f"id: {todo['id']}")
    print(f"Title: {todo['title']}")
    print(f"Completed: {todo['completed']}\n")