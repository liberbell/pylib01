import urllib.request

sample_url = "http://httpbin.org/xml"

resp = urllib.request.urlopen(sample_url)

status_code = resp.status
print(status_code)


if status >= 200 and status_code < 300:
    pass
