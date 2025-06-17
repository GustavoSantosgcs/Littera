# Conferencia para evitar entrada vazia:
def input_nao_vazio(mensagem):
    """Garante entrada não vazia (string)."""
    entrada = input(mensagem).strip()
    while entrada == "":
        entrada = input("Entrada vazia. \n" + mensagem).strip()
    return entrada


# Conferencia de número inteiro:
def input_inteiro(mensagem):
    entrada = input(mensagem).strip()
    while not entrada.isdigit():
        entrada = input("Erro. Digite um número inteiro.\n" + mensagem).strip()
    return int(entrada)


# Função Mensagem inicial:
def mensagem_boas_vindas(nome, idade, cidade, estado):
    print(f"\nOlá, {nome}! Seja, mais uma vez, muito bem-vindo(a) ao Littera. 💖")
    print(f"Que legal ver alguém de {cidade} - {estado}, aos seus {idade}"
          " anos de idade,\ncultivando e compartilhando o seu hábito da leitura conosco!\n")
    print("Vamos descobrir juntos como anda sua jornada liTTerária? 📖✨")


#Estimar livros futuros:
def estimar_livros_futuros(livros_digitais, livros_fisicos,nome):
    total_futuro = (livros_digitais + livros_fisicos) * 5

    print("\n📚 Estimativa Littera dos seus próximos 5 anos:")
    print(f"Livros digitais: {livros_digitais * 5} em 5 anos")
    print(f"Livros físicos: {livros_fisicos * 5} em 5 anos")
    print(f"Ou seja, você pode ler cerca de {total_futuro} livros nos próximos 5 anos!")
   
    if total_futuro >= 100:
        print(f"\n🚀 Incrível, {nome}! Você tem o perfil dedicado ao saber! Selo LITTERA para você 😎!")
    elif total_futuro >= 30:
        print("\nÓtimo, né? Sua média de leitura é consistente.")
    elif total_futuro >= 10:
        print("\nInteressante, né? Ler um pouco já faz muita diferença.")
    else:
        print(f"\nih... tá meio baixo, hein?\nVamos juntos aumentar essa prática de leitura, {nome}? 😉")


#Calculo de horas anuais:
def calcular_horas_anuais(horas_semanais):
    return horas_semanais * 52


#Equilibrio:
def analisar_equilibrio(estudo_ano, entretenimento_ano):
    print(f"\n📊 Você estudou cerca de {estudo_ano} horas em 1 ano.")
    print(f"📖 E dedicou {entretenimento_ano} horas à leitura por lazer.")
    
    if estudo_ano > entretenimento_ano:
        print("Você está bem focado nos estudos, hein? Continue assim. 📚")
    elif estudo_ano < entretenimento_ano:
        print("Muito bom! Equilibrar diversão e aprendizado é essencial. 😊")
    elif estudo_ano != 0:
        print("Você tem um ótimo equilíbrio entre estudo e lazer! ⚖️")
    else:
        print("Zero horas!? 😢 Que tal começar com algo curtinho pra engrenar?")


#Preferência:
def sugestao_de_preferencia(preferencia):
    match preferencia:
        case '1':
            print("\n🔍 Dica Littera: Considere explorar audiobooks!\n"
                  "Eles se encaixam bem com leitura digital.")
        case '2':
            print("\n📖 Dica Littera: Que tal visitar um sebo local?\n"
                  "Você pode fazer descobertas incríveis.")
        case '3':    
            print("\n🤔 Dica Littera: Experimente diferentes formatos para ver qual se adapta "
              "melhor à sua rotina!")


# Inicio do programa (terminal):
print("\n" + "═" * 50)
print(f"📚  Bem-vindo(a) ao Littera — seu hub de leitura")
print("═" * 50)
print("Analisaremos seus hábitos e traremos insights para\nturbinar sua jornada liTTerária. Vamos nessa?\n")

# Informações pessoais:
nome = input_nao_vazio("Digite seu nome: ")
idade = input_inteiro("Informe sua idade: ")
cidade = input_nao_vazio("Sua cidade: ")
estado = input_nao_vazio("Estado (sigla - exemplo: PE): ")

# informações sobre leitura:
livros_digitais = input_inteiro(f"\nQuantos livros digitais você leu no último ano, {nome}? ")
livros_fisicos = input_inteiro("Quantos livros físicos leu no último ano? ")


print("\nPreferencia de leitura:")
preferencia = input("[1] - Leitura Digital (Kindle), [2] - Livro Físico ou [3] - Indiferente: ").strip()
while preferencia not in ["1", "2", "3"]:
    print("Não entendi sua preferencia de leitura. Digite apenas a numeração.")
    preferencia = input("[1] - Leitura Digital (Kindle), [2] - Livro Físico ou [3] - Indiferente: ").strip()


horas_estudo = input_inteiro("\nQuantas horas (aprox.) de leitura você dedica ao estudo"
                            " por semana? (apenas numeros inteiros) ")
horas_lazer = input_inteiro("E quantas horas de leitura por entretenimento na semana? ")
genero_favorito = input_nao_vazio(f"\n{nome}, diz ai seu gênero literário favorito ou"
                                  " o que tem mais afinidade (ex. Terror): ")

# Processamento:
mensagem_boas_vindas(nome, idade, cidade, estado)
estimar_livros_futuros(livros_digitais, livros_fisicos,nome)
horas_estudo_ano = calcular_horas_anuais(horas_estudo)
horas_lazer_ano = calcular_horas_anuais(horas_lazer)

analisar_equilibrio(horas_estudo_ano, horas_lazer_ano)
sugestao_de_preferencia(preferencia)

print(f"\n📌 Curte {genero_favorito}? Que massa!\n"
      "Que tal procurar um clube de leitura sobre esse tema?")
print(f"\nObrigado por usar o Littera, {nome}! Não esquece de divulgar para os seus amigos, tá? 😁"
      "\nVolte sempre. 🌱")
