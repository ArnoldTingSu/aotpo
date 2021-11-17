import requests
from PIL import Image
response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/70110")
art = response.json()

image = art['primaryImage']
name = art['objectName']
title = art['title']
date = art['objectDate']
era = art['period']

print(response)

print(art)
print(image)
print(name)
print(title)
print(date)
print()


img=image