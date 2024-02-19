import requests
from api.db_utils import connect, exec_sql_file


def insert_test_data():
    exec_sql_file('tests/test_data.sql')


def assert_sql_count(test, sql, n,
                     msg='Expected row count did not match query'):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    test.assertEqual(n, cur.rowcount, msg)
    conn.close()


def get_rest_call(test, url, params={}, expected_code=200):
    response = requests.get(url, params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()


def post_rest_call(test, url, params={}, expected_code=200):
    response = requests.post(url, params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()


def get_rest_call(test, url, params={}, get_header={}, expected_code=200):
    response = requests.get(url, params, headers=get_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()


def post_rest_call(test, url, params={}, post_header={}, expected_code=200):
    '''Implements a REST api using the POST verb'''
    response = requests.post(url, params, headers=post_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()


def put_rest_call(test, url, params={}, put_header={}, expected_code=200):
    '''Implements a REST api using the PUT verb'''
    response = requests.put(url, params, headers=put_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def delete_rest_call(test, url, delete_header={}, expected_code = 200):
    '''Implements a REST api using the DELETE verb'''
    response = requests.delete(url, headers = delete_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()