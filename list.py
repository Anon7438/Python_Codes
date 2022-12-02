#list in python----------->& their Operations 

vechile_list =  ["Car","Bus", "scooty", "Byke ", "Bycycle","Train","Flight"]
#To print whole list
print(vechile_list)
#To print Data Type
print(type(vechile_list))
#to print specific Element from List by Index Number 
print(vechile_list[2])
#TO know Length Of List 
print(len(vechile_list))
#TO know specific Element Length From List 
print(len(vechile_list[3]))
#TO replce a particular Element
vechile_list[2] = "Scooter"
print(vechile_list)
#Insert Elemnt at last 
vechile_list.append("Metro")
print(vechile_list)
#Insert Elemnt with index Number at desired place  
vechile_list.insert(3,"Auto")
print(vechile_list)
#TO sort List 
vechile_list.sort()
print(vechile_list)
#To Remove Element From List
vechile_list.remove("Auto")
print(vechile_list)
#Remove Elemnt with index Number at desired place  
vechile_list.pop(0)
print(vechile_list)
#To Concinate
#combine = list 1 +list 2 print (combine)
