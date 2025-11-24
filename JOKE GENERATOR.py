import requests
import random
print("-"*175)
print(' UNLIMITED JOKE GENERATOR'.center(175," "))
print("-"*175)

def get_joke():
    # Two joke APIs (backup if one fails)
    apis = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://v2.jokeapi.dev/joke/Any?type=single"
    ]
    url = random.choice(apis)
    try:
        response=requests.get(url,timeout=5)
        data=response.json()

        if "setup" in data:
            return data["setup"], data["punchline"]
        elif "joke" in data:
            return data["joke"]
        else:
            return "Oops! Couldn't get a joke right now"
    except:
        return "Oops! Couldn't get a joke"


while True:
    user_input = input("Hit Enter or type 'quit': ").strip().lower()
    if user_input == "quit":
        print("Thanks for laughing! Goodbye 🤝")
        break

    joke = get_joke()
    print(  joke )
    print("-"*150)


