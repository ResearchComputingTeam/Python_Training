# Create a dictionary with chemical names as keys and properties as values 
chemicals = {"Ethanol":"C2H5OH" , "Sodium Chloride":"NaCl" , "Sulfuric Acid":"H2S04"}
# print(chemicals.keys())


if any("NaCl" in entry for entry in chemicals.values()):
    print("yes")
else:
    print("no")

khash = id(chemicals["Ethanol"])
print(khash)

chemicals["key_1"] = "value_1"
chemicals["key_2"] = "value_2"
chemicals["key_3"] = "value_3"
chemicals["key_4"] = "value_4"

print(chemicals)
print(id(chemicals["key_1"]))
print(id(chemicals["key_2"]))
print(id(chemicals["key_3"]))
print(id(chemicals["key_4"]))

# chemicals["Ethanol"] = "Liquid"
# chemicals["Benzene"] = "C6H6"

# print(chemicals)
# removed_value = chemicals.pop("Sulfuric Acid")
# print(chemicals)
# print(removed_value)

# del chemicals["Benzene"]
# print(chemicals)

# chemicals.clear()
# print(chemicals)



