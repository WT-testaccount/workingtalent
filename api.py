print('Start API Read application')

import requests

paginaresults = request.get('https://catfact.ninja/facts')
feitjes = paginaresults.json()

print(feitjes['data'][0])