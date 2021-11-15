import requests

def get_quote():
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    response = requests.get(url).json()
    return f'{response[0]["quote"]} \n said: {response[0]["author"]}'
    
if __name__== "__main__":
    print(get_quote())
