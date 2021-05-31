import requests

API_URL = "https://movie-quote-api.herokuapp.com/v1/quote/"

def get_quote():
    res = requests.get(API_URL)
    return res.json()
    
if __name__ == "__main__":
    print(get_quote())