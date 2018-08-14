import json
res = requests.get('https:///api/users?page=2')

data = res.json()

# write data into a json file 

f = open('result2.json', 'w')
f.write(json.dumps(data))
f.close()