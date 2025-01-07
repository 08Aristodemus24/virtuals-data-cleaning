import requests
import requests.auth

import os
from pathlib import Path
from dotenv import load_dotenv

env_dir = Path('./').resolve()
load_dotenv(os.path.join(env_dir, '.env'))

if __name__ == "__main__":

    # getting an access token to access the reddit api
    # reddit@reddit-VirtualBox:~$ curl -X POST -d 'grant_type=password&username=reddit_bot&password=snoo' --user 'p-jcoLKBynTLew:gko_LXELoV07ZBNUXrvWZfzE3aI' https://www.reddit.com/api/v1/access_token
    # {
    #     "access_token": "J1qK1c18UUGJFAzz9xnH56584l4", 
    #     "expires_in": 3600, 
    #     "scope": "*", 
    #     "token_type": "bearer"
    # }

    # equivalent python code to this curl request is the ff.
    
    # load env variables
    client_id = os.environ['REDDIT_CLIENT_ID'] 
    client_secret = os.environ['REDDIT_CLIENT_SECRET']
    username = os.environ['REDDIT_USERNAME']
    password = os.environ['REDDIT_PASSWORD']

    # login to reddit account programmatically with credentials
    # to extract a token that can be used to make requests to the reddit api
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    payload = {
        "grant_type": "password", 
        "username": username, 
        "password": password
    }
    headers = {"User-Agent": f"ChangeMeClient/0.1 by {username}"}
    url = "https://www.reddit.com/api/v1/access_token"
    response = requests.post(url, auth=client_auth, data=payload, headers=headers)
    data = response.json()
    token = data['access_token']

    # make sample post to r/test
    url = "https://www.reddit.com/api/submit"
    params = {
        "sr": "test",
        "title": "test title from script",
        "text": "this is a sample text from a python script",
        "kind": "self"
    }
    headers = {
        "Authorization": f"bearer {token}"
    }
    response = requests.post(url, params=params, headers=headers)
    print(response.json())






