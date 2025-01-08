# request module
import requests

# response = requests.get("https://www.google.com")

url = "https://jsonplaceholder.typicode.com/posts"
data = {"shek": 10000, "aadi": 13000, "kari": 13090}
headers = {"Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, headers=headers, json=data)
print(response.text)