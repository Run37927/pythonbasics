import requests

req = requests.get("https://hairun.netlify.app")
print(req.status_code)
