# Projeto: Sistema de Gerenciamento de Notas
# Objetivo
# Criar um sistema que permita:

# Cadastrar alunos.
# Inserir notas para os alunos.
# Calcular a média e status de aprovação.
# Exibir o relatório com os dados de todos os alunos.

def menu():
    print("=== Sistema de Gerenciamento de Notas ===")
    print("1. Cadastrar aluno")
    print("2. Inserir Notas")
    print("3. Exibir Relatório")
    print("4. Sair")
    return input("Escolha uma opção: ")

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")

    if nome.strip() == "":
        print("Nome não pode ser vazio.")
        return
    if nome in alunos:
        print("Aluno já existe.")
        return
    
    alunos[nome] = []

    print(f"Aluno {nome} cadastrado.")

def inserir_notas(alunos):
    nome = input("Digite o nome do aluno: ")

    if nome not in alunos:
        print("O aluno não foi encontrado.")
        return
    
    print(f"Digite as notas do aluno {nome}. O número deve ser de 0 a 10, digite fim para encerrar.")

    while True:
        nota = input(f"Nota {len(alunos[nome]) + 1}: ")

        if nota.lower() == "fim":
            break

        try:
            nota = float(nota)

            if 0 <= nota <= 10:
                alunos[nome].append(nota)
                print(f"Nota {nota} inserida no aluno {nome}")
            else:
                print("A nota deve ser entre 0 e 10")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def calcular_media_status(notas):
    if not notas:
        return 0, "Sem notas"
    
    media = sum(notas) / len(notas)

    status = "Aprovado" if media >= 7 else "Reprovado"

    return media, status

def exibir_relatorio(alunos):
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    
    print("=== Relatório alunos ===")
    for nome, notas in alunos.items():
        media, status = calcular_media_status(notas)
        print(f"Aluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media}")
        print(f"Status: {status}")
        print("-" * 30)

    

def main():

    alunos = {}

    while True:
        opcao = menu()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            inserir_notas(alunos)
        elif opcao == "3":
            exibir_relatorio(alunos)
        elif opcao == "4":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()