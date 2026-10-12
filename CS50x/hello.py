name = str(input("What is your name? "))
s = True
while s:
 s = False
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor!")

    case "Draco":
        print("Slytherin!")
    case "Voldemort":
        print("WHAT! It's He Who Must Not Be Named!")
        print("But still.....")
        print("Slytherin")
        print(" Avada Kedavra! ")
    case _:
        print("WHO? ")

s = True