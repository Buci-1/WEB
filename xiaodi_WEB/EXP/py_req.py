import requests

x= requests.get('https://ustc.love')

print(x.text.encode('utf-8').decode('utf-8'))
