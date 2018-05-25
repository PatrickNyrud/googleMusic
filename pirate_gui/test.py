import requests
print "RUNNING"
r = requests.get("https://x1337x.eu/popular-movies", 
        proxies={"http": "http://104.25.114.28:80"})
print(r.text)
print "DONE"
