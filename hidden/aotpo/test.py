import requests
from PIL import Image
import random


randomInt = random.randrange(476713)

response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{randomInt}")
print(f"this number is random {randomInt}")
art = response.json()
image = art['primaryImage']
name = art['objectURL']
title = art['title']
date = art['objectDate']
era = art['period']

print(f"Primary image URL: {image}")
print(f"Image Name: {name}")
print(f"Image Title: {title}")
print(f" Artwork Date: {date}")
print()

