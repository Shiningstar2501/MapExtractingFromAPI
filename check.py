# # import json
# # import requests

# # # Load geojson properties only (ignore geometry)
# # with open("countries_completed.geo.json", "r", encoding="utf-8") as f:
# #     geojson_data = json.load(f)

# # geojson_iso2 = set()
# # for feature in geojson_data["features"]:
# #     iso2 = feature.get("properties", {}).get("iso_a2")
# #     if iso2:
# #         geojson_iso2.add(iso2.upper())

# # # Fetch ISO2 codes from the API
# # url = "https://visacent.com/la/api/visa_eligible_countries/New-Zealand"
# # headers = {
# #     "X-Mashape-Host": "visacent",
# #     "X-Mashape-Key": "visacent@2018"
# # }
# # response = requests.get(url, headers=headers)
# # data = response.json().get("data", {})

# # api_iso2 = set()
# # for category in ["regular_visa", "visa_not_required", "e_visa"]:
# #     for country in data.get(category, []):
# #         code = country.get("country_code")
# #         if code:
# #             api_iso2.add(code.upper())

# # # Find mismatches
# # missing_in_geojson = sorted(api_iso2 - geojson_iso2)
# # matched = sorted(api_iso2 & geojson_iso2)

# # print("✅ Matched ISO2 codes:", matched)
# # print("\n❌ Missing in GeoJSON:", missing_in_geojson)


# import json
# import requests

# # --- Load GeoJSON ISO2 codes ---
# with open("countries_completed.geo.json", "r", encoding="utf-8") as f:
#     geojson_data = json.load(f)

# geojson_iso2 = set()
# for feature in geojson_data["features"]:
#     iso2 = feature.get("properties", {}).get("iso_a2")
#     if iso2:
#         geojson_iso2.add(iso2.upper())

# # --- Fetch from API ---
# url = "https://visacent.com/la/api/visa_eligible_countries/New-Zealand"
# headers = {
#     "X-Mashape-Host": "visacent",
#     "X-Mashape-Key": "visacent@2018"
# }
# response = requests.get(url, headers=headers)
# data = response.json().get("data", {})

# api_iso2 = set()
# api_code_list = []  # Debug list

# for category in ["regular_visa", "visa_not_required", "e_visa"]:
#     for country in data.get(category, []):
#         code = country.get("country_code")
#         if code:
#             upper_code = code.upper()
#             api_iso2.add(upper_code)
#             api_code_list.append(upper_code)

# # --- Sort everything for clearer comparison ---
# sorted_api = sorted(api_iso2)
# sorted_geojson = sorted(geojson_iso2)

# # --- Debug Print ---
# print("==== API ISO2 Country Codes ====")
# print(sorted_api)
# print("\n==== GEOJSON ISO2 Country Codes ====")
# print(sorted_geojson)

# # --- Matching and missing ---
# matched = sorted(api_iso2 & geojson_iso2)
# missing = sorted(api_iso2 - geojson_iso2)

# print("\n✅ Matched ISO2 codes:")
# print(matched)

# print("\n❌ Missing in GeoJSON:")
# print(missing)





import requests
import json

# API URL and headers
url = 'https://visacent.com/la/api/countries_list'
headers = {
    "X-Mashape-Host": "visacent",
    "X-Mashape-Key": "visacent@2018"
}

# Send the request
response = requests.get(url, headers=headers)

# Check and save the response
if response.status_code == 200:
    data = response.json()
    # Save to file
    with open("api_countries_list.json", "w") as f:
        json.dump(data, f, indent=4)
    result = "✅ API data fetched and saved as 'api_countries_list.json'."
else:
    result = f"❌ Failed to fetch API data. Status code: {response.status_code}"

result
