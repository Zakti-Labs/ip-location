import requests
f = open('ips.txt', 'r')
ips = f.readlines()
ips = list(map(lambda x: x.strip(), ips))
f.close()
for ip in ips:
    r = requests.get('http://ip-api.com/json/{}'.format(ip))
    json = r.json()
    print(
"""
IP Address: {}
Country: {}
Region: {}
City: {}
Zip/Postal Code: {}
ISP: {}
Organization: {}
Latitude: {}
Longitude: {}
""".format(json["query"], json["country"], json["regionName"], json["city"], json["zip"], json["isp"], json["org"], json["lat"], json["lon"])
    )