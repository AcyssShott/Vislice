import random
import json

#Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o' 
NAPACNA_CRKA = '-'

## if crka == model.PRAVILNA_CRKA:

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

# Definiramo logični model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #string
        self.crke = crke #list
        return

    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne.append(crka)
        return napacne

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        if self.poraz():
            return False
        else:
            for crka in self.geslo:
                if crka not in self.crke:
                    return False
            return True

    def poraz(self):
        return self.stevilo_napak() >STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz+= ' _'
        niz = niz.strip()    #počistimo presledke
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                     return PORAZ
            else:
                return NAPACNA_CRKA
            
# Izluščimo vse slovenske besede
bazen_besed= []

with open("besede.txt", 'r', encoding= 'utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

                 

# Funkcije za generiranje iger

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])

class Vislice:

    def __init__(self, datoteka_s_stanjem):
        # v slovarju iger ima vsaka svoj ID
        # ID je celo število
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        return

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        #naredi novo igro z naključnim geslom
        igra = nova_igra()
        nov_id = self.prost_id_igre()
        #shrani (ZACETEK, igra) v slovar z novim ID
        self.igre[nov_id] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return nov_id

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        #Pridobi igro
        (igra, _) = self.igre[id_igre]
        #Ugibaj
        nov_poskus = igra.ugibaj(crka)
        #Shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, nov_poskus)
        self.zapisi_igre_v_datoteko()
        return

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as datoteka:
            zakodirane_igre = json.load(datoteka) #dobimo slovar z (geslo, črke)
            igre = {}
            for id_igre in zakodirane_igre:
                igra = zakodirane_igre[id_igre]
                igre[int(id_igre)] = (Igra(igra['geslo'], igra['crke']), igra['poskus'])
            self.igre = igre
        return

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w') as datoteka:
            zakodirane_igre = {}
            for id_igre in self.igre:
                (igra, poskus) = self.igre[id_igre]
                zakodirane_igre[id_igre] = {'geslo': igra.geslo, 'crke': igra.crke, 'poskus': poskus}
            json.dump(zakodirane_igre, datoteka)
        return

