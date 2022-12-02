#Tuples in python----------->& their Operations 

vechile_Tuple =  ("Car","Bus", "scooty", "Byke ", "Bycycle","Train","Flight")
#To print whole Tuple
print(vechile_Tuple)
#To print Data Type
print(type(vechile_Tuple))
#to print specific Element from Tuple by Index Number 
print(vechile_Tuple[2])
#TO know Length Of Tuple 
print(len(vechile_Tuple))
#TO know specific Element Length From Tuple 
print(len(vechile_Tuple[3]))
#TO replce a particular Element
vechile_Tuple[2] = "Scooter"
print(vechile_Tuple)
#Insert Elemnt at last 
vechile_Tuple.append("Metro")
print(vechile_Tuple)
#Insert Elemnt with index Number at desired place  
vechile_Tuple.insert(3,"Auto")
print(vechile_Tuple)
#TO sort Tuple 
vechile_Tuple.sort()
print(vechile_Tuple)
#To Remove Element From Tuple
vechile_Tuple.remove("Auto")
print(vechile_Tuple)
#Remove Elemnt with index Number at desired place  
vechile_Tuple.pop(0)
print(vechile_Tuple)
#To Concinate
#combine = Tuple 1 +Tuple 2 print (combine)
