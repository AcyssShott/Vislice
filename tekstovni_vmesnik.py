#Funkcije, ki generirajo izpis za igralca
import model

def izpis_poraza(igra):
    return 'Porabili ste preveč poskusov. Pravilno geslo ne {}.'.format(igra.geslo)

def izpis_zmage(igra):
    return 'Uspešno ste uganili geslo {}!'.format(igra.geslo)

def izpis_igre(igra):
    tekst = (
        '===============================\n\n'
        '    {trenutno_stanje}\n\n'
        'Poskusili ste ze :{poskusi}\n\n'
        '===============================\n\n'
    ).format(trenutno_stanje=igra.pravilni_del_gesla(), poskusi = igra.nepravilni_ugibi())

    return tekst

def zahtevaj_vnos():
    vnos = input('Poskusi uganiti črko: ')
    return vnos

def preveri_vnos(vnos):
    #Funkcija vrne true, če je vnos primeren,sicer igralca opozori in vrne False
    if len(vnos) != 1:
        print('Neveljaven vnos! Vnesi zgolj eno črko!')
        return False
    else:
        return True

#Izvajanje umesnika

def zazeni_vmesnik():
    igra = model.nova_igra()

    while True:
        #izpišemo stanje
        print(izpis_igre(igra))
        #igralec ugiba
        poskus = zahtevaj_vnos() # !! še ni napisano!!
        if not preveri_vnos(poskus):
            continue

        rezultat = igra.ugibaj(poskus)
        #preverimo, če je igre konec
        if igra.poraz(): #if rezultat = model.poraz:
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return


