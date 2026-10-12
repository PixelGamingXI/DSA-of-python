str = "Anything you like"
print(str[0 : 20]) # 20 is the length of the string, it will print the whole string
print(str[0 : len(str)]) # it will print the whole string, because len(str) will return the length of the string
print(str[:20]) # it will print the whole string, Because it will consider 0 in the beginning

#-----------------------------------------------------------------------------------------------------------------------------------

str = "anything you like like like like like like"
print(str.endswith("er"))  # it will print True if the string ends with "er", otherwise False
print(str.capitalize())  # it will print the string with the first letter capitalized
print(str.replace("o" , "a"))  # it will replace all occurrences of "o" with "a" in the string
print(str.find("y"))  # it will return the index of the first occurrence of "y" in the string, if not found it will return -1
print(str.count("like"))  # it will return the number of occurrences of "like" in the string