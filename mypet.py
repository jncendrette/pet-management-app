# Coleta do nome do pet
def coletar_nome_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ").strip()
    nome = input("Nome do pet: ").strip()
    if not nome:
        print("O nome não pode estar vazio. Tente novamente.")
        return coletar_nome_pet()
    return nome

# Coleta da idade do pet, garantindo que seja um número inteiro
def coletar_idade_pet():
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

# Coleta do peso do pet, garantindo que seja um número flutuante
def coletar_peso_pet():
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

# Coleta o tipo do pet
def coletar_tipo_pet():
    tipos_validos = ["Cachorro", "Gato", "Pássaro", "Outro"]
    print("Tipos disponíveis: ", ", ".join(tipos_validos))
    tipo = input("Tipo do pet: ").strip().capitalize()

    if tipo in tipos_validos:
            return tipo
    else:
        print("Tipo inválido. Tente novamente.")
        return coletar_tipo_pet()

def coletar_informacoes_pet():
    """Função principal que coleta todas as informações sobre o pet."""
    print("Por favor, insira as informações sobre seu pet.")
    
    nome = coletar_nome_pet()
    idade = coletar_idade_pet()
    peso = coletar_peso_pet()
    tipo = coletar_tipo_pet()

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
