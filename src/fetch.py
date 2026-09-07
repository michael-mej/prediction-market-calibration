import requests

payload = {"limit" : 1, "closed" : True}

r = requests.get("https://gamma-api.polymarket.com/markets", params = payload)

if (r.status_code == 200):
    with open("data.Json", "w", encoding = "utf-8") as file:
        file.write(r.text)
else:
    print("opening the Json was unsuccesfull")
