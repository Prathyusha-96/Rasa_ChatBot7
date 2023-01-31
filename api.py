import requests
def quote_api():
    url = "https://api.quotable.io/random"
    json_data = requests.get(url).json()
    format_add = json_data['content']
    print(format_add)
    return(format_add)