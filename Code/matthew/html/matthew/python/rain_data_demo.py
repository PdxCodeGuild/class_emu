


import requests
import re

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
text = response.text

regex = '(\d+-\w+-\d+)\s+(\d+)'

results = re.findall(regex, text)
print(results)
