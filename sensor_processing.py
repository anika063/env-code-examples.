Add assignment 2 code
ss|stations = [
    {"station_id": "A1", "PM2.5 (µg/m³)": 62},
    {"station_id": "B5", "PM2.5 (µg/m³)": 97},
    {"station_id": "C3", "PM2.5 (µg/m³)": 155},
]

for station in stations:
    sid = station["station_id"]
    info = station  # Now 'info' refers to the current station dictionary

    if info["PM2.5 (µg/m³)"] >= 100:
        status = "danger!"
    else:
        status = "safe"

    print(sid, "", info["PM2.5 (µg/m³)"], "µg/m³", f"({status})")
swsssssSfss
