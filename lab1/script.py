import requests

response = requests.get("https://raw.github.com/amahesh19/CMPUT404-Lab1/master/script.py")
print(response.text)