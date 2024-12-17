import random
Europa=['Bayern','PSG','Real Madrid',
'Benfica','Porto','City','Atlético de Madrid',
'Juventus','Borussia Dortmund','Inter de Milão','Chelsea','Salzburg']
America=['Palmeiras','Botafogo','Flamengo',
'Fluminense','River Plate','Boca Juniors','Inter Miami', 'Pachuca','Leon','Monterrey','Seattle Sounders ']
Africa=['Al-Ahly ','Wydad Casablanca','Mamelodi Sundowns','Espérance de Tunis']
Asia=['Al-Hilal','Al Ain','Ulsan','Urawa Red Diamonds']
Oceania=['Auckland City ']
Pote1=['Manchester City', 'Real Madrid', 'Bayern de Munique', 'PSG','Flamengo', 'Palmeiras', 'River Plate', 'Fluminense']
Pote2=['Chelsea', 'Borussia Dortmund', 'Inter de Milão', 'Porto', 'Atlético de Madrid', 'Benfica', 'Juventus', 'Red Bull Salzburg']
Pote3=['Al-Hilal', 'Ulsan Hyundai', 'Al-Ahly', 'Wydad Casablanca', 'Monterrey', 'León', 'Boca Juniors', 'Botafogo']
Pote4=['Urawa Red Diamonds', 'Al-Ain', 'Espérance de Tunis', 'Mamelodi Sundowns', 'Pachuca', 'Seattle Sounders', 'Auckland City', 'Inter Miami']
continentes=[Europa,America,Oceania,Asia]
Potes=[Pote1,Pote2,Pote3,Pote4]
grupo=[]
grupos = {}
i = 1  # Inicia o contador de grupos
while i <= 8:
    grupo = []  # Reinicia a lista do grupo para cada iteração do `while`
    for time in Potes:
        # Sorteia um time de cada pote
        sorteio = random.choice(time)
        grupo.append(sorteio)  # Adiciona ao grupo
    grupos[f"Grupo{i}"] = grupo  # Associa o grupo ao seu nome
    print(f"Grupo {i}: {grupo}")  # Exibe o grupo formado
    i += 1  # Incrementa o contador de grupos





    # while time in sorteio:  # Extrai o único elemento sorteado
    #     sorteio = random.sample(Europa,AmericaSul,AmericaNorte,Oceania,Asia, k=1)
    # sorteio=', '.join(sorteio)
    # i+=1
    # print(f"{time}, {sorteio}")

# for time in AmericaSul:
#     sorteio = random.sample(, k=2)



