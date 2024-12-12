# Criando um dicionário vazio
grupos = {}

# Adicionando valores dinamicamente
for i in range(1, 6):  # Isso cria do Grupo1 ao Grupo5
    grupos[f"Grupo{i}"] = f"Conteúdo do Grupo {i}"

# Agora, o dicionário 'grupos' contém os pares "chave: valor"
print(grupos)  # Saída: {'Grupo1': 'Conteúdo do Grupo 1', 'Grupo2': 'Conteúdo do Grupo 2', ...}

# Acessando os valores
print(grupos["Grupo1"])  # Saída: Conteúdo do Grupo 1
print(grupos["Grupo3"])  # Saída: Conteúdo do Grupo 3
