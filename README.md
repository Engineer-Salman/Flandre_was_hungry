# Flandre Was Hungry

**Flandre Was Hungry** is a Python automation script that queries the OpenStreetMap (OSM) database for all cafés and bakeries within a 50 km radius of CCIS (King Saud University, Riyadh), and exports the results — including names, locations, and any available contact info — into an Excel file.

Perfect for local outreach, PR stunts, or just stalking your next croissant.

---

## 🍰 Features

- Queries OSM using Overpass API via `overpy`
- Filters for relevant business types:
  - `amenity=cafe`
  - `amenity=bakery`
  - `shop=bakery`
- Extracts and exports:
  - Name
  - Latitude / Longitude
  - Phone number
  - Website
  - Email
- Outputs to `Scraped_data_ksu.xlsx`

---

## 🔧 Requirements

```bash
pip install overpy openpyxl geopy
