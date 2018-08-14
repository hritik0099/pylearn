import http.client
conn = http.client.HTTPSConnection("https://api.github.com/events" , 443)
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
