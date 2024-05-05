# Create a dictionary with reaction names as keys and reactants as values 
reactions = dict()
reactions["Haber-Bosch Process"] = ["N2", "H2"]
reactions["Combustion of Methane"] = ["CH4", "02"]
reactions["Neutralization of Sulfuric Acid"] = ["H2SO4", "NaOH"]
# print(reactions["Haber-Bosch Process"])


# Create a dictionary with chemical names as keys and properties as values 
chemicals = {"Ethanol":"C2H5OH" , "Sodium Chloride":"NaCl" , "Sulfuric Acid":"H2S04"}
# Access information using the chemical name (key)

formula = chemicals.get("NaCl")
if (formula):
    print(formula)
else:
    print("chemical not existing")
