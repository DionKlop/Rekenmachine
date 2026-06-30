def addition(more, choice, uitkomst):
    if more == True:
        n1 = uitkomst
    else:
        try:
            n1 = int(input("Geef het eerste getal: "))
        except:
            print("voer een getal in.")
    if choice == "E":
        n2 = 1
    else:
        try:
            n2 = int(input("Geef het Tweede getal: "))
        except:
            print("voer een getal in.")
    print(f"{n1} + {n2} = {n1+n2}")
    n1 = n1 + n2
    return n1

def subtraction(more, choice, uitkomst):
    if more == True:
        n1 = uitkomst
    else:
        try:
            n1 = int(input("Geef het eerste getal: "))
        except:
            print("voer een getal in.")
    if choice == "F":
        n2 = 1
    else:
        try:
            n2 = int(input("Geef het Tweede getal: "))
        except:
            print("voer een getal in.")
    print(f"{n1} - {n2} = {n1-n2}")
    n1 = n1 - n2
    return n1

def multiplication(more, choice, uitkomst):
    if more == True:
        n1 = uitkomst
    else:
        try:
            n1 = int(input("Geef het eerste getal: "))
        except:
            print("voer een getal in.")
    if choice == "G":
        n2 = 2
    else:
        try:
            n2 = int(input("Geef het Tweede getal: "))
        except:
            print("voer een getal in.")
    print(f"{n1} * {n2} = {n1*n2}")
    n1 = n1 * n2
    return n1

def division(more, choice, uitkomst):
    if more == True:
        n1 = uitkomst
    else:
        try:
            n1 = int(input("Geef het eerste getal: "))
        except:
            print("voer een getal in.")
    if choice == "H":
        n2 = 2
    else:
        try:
            n2 = int(input("Geef het Tweede getal: "))
        except:
            print("voer een getal in.")
    print(f"{n1} : {n2} = {n1/n2}")
    n1 = n1 / n2
    return n1

        