from os import system, name
import math


def main():
    print("[1] Vzorecky a kalkulacka\n"
          "[2] O aplikaci\n"
          "[0] Ukoncit aplikaci")
    inp = input()
    return inp


def main_object():
    print("[1] Krychle\n"
          "[2] Kvadr\n"
          "[3] Valec\n"
          "[4] Kuzel\n"
          "[5] Koule\n"
          "[6] Trojboky hranol\n"
          "[7] Ctyrboky jehlan\n"
          "[0] Zpet")
    inp = input()
    return inp


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


option = main()

while option != "0":
    if option == "1":
        clear()
        option2 = main_object()
        clear()

        while option2 != "0":
            if option2 == "1":
                clear()
                print("Krychle\n"
                      "V = aˆ3\n"
                      "S = 6 * aˆ2")

                try:
                    a = float(input("zadejte stranu a: "))
                    print("Objem krychle:", a ** 3, "\n"
                                                    "Obsah krychle:", 6 * (a ** 2), "\n\n"
                                                                                    "Pro navrat k vyberu teles "
                                                                                    "stisknete enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            elif option2 == "2":
                clear()
                print("Kvadr\n"
                      "V = a * b * c\n"
                      "S = 2 * (ab + ac + bc)")

                try:
                    a = float(input("zadejte stranu a: "))
                    b = float(input("zadejte stranu b: "))
                    c = float(input("zadejte stranu c: "))
                    print("Objem kvadru:", a * b * c, "\n"
                                                      "Obsah kvadru:", 2 * (a * b + a * c + b * c), "\n\n"
                                                                                                    "Pro navrat k "
                                                                                                    "vyberu teles "
                                                                                                    "stisknete "
                                                                                                    "enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            elif option2 == "3":
                clear()
                print("Valec\n"
                      "V = π * rˆ2 * v\n"
                      "S = 2πr * (r + v)")

                try:
                    r = float(input("zadejte polomer: "))
                    v = float(input("zadejte vysku: "))
                    print("Objem valce:", math.pi * (r ** 2) * v, "\nObsah valce:", 2 * math.pi * r * (r + v),
                          "\n\nPro navrat k vyberu teles stisknete enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            elif option2 == "4":
                clear()
                print("Kuzel\n"
                      "V = 1/3π * rˆ2 * v\n"
                      "S = πr * (r + s)")

                try:
                    r = float(input("zadejte polomer: "))
                    v = float(input("zadejte vysku: "))
                    s = float(input("zadejte delku strany: "))
                    print("Objem kuzele:", 1 / 3 * math.pi * (r ** 2) * v, "\n"
                                                                           "Obsah kuzele:", math.pi * r * (r + s),
                          "\n\n"
                          "Pro navrat k vyberu teles stisknete enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            elif option2 == "5":
                clear()
                print("Koule\n"
                      "V = 4/3π * rˆ3\n"
                      "S = 4π * rˆ2")

                try:
                    r = float(input("zadejte polomer: "))
                    print("Objem koule:", 4 / 3 * math.pi * (r ** 3), "\nObsah koule:", 4 * math.pi * (r ** 2),
                          "\n\nPro navrat k vyberu teles stisknete enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            elif option2 == "6":
                clear()
                print("Trojboky hranol\n"
                      "V = Sp * v\n"
                      "S = 2 * Sp + Spl")

                try:
                    a = float(input("zadejte hranu: "))
                    v = float(input("zadejte vysku: "))
                    print("Objem hranolu:", ((math.sqrt(3) / 4) * (a ** 2)) * v, "\n"
                                                                                 "Obsah hranolu:",
                          (2 * ((math.sqrt(3) / 4) * (a ** 2))) + 3 * a * v, "\n\n"
                                                                             "Pro navrat k vyberu teles "
                                                                             "stisknete enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            elif option2 == "7":
                clear()
                print("Ctyrboky jehlan\n"
                      "V = 1/3 * Sp * v\n"
                      "S = Sp + Spl")

                try:
                    a = float(input("zadejte hranu: "))
                    s = float(input("zadejte stranu: "))
                    v = (s ** 2) - ((a / 2) ** 2)
                    v = math.sqrt(v)
                    v2 = (v ** 2) - ((a / 2) ** 2)
                    v2 = math.sqrt(v2)
                    v = v2
                    print("vyska", v)
                    pol = (a + (2 * s)) / 2
                    obs = pol * ((pol - s) ** 2) * (pol - a)
                    obs = math.sqrt(obs)
                    print("Objem jehlanu:", 1 / 3 * (a ** 2) * v, "\n"
                                                                  "Obsah jehlanu:", a ** 2 + (4 * obs), "\n\n"
                                                                                                        "Pro navrat k "
                                                                                                        "vyberu teles "
                                                                                                        "stisknete "
                                                                                                        "enter..")
                except ValueError:
                    print("\n\nNeplatna hodnota! Stisknete enter pro navrat k vyberu teles..")

                input()
                clear()

            else:
                print("Neplatna moznost!!")

                for x in range(15):
                    print()

                print("Pro navrat k vyberu teles stisknete enter..", end="")
                input()
                clear()

            option2 = main_object()
            clear()

    elif option == "2":
        clear()
        print("Unpublished Work © 2022 Petra Spackova")

        for x in range(15):
            print()

        print("Pro navrat do hlavniho menu stisknete enter..", end="")
        input()
        clear()

    else:
        print("Neplatna moznost!!")

        for x in range(15):
            print()

        print("Pro navrat do hlavniho menu stisknete enter..", end="")
        input()
        clear()

    option = main()

clear()
exit()
