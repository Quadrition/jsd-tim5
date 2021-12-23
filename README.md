### Opis projekta: 

Jezik za kreiranje turistickih ponuda, koji treba da omogući brz i efikasan unos ponuda u bazu.
  Za opis jedne ponude potrebno je uneti lokaciju, tip ponude, smestaj, periode relizacije, smestajne jedinice itd.
	Jezik je baziran na textX gramatici.


### Primer:
```
turisticka_ponuda {
	id: 1235468,
	lokacija: kopaonik,
	tip_ponude: zimovanje,
	smestaj: hotel Pahulja,
	prevoz: bus,
	periodi: {
		period {
			od: 2022/01/01,
			do: 2022/01/08,
		},
		period {
			od: 2022/01/08,
			do: 2022/01/15,
		},
	},
	smestajne_jedinice {
		smestajna_jedinica {
			naziv: Ap5,
			tip: apartman,
			opis: 'pogled na dvoriste',
			detalji {
				spavaca_soba: true,
				dnevni_boravak: true,
				kapacitet: 4,
				kuhinja: true,
				terasa: false,
				dozvoljeno_pusenje: false,
				tv: true,
				mini_bar: true,
				ac: false,
			},
		},
		smestajna_jedinica {
			naziv: Ap4,
			tip: apartman,
			opis: 'pogled na ski stazu',
			detalji {
				spavaca_soba: true,
				dnevni_boravak: true,
				kapacitet: 4,
				kuhinja: true,
				terasa: false,
				dozvoljeno_pusenje: false,
				tv: true,
				mini_bar: true,
				ac: false,
			},
		},
		smestajna_jedinica {
			naziv: S1,
			tip: soba,
			opis: 'pogled u zgradu',
			detalji {
				kapacitet: 4,
				tv: true,
				mini_bar: true,
				ac: false,
				dozvoljeno_pusenje: false,
			},
		},
		smestajna_jedinica {
			naziv: S2,
			tip: soba,
			opis: 'pogled na sumu',
			detalji {
				kapacitet: 4,
				tv: true,
				mini_bar: true,
				ac: false,
				dozvoljeno_pusenje: false,
			},
		},
	}
}
```
