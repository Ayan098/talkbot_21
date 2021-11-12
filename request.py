import requests

msg = input("request:")
req = requests.post("http://127.0.0.1:5000/predict", json={"message": msg})

print(req.json())
