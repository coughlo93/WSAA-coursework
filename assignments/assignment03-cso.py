import requests

url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'
response = requests.get(url)
with open('cso.json', 'wb') as file:
    file.write(response.content)
print('File downloaded')
