import requests

url = 'http://localhost:9696/predict'

film = {"title": "enter_the_anime",
        "genre": "documentary",
        "premiere": "august_5,_2019",
        "runtime": 58,
        "rating": 2.5,
        "language": "english/japanese",
        "date": "2019-08-05",
        "year": 2019,
        "month": "aug",
        "week_day": "mon"

        }

response = requests.post(url, json=film).json()
print(response)

if response['low_rate'] == True:
    print('film have a low rate')
else:
    print('film have a high rate' )