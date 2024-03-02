import requests
# import db_utils

# search_endpoint = r'https://openlibrary.org/search.json?q='
# query = r'horror'

# r = requests.get(search_endpoint+query)
# print(r.status_code)
# print(r.text)

subject_endpoint = r'https://openlibrary.org/subjects/romance.json?limit=1?details=true'
response = requests.get(subject_endpoint)
print(response.status_code)
# print(response.json())
resp_dict = dict(response.json())

for key in resp_dict:
    print()
    print(key)
    print(resp_dict[key])

print("--------WORKS--------")
works = resp_dict['works']
for work in works:
    work_dict = dict(work)
    # print(work)
    print(work_dict.keys())
    title = work_dict['title']
    genre = work_dict['subject']
    author = work_dict['authors']
    page_count = 0
    publisher = 'first_publish_year'
    value = 0
