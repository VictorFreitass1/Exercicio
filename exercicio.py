import requests
import json


def solicita_carta():
    naipe = input("Digite o naipe desejado (ex: hearts, diamonds, clubs, spades): ").upper()
    carta = input("Digite a carta desejada (ex: ace, 2, 3,jack, queen, king): ").upper()
    return naipe, carta


naipe, carta = solicita_carta()


url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
deck_id = response.json()['deck_id']


carta_encontrada = False


while not carta_encontrada:
    
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
    response = requests.get(url)
    json_response = response.json()
    carta_comprada = json_response['cards'][0]
    
   
    if carta_comprada['value'] == carta and carta_comprada['suit'] == naipe:
        print("Acertou! A carta comprada foi:", carta_comprada['value'], "de", carta_comprada['suit'])
        
        with open('retorno.json', 'w') as f:
            json.dump(json_response, f)
        
        naipe, carta = solicita_carta()
       
        carta_encontrada = True
    else:
        print("Errou! A carta comprada foi:", carta_comprada['value'], "de", carta_comprada['suit'])