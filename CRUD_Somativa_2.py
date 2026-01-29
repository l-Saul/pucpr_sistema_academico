#Fazer a importação do modulo JSON.
import json
caminho_json = "/Users/luishenriqueengelsaul/Library/Mobile Documents/com~apple~CloudDocs/1.5. PUCPR/ADS/1. Raciocínio Computacional/RC_Somativa_2_dados.json"

#função para a abertura do arquivo json ao iniciar o programa com o objetivo de na hora da função, ele consultar se ja existe o codigo cadastrado no sistema
def ler_json():
    with open(caminho_json, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except:
            dados = {
            "estudantes": [],
            "disciplinas": [],
            "professores": [],
            "turmas": [],
            "matriculas": []
            }
        return dados

#Função para salvar as informaçoes em um arquivo json
def salvar_json():
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False)

#Listas para extrair do arquivo json os dados e adicionar para as listas determinadas com .get as informaçoes do arquivo json. 
#Entendo que talvez a atividade precisava que o arquivo json fosse aberto apenas nas funções, mas eu optei por adicionar listas que puxam as informações do arquivo json, ao inves de colocar listas vaizas.
dados = ler_json()
estudantes = dados.get("estudantes")
disciplinas = dados.get("disciplinas")
professores = dados.get("professores")
turmas = dados.get("turmas")
matriculas = dados.get("matriculas")

#Função para organizar a abertura dos menus principais e secundarios, juntamente com a capacidade de questionar e armazenar a escolha feita
def menu(titulo, escolha_menu):
    if escolha_menu == "opcoes_principais":
        opcoes = {
        1: "Estudantes",
        2: "Disciplinas",
        3: "Professores",
        4: "Turmas",
        5: "Matrículas",
        9: "Encerrar Chamado"
        }

    elif escolha_menu == "opcoes_secundarias":
        opcoes = {
        1: "Incluir",
        2: "Listar",
        3: "Atualizar",
        4: "Excluir",
        9: "Voltar",
        }
        
    print(f"--- {titulo} ---")
    for opcao_cod, opcao_nome in opcoes.items():
        print(f"({opcao_cod}) {opcao_nome}")
    print("-" * (len(titulo) + 8))

    try:
        escolha_usuario = int(input("Digite o número correspondente à opção desejada: "))
        if escolha_usuario in opcoes:
            print(f"Opção selecionada: {opcoes[escolha_usuario]}")
            return escolha_usuario
        else:
            print("Erro: Opção inválida! Digite um número existente no menu.")
    except ValueError:
        print("Erro: Opção inválida! Digite um número existente no menu.")

#Função para para aprimorar o teste que verifica se o codigo lanção ja existe no aquivo JSON //funçao utilizando any, dica da prof liza//
def validacao_codigo(lista, codigo, teste):
    return any(item[teste] == codigo for item in lista)

#Função para cadastrar novas informações, realizando um teste try para caso o codigo nao seja inteiro e um for para caso o codigo ja tenha sido cadastrado na lista do json, em ambos os erros ele apenas cancela os dados inseridos e apresenta uma mensagem
def incluir(categoria):
    if categoria == 1:
        while True:
            try:
                nome_estudantes = input("Digite o NOME: ")
                cod_estudantes = int(input("Digite o CÓDIGO: "))
                cpf_estudantes = input("Digite o CPF: ")
                if validacao_codigo(estudantes, cod_estudantes, "CódigoEstudantes"):
                    print("Erro: Código já existente.")
                    continue
                dicionario_estudantes = {"CódigoEstudantes": cod_estudantes, "NomeEstudantes": nome_estudantes, "CpfEstudantes": cpf_estudantes}
                estudantes.append(dicionario_estudantes)
                salvar_json()
                print("Estudante cadastrado com sucesso!" )
            except ValueError:
                print("Erro: Código deve ser um número inteiro")
                continue
            break
    elif categoria == 2:
        while True:
            try:
                nome_disciplinas = input("Digite o NOME: ")
                cod_disciplinas = int(input("Digite o CÓDIGO: "))
                if validacao_codigo(disciplinas, cod_disciplinas, "CódigoDisciplinas"):
                    print("Erro: Código já existente.")
                    continue
                dicionario_disciplinas = {"CódigoDisciplinas": cod_disciplinas, "NomeDisciplinas": nome_disciplinas}
                disciplinas.append(dicionario_disciplinas)
                salvar_json()
                print("Disciplina cadastrada com sucesso!" )
            except ValueError:
                print("Erro: Código deve ser um número inteiro")
                continue
            break
    elif categoria ==  3:
         while True:
            try:
                nome_professores = input("Digite o NOME: ")
                cod_professores = int(input("Digite o CÓDIGO: "))
                cpf_professores = input("Digite o CPF: ")
                if validacao_codigo(professores, cod_professores, "CódigoProfessores"):
                    print("Erro: Código já existente.")
                    continue
                dicionario_professores = {"CódigoProfessores": cod_professores, "NomeProfessores": nome_professores, "CpfProfessores": cpf_professores}
                professores.append(dicionario_professores)
                salvar_json()
                print("Professor cadastrado com sucesso!" )
            except ValueError:
                print("Erro: Código deve ser um número inteiro")
                continue
            break
    elif categoria == 4:
         while True:
            try:
                cod_turmas = int(input("Digite o CÓDIGO da turma: "))
                cod_professores = int(input("Digite o CÓDIGO do Professor: "))
                cod_disciplinas = int(input("Digite o CÓDIGO da disciplina: "))
                if validacao_codigo(turmas, cod_turmas, "CódigoTurmas"):
                    print("Erro: Código já existente.")
                    continue    
                dicionario_turmas = {"CódigoTurmas": cod_turmas, "CódigoProfessores": cod_professores, "CódigoDisciplinas": cod_disciplinas}
                turmas.append(dicionario_turmas)
                salvar_json()
                print("Turma cadastrada com sucesso!" )
            except ValueError:
                print("Erro: Código deve ser um número inteiro")
                continue
            break
    elif categoria == 5:
        while True:
            try:
                cod_turmas = int(input("Digite o CÓDIGO da turma: "))
                cod_estudantes = int(input("Digite o CÓDIGO do estudante: "))
                dicionario_matriculas = {"CódigoTurmas": cod_turmas, "CódigoEstudantes": cod_estudantes}
                matriculas.append(dicionario_matriculas)
                salvar_json()
                print("Matrícula cadastrada com sucesso!" )
            except ValueError:
                print("Erro: Código deve ser um número inteiro")
                continue
            break

