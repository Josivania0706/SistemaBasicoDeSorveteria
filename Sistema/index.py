#coding: utf-8
import administrador as admin
import itens as item
import banco_de_dados as bd
from random import randrange


class Main:
    
    def principal():
        print("\nO que deseja pedir?")
        
        opcao = int(input(" 1- Acaí \n 2- Milkshake \n 3- Sorvete \n 4- Realizar Login como Administrador\n"))
        if opcao == 1:#escolheu acai
            bd.tela_Ativa = 2 #chamar a funcao tela_Acai()
        elif opcao == 2:#escolheu Milkshake
            bd.tela_Ativa = 3
        elif opcao == 3:#escolheu Sorvete
            bd.tela_Ativa = 4
        elif opcao == 4:#escolheu Administrador
            bd.tela_Ativa = 5
               
    def tela_Acai():
        global recipienteAcai
        adicional = []
       
        while True :
            print("\nSelecione o recipiente: ")
            aux = 1
            for i in item.recipiente_Acai:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 

            if op > 0  and op <= len(item.recipiente_Acai):
                recipienteAcai = item.recipiente_Acai[op-1].nome
                item.PrecoFinal = item.PrecoFinal + item.recipiente_Acai[op-1].preco
                break

        while True : 
            print("\nSelecione o Adicional: ")
            aux = 1
            for i in item.adicional_Acai:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 

            if op > 0  and op <= len(item.adicional_Acai):
                adicional.append(item.adicional_Acai[op-1].nome)
                item.PrecoFinal = item.PrecoFinal + item.adicional_Acai[op-1].preco

            opp = int(input("\nDeseja escolher mais adicionais?\n 1- Sim\n 2- Nao\n"))
            if(opp == 2):
                break

        print("\nO valor total do pedido foi de: R$",item.PrecoFinal )

        while True:
            op = int(input("\nEscolher forma de pagamento?\n 1- Sim\n 2- Nao\n"))
            if op == 1:
                bd.tela_Ativa = 9
                break
            else:
                op = int(input('Cancelar pedido?\n 1- Sim\n 2- Nao\n'))
                if op == 1:
                    print("\n Pedido Finalizado")
                    item.PrecoFinal = 0
                    bd.tela_Ativa = 1
                    break

    def Finalizacao_de_Pedido():
        op = int(input('Finalizar pedido?\n 1- Sim\n 2- Nao\n'))
        if op == 1:
            senhaRetirada = randrange(0, 1000)
            print("\n**************************************")
            print("\nSenha para retirada: ", senhaRetirada)
            print("\n Pedido Finalizado\n")
            print("**************************************\n")
        
        item.PrecoFinal = 0
        bd.tela_Ativa = 1

    def tela_Pagamento():
        while True:
            op = int(input("\nSelecione a forma de pagamento:\n 1- Cartão de Crédito\n 2- Cartão de Débito\n 3- Pague com PIX\n"))
            if op == 1:
                input_numCartao = input("\nInsira o número do Cartão\n")
                print("\nSelecione o número de parcelas\n 1-  1x de R$",item.PrecoFinal,"\n 2- 2x de R$",item.PrecoFinal/2)
                input_numParcelas = int(input())
                
                if input_numCartao == '':
                    print("\nO campo referente ao número do cartão não foi preenchido!")
                elif  input_numParcelas != 1 and  input_numParcelas != 2:
                    print("\nVocê não selecionou o número de parcelas!")
                else:
                    print("\nDados confirmados com sucesso!\n")
                    bd.tela_Ativa = 10
                    break
      
    def tela_Milkshake():
        global recipienteMilk
        global sabor
       
        while True :
            print("\nSelecione o recipiente: ")
            aux = 1
            for i in item.recipiente_Milkshake:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 

            if op > 0  and op <= len(item.recipiente_Milkshake):
                recipienteMilk = item.recipiente_Milkshake[op-1].nome
                item.PrecoFinal = item.PrecoFinal + item.recipiente_Milkshake[op-1].preco
                break
        
        while True :
            print("\nSelecione o Sabor:")
            aux = 1
            for i in item.sabores_Milkshake:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 
            
            if op > 0  and op <= len(item.sabores_Milkshake):
                sabor = item.sabores_Milkshake[op-1].nome
                item.PrecoFinal = item.PrecoFinal + item.sabores_Milkshake[op-1].preco
                break
        
        print("\nO valor total do pedido foi de: R$",item.PrecoFinal )

        while True:
            op = int(input("\nEscolher forma de pagamento?\n 1- Sim\n 2- Nao\n"))
            if op == 1:
                bd.tela_Ativa = 9
                break
            else:
                op = int(input('Cancelar pedido?\n 1- Sim\n 2- Nao\n'))
                if op == 1:
                    print("\n Pedido Finalizado")
                    item.PrecoFinal = 0
                    bd.tela_Ativa = 1
                    break
            
    def tela_Sorvete():
        global adicional
        global recipienteSorvete
        global sabor
        while True :
            print("\nSelecione o recipiente: ")
            aux = 1
            for i in item.recipiente_Sorvete:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 

            if op > 0  and op <= len(item.recipiente_Sorvete):
                recipienteSorvete = item.recipiente_Sorvete[op-1].nome
                item.PrecoFinal = item.PrecoFinal + item.recipiente_Sorvete[op-1].preco
                break
            
        while True :
            print("\nSelecione o Sabor:")
            aux = 1
            for i in item.sabores_Sorvete:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 
            
            if op > 0  and op <= len(item.sabores_Sorvete):
                sabor = item.sabores_Sorvete[op-1].nome
                item.PrecoFinal = item.PrecoFinal + item.sabores_Sorvete[op-1].preco
                break
        
        while True :
            print("\nSelecione o Adicional:")
            aux = 1
            for i in item.adicional_Sorvete:
                print(" ",aux,"- ", i.nome)
                aux = aux + 1
            op = int(input("\n ")) 
            
            if op > 0  and op <= len(item.adicional_Sorvete):
                adicional = item.adicional_Sorvete[op-1].nome
                item.PrecoFinal = item.PrecoFinal + item.adicional_Sorvete[op-1].preco
                break

        print("\nO valor total do pedido foi de: R$",item.PrecoFinal)

        while True:
            op = int(input("\nEscolher forma de pagamento?\n 1- Sim\n 2- Não\n"))
            if op == 1:
                bd.tela_Ativa = 9
                break
            else:
                op = int(input('Cancelar pedido?\n 1- Sim\n 2- Não\n'))
                if op == 1:
                    print("\n Pedido Finalizado")
                    item.PrecoFinal = 0
                    bd.tela_Ativa = 1
                    break

    def tela_Admin():

        while True:
            usuario = input("\nDigite seu usuário: ")
            senha = input("\nDigite sua senha: ")
        
            if usuario != "" and senha != "":
                if admin.Administrador.autenticar_Admin(usuario,senha):

                    bd.tela_Ativa = 6   
                    break 
                else:
                    print('Usuário ou Senha incorretos!')

    def tela_Controle_Estoque():
        while True:
            op = int(input("\n---Administrador---\n 1- Gerenciar Produto\n 2- Cadastrar Cardápio\n 3- Sair\n") )
            if op == 1:
                bd.tela_Ativa = 7
                break
            elif op == 2:
                bd.tela_Ativa = 8
                break
            elif op == 3:
                bd.tela_Ativa = 1
                break

    def tela_Gerenciar_Produto():
    
        while True :
            op = int(input("\nVisualizar:\n 1- Recipiente do Sorvete\n 2- Recipiente do Acaí\n 3- Recipiente do Milkshake\n 4- Sabor do Soverte\n 5- Sabor do Milkshake\n 6- Adicionais do Acaí\n 7- Adicionais do Sorvete\n 8- Voltar ao Menu de Controle\n"))
            if op == 1:
                aux = 1
                for i in item.recipiente_Sorvete:
                    print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                    aux = aux + 1
                op = int(input("\n ")) 
                qnt = int(input("\nQuantidade nova: ")) 

                if op > 0  and op <= len(item.recipiente_Sorvete):
                    item.recipiente_Sorvete[op-1].qnt = qnt
                    break
            elif op == 2:
                aux = 1
                for i in item.recipiente_Acai:
                    print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                    aux = aux + 1
                op = int(input("\n ")) 
                qnt = int(input("\nQuantidade nova: ")) 

                if op > 0  and op <= len(item.recipiente_Acai):
                    item.recipiente_Acai[op-1].qnt = qnt
                    break
            elif op == 3:
                aux = 1
                for i in item.recipiente_Milkshake:
                    print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                    aux = aux + 1
                op = int(input("\n ")) 
                qnt = int(input("\nQuantidade nova: ")) 

                if op > 0  and op <= len(item.recipiente_Milkshake):
                    item.recipiente_Milkshake[op-1].qnt = qnt
                    break
            elif op == 4:
                aux = 1
                for i in item.sabores_Sorvete:
                    print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                    aux = aux + 1
                op = int(input("\n ")) 
                qnt = int(input("\nQuantidade nova: ")) 

                if op > 0  and op <= len(item.sabores_Sorvete):
                    item.sabores_Sorvete[op-1].qnt = qnt
                    break
            elif op == 5:
                    aux = 1
                    for i in item.sabores_Milkshake:
                        print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                        aux = aux + 1
                    op = int(input("\n ")) 
                    qnt = int(input("\nQuantidade nova: ")) 

                    if op > 0  and op <= len(item.sabores_Milkshake):
                        item.sabores_Milkshake[op-1].qnt = qnt
                        break
            elif op == 6:
                    aux = 1
                    for i in item.adicional_Acai:
                        print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                        aux = aux + 1
                    op = int(input("\n ")) 
                    qnt = int(input("\nQuantidade nova: ")) 

                    if op > 0  and op <= len(item.adicional_Acai):
                        item.adicional_Acai[op-1].qnt = qnt
                        break
            elif op == 7:
                    aux = 1
                    for i in item.adicional_Sorvete:
                        print(" ",aux,"- ", i.nome," quantidade: ",i.qnt)
                        aux = aux + 1
                    op = int(input("\n ")) 
                    qnt = int(input("\nQuantidade nova: ")) 

                    if op > 0  and op <= len(item.adicional_Sorvete):
                        item.adicional_Sorvete[op-1].qnt = qnt
                        break
            elif op == 8:
                bd.tela_Ativa == 6
                break
               
    def tela_Cadastrar_Cardápio():

        while True :
            op = int(input("\nCadastrar:\n 1- Recipiente do Sorvete\n 2- Recipiente do Acaí\n 3- Recipiente do Milkshake\n 4- Sabor do Soverte\n 5- Sabor do Milkshake\n 6- Adicionais do Acaí\n 7- Adicionais do Sorvete\n 8- Voltar ao Menu de Controle\n"))
            Nome_Item = input('Cadastrar Item Novo')
            qnt_Item = input('Quantidade de Item Novo') 
            preco_item = input('Preço do Item Novo')
            if op == 1:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.recipiente_Sorvete.append(novo_item)
            elif op == 2:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.recipiente_Acai.append(novo_item)
            elif op == 3:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.recipiente_Milkshake.append(novo_item)
            elif op == 4:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.sabores_Sorvete.append(novo_item)
            elif op == 5:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.sabores_Milkshake.append(novo_item)
            elif op == 6:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.adicional_Acai.append(novo_item)
            elif op == 7:
                novo_item = item.Itens( Nome_Item,qnt_Item, preco_item)
                item.adicional_Sorvete.append(novo_item)
            elif op == 8:
                bd.tela_Ativa = 6 
                break

def main():
    run = Main
    while True:
        if bd.tela_Ativa == 1:
            run.principal()
        if bd.tela_Ativa == 2:
            run.tela_Acai()
        if bd.tela_Ativa == 3:
            run.tela_Milkshake()
        if bd.tela_Ativa == 4:
            run.tela_Sorvete()
        if bd.tela_Ativa == 5:
            run.tela_Admin()
        if bd.tela_Ativa == 6:
            run.tela_Controle_Estoque()
        if bd.tela_Ativa == 7:
            run.tela_Gerenciar_Produto()
        if bd.tela_Ativa == 8:
            run.tela_Cadastrar_Cardápio()
        if bd.tela_Ativa == 9:
            run.tela_Pagamento()
        if bd.tela_Ativa == 10:
            run.Finalizacao_de_Pedido()

main() 
    

