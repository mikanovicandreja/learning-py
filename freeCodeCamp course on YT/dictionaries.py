# Dictionaries in Python

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items in dictionaries
print(band["vocals"])
print(band.get("guitar"))