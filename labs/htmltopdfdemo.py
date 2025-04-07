# converts a web page to a pdf 


import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://en.wikipedia.org"
#targetUrl = "https://www.atu.ie/"

apikey = "knufL1h6lXy5hPmG4dJ3Fj4qsYzGCXauUr0SZ4WV880Ox5FMoxUDdeNtTLLJ59ml"
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)