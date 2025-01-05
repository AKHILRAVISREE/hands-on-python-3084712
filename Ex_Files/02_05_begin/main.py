import os

father = "Ravi kumar"
Mother = "Sreeja C G"
Son = "Akhil R S"
Wife = "Soubhagya M"

Input_var = os.environ.get("input", Son)

if Input_var == Son:
  print("Akhil is your Son")
elif Input_var == father:
  print("Ravikumar is ",father)
elif Input_var in [Wife,Mother]:
  print(Mother," or ",Wife)
else:
  print("Error in Input")