#coding: utf-8

import streamlit as st
from PIL import Image
import administrador as admin
import itens as item
import banco_de_dados as bd
from random import randrange
# streamlit run index1.py

class Main:
    
    def principal():
        st.image('../imgs/banner.png')
        st.title("O que deseja pedir?")
        col1, col2, col3 = st.columns(3)
        # escolher a opção acaí
        with col1:
            image1 = Image.open('../imgs/acai.png')
            st.image(image1)
            if st.button('Acaí'):
                bd.tela_Ativa = 2
                st.experimental_rerun()
        # escolher a opção milkshake
        with col2:
            image2 = Image.open('../imgs/milk.png')
            st.image(image2)
            if  st.button('Milkshake'):
                bd.tela_Ativa = 3
                st.experimental_rerun()
        # escolher a opção sorvete
        with col3:
            image3 = Image.open('../imgs/sorvete.png')
            st.image(image3)
            if st.button('Sorvete'):
                bd.tela_Ativa = 4
                st.experimental_rerun()
        if st.button('Realizar Login como Administrador'):
            bd.tela_Ativa = 5
            st.experimental_rerun()

    def tela_Acai():
        global recipienteAcai
        vetorRecipiente = ['']

        global precoRecipiente
        precoAdicional = []
      
        st.image('../imgs/banner_acai.png')
        st.title("Escolha as opções disponíveis:")

        # criação de formulário
        with st.form(key = "Açaí"):
            for i in item.recipiente_Acai:
                if i.qnt > 0:
                    vetorRecipiente.append(i.nome)
                    
            recipienteAcai = st.selectbox('Selecione o recipiente:',vetorRecipiente)

            if recipienteAcai in vetorRecipiente:
                for i in item.recipiente_Acai:
                    if recipienteAcai == i.nome:
                        precoRecipiente =  i.preco
            
            for i in item.adicional_Acai:
                if i.qnt > 0:
                    if st.checkbox(i.nome):
                        precoAdicional.append(i.preco)
            
            if st.form_submit_button("adicionar"):
                item.PrecoFinal = precoRecipiente + sum(precoAdicional)
                st.info(f'O seu pedido total foi de: R$ {item.PrecoFinal}')

        with st.form(key="pagamento"):
            if st.form_submit_button("Escolher forma de pagamento"):
                bd.tela_Ativa = 9
                st.experimental_rerun() 

        if st.button('Voltar'):
            bd.tela_Ativa = 1
            st.experimental_rerun()

    def Finalizacao_de_Pedido():

        st.title("Pedido efetuado com sucesso!")
        senhaRetirada = randrange(0, 1000)
        st.success(f'*********************\nSenha para retirada:{senhaRetirada}\n*********************')

        if st.button('Voltar'):
            bd.tela_Ativa = 1
            st.experimental_rerun()

        
        item.PrecoFinal = 0
        bd.tela_Ativa = 1

    def tela_Pagamento():
        
        input_formaPag = ""

        with st.form(key = "Adicionar Cartão de Crédito"):
            
            input_formaPag = st.selectbox("Selecione a forma de pagamento:", [" ", "Cartão de Crédito", "Cartão de Débito", "Pague com PIX"])
            
            if input_formaPag != '':
                if input_formaPag == "Cartão de Crédito":
                    input_numeroCartao = st.text_input(label = "Insira o número do Cartão")
                    input_numeroParcelas = st.selectbox("Selecione o número de parcelas", options = [f" ", f"1x de {item.PrecoFinal}", f"2x de {item.PrecoFinal/2}", f"3x de {item.PrecoFinal/3}"])
                
                if st.form_submit_button("Confirmar"):
                    bd.auxiliador = bd.auxiliador+1
                    if bd.auxiliador > 1:
                        if input_numeroCartao == "":
                            st.error('O campo referente ao número do cartão não foi preenchido!')
                        if input_numeroParcelas == " ":
                            st.error('Você não selecionou o número de parcelas!')

                        if input_numeroCartao != "" and input_numeroParcelas != " ":
                            bd.sucesso  = 1
                            bd.auxiliador = 0 
                            st.success('Dados confirmados com sucesso!')
                                             
        if st.button('Finalizar') and bd.sucesso == 1:
                bd.tela_Ativa = 10
                st.experimental_rerun()
      
    def tela_Milkshake():
        global recipienteMilk
        vetorRecipiente = ['']
        vetorSabor = ['']

        global precoRecipiente
        global precoSabor        
        global sabor

        st.image('../imgs/banner_milkshake.png')
        st.title("Escolha as opções disponíveis:")
       
        with st.form(key = "Açaí"):
            ###
            for i in item.recipiente_Milkshake:
                if i.qnt > 0:
                    vetorRecipiente.append(i.nome)
                    
            recipienteMilk = st.selectbox('Selecione o recipiente:',vetorRecipiente)

            if recipienteMilk in vetorRecipiente:
                for i in item.recipiente_Milkshake:
                    if recipienteMilk == i.nome:
                        precoRecipiente =  i.preco
            ###
            for i in item.sabores_Milkshake:
                if i.qnt > 0:
                    vetorSabor.append(i.nome)

            sabor = st.selectbox('Selecione o sabor:',vetorSabor)

            if sabor in vetorSabor:
                for i in item.sabores_Milkshake:
                    if sabor == i.nome:
                        precoSabor =  i.preco
        
            if st.form_submit_button("adicionar"):
                    item.PrecoFinal = precoRecipiente + precoSabor
                    st.info(f'O seu pedido total foi de: R$ {item.PrecoFinal}')

        with st.form(key="pagamento"):
            if st.form_submit_button("Escolher forma de pagamento"):
                bd.tela_Ativa = 9
                st.experimental_rerun() 

        if st.button('Voltar'):
            bd.tela_Ativa = 1
            st.experimental_rerun()
            
    def tela_Sorvete():
    
        global recipienteSorvete
        global precoRecipiente
        
        global precoSabor 
        precoAdicional = []
        vetorRecipiente = ['']
        vetorSabor = ['']
        global sabor

        st.image('../imgs/banner_sorvete.png')
        st.title("Escolha as opções disponíveis:")
        
        with st.form(key = "Açaí"):
            ###
            for i in item.recipiente_Sorvete:
                if i.qnt > 0:
                    vetorRecipiente.append(i.nome)
                    
            recipienteSorvete = st.selectbox('Selecione o recipiente:',vetorRecipiente)
            if recipienteSorvete in vetorRecipiente:
                for i in item.recipiente_Sorvete:
                    if recipienteSorvete == i.nome:
                        precoRecipiente =  i.preco
            
            ###
            for i in item.sabores_Sorvete:
                if i.qnt > 0:
                    vetorSabor.append(i.nome)
                    
            sabor = st.selectbox('Selecione o sabor:',vetorSabor)
            if sabor in vetorSabor:
                for i in item.sabores_Sorvete:
                    if sabor == i.nome:
                        precoSabor =  i.preco
    
            ###           
            for i in item.adicional_Sorvete:
                if i.qnt > 0:
                    if st.checkbox(i.nome):
                        precoAdicional.append(i.preco)
            
            if st.form_submit_button("adicionar"):
                item.PrecoFinal = precoRecipiente + precoSabor + sum(precoAdicional)
                st.info(f'O seu pedido total foi de: R$ {item.PrecoFinal}')

        with st.form(key="pagamento"):
            if st.form_submit_button("Escolher forma de pagamento"):
                bd.tela_Ativa = 9
                st.experimental_rerun() 

        if st.button('Voltar'):
            bd.tela_Ativa = 1
            st.experimental_rerun()

    def tela_Admin():

        st.image('../imgs/banner_admin.png')
        st.title("Realizar login:")
        
        with st.form(key = 'admin'):
            usuario = st.text_input(label = 'Usuário')
            senha = st.text_input(label = 'Senha')
           
            botao_entrar = st.form_submit_button('Entrar')
           
            if botao_entrar:
                if admin.Administrador.autenticar_Admin(usuario, senha):
                    bd.tela_Ativa = 6
                    st.experimental_rerun()
                else:
                    st.error('Usuário ou Senha incorretos!')
        
        if st.button('Sair'):
            bd.tela_Ativa = 1
            st.experimental_rerun()

    def tela_Controle_Estoque():
        st.image('../imgs/banner_admin.png')
        st.title("Controle:")

        if st.button('Gerenciar Produto'):
            bd.tela_Ativa = 7
            st.experimental_rerun()
        if st.button('Cadastrar Cardápio'):
            bd.tela_Ativa = 8
            st.experimental_rerun()
        if st.button('Sair '):
            bd.tela_Ativa = 1
            st.experimental_rerun()
    
    def tela_Gerenciar_Produto():
    
        st.image('../imgs/banner_admin.png')

        with st.form(key="alterar_qnt"):

            mudar = st.selectbox("Alterar quantidade:", ["", "Recipiente do Sorvete", "Recipiente do Acai", "Recipiente do Milkshake", "Sabor do Soverte", "Sabor do Milkshake", "Adicionais do Acai", "Adicionais do Sorvete"])  
        
            # salvar as alterações feitas  
            if st.form_submit_button('Concluir'): 
                bd.auxiliador = 1

        if bd.auxiliador == 1:
            with st.form(key="_qnt "):      
                if mudar == "Recipiente do Sorvete":
                # show os itens disponíveis no sistema
                    for i in item.recipiente_Sorvete:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                elif mudar == "Recipiente do Acai": 
                    for i in item.recipiente_Acai:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                elif mudar == "Recipiente do Milkshake": 
                    for i in item.recipiente_Milkshake:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                elif mudar == "Sabor do Soverte": 
                    for i in item.sabores_Sorvete:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                elif mudar == "Sabor do Milkshake": 
                    for i in item.sabores_Milkshake:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                elif mudar == "Adicionais do Acai": 
                    for i in item.adicional_Acai:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                elif mudar == "Adicionais do Sorvete": 
                    for i in item.adicional_Sorvete:
                        i.qnt = st.number_input(label=i.nome ,min_value=0, value= i.qnt, format = "%d", step=1)  
                
                if st.form_submit_button('Concluir'): 
                    bd.auxiliador = 0
                    st.success('Alteração feita com sucesso!') 
            
        
        if st.button('Voltar ao Menu de Controle'):
            bd.tela_Ativa = 6
            st.experimental_rerun()
        if st.button('Sair '):
            bd.tela_Ativa = 1
            st.experimental_rerun()
              
    def tela_Cadastrar_Cardápio():

        st.image('../imgs/banner_admin.png')


        with st.form(key="alterar_qnt"):

            mudar = st.selectbox("Adicionar:", ["", "Recipiente do Sorvete", "Recipiente do Acai", "Recipiente do Milkshake", "Sabor do Soverte", "Sabor do Milkshake", "Adicionais do Acai", "Adicionais do Sorvete"])  
        
            # salvar as alterações feitas  
            if st.form_submit_button('Concluir'): 
                bd.auxiliador = 1

            if bd.sucesso == 1:
                bd.sucesso = 0
                st.success('Item cadastrado com sucesso!')

        if bd.auxiliador == 1:
            with st.form(key="_qnt "): 
                Nome_Item = st.text_input(label = 'Cadastrar Item Novo')
                qnt_Item = st.number_input(label="Quantidade de Item Novo", format = "%d", step=1)
                preco_item = st.text_input(label = 'Preço Item Novo')     
                
                if Nome_Item != '' and qnt_Item != '' and preco_item != '':
                    if mudar == "Recipiente do Sorvete":
                    # show os itens disponíveis no sistema
                        precoo = float(preco_item)
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.recipiente_Sorvete.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                            
                    elif mudar == "Recipiente do Acai": 
                        precoo = float(preco_item)
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.recipiente_Acai.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                    
                    elif mudar == "Recipiente do Milkshake": 
                        precoo = float(preco_item)
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.recipiente_Milkshake.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                        
                    elif mudar == "Sabor do Soverte":
                        precoo = float(preco_item) 
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.sabores_Sorvete.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                        
                    elif mudar == "Sabor do Milkshake": 
                        precoo = float(preco_item)
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.sabores_Milkshake.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                        
                    elif mudar == "Adicionais do Acai": 
                        precoo = float(preco_item)
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.adicional_Acai.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                        
                    elif mudar == "Adicionais do Sorvete":
                        precoo = float(preco_item)
                        novo_item = item.Itens( Nome_Item,qnt_Item, precoo)
                        item.adicional_Sorvete.append(novo_item)
                        bd.auxiliador = 0
                        bd.sucesso = 1
                    if bd.sucesso ==1:
                        Nome_Item = '' 
                        qnt_Item = ''
                        preco_item = ''
                        
                if st.form_submit_button('Cadastrar') and bd.sucesso == 1:
                   st.experimental_rerun()
                    
        if st.button('Voltar ao Menu de Controle'):
            bd.tela_Ativa = 6
            st.experimental_rerun()
        if st.button('Sair '):
            bd.tela_Ativa = 1
            st.experimental_rerun()
       
def main():
    run = Main
    
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