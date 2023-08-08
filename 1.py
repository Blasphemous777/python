import requests

cities = ['san%20francisco', 'Череповец', 'Шереметьево', 'Лондон']

def get_weather(city):
    url = 'https://wttr.in/' + city + '?lang=ru&?M?m?n?q?T'
    response = requests.get(url)
    response.raise_for_status()
    return response.text    

if __name__ == "__main__":
    for i in cities:
        print(get_weather(i))
