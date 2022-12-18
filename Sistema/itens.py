
recipiente_Sorvete = []
sabores_Sorvete = []
adicional_Sorvete = []

recipiente_Milkshake = []
sabores_Milkshake = []

recipiente_Acai = []
adicional_Acai = []

PrecoFinal = 0

class Itens:
    # inicialização do item
    def __init__(self, _nome, _qnt,_preco):
        self.nome = _nome
        self.qnt = _qnt
        self.preco = _preco

novo_item = Itens("Casquinha",2,1.50)
recipiente_Sorvete.append(novo_item)
novo_item = Itens("Copo - 100ml", 2,2.00)
recipiente_Sorvete.append(novo_item)
novo_item = Itens("Copo - 200ml",2,2.50)
recipiente_Sorvete.append(novo_item)
novo_item = Itens("Copo - 300ml",2,3.50)
recipiente_Sorvete.append(novo_item)

novo_item = Itens("Morango", 5,2.50)
sabores_Sorvete.append(novo_item)
novo_item = Itens("Flocos", 2, 2.50)
sabores_Sorvete.append(novo_item)
novo_item = Itens("Napolitano", 2,2.00)
sabores_Sorvete.append(novo_item)
novo_item = Itens("Chocolate", 3,2.00)
sabores_Sorvete.append(novo_item)

novo_item = Itens("Confetes", 3,1.00)
adicional_Sorvete.append(novo_item)
novo_item = Itens("Bis", 3,1.50)
adicional_Sorvete.append(novo_item)


novo_item = Itens("Copo - 200ml",1,2.50)
recipiente_Acai.append(novo_item)
novo_item = Itens("Copo - 300ml", 2,3.00)
recipiente_Acai.append(novo_item)
novo_item = Itens("Copo - 400ml",2,4.50)
recipiente_Acai.append(novo_item)
novo_item = Itens("Copo - 500ml",2,6.50)
recipiente_Acai.append(novo_item)


#adicionais do acaí
novo_item = Itens("Banana", 1,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Beijinho", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Brigadeiro", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Chips de coco", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Confeites (M&Ms)", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Farofa doce", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Granola", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Leite condensado", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Leite em pó", 3,2.00)
adicional_Acai.append(novo_item)
novo_item = Itens("Paçoca", 3,2.00)
adicional_Acai.append(novo_item)


novo_item = Itens("Morango", 5,2.50)
sabores_Milkshake.append(novo_item)

novo_item = Itens("Chocolate", 5,2.50)
sabores_Milkshake.append(novo_item)

novo_item = Itens("Copo - 200ml",2,2.50)
recipiente_Milkshake.append(novo_item)
novo_item = Itens("Copo - 300ml", 2,3.00)
recipiente_Milkshake.append(novo_item)
novo_item = Itens("Copo - 400ml",2,4.50)
recipiente_Milkshake.append(novo_item)
novo_item = Itens("Copo - 500ml",2,6.50)
recipiente_Milkshake.append(novo_item)