import json

with open("atzfail.json", "r")as f:
    fail_pag = json.load(f)

while True:
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print("Ievadiet ciparu, lai izveletos darbibu")
    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    print("1 = ievadit prieksmetus")
    print("2 = ievadit atzimes")
    print("3 = dzest prieksmetus")
    print("4 = dzest atzimes")
    print("5 = izvadit visus prieksmetus")
    print("6 = paradit konkreta prieksmeta atzimes")
    print("7 = saglabat pasreizejas sesijas darbu faila un iziet")
    print("8 = iziet bez saglabasanas")
#          9 = izvadit pasreizejo "fail_pag" stavokli
    print("::::::::::::::::::::::::::::::::::::::::::::::::")

    izv = str(input("Ludzu izveleties opciju: "))
    
#ievada prieksmetus
    if izv == "1":
        while True:
            prieks_iev = input("Ludzu ievadiet prieksmeta nosaukumu, ko pievienot datubazei vai \"stop\", lai atceltu/parstatu ievadi un atgrieztos pie galvenas izvelnes: ")
            if prieks_iev == "stop":
                break
            elif prieks_iev in fail_pag:
                print("Prieksmets jau eksiste")
            else:
                fail_pag[prieks_iev] = []
                print(f"prieksmets \"{prieks_iev}\" pievienots")

#ievada atzimes izveletaja prieskmeta
    elif izv == "2":
        while True:
            prieks_iev = str(input("Ludzu ievadiet prieksmeta nosaukumu, kuram ievadit atzimes vai \"stop\", lai atceltu/parstatu ievadi un atgieztos pie galvenas izvelnes: "))
            if prieks_iev == "stop":
                break
            elif prieks_iev not in fail_pag:
                print("Izveletais prieksmets neeksiste")
            else:
                print(f"Paslaik ievada atzimes pie prieksmeta \"{prieks_iev}\" (1 - 10 vai \"nv\"), ievadiet \"stop\", lai atceltu/parstatu ievadi un atgrieztos pie prieksmeta izveles")
                while True:
                    print(f"pasreizejais \"{prieks_iev}\" atzimju stavoklis: {fail_pag[prieks_iev]}")
                    atz_iev = input("")
                    if atz_iev == "stop":
                        break
                    elif atz_iev in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                        (fail_pag[prieks_iev]).append(int(atz_iev))
                        print(fail_pag[prieks_iev])
                    elif atz_iev == "nv":
                        (fail_pag[prieks_iev]).append(atz_iev)
                        print(fail_pag[prieks_iev])
                    else:
                        print("Ievadita nederiga atzime, meginiet velreiz")

#izdes izveleto prieksmetu
    elif izv == "3":
        while True:
            prieks_iev = str(input("Ludzu ievadiet prieksmeta nosaukumu, kuru dzest vai \"stop\", lai atceltu/parstatu ievadi un atgriezdos pie galvenas izvelnes: "))
            if prieks_iev == "stop":
                break
            elif prieks_iev in fail_pag:
                fail_pag.pop(prieks_iev)
                print(f"Prieksmets \"{prieks_iev}\" ir dzests")
            else:
                print("Prieksmets neeksiste vai jau dzests")

#izdzes izveletas atzimes izveleta prieksmeta
    elif izv == "4":
        while True:
            prieks_iev = str(input("Ludzu ievadiet prieksmeta nosaukumu, kuram dzest atzimes vai \"stop\", lai atceltu/parstatu ievadi un atgrieztos pie galvenas izvelnes: "))
            if prieks_iev == "stop":
                break
            elif prieks_iev not in fail_pag:
                print("Izveletais prieksmets neeksiste")
            else:
                print(f"Paslaik dzes atzimes pie prieksmeta \"{prieks_iev}\" ievadiet atzimes indeksu saraksta no 0 lidz {len((fail_pag[prieks_iev]))-1} vai \"notirit\""
                      ", lai nodzestu visas atzimes pie prieksmeta, ievadiet \"stop\" lai atceltu/parstatu ievadi un atgrieztos pie prieksmeta izveles")
                while True:
                    print(print(f"pasreizejais \"{prieks_iev}\" atzimju stavoklis: {fail_pag[prieks_iev]}"))
                    atz_iev = input(f"ievadiet 0-{len((fail_pag[prieks_iev]))-1} vai \"notirit\" vai \"stop\": ")
                    if atz_iev == "stop":
                        break
                    elif atz_iev == "notirit":
                        (fail_pag[prieks_iev]).clear
                    elif atz_iev.isnumeric() == True and int(atz_iev) >= 0 and int(atz_iev) <= (len((fail_pag[prieks_iev]))-1):
                        (fail_pag[prieks_iev]).pop(atz_iev)
                    else:
                        print("Ievadits nederigs saraksta indekss")

#izvada visus prieksmetus
    elif izv == "5":
        print()
        for i in (fail_pag.keys()):
            print(i)
        print()

#izvada atzimes izveletajam prieksmetam
    elif izv == "6":
        while True:
            prieks_iev = input("ludzu ievadiet prieksmetu, kam velaties skatit atzimes, vai \"stop\", lai atgrrieztos pie galvenas izvelnes: ")
            if prieks_iev == "stop":
                break
            elif prieks_iev in fail_pag:
                print(fail_pag[prieks_iev])
            else:
                print("Ievaditais prieksmets neeksiste")

#saglaba programmas sakuma izeidoto un programmas gaita mainiito .json faila kopiju: vardnicu "fail_pag" ka jauno .json faila versiju
    elif izv == "7":
        with open("atzfail.json", "w") as g:
            json.dump(fail_pag, g)
        break

#programmu beidz neparrakstot .json failu ar vardnicu "fail_pag" 
    elif izv == "8":
        break

#izvada tagadejo vardnicas "fail_pag" stavokli
    elif izv == "9":
        print(fail_pag)

# atsak ciklu ja ievade nebiija naturals skaitlis no 1-9  
    else:
        print("nederiga izvele, meginiet velreiz")        