import requests
res = requests.get('https://tonari-it.com')
with open('tonari-it.html', 'w') as file:
    file.write(res.text)
