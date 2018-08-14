import requests
import json
res = requests.get('https://api.github.com/events')

data = res.json()

# write data into a json file 

f = open('result.json', 'w')
f.write(json.dumps(data))
f.close()


