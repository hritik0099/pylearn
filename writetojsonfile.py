import json
 
data = {
    "FirstName":"HA",
    "DateOfBirth":"30/01/89",
    },

jsonData = json.dumps(data)
print(jsonData)
 
with open('info.json', 'w') as f:
     json.dump(jsonData, f)