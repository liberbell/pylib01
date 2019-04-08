import urllib.request

sample_url = "http://httpbin.org/xml"

resp = urllib.request.urlopen(sample_url)

status_code = resp.status
print(status_code)


if status_code >= 200 and status_code < 300:
    print(resp.getheaders())
    print(resp.getheader("Content-length"))
    print(resp.headers('Content-type'))
