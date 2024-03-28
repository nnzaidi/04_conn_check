import requests
from requests.exceptions import ConnectionError

def check_connection():
    url = 'https://www.google.com/'
    print(f'Attempting to access {url} to check internet connection status')

    try:
        print(url)
        resp = requests.get(url, timeout=10)
        resp.text
        resp.status_code
        print(f'Connection to {url} was successful.')
        return True
    
    except ConnectionError as e:
        requests.ConnectionError
        print(f'Connection to {url} failed.')
        return False
    
    except:
        print(f'Connection failed with unparsed reason.')
        return False
    
check_connection()