from db import cursor, banco


class Cliente:
    def __init__(self, nome, cpf, rg, endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco

    def gravarCliente(self) -> None:
        insert_clientes = 'INSERT INTO clientes (nome, cpf, rg, endereco) VALUES (?, ?, ?, ?)'
        novoCliente = [self.nome, self.cpf, self.rg, self.endereco]

        cursor.execute(insert_clientes, novoCliente)
        banco.commit()

    def atualizarCliente(self, id) -> None:
        # update_cliente = f'UPDATE clientes set nome = "{self.nome}", cpf="{self.cpf}", rg ="{self.rg}", endereco="{self.endereco}" where id= {id}'

        update_cliente = 'UPDATE clientes set nome = ?, cpf=?, rg =?, endereco=? where id= ?'

        # print(update_cliente)
        attCliente = [self.nome, self.cpf, self.rg, self.endereco, id]

        cursor.execute(update_cliente, attCliente)
        banco.commit()

    def excluirCliente(self, id) -> None:

        delete_cliente = 'DELETE from clientes where id= ?'

        # print(update_cliente)
        excCliente = [id]

        cursor.execute(delete_cliente, excCliente)
        banco.commit()

    def ulimosCliente(self):
        pesquisa_clientes = 'SELECT * from clientes ORDER BY ID DESC LIMIT 20'

        cursor.execute(pesquisa_clientes)
        clientes = cursor.fetchall()
        return clientes

    def pesquisaCliente(self, nome):
        pesquisa_clientes = f'SELECT * from clientes where nome like "%{nome}%" ORDER BY ID DESC'
        cursor.execute(pesquisa_clientes)
        clientes = cursor.fetchall()
        return clientes
