import random

NUM_POCET = 3 #3 #zadanie maximalnej velkosti cisla na hadanie
MAX_GUESSES = 10 #zadanie maximalneho poctu pokuv pre hadnutie cisla


#telo hlavnej funkcie
def main():
    while True:
        taj_cislo = getSecretNum() #vytvorenie tajneho cisla
        print("Myslim si cislo")
        print("Mas {} pokusov na uhadnutie cisla.".format(MAX_GUESSES))
        akt_pokus = 1

        #pokial je pocet zivotou mensi ako pocet hadanych cisel hra bude pokracovat
        while akt_pokus <= MAX_GUESSES:
            pokus = ''
            #urcenie ake napovedy maju byt vypisane pri zadani cisla
            # ak ani jedno cislo nie je rovne ziadnemu cisli v trojcisli co bolo zadane ale je zadane nieco ine ako cislo
            while len(pokus) != NUM_POCET or not pokus.isdecimal():
                print("Pokus cislo {} => ".format(akt_pokus))
                pokus = input("> ")
            
            napovedy = getNapovedy(pokus, taj_cislo)
            print(napovedy)
            akt_pokus += 1

            #ak je hadane cislo rovne typovanemu
            if pokus == taj_cislo:
                print("Spravne cislo!")
                break

            #ak hrac prekroci pocet pokusov
            if akt_pokus > MAX_GUESSES:
                print("Pozor! Prekrocil si maximalny pocet pokusov!")
                print("Spravna odpovd bola: {}".format(taj_cislo))

        #spytanie sa hraca ci chce hrat dalsiu hru
        print("Chces hrat dalsiu hru? (yes alebo no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Dakujem za hru!")

#generuje niekolko ciferne cilo ale generuje nahodne usporiadany string s danym mnozstvom cisel
def getSecretNum():
    cisla = list("0123456789") #vytvorenie listu obsahujuci vsetky cisla od 0 po 9
    random.shuffle(cisla) #pomiesanie cisel v liste hodnot

    #z pomiesaneho listu sa vytiahne mnozstvo cisel podla NUM_POCET. Takto sa vytvori string obsahujuci cisla a podla mnozstva moze ziskat max 10 cif. cislo
    taj_cislo = ''
    for i in range(NUM_POCET):
        taj_cislo += str(cisla[i])
    return taj_cislo

#Vytvorenie funkcie pre tvorbu napovedy
def getNapovedy(pokus, taj_cislo):
    #ak je napveda rovnaka ako tajne cislo
    if pokus == taj_cislo:
        return "Spravne!"
    
    #vytvorenie prazdnej napovedy
    napoveda = []

    #tvorba napovedy
    for i in range(len(pokus)):
        #ak sa jedno cislo nachadza v casti hladaneho cisla a je na spravnom mieste
        if pokus[i] == taj_cislo[i]:
            napoveda.append("Fermi")

        #ak sa jedno cislo nachadza v casti hadaneho cisla ale nie je na spravnom mieste
        elif pokus[i] in taj_cislo:
            napoveda.append("Pico")
    
    #ak sa v typovanom cisle nenachadza ani jedna cislica
    if len(napoveda) == 0:
        return 'Bagels'
    else:
        napoveda.sort()
        return " ".join(napoveda)
    
#spustenie programu
if __name__ == '__main__':
    main()

