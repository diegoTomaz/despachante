import sqlite3

banco = sqlite3.connect('despachante.db', check_same_thread=False)

cursor = banco.cursor()

tabela_cliente = """
                CREATE TABLE IF NOT EXISTS clientes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome text,
                cpf text,
                rg text,
                endereco text)
                """
cursor.execute(tabela_cliente)

# insert_clientes = 'INSERT INTO clientes (nome, cpf, rg, endereco) VALUES (?, ?, ?, ?)'


# def inserirCliente(cursor, nome, cpf, rg, endereco):
#     novoCliente = (
#         (nome, cpf, rg, endereco)

#     )
#     cursor.executemany(insert_clientes, novoCliente)
#     banco.commit()


def pesquisarClientes():
    pass
