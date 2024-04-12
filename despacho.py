from db import cursor, banco


class Despacho:
    def __init__(self, placa, veiculo, marca, ano_veiculo, cor, chassi, combustivel, renavam, numero_motor, valor, data_aquisicao, data_servico, valor_servico, observacao, cliente_id) -> None:
        self.placa = placa
        self.veiculo = veiculo
        self.marca = marca
        self.ano_veiculo = ano_veiculo
        self.cor = cor
        self.chassi = chassi
        self.combustivel = combustivel
        self.renavam = renavam
        self.numero_motor = numero_motor
        self.valor = valor
        self.data_aquisicao = data_aquisicao
        self.data_servico = data_servico
        self.valor_servico = valor_servico
        self.observacao = observacao
        self.cliente_id = cliente_id

    def gravarDespacho(self):
        insert_despacho = """
                        INSERT INTO despacho 
                        (placa, veiculo, marca, ano_veiculo, cor, chassi, combustivel, renavam, numero_motor, valor, data_aquisicao, data_servico, valor_servico, observacao, cliente_id) 
                        VALUES (?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?)
                        """
        novoDespacho = [self.placa,
                        self.veiculo,
                        self.marca,
                        self.ano_veiculo,
                        self.cor,
                        self.chassi,
                        self.combustivel,
                        self.renavam,
                        self.numero_motor,
                        self.valor,
                        self.data_aquisicao,
                        self.data_servico,
                        self.valor_servico,
                        self.observacao,
                        self.cliente_id,
                        ]

        cursor.execute(insert_despacho, novoDespacho)
        banco.commit()
        return True

    def atualizarCliente(self, id) -> None:
        # update_cliente = f'UPDATE clientes set nome = "{self.nome}", cpf="{self.cpf}", rg ="{self.rg}", endereco="{self.endereco}" where id= {id}'

        update_cliente = 'UPDATE clientes set nome = ?, cpf=?, rg =?, endereco=? , telefone=? where id= ?'

        # print(update_cliente)
        attCliente = [self.nome, self.cpf, self.rg,
                      self.endereco, self.telefone, id]

        cursor.execute(update_cliente, attCliente)
        banco.commit()

    def excluirCliente(self, id) -> None:

        delete_cliente = 'DELETE from clientes where id= ?'

        # print(update_cliente)
        excCliente = [id]

        cursor.execute(delete_cliente, excCliente)
        banco.commit()

    def ulimosCliente(self):
        pesquisa_clientes = 'SELECT id,nome,cpf,rg,endereco,telefone from clientes ORDER BY ID DESC LIMIT 20'

        cursor.execute(pesquisa_clientes)
        clientes = cursor.fetchall()
        return clientes

    def pesquisaCliente(self, nome):
        pesquisa_clientes = f'SELECT id,nome,cpf,rg,endereco,telefone from clientes where nome like "%{nome}%" ORDER BY ID DESC'
        cursor.execute(pesquisa_clientes)
        clientes = cursor.fetchall()
        return clientes
