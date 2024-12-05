import random
Europa=['Bayern','PSG','Real Madrid',
'Benfica','Porto','City','Atlético de Madrid',
'Juventus','Borussia Dortmund','Inter de Milão','Chelsea','Salzburg']
AmericaSul=['Palmeiras','Botafogo','Flamengo',
'Fluminense','River Plate','Boca Juniors']
AmericaNorte=['Inter Miami', 'Pachuca','Leon','Monterrey','Seattle Sounders ']
Africa=['Al-Ahly ','Wydad Casablanca','Mamelodi Sundowns','Espérance de Tunis']
Asia=['Al-Hilal','Al Ain','Ulsan','Urawa Red Diamonds']
Oceania=['Auckland City ']
for time in Europa:
    sorteio = random.sample(Europa, k=2)[0]  # Extrai o único elemento sorteado
    while time == sorteio:  # Verifica diretamente o elemento
        sorteio = random.sample(Europa, k=2)[0]
    print(f"{time}, {sorteio}")  # Usa f-string para imprimir o resultado
