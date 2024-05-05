from pprint import pprint
# Create a dict with chemical names as keys & properties as values 
chemicals = {
  "Ethanol": {
    "Formula": "C2H5OH",
    "Boiling Point": 78.4,  # Degrees Celsius
    "State": "Liquid",
    "Corrosive": False
  },
  "Sodium Chloride": {
    "Formula": "NaCl",
    "Melting Point": 801,  # Degrees Celsius
    "Solubility": "High in water"
  },
  "Sulfuric Acid": {
    "Formula": "H2SO4",
    "Density": 1.84,  # g/cm3
    "Corrosive": True,
    "State" : "Liquid"
  }
}
pprint(chemicals)

print('\n')
# Access information using the chemical name (key)
print(chemicals["Ethanol"]["Formula"])  # This will print "C2H5OH"

print(type(chemicals["Ethanol"]["Corrosive"]))
