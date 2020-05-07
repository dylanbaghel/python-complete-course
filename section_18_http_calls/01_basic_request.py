import requests as r

response = r.get("https://news.ycombinator.com")

print(response.status_code)
print(response.headers)
print(response.text);