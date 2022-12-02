car = {'car': 'Renault', 'Model': 'Duster', 'Color': 'Black', 'Year': 2014}

print(car)

#print(type(car))

#before changes
print(car.keys())
print(car.values())

#After Changes
car["range"]="premium"
print(car.keys())
print(car.values())

print(car.items())

for x in car: 
 print(x)