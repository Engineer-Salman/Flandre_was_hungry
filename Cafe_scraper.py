import overpy
import openpyxl
from geopy.distance import geodesic

CENTER = (24.7254, 46.6311) #CCIS_KSU
RADIUS_KM = 50

api = overpy.Overpass() #overpass API

query = f"""
[out:json][timeout:60];
(
  node(around:{RADIUS_KM * 1000},{CENTER[0]},{CENTER[1]})["amenity"~"cafe|bakery"];
  node(around:{RADIUS_KM * 1000},{CENTER[0]},{CENTER[1]})["shop"="bakery"];
  way(around:{RADIUS_KM * 1000},{CENTER[0]},{CENTER[1]})["amenity"~"cafe|bakery"];
  way(around:{RADIUS_KM * 1000},{CENTER[0]},{CENTER[1]})["shop"="bakery"];
  relation(around:{RADIUS_KM * 1000},{CENTER[0]},{CENTER[1]})["amenity"~"cafe|bakery"];
  relation(around:{RADIUS_KM * 1000},{CENTER[0]},{CENTER[1]})["shop"="bakery"];
);
out center tags;
"""
print("Querying Overpass API...")
result = api.query(query)
print("Query complete!")

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Type", "Name", "Latitude", "Longitude", "Phone", "Website", "Email"])

# Helper to extract contact info
def get_contact(tag, keys):
    for key in keys:
        if key in tag:
            return tag[key]
    return ""

for node in result.nodes:
    name = node.tags.get("name", "Unknown")
    lat, lon = float(node.lat), float(node.lon)
    if geodesic(CENTER, (lat, lon)).km <= RADIUS_KM:
        ws.append([
            "Node", name, lat, lon,
            get_contact(node.tags, ["contact:phone", "phone"]),
            get_contact(node.tags, ["contact:website", "website"]),
            get_contact(node.tags, ["contact:email", "email"]),
        ])

filename = "Scraped_data_ksu.xlsx"
wb.save(filename)
print(f"Saved results to {filename}")



