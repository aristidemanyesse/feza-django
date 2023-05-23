import geojson, requests, json

print("klglrglrk")
url = "./text.json"
with open("./text.json", "r") as file:
    data = json.load(file)
    geometry = data['routes'][0]['legs'][0]['steps'][0]['geometry']
    multilinestring = json.dumps(geometry)
    print(type(multilinestring), multilinestring)
