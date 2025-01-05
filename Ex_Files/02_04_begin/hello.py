Name = ["Akhil", "Ravi", "Sreeja", "Soubhagya"]
Ages = [10,20,30,40]

i = 0
while i < len(Name):
  #print(Name[i])
  i=i+1

#for name in Name:
  #print(name)

for name, age in zip(Name,Ages):
  print(f"Name:{name},Age:{age}")