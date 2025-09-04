import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()

    if data["type"] == "single":
        return data["joke"]
    else:
        return f"{data['setup']} ... {data['delivery']}"