Hogwarts = ["Harry", "Ron", "Hermione", "Draco", "Snape"]
Hogwarts.append("Hagrid") # Will add hagrid to the end of the list
print(Hogwarts)

#------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts.sort() # Will sort the list in alphabetical order
print(Hogwarts)
#------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts.sort(reverse = True) # Will sort the list in reverse alphabetical order
print(Hogwarts)
#------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts.reverse() # Will reverse the order of the list
print(Hogwarts)
#------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts.insert(5, "Professor McGonagall") # Will insert Professor McGonagall at index 5
print(Hogwarts)        
#------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts.remove("Professor McGonagall") # Will remove Professor McGonagall from the list
print(Hogwarts)
#------------------------------------------------------------------------------------------------------------------------------------------------------
Hogwarts.pop(3) # Will remove the item at index 3 (Draco) from the list
print(Hogwarts)