#exibe o nome do programa
def exibir_nome_do_programa():
    print("SISTEMA DE GERENCIAMENTO ACADÊMICO\n")
    
#exibe o menu. vai receber a opcao desejada
def exibir_menu():
    print("========== SISTEMA ACADÊMICO ==========" )
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Alterar situação")
    print("0 - Sair")
    print("="*30)
    
#cadastra o estudante
def cadastrar_estudante():
    print("Opção Cadastrar estudante selecionada\n")

#lista os estudantes
def listar_estudantes():
    print("Opção Listar estudantes selecionada\n")

#altera a situacao do estudante
def alterar_situacao_estudante():
    print("Opção Alterar situação selecionada\n")

#informa que a opcao escolhida pelo usuario nao existe
def opcao_invalida():
    print("Opção inválida!\n")

#encerra o programa
def finalizar_programa():
    print("Sistema encerrado \n")
    
#vai realizar a opcao que o usuario selecionou  
def main():
    exibir_nome_do_programa()

    while True:
        exibir_menu()
        opcao = int (input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_estudante()
        elif opcao == 2:
            listar_estudantes()
        elif opcao == 3:
            alterar_situacao_estudante()
        elif opcao == 0:
            finalizar_programa()
            break
        else:
            opcao_invalida()
main()