import requests
import json

def chamada_api(endpoint):
    url = 'https://disease.sh/v3/covid-19/countries/' + endpoint
    print (url)

    response = requests.get(url, )

    return response

chamada = chamada_api('br')
print (chamada.status_code)
print (chamada.text)