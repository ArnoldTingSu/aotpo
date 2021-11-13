import requests
response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/70110")
art = response.json()

image = art['primaryImage']

print(response)
print(art)
print(image)


img=image