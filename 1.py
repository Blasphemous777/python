import requests

url = 'https://wttr.in/san%20francisco?lang=ru&?M?m?n?q?T'
response = requests.get(url)
response.raise_for_status()
print(response.text)


url = 'https://wttr.in/Череповец?lang=ru&?M?m?n?q?T'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/Шереметьево?lang=ru&?M?m?n?q?T'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/Лондон?lang=ru&?M?m?n?q?T'
response = requests.get(url)
response.raise_for_status()
print(response.text)