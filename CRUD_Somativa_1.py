#Nome: LUIS HENRIQUE ENGEL SAUL
#Curso: Superior de Tecnologia em Análise e Desenvolvimento de Sistemas

#Listas para armazenar as informações
estudantes = []

#Funçao para simplificar a utilização dos menus
def menu_principal():
    print("--- MENU PRINCIPAL ---")
    print("(1) Estudantes")
    print("(2) Disciplinas")
    print("(3) Professores")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(9) Sair")
    print("-"*len("--- MENU PRINCIPAL ---"))

def menu_secundario():
    print("--- MENU DE OPERAÇÃO ---")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(9) Voltar")
    print("-"*len("--- MENU DE OPERAÇÃO ---"))

#Função para incluir estudantes a sua respectiva lista
def incluir_estudantes():
    while True:
        nome = input("Digite o nome do estudante: ")
        if nome:
            estudantes.append(nome)
            print("Estudante " + nome.upper() + " cadastrado com sucesso!")
            break
        else:
            print("Erro: Digite um nome válido.")

#Função para listar estudantes
def listar_estudantes():
    if estudantes:
        print("--- LISTA DE ESTUDANTES ---")
        for estudante in estudantes:
            print("- " + estudante.upper())
    else:
        print("Não há estudantes cadastrados.")

#Iniciar a seleção do primeiro menu
while True:
    menu_principal()

    #Realizar a seleção da opção desejada pelo usuário
    while True:
        try:
            opcao_pri = int(input("Digite o número correspondente à opção desejada: "))
            if opcao_pri in {1, 2, 3, 4, 5, 9}:
                break
            else:
                print("Erro: Opção inválida! Digite um número existente no menu.")
        except ValueError:
            print("Erro: Digite um número válido.")

    #Apresentar ao usuário qual foi a opção escolhida
    opcao_pri_dic = {   #Dicionario para auxiliar no retorno da opção selecionada
        1: "Estudantes",
        2: "Disciplinas",
        3: "Professores",
        4: "Turmas",
        5: "Matrículas",
        9: "Sair"
    }

    if opcao_pri == 1:
        opcao_pri_sel = opcao_pri_dic[opcao_pri]
        print(f"Opção selecionada: {opcao_pri_sel.upper()}")
        
        #Iniciar a seleção do segundo menu
        while True:
            menu_secundario()

            #Realizar a seleção da opção desejada pelo usuário
            while True:
                try:
                    opcao_sec = int(input("Digite o número correspondente à opção desejada: "))
                    if opcao_sec in {1, 2, 3, 4, 9}:
                        break
                    else:
                        print("Erro: Opção inválida! Digite um número existente no menu.")
                except ValueError:
                    print("Erro: Digite um número válido.")

            #Apresentar ao usuário qual foi a opção escolhida
            opcao_sec_dic = {   #Dicionario para auxiliar no retorno da opção selecionada
                1: "Incluir",
                2: "Listar",
                3: "Atualizar",
                4: "Excluir",
                9: "Voltar",
            }

            if opcao_sec == 1:
                opcao_sec_sel = opcao_sec_dic[opcao_sec]
                print(f"Opção selecionada: {opcao_sec_sel.upper()}")
                incluir_estudantes()

            elif opcao_sec == 2:
                opcao_sec_sel = opcao_sec_dic[opcao_sec]
                print(f"Opção selecionada: {opcao_sec_sel.upper()}")
                listar_estudantes()

            elif opcao_sec in {3, 4}:
                print("Em Desenvolvimento, selecione outra opção")

            elif opcao_sec == 9:
                opcao_sec_sel = opcao_sec_dic[opcao_sec]
                print(f"Opção selecionada: {opcao_sec_sel.upper()}")
                break

    elif opcao_pri in {2, 3, 4, 5}:
        opcao_pri_sel = opcao_pri_dic[opcao_pri]
        print("Em Desenvolvimento, selecione outra opção")

    elif opcao_pri == 9:
        opcao_pri_sel = opcao_pri_dic[opcao_pri]
        print("Chamado Encerrado")
        break
