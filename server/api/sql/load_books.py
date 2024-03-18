import requests

search_endpoint = r'https://openlibrary.org/search.json?q='
query = r'the+lord+of+the+rings'

r = requests.get(search_endpoint+query)
print(r.status_code)
print(r.text)
