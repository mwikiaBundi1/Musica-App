from app import app
import urllib.request as request
import json 
def quotes():
    with request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
    return data
