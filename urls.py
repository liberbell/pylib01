import urllib.parse

sample_url = "http://server.example.com:8080/example.html?val1=1&val2=Hello+World"

result = urllib.parse.urlparse(sample_url)
print(result)
print(result.scheme, result.hostname, result.path)
print(result.geturl())

sample_string = "Hello El Nino"

query_data = {
    "Name": "Jhon Doe",
    "City": "Anytown USA",
    "Age": 37
}
