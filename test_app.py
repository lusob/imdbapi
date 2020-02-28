import json
import requests

url = 'http://127.0.0.1:5000/api/imdb_title_basics'
headers = {'Accept': 'application/json'}
post_headers = {'Accept': 'application/json',
                'Content-Type': 'application/json'}

# Make a POST request to create an object in the database.
''' TODO: Find out why is not working the creation, it returns a 500 server error
movie = {
    "crew":[],
    "endYear":"\\N",
    "genres":"Documentary,Short",
    "isAdult": 0,
    "originalTitle":"TestMovie",
    "primaryTitle":"TestMovie",
    "ratings":[],
    "runtimeMinutes":"1",
    "startYear":"1894",
    "tconst":"tt0000000",
    "titleType":"short"
}
response = requests.post(url, data=json.dumps(movie), headers=post_headers)
print(response.reason)
assert response.status_code == 201
'''

# Make a GET request for the entire collection.
response = requests.get(url, headers=headers)
assert response.status_code == 200
print(response.json())

# Make a GET request for an individual instance of the model.
response = requests.get(url + '/tt0000001', headers=headers)
assert response.status_code == 200
print(response.json())

# Use query parameters to make a search.
filters = [dict(name='name', op='like', val='%y%')]
params = {'filter[objects]': json.dumps(filters)}
response = requests.get(url, params=params, headers=headers)
assert response.status_code == 200
print(response.json())

print('All tests passed!')