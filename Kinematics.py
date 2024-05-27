from ClassBank import FindS, FindU, FindV, FindA, FindT

findS = FindS()
findU = FindU()
findV = FindV()
findA = FindA()
findT = FindT()

result = 0


def conc():
    print("Answer: " + str(result))


# Converts all input to lowercase, - remove special chars/pass error
# var2 sorts input to alphabetical order
var1 = input("Variable to be found: ").lower()
var2 = "".join(sorted(input("Variables available: ")))


# Chooses formulae based on required variables
def kinematics():
    global result
    if var1 == "s":
        if var2 == "atu":
            result = findS.noV()
            print(conc())
        elif var2 == "tuv":
            result = findS.noA()
            print(conc())
        elif var2 == "auv":
            result = findS.noT()
            print(conc())
        else:
            print("Syntax error!")
    elif var1 == "u":
        if var2 == "ast":
            result = findU.noV()
            print(conc())
        elif var2 == "stv":
            result = findU.noA()
            print(conc())
        elif var2 == "asv":
            result = findU.noT()
            print(conc())
        elif var2 == "atv":
            result = findU.noS()
            print(conc())
        else:
            print("Syntax error!")
    elif var1 == "v":
        if var2 == "stu":
            result = findV.noA()
            print(conc())
        elif var2 == "asu":
            result = findV.noT()
            print(conc())
        elif var2 == "atu":
            result = findV.noS()
            print(conc())
        else:
            print("Syntax error!")
    elif var1 == "a":
        if var2 == "stu":
            result = findA.noV()
            print(conc())
        elif var2 == "suv":
            result = findA.noT()
            print(conc())
        elif var2 == "tuv":
            result = findA.noS()
            print(conc())
        else:
            print("Syntax error!")
    elif var1 == "t":
        if var2 == "suv":
            result = findT.noA()
            print(conc())
        elif var2 == "auv":
            result = findT.noS()
            print(conc())
        elif var2 == "asv":
            result = findT.noU()
            print(conc())
        else:
            print("Syntax error!")
    else:
        print("Variable entered is invalid.")