import urllib.request
import json

req = urllib.request.urlopen("http://httpbin.org/json")
data = req.read().decode("utf-8")
print(data)

obj = json.loads(data)
print(obj["slideshow"]["author"])

objdata = {
    "name": "Joe Marine",
    "author": True,
    "titles": [
    "Leading Python", "Advanced Python", "Python Standard Library Essential Training"
    ]
}
