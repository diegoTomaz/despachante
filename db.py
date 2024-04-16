import sqlite3

banco = sqlite3.connect('despachante.db', check_same_thread=False)

cursor = banco.cursor()

tabela_cliente = """
                CREATE TABLE IF NOT EXISTS clientes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome text,
                cpf text,
                rg text,
                telefone text,
                endereco text)
                """
cursor.execute(tabela_cliente)

tabela_despacho = """
                CREATE TABLE IF NOT EXISTS despacho
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa text,
                veiculo text,
                marca text,
                ano_veiculo text,
                cor text,
                chassi text,
                combustivel text,
                renavam text,
                numero_motor text,
                valor real,
                data_aquisicao text,
                data_servico text,
                valor_servico real,
                observacao text,
                cliente_id integer,
                FOREIGN KEY (cliente_id) REFERENCES cliente (id))
                """
cursor.execute(tabela_despacho)

# insert_clientes = 'INSERT INTO clientes (nome, cpf, rg, endereco) VALUES (?, ?, ?, ?)'


# def inserirCliente(cursor, nome, cpf, rg, endereco):
#     novoCliente = (
#         (nome, cpf, rg, endereco)

#     )
#     cursor.executemany(insert_clientes, novoCliente)
#     banco.commit()


def pesquisarClientes():
    pass