#Função para apresentar as informações cadastradas nas listas
def listar(categoria): 
    if categoria == 1:
        if estudantes:
            print("--- CADASTROS REGISTRADOS ---")
            for dicionario in estudantes:
                print(f"Código: {dicionario['CódigoEstudantes']} | Nome: {dicionario['NomeEstudantes']} | CPF: {dicionario['CpfEstudantes']}")
            print("-" * (len("--- CADASTROS REGISTRADOS ---")))
        else:
            print("Não há cadastros registrados.")
    elif categoria == 2:
        if disciplinas:
            print("--- CADASTROS REGISTRADOS ---")
            for dicionario in disciplinas:
                print(f"Código: {dicionario['CódigoDisciplinas']} | Nome: {dicionario['NomeDisciplinas']}")
            print("-" * (len("--- CADASTROS REGISTRADOS ---")))
        else:
            print("Não há cadastros registrados.")
    elif categoria == 3:
        if professores:
            print("--- CADASTROS REGISTRADOS ---")
            for dicionario in professores:
                print(f"Código: {dicionario['CódigoProfessores']} | Nome: {dicionario['NomeProfessores']} | CPF: {dicionario['CpfProfessores']}")
            print("-" * (len("--- CADASTROS REGISTRADOS ---")))
        else:
            print("Não há cadastros registrados.")
    elif categoria == 4:
        if turmas:
            print("--- CADASTROS REGISTRADOS ---")
            for dicionario in turmas:
                print(f"Turma: {dicionario['CódigoTurmas']} | Professor: {dicionario['CódigoProfessores']} | Disciplina: {dicionario['CódigoDisciplinas']}")
            print("-" * (len("--- CADASTROS REGISTRADOS ---")))
        else:
            print("Não há cadastros registrados.")
    elif categoria == 5:
        if matriculas:
            print("--- CADASTROS REGISTRADOS ---")
            for dicionario in matriculas:
                print(f"Turma: {dicionario['CódigoTurmas']} | Estudante: {dicionario['CódigoEstudantes']}")
            print("-" * (len("--- CADASTROS REGISTRADOS ---")))
        else:
            print("Não há cadastros registrados.")

