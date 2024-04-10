from db import cursor, banco
class Cliente:
    def __init__(self,nome, cpf, rg, endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco

    def gravarCliente(self)-> None:
        insert_clientes = 'INSERT INTO clientes (nome, cpf, rg, endereco) VALUES (?, ?, ?, ?)'
        novoCliente = [self.nome, self.cpf, self.rg, self.endereco]

        cursor.execute(insert_clientes, novoCliente)
        banco.commit()

    def ulimosCliente(self):
        pesquisa_clientes = 'SELECT * from clientes ORDER BY ID DESC LIMIT 20'

        cursor.execute(pesquisa_clientes)
        clientes = cursor.fetchall()
        return clientes