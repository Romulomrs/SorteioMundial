import random

# Definição das listas de confederações e times
Uefa = ['Bayern de Munique', 'PSG', 'Real Madrid', 'Benfica', 'Porto', 'Manchester City', 'Atlético de Madrid',
        'Juventus', 'Borussia Dortmund', 'Inter de Milão', 'Chelsea', 'Red Bull Salzburg']
Commebol = ['Palmeiras', 'Botafogo', 'Flamengo', 'Fluminense', 'River Plate', 'Boca Juniors']
Concacaf = ['Pachuca', 'León', 'Monterrey', 'Seattle Sounders', 'Inter Miami']
Africa = ['Al-Ahly', 'Wydad Casablanca', 'Mamelodi Sundowns', 'Espérance de Tunis']
Asia = ['Al-Hilal', 'Al-Ain', 'Ulsan Hyundai', 'Urawa Red Diamonds']
Oceania = ['Auckland City']

# Potes definidos
Pote1 = ['Manchester City', 'Real Madrid', 'Bayern de Munique', 'PSG', 'Flamengo', 'Palmeiras', 'River Plate', 'Fluminense']
Pote2 = ['Chelsea', 'Borussia Dortmund', 'Inter de Milão', 'Porto', 'Atlético de Madrid', 'Benfica', 'Juventus', 'Red Bull Salzburg']
Pote3 = ['Al-Hilal', 'Ulsan Hyundai', 'Al-Ahly', 'Wydad Casablanca', 'Monterrey', 'León', 'Boca Juniors', 'Botafogo']
Pote4 = ['Urawa Red Diamonds', 'Al-Ain', 'Espérance de Tunis', 'Mamelodi Sundowns', 'Pachuca', 'Seattle Sounders', 'Auckland City', 'Inter Miami']

# Dicionário de confederações
Confederacoes = {
    "Uefa": Uefa,
    "Commebol": Commebol,
    "Concacaf": Concacaf,
    "Africa": Africa,
    "Asia": Asia,
    "Oceania": Oceania
}

Potes = [Pote1, Pote2, Pote3, Pote4]
grupos = {f"Grupo{i}": [] for i in range(1, 9)}
times_sorteados = []

# Função para determinar a confederação de um time
def verificar_confederacao(time):
    time = time.strip()
    for confederacao, lista_times in Confederacoes.items():
        if time in [t.strip() for t in lista_times]:
            return confederacao
    return None

# Função para distribuir os times do Pote 1
def distribuir_pote1():
    times_pote1 = random.sample(Pote1, len(Pote1))  # Sorteia os times do Pote 1
    for i, time in enumerate(times_pote1):
        grupos[f"Grupo{i + 1}"].append(time)
        times_sorteados.append(time)

# Função para distribuir os outros times pelos grupos
def distribuir_outros_times():
    for pote in Potes[1:]:  # Ignora o Pote 1, que já foi distribuído
        times_pote = random.sample(pote, len(pote))  # Sorteia os times do pote
        for time in times_pote:
            for grupo in grupos:
                grupo_times = grupos[grupo]
                confederacoes_no_grupo = [verificar_confederacao(t) for t in grupo_times]

                # Verifica as condições para adicionar o time ao grupo
                confederacao_time = verificar_confederacao(time)
                if confederacao_time == "Uefa":
                    if confederacoes_no_grupo.count("Uefa") < 2 and len(grupo_times) < 4:
                        grupos[grupo].append(time)
                        times_sorteados.append(time)
                        break
                else:
                    if confederacoes_no_grupo.count(confederacao_time) == 0 and len(grupo_times) < 4:
                        grupos[grupo].append(time)
                        times_sorteados.append(time)
                        break

# Distribuir os times
distribuir_pote1()
distribuir_outros_times()

# Exibe o resultado final
print("\nResultado final dos grupos:")
for grupo, times in grupos.items():
    print(f"{grupo}: {times}")