#Função para modificar o que ja foi cadastrado, verificando se todo codigo é inteiro e se o novo codigo ja existe no arquivo json que esta aberto no comeco do codigo
def atualizar(categoria):
    try:
        atualizar_dados = int(input("Digite o Código: "))
        if categoria == 1:
            for dicionario in estudantes:
                if dicionario["CódigoEstudantes"] == atualizar_dados:
                    try:
                        novo_nome_estudantes = input("Digite o novo NOME: ")
                        novo_cod_estudantes = int(input("Digite o novo CÓDIGO: "))
                        novo_cpf_estudantes = input("Digite o novo CPF: ")
                        if validacao_codigo(estudantes, novo_cod_estudantes, "CódigoEstudantes"):
                            print("Erro: Código já existente.")
                            continue
                        dicionario["NomeEstudantes"] = novo_nome_estudantes
                        dicionario["CódigoEstudantes"] = novo_cod_estudantes
                        dicionario["CpfEstudantes"] = novo_cpf_estudantes
                        salvar_json()
                        print("Atualizado com sucesso.")
                    except ValueError:
                        print("Erro: Código deve ser um número inteiro")
                        continue
                    break
        elif categoria == 2:
            for dicionario in disciplinas:
                if dicionario["CódigoDisciplinas"] == atualizar_dados:
                    try:
                        novo_nome_disciplinas = input("Digite o novo NOME: ")
                        novo_cod_disciplinas = int(input("Digite o novo CÓDIGO: "))
                        if validacao_codigo(disciplinas, novo_cod_disciplinas, "CódigoDisciplinas"):
                            print("Erro: Código já existente.")
                            continue
                        dicionario["NomeDisciplinas"] = novo_nome_disciplinas
                        dicionario["CódigoDisciplinas"] = novo_cod_disciplinas
                        salvar_json()
                        print("Atualizado com sucesso.")
                    except ValueError:
                        print("Erro: Código deve ser um número inteiro")
                        continue
                    break
        elif categoria == 3:
            for dicionario in professores:
                if dicionario["CódigoProfessores"] == atualizar_dados:
                    try:
                        novo_nome_professores = input("Digite o novo NOME: ")
                        novo_cod_professores = int(input("Digite o novo CÓDIGO: "))
                        novo_cpf_professores = input("Digite o novo CPF: ")
                        if validacao_codigo(professores, novo_cod_professores, "CódigoProfessores"):
                            print("Erro: Código já existente.")
                            continue
                        dicionario["NomeProfessores"] = novo_nome_professores
                        dicionario["CódigoProfessores"] = novo_cod_professores
                        dicionario["CpfProfessores"] = novo_cpf_professores
                        salvar_json()
                        print("Atualizado com sucesso.")
                    except ValueError:
                        print("Erro: Código deve ser um número inteiro")
                        continue
                    break
        elif categoria == 4:
            for dicionario in turmas:
                if dicionario["CódigoTurmas"] == atualizar_dados:
                    try:
                        novo_cod_turmas = int(input("Digite o novo CÓDIGO da Turma: "))
                        novo_cod_professores = int(input("Digite o novo CÓDIGO do Professor: "))
                        novo_cod_disciplinas = int(input("Digite o novo CÓDIGO da Disciplina: "))
                        if validacao_codigo(turmas, novo_cod_turmas, "CódigoTurmas"):
                            print("Erro: Código já existente.")
                            continue
                        dicionario["CódigoTurmas"] = novo_cod_turmas
                        dicionario["CódigoProfessores"] = novo_cod_professores
                        dicionario["CódigoDisciplinas"] = novo_cod_disciplinas
                        salvar_json()
                        print("Atualizado com sucesso.")
                    except ValueError:
                        print("Erro: Código deve ser um número inteiro")
                        continue
                    break
        elif categoria == 5:
            for dicionario in matriculas:
                if dicionario["CódigoTurmas"] == atualizar_dados:
                    try:
                        dicionario["CódigoTurmas"] = int(input("Digite o novo CÓDIGO da Turma: "))
                        dicionario["CódigoEstudantes"] = int(input("Digite o novo CÓDIGO do Estudantes: "))
                        salvar_json()
                        print("Atualizado com sucesso.")
                    except ValueError:
                        print("Erro: Código deve ser um número inteiro")
                        continue
                    break
        else:
            print("Erro: Código não cadastrado.")
    except ValueError:
        print("Erro: Código inválido.")

#Função para remover os dados selecionados
def remover(selecao, codigo_remover, tipo):
    excluir_dados = int(input(f"Digite o Código {tipo} que deseja remover: "))
    for dicionario in selecao:
        if dicionario[codigo_remover] == excluir_dados:
            selecao.remove(dicionario)
            salvar_json()
            print("Excluído com sucesso.")
            break

#Função para remover algum cadastro ja feito dentro do menu secundario, no comeco verifica se o codigo requisitado é um numero inteiro caso contrario ele remove da lista e salva no arquivo jsoan
def excluir(categoria):
    try:
        if categoria == 1:
            remover(estudantes, "CódigoEstudantes", "Estudantes")
        elif categoria == 2:
            remover(disciplinas, "CódigoDisciplinas", "Disciplinas")
        elif categoria == 3:
            remover(professores, "CódigoProfessores", "Professores")
        elif categoria == 4:
            remover(turmas, "CódigoTurmas", "Turmas")
        elif categoria == 5:
            remover(matriculas, "CódigoTurmas", "Turmas")
        else:
            print("Erro: Código não cadastrado.")
    except ValueError:
        print("Erro: Código inválido.")

#Loop para iniciar para abrir a seleção do primeiro menu, apos rodar a função menu(), ele ja inicia o if de acordo com a opção desejada
while True:
    escolha_inicial = menu("MENU PRINCIPAL", "opcoes_principais")
    if escolha_inicial in {1, 2, 3, 4, 5}:

        #Loop para inicar a funcao para a seleção do segundo menu, juntamente com a capacidade de ja iniciar a função das atividades de acordo com a escolha feita
        while True:
            escolha_secundaria = menu("MENU DE OPÇÕES", "opcoes_secundarias")
            if escolha_secundaria == 1:
                incluir(escolha_inicial)
            elif escolha_secundaria == 2:
                listar(escolha_inicial)
            elif escolha_secundaria == 3:
                atualizar(escolha_inicial)
            elif escolha_secundaria == 4:
                excluir(escolha_inicial)
            elif escolha_secundaria == 9:
                break

    elif escolha_inicial == 9:
        print("Chamado Encerrado.")
        break