from functions import addition, subtraction, multiplication, division

keuzes = "A) optellen, B) aftrekken, C) vermenigvuldigen, D) delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? "
more = False
uitkomst = 0

choice = input(f"wat wilt u doen? {keuzes}").capitalize()
if choice != "I":
    while choice != "I":
        if choice == "A" or choice == "E":
            if choice == "E":
                other = True
            uitkomst = addition(more, choice, uitkomst)
        elif choice == "B" or choice == "F":
            if choice == "F":
                other = True
            uitkomst = subtraction(more, choice, uitkomst)
        elif choice == "C" or choice == "G":
            if choice == "G":
                other = True
            uitkomst = multiplication(more, choice, uitkomst)
        elif choice == "D" or choice == "H":
            if choice == "H":
                other = True
            uitkomst = division(more, choice, uitkomst)
        choice = input(f"Wil je wat met de uitkomst ({uitkomst}) doen? {keuzes} ").capitalize()
        if choice != "I":
            more = True
        other = False
