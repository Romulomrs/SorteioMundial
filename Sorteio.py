import random
Europa=['Bayern','PSG','Real Madrid',
'Benfica','Porto','City','Atlético de Madrid',
'Juventus','Borussia Dortmund','Inter de Milão','Chelsea','Salzburg']
America=['Palmeiras','Botafogo','Flamengo',
'Fluminense','River Plate','Boca Juniors','Inter Miami', 'Pachuca','Leon','Monterrey','Seattle Sounders ']
Africa=['Al-Ahly ','Wydad Casablanca','Mamelodi Sundowns','Espérance de Tunis']
Asia=['Al-Hilal','Al Ain','Ulsan','Urawa Red Diamonds']
Oceania=['Auckland City ']
continentes=[Europa,America,Oceania,Asia]
grupo=[]
for time in continentes:
    sorteio = random.choice(time)  # Sorteia diretamente o item
    grupo.append(sorteio)
print(grupo)


    # while time in sorteio:  # Extrai o único elemento sorteado
    #     sorteio = random.sample(Europa,AmericaSul,AmericaNorte,Oceania,Asia, k=1)
    # sorteio=', '.join(sorteio)
    # i+=1
    # print(f"{time}, {sorteio}")

# for time in AmericaSul:
#     sorteio = random.sample(, k=2)



