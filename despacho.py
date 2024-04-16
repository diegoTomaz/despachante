from db import cursor, banco


class Despacho:
    # def __init__(self, placa, veiculo, marca, ano_veiculo, cor, chassi, combustivel, renavam, numero_motor, valor, data_aquisicao, data_servico, valor_servico, observacao, cliente_id) -> None:
    # self.placa = placa
    # self.veiculo = veiculo
    # self.marca = marca
    # self.ano_veiculo = ano_veiculo
    # self.cor = cor
    # self.chassi = chassi
    # self.combustivel = combustivel
    # self.renavam = renavam
    # self.numero_motor = numero_motor
    # self.valor = valor
    # self.data_aquisicao = data_aquisicao
    # self.data_servico = data_servico
    # self.valor_servico = valor_servico
    # self.observacao = observacao
    # self.cliente_id = cliente_id

    def gravarDespacho(self):
        insert_despacho = """
                        INSERT INTO despacho
                        (placa, veiculo, marca, ano_veiculo, cor, chassi, combustivel, renavam, numero_motor,
                         valor, data_aquisicao, data_servico, valor_servico, observacao, cliente_id)
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

    def atualizarDespacho(self, id) -> None:
        # update_cliente = f'UPDATE clientes set nome = "{self.nome}", cpf="{self.cpf}", rg ="{self.rg}", endereco="{self.endereco}" where id= {id}'

        update_despacho = '''
                        UPDATE despacho 
                        set placa = ?, 
                        veiculo=?, 
                        marca =?,
                        ano_veiculo=? , 
                        cor=? ,
                        chassi=? ,
                        combustivel=? ,
                        renavam=? ,
                        numero_motor=? ,
                        valor=? ,
                        data_aquisicao=? ,
                        data_servico=? ,
                        valor_servico=? ,
                        observacao=? ,
                        cliente_id=? 
                        where id= ?
                        '''

        # print(update_cliente)
        attDespacho = [
            self.placa,
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
            id
        ]

        cursor.execute(update_despacho, attDespacho)
        banco.commit()

    def excluirDespacho(self, id) -> None:

        delete_despacho = 'DELETE from despacho where id= ?'

        # print(update_cliente)
        excDesp = [id]

        cursor.execute(delete_despacho, excDesp)
        banco.commit()

    def ultimosDespachos():
        pesquisa_despachos = '''
                   SELECT
                    C.nome,
                    D.PLACA,
                    D.veiculo,
                    D.marca,
                    D.ano_veiculo,
                    D.cor,
                    D.chassi,
                    D.combustivel,
                    D.renavam,
                    D.numero_motor,
                    D.valor,
                    D.data_aquisicao,
                    D.data_servico,
                    D.valor_servico,
                    D.observacao,
                    D.id,
                    C.ID

                FROM
                    despacho D
                INNER JOIN
                clientes C
                ON D.cliente_id = C.id
                order by d.id   DESC LIMIT 20
                    '''

        cursor.execute(pesquisa_despachos)
        despachos = cursor.fetchall()
        return despachos

    def pesquisaDespacho(self, valor):
        pesquisa_despachos = f'''
                   SELECT
                    C.nome,
                    D.PLACA,
                    D.veiculo,
                    D.marca,
                    D.ano_veiculo,
                    D.cor,
                    D.chassi,
                    D.combustivel,
                    D.renavam,
                    D.numero_motor,
                    D.valor,
                    D.data_aquisicao,
                    D.data_servico,
                    D.valor_servico,
                    D.observacao,
                    D.id,
                    C.id

                FROM
                    despacho D
                INNER JOIN
                clientes C
                ON D.cliente_id = C.id
                where c.nome like "%{valor}%" OR c.cpf like "%{valor}%" OR d.placa like "%{valor}%"
                order by d.id   
                    '''
        cursor.execute(pesquisa_despachos)
        despachos = cursor.fetchall()
        return despachos
