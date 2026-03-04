class Produto:
    nome:str
    preco:float
    quantidade:int

    def valor_total_estoque(self) -> float:
        return self.quantidade * self.preco
    

    def adicionar_produtos(self, quantidade) -> int:
        self.quantidade += quantidade
    def remover_produtos(self, quantidade) -> int:
        self.quantidade -= quantidade

    def saida_de_dados(self) -> str:
        return f"\tNome do produto: {self.nome}\n\
\tValor de compra do produto: {self.preco}\n\
\t Quantidade em estoque: {self.quantidade}\n\
\tValor total em estoque: {self.valor_total_estoque()}"