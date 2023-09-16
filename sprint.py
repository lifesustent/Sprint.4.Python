register_data = {
    'Endereço' : {
        'Rua' : '',
        'Número da rua' : '',
        'CEP': '',
        'Estado': '',
        'Cidade' : '',
    },
    'E-mail': '',
    'Número de Telefone': [],
    'Nome': '',
    'Idade': '',
    'Senha': ''
}

#Função de cadastro

def register(register_dic):
    for key in register_dic.keys():
        if type(register_dic[key]) == dict:
            register(register_dic[key])
        else:
            register_dic[key] = input(f"Digite seu/a {key}: ")
    return register_dic

#Função para logar no sistema

def login(register):
    user = input("Digite seu E-mail: ")
    password = input("Digite sua senha: ")
    while user != register['E-mail'] and password != register['Password']:
        print("Seu E-mail ou/e sua senha está incorreta")
        user = input("Digite seu E-mail: ")
        password = input("Digite sua senha: ")

# Função de mensagem de umidade do ar

def transmitir_mensagem_umidade(umidade):
     if umidade > 80:
         return "A umidade está alta. Certifique-se de se manter hidratado."
     elif umidade >= 50:
         return "A umidade está em um nível ideal, segundo a OMS. Aproveite o dia!"
     elif umidade >= 20:
         return "A umidade está em um nível de atenção."
     else:
         return "A umidade está baixa. É um nível compatível com o do Deserto do Saara, por exemplo."

# Função de mensagem de qualidade do ar

def transmitir_mensagem_monoxido(monoxido):
    if monoxido >= 50:
        return "Há níveis perigosos de monóxido de carbono no ar. Evite a exposição prolongada."
    elif monoxido >= 30:
        return "Há uma quantidade moderada de monóxido de carbono no ar. Mantenha-se atento."
    else:
        return "A quantidade de monóxido de carbono está dentro dos níveis seguros."

def transmitir_mensagem_volume(volume):
    if volume >= 85:
        return "O volume está muito alto. Proteja seus ouvidos utilizando protetores auriculares."
    elif volume >= 60:
        return "O volume está em um nível moderado. Aprecie a música!"
    else:
        return "O volume está dentro dos limites seguros."

def verifica_num(frase):
    num1 = input(frase)
    while not num1.isnumeric():
        num1 = input(frase)
    num1 = int(num1)
    return num1

def leave(mensagem, options):
    sair = input(mensagem)
    while sair not in options:
        sair = input(mensagem)
    print(sair)
    return sair
def menu():
    print("Bem-vindo a LifeSustent. Monitoramento Ambiental em tempo real.\n"
          "Aqui vamos verificar qualidade da umidade, do ar e da sonoridade em cidades inteligentes.\n"
          "Antes de começar a usar nosso serviço, Você precisa se cadastrar!"
    )
    register(register_data)
    print("\nPronto, agora é só fazer login e você poderá usufruir dos nossos serviços!")
    login(register_data)
    print("\nAgora que você está logado em nosso sistema, vamos começar pedindo as seguintes informações:\n")
    while True:
        umidade = verifica_num("Digite a umidade do ar (em %): \n")
        monoxido = verifica_num("Digite o nível de monóxido de carbono (em ppm): \n")
        volume = verifica_num("Digite o volume em decibéis: \n")
        mensagem_umidade = transmitir_mensagem_umidade(umidade)
        mensagem_monoxido = transmitir_mensagem_monoxido(monoxido)
        mensagem_volume = transmitir_mensagem_volume(volume)
        print("De acordo com os dados de nosso banco de dados, com apoio das informações divulgadas da OMS e OSHA:\n\n"
            f"{mensagem_umidade}\n"
              f"{mensagem_monoxido}\n"
              f"{mensagem_volume}\n")

        if leave("você gostaria de sair ou fazer mais uma verificação(S/V)?",["S", "V"]) == "S":
            print("Muito Obrigado por usar nossos Serviços")
            break
        else:
            continue

menu()