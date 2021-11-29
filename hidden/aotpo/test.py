import requests
import random
import json

## 476713 NUMBER OF OBJECTS FROM THE MET MUSEUM

randomInt = random.randrange(476713)

## RANDOM JSON RESPONSE CALL 

response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{randomInt}")

## JSON 
## responseAll = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{randomInt}")
print(f"this number is random {randomInt}")
art = response.json()
image = art['primaryImage']
name = art['objectURL']
title = art['title']
date = art['objectDate']
era = art['period']

## SPECIFIC PULLED DATA ##

print(f"Primary image URL: {image}")
print(f"Image Name: {name}")
print(f"Image Title: {title}")
print(f" Artwork Date: {date}")
print(response.status_code)

## UNSORTED DATA ##

print(response.json())
print()

## SORTED JSON OBJECT STRING ##

def jprint(object):
    text = json.dumps(object, sort_keys=False, indent=4)
    print(text)
jprint(response.json())

