import requests
from bs4 import BeautifulSoup
import json

url = "https://www.fiskistofa.is/veidar/aflaupplysingar/landanir/"
hausar = {"User-Agent": "Mozilla/5.0 (Vefapp um Austfjarðahafnir í þróun)"}

try:
    svar = requests.get(url, headers=hausar)
    svar.raise_for_status()
    vefsida = BeautifulSoup(svar.text, "html.parser")
    tafla = vefsida.find("table")
    
    gogn = []
    if tafla:
        faerslur = tafla.find_all("tr")
        for lina in faerslur[1:20]: # Tökum fyrstu 20 línurnar sem dæmi
            dalkar = lina.find_all("td")
            if len(dalkar) >= 4:
                hofn = dalkar[2].text.strip()
                # Einföld sía fyrir Austfirði (hægt að stækka listann)
                if hofn in ["Neskaupstaður", "Seyðisfjörður", "Eskifjörður", "Vopnafjörður", "Reyðarfjörður", "Fáskrúðsfjörður", "Stöðvarfjörður", "Djúpivogur"]:
                    gogn.append({
                        "dags": dalkar[0].text.strip(),
                        "skip": dalkar[1].text.strip(),
                        "hofn": hofn,
                        "afli": dalkar[3].text.strip()
                    })
    
    # Vistum gögnin í skrá
    with open('landanir.json', 'w', encoding='utf-8') as f:
        json.dump(gogn, f, ensure_ascii=False, indent=2)
        
except Exception as e:
    print(f"Villa: {e}")
