first_experiment_id : int = input("Versuchs ID eingeben") #input gibt immer ein string zurück(also aufpassen)

try:
  first_experiment_id = int(first_experiment_id) #deshalb hier int()
except ValueError:
  print("Fehler!! Versuchs ID muss eine Zahl sein")

Leistungstest : list =[]

for i in range(10):
    Experimente= { "id" : first_experiment_id,
                  "Versuchsleiter" : "Paul",
                   "Datum" : "14.03.2025"}
    Leistungstest.append(Experimente)
    first_experiment_id += 1

#print(Leistungstest)

for j in range(5):
    print(Leistungstest[j])

count=0
for k in (Leistungstest):
  if int(k["id"]) % 2 ==0: 
    count +=1
print(count)
