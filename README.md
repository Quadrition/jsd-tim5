## JSD - Tim 5
Petar Cerović R2 33/2022  
Aleksandra Jordanović R2 13/2021  
Tamara Glišić R2 11/2021

## Opis projekta: 

Jezik za beleženje poena na odbojkaškim  utakmicama nakon čega se dobija izgenerisan pdf izveštaj o statističkim podacima kao što su:
- poeni po setu
- najčešće gađane zone pri servisu 
- najčešće gađane zone pri prebačenim loptama
- najduža razmena lopti
- prosečna dužina razmenjenih lopti...


## Primer unosa:
```
begin
    teamA: 'ZOK Novi Sad'
    teamB: 'Radnicki' 
  set 1 {
  	team A serve 10 from 6 to 6 . B6 receive B88 over from 4 to 3 . A25 receive out,
	team B serve 23 from 6 to 1 . A6 receive A10 pass A4 over from 2 to 5 . B25 receive net,
	team A serve 12 from 5 to 3 ace
    }
    set 2 {
  	team A serve 10 from 6 to 1 . B6 receive B88 over from 4 to 3 . A25 receive out,
	team B serve 23 from 6 to 1 . A6 receive A10 pass A4 over from 2 to 5 . B25 receive net,
	team A serve 12 from 5 to 3 ace
    }
end
```
## Instrukcije za poretanje
```
git clone https://github.com/Quadrition/jsd-tim5.git
cd jsd-tim5  // pozicionirati se u folder repozitorijuma
python -m venv venv // kreirati okruzenje
venv\Scripts\activate.bat // aktivirati okruzenje
pip install -r requirements.txt // instaliranje neophodnih biblioteka
pip install -e . 
cd src 
textx generate src.sctv --target csv+pdf // generisanje izvestaja za primer src.sctv
```
