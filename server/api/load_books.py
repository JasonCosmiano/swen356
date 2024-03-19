import requests
from api.db_utils import *

def loadBooks() :
    genres = ['romance', 'horror', 'children', 'fiction', 'nonfiction', 'mystery', 'fantasy', 'scifi', 'history']

    for req_genre in genres:

        endpoint = rf'https://openlibrary.org/subjects/{req_genre}.json?details=true'
        response = requests.get(endpoint)

        if response.status_code != 200:
            continue
            
        resp_dict = dict(response.json())

        # Take a look at the response
        # print(response.status_code)
        # with open(r'server\api\response.json', 'w') as f:
        #     f.write(response.text)

        # for key in resp_dict:
        #     print()
        #     print(key)
        #     print(resp_dict[key])

        # Get the list of books ("works" field in JSON response) and 
        # iterate over it, converting each "work" to a dictionary and
        # parsing out information using the keys
        print(f"--------WORKS: {req_genre}--------")
        works = resp_dict['works']
        for work in works:
            work_dict = dict(work)

            # Extract book attributes
            title = work_dict['title']
            genre = req_genre
            author = work_dict['authors'][0]['name']
            page_count = 0
            # publisher = work_dict['publishers'][0]['name']
            publish_year = work_dict['first_publish_year']
            value = 0

            # Sanity check
            print(f"Title: {title}, Genre: {genre}, Author: {author}, Pages: {page_count}, Publish Year: {publish_year}, Value: {value}")   
        
        # Insert into Books Table
            sql_command = """
                INSERT INTO Books(title, genre, author, pub_date)
                VALUES(%s, %s, %s, %s)
            """
            exec_insert_update_delete(sql_command, (title, genre, author, publish_year))
