## JSD - Tim 5
Petar Cerović R2 33/2022  
Aleksandra Jordanović R2 13/2021  
Tamara Glišić R2 11/2021

## Opis projekta: 

Jezik za generisanje html i pdf dokumenata koji se odnose na gotovinske račune, zahteve za servisiranje i izveštaj o servisiranju.

### Neophodni podaci za gotovinski račun:
```
Prodavac:
	naziv_firme
	adresa
	PIB
Kupac:
	naziv_firme
	adresa
	PIB
Datum_prometa_dobara
Mesto_prometa_dobara
Br_računa
Datum_izdavanja_računa
Mesto_izdavanja_računa
Načina_plaćanja
Artikli: [
	naziv_artikla
	količina
	jedinica_mere
	cena
	popust
	osnovica
	pdv
	iznos
]
ukupan_iznos
```
### Neophodni podaci za zahtev za servisiranje:
```
Naručilac:
	naziv
	adresa
	telefon
	vozilo
	reg_broj
	stanje_km
	broj_šasije
	broj_motora
Lice_za_kontakt:
	ime_prezime
	telefon
	mail
tražene_usluge: []
maksimalan_budžet:
	iznos
	valuta
datum_podnošenja_zahteva
rok_za_završetak
prioritet
```
### Neophodini podaci za izveštaj o servisiranju
```
Naručilac:
	naziv
	adresa
	telefon
	vozilo
	reg_broj
	stanje_km
	broj_šasije
	broj_motora
zahtev_primio
zahtev_izvršio
datum_prijema_zahteva
datum_završetka_radova
izvršeni_radovi: [
	opis
	cena_usluge
]
ugrađeni_delovi: [
	naziv
	količina
	jedinica_mere
	cena
	važenje_garancije_za_deo
]
napomena_servisera
važenje_garancije_za_radove
ukupna_cena


```
## Primer unosa:
```
pocetak
  zahtev_za_servisiranje:
    naručilac:
	naziv: FIrma doo
	adresa: Petra Petrovica 252
	telefon: 00123456
	vozilo: BMW x5
	reg_broj: NS 12345 IR
	stanje_km: 250000
	broj_šasije: ABCD1235WW
	broj_motora: xxxx123
    lice_za_kontakt:
	ime_prezime: Marko Markovic
	telefon: 12345678
	mail: marko@gmail.com
    tražene_usluge: [zamena retrovizora, zamena ulja, zamena akumulatora]
    maksimalan_budžet:
	iznos: 500
	valuta: eur
    datum_podnošenja_zahteva: 2022/06/30
    rok_za_završetak: 2022/07/15
    prioritet: STANDARDNO
kraj
```
