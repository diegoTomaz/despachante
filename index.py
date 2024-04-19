import flet as ft
from db import cursor, banco
from cliente import Cliente
from despacho import Despacho
from datetime import datetime
import pandas as pd


def mostrarMensagem(msg: str, color: str):
    alertMesg.content.value = str(msg)
    alertMesg.content.color = str(color)
    alertMesg.open = True
    body.update()


def limparFormCliente():
    txtNome.content.value = ""
    txtCpf.content.value = ""
    txtRg.content.value = ""
    txtEndereco.content.value = ""
    txtTelefone.content.value = ""
    txtId.content.value = ""
    txtIdExclusao.content.value = ""
    pesquisaPessoa.value = ""
    # pessoa.update()
    # mostrarMensagem(e)


def gravarPessoa(e):
    nome = txtNome.content.value
    cpf = txtCpf.content.value
    rg = txtRg.content.value
    endereco = txtEndereco.content.value
    telefone = txtTelefone.content.value
    id = txtId.content.value
    if (nome == None or (nome.lstrip()) == ""):
        mostrarMensagem(msg="Informe o nome do cliente!", color=ft.colors.RED)
    else:
        if (id != None and id != ""):
            cliente = Cliente(nome=nome, cpf=cpf, rg=rg,
                              endereco=endereco, telefone=telefone)
            cliente.atualizarCliente(id)
            limparFormCliente()
            mostrarMensagem(msg="Cliente atualizado!",
                            color=ft.colors.GREEN)
            atualizarGridPessoas()
        else:
            cliente = Cliente(nome=nome, cpf=cpf, rg=rg,
                              endereco=endereco, telefone=telefone)
            cliente.gravarCliente()
            limparFormCliente()
            mostrarMensagem(msg="Cliente cadastrado!", color=ft.colors.GREEN)
            atualizarGridPessoas()
            # irPraCliente()


txtNome = ft.Container(content=ft.TextField(
    label='Nome',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12, max_length=255,
    focused_bgcolor=ft.colors.BLUE_GREY_200
), expand=True)
txtCpf = ft.Container(content=ft.TextField(
    label='CPF',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200
), expand=True)
txtRg = ft.Container(content=ft.TextField(
    label='RG',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200
), expand=True)
txtEndereco = ft.Container(content=ft.TextField(
    label='Endereço',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200
), expand=True)
txtTelefone = ft.Container(content=ft.TextField(
    label='Telefone',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
))
txtId = ft.Container(content=ft.TextField(
    label='ID',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    visible=False
), expand=True)
txtIdExclusao = ft.Container(content=ft.TextField(
    label='ID exlusao',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    visible=False
), expand=True)


alertMesg = ft.SnackBar(
    content=ft.Text("Cliente cadastrado!", color=ft.colors.GREEN, size=25),
    open=False,
    bgcolor=ft.colors.WHITE,
    show_close_icon=True,
    padding=20,
    close_icon_color=ft.colors.RED
)


btnStyle = ft.ButtonStyle(
    color={
        ft.MaterialState.HOVERED: ft.colors.BLACK,
        ft.MaterialState.FOCUSED: ft.colors.BLUE,
        ft.MaterialState.DEFAULT: ft.colors.BLUE,
    },
    shape={
        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
    },
    side={
        ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.RED),
        ft.MaterialState.HOVERED: ft.BorderSide(1, ft.colors.RED),
    }
)
btnGravar = ft.ElevatedButton(
    text="Gravar", icon=ft.icons.ADD_ROUNDED, style=btnStyle, on_click=gravarPessoa)


def fecharModal(e):
    confirmaExclusao.open = False
    pessoa.update()


def excluir_cliente(e):
    id = txtIdExclusao.content.value

    if (id != None):
        cliente = Cliente(nome="oi", cpf="oi", rg="oi",
                          endereco="oi", telefone="oi")
        retorno = cliente.excluirCliente(id)
        limparFormCliente()
        if (retorno):
            mostrarMensagem(msg="Cliente excluído!",
                            color=ft.colors.GREEN)
        else:
            mostrarMensagem(msg="Cliente com serviços não podem ser excluídos!",
                            color=ft.colors.RED)
        atualizarGridPessoas()
        fecharModal(e)


confirmaExclusao = ft.AlertDialog(
    modal=True,
    title=ft.Text("Tem certeza?"),
    content=ft.Text("Essa operaçâo não poderá ser desfeita"),
    actions=[
        ft.TextButton("Sim", on_click=excluir_cliente),
        ft.TextButton("Não", on_click=fecharModal),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
    # on_dismiss=lambda e: print("Modal dialog dismissed!"),
)


def confirma_excluir_cliente(e):
    txtIdExclusao.content.value = e.control.data
    pessoa.update()

    confirmaExclusao.open = True
    pessoa.update()


def editar_cliente(e):
    txtNome.content.value = e.control.data[1]
    txtCpf.content.value = e.control.data[2]
    txtRg.content.value = e.control.data[3]
    txtEndereco.content.value = e.control.data[4]
    txtTelefone.content.value = e.control.data[5]
    txtId.content.value = e.control.data[0]
    pessoa.update()


def adicionaClienteNoDespacho(e):
    txtIdClienteDespacho.content.value = e.control.data[0]
    txtClienteDespacho.content.value = e.control.data[1]
    irParaDespacho()


linhasTabela = [

]
tabelaPessoas = ft.DataTable(
    expand_loose=False,
    bgcolor=ft.colors.WHITE,
    border=ft.border.all(2, ft.colors.BLUE_100),
    border_radius=10,
    vertical_lines=ft.border.BorderSide(3, ft.colors.BLUE_100),
    horizontal_lines=ft.border.BorderSide(1, ft.colors.BLUE_100),
    heading_row_color=ft.colors.BLUE_100,
    data_row_color={"hovered": "0x30FF0000"},
    columns=[
        ft.DataColumn(ft.Text("")),
        ft.DataColumn(ft.Text("Nome")),
        ft.DataColumn(ft.Text("Cpf")),
        ft.DataColumn(ft.Text("Rg")),
        ft.DataColumn(ft.Text("Endereço")),
        ft.DataColumn(ft.Text("Telefone")),

    ],
    rows=linhasTabela
)


cliente = Cliente(nome="oi", cpf="oi", rg="oi", endereco="oi", telefone="oi")
clientes = cliente.ultimosCliente()

tabelaPessoas.rows = []

for cl in clientes:
    tabelaPessoas.rows.append(ft.DataRow(
        cells=[
            ft.DataCell(
                ft.Row([
                    ft.IconButton(icon=ft.icons.ADD, icon_color="red",
                                  data=cl, tooltip="Incluir", on_click=adicionaClienteNoDespacho, icon_size=40, width=60, height=60),
                    ft.IconButton("edit", icon_color="blue",
                                  data=cl, tooltip="Editar", on_click=editar_cliente),
                    ft.IconButton("delete", icon_color="red",
                                  data=cl[0], tooltip="Excluir", on_click=confirma_excluir_cliente),
                ])),
            ft.DataCell(ft.Text(str(cl[1]))),
            ft.DataCell(ft.Text(str(cl[2]))),
            ft.DataCell(ft.Text(str(cl[3]))),
            ft.DataCell(ft.Text(str(cl[4]))),
            ft.DataCell(ft.Text(str(cl[5]))),

        ],
    ))


def limparPesquisa(e):
    pesquisaPessoa.value = ""
    search(e)


def search(e):
    nome = pesquisaPessoa.value.upper()
    cliente = Cliente(nome="oi", cpf="oi", rg="oi",
                      endereco="oi", telefone="oi")
   # cliente.pesquisaCliente(nome)
    clientes = cliente.pesquisaCliente(nome)

    tabelaPessoas.rows = []

    for cl in clientes:
        tabelaPessoas.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(icon=ft.icons.ADD, icon_color="red",
                                      data=cl, tooltip="Incluir", on_click=adicionaClienteNoDespacho, icon_size=40, width=60, height=60),
                        ft.IconButton("edit", icon_color="blue",
                                      data=cl, tooltip="Editar", on_click=editar_cliente),
                        ft.IconButton("delete", icon_color="red",
                                      data=cl[0], tooltip="Excluir", on_click=confirma_excluir_cliente),
                    ])),
                ft.DataCell(ft.Text(str(cl[1]))),
                ft.DataCell(ft.Text(str(cl[2]))),
                ft.DataCell(ft.Text(str(cl[3]))),
                ft.DataCell(ft.Text(str(cl[4]))),
                ft.DataCell(ft.Text(str(cl[5]))),

            ],
        ))
    pessoa.update()


pesquisaPessoa = ft.TextField(
    prefix_icon=ft.icons.SEARCH,
    hint_text='Digite o nome para buscar...',
    on_submit=search
)

searchPessoa = ft.Container(
    content=ft.Column(controls=[pesquisaPessoa],
                      horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
    expand=True)

gridPessoas = ft.Container(
    content=ft.Column(controls=[tabelaPessoas], scroll=ft.ScrollMode.ALWAYS,
                      horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
    expand=True)


def atualizarGridPessoas():
    cliente = Cliente(nome="oi", cpf="oi", rg="oi",
                      endereco="oi", telefone="oi")
    clientes = cliente.ultimosCliente()

    primerioClinete = False
    idPrimeiro = None
    nomePrimeiro = None
    tabelaPessoas.rows = []

    for cl in clientes:
        if (not primerioClinete):
            idPrimeiro = cl[0]
            nomePrimeiro = cl[1]
        tabelaPessoas.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(icon=ft.icons.ADD, icon_color="red",
                                      data=cl, tooltip="Incluir", on_click=adicionaClienteNoDespacho, icon_size=40, width=60, height=60),
                        ft.IconButton("edit", icon_color="blue",
                                      data=cl, tooltip="Editar", on_click=editar_cliente),
                        ft.IconButton("delete", icon_color="red",
                                      data=cl[0], tooltip="Excluir",  on_click=confirma_excluir_cliente),
                    ])),
                ft.DataCell(ft.Text(str(cl[1]))),
                ft.DataCell(ft.Text(str(cl[2]))),
                ft.DataCell(ft.Text(str(cl[3]))),
                ft.DataCell(ft.Text(str(cl[4]))),
                ft.DataCell(ft.Text(str(cl[5]))),

            ],
        ))
        primerioClinete = True

    # tabelaPessoas.rows.insert(0,ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("Deigo tomaz")),
    #                     ft.DataCell(ft.Text("Wong")),
    #                     ft.DataCell(ft.Text("324")),
    #                     ft.DataCell(ft.Text("43")),
    #                 ],
    #             ))

    tabelaPessoas.update()
    txtIdClienteDespacho.content.value = idPrimeiro
    txtClienteDespacho.content.value = nomePrimeiro


pessoa = ft.Column(scroll=ft.ScrollMode.ALWAYS, controls=[
    ft.Container(
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        txtNome,
                    ],


                ),
                ft.Container(
                    content=ft.Row(controls=[
                        txtCpf,
                        txtRg
                    ])),

                ft.Container(
                    content=ft.Row(controls=[
                        txtEndereco,
                        txtTelefone
                    ])),
                ft.Container(
                    content=ft.Row(controls=[
                        txtId
                    ])),
                ft.Container(
                    content=ft.Row(controls=[
                        txtIdExclusao
                    ])),

                ft.Row(
                    controls=[
                        btnGravar,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                alertMesg,
                confirmaExclusao
            ],
        ),
        margin=ft.margin.all(50),
        padding=10,
    ),
    ft.Container(
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        searchPessoa,
                        ft.ElevatedButton(
                            text="Limpar pesquisa", icon=ft.icons.CLEAR_SHARP, style=btnStyle, on_click=limparPesquisa)
                    ],
                ),
                ft.Row(
                    controls=[
                        gridPessoas,
                    ],


                ),
            ],
        ),
        margin=ft.margin.all(50),
        padding=10,
    )
])

############################## DESPACHO#######################################################################################


def limparFormDespacho():
    searchCliente.data = None
    searchCliente.value = ""
    searchCliente.controls = []
    txtPlaca.content.value = ""
    txtMarca.content.value = ""
    txtAnoVeiculo.content.value = ""
    txtCor.content.value = ""
    txtChassi.content.value = ""
    txtCombustivel.content.value = ""
    txtRenavam.content.value = ""
    txtNumeroMotor.content.value = ""
    txtValor.content.value = ""
    txtDataAquisicao.content.value = ""
    txtDataServico.content.value = ""
    txtValorServico.content.value = ""
    txtObservacao.content.value = ""
    txtIdDespacho.content.value = ""
    txtClienteDespacho.content.value = ""
    txtIdClienteDespacho.content.value = ""
    txtIdExclusaoDespacho.content.value = ""
    # irParaClienteDespacho()
    # irParaDespacho()


def mostrarMensagemDespacho(msg: str, color: str):
    alertMesgDespacho.content.value = str(msg)
    alertMesgDespacho.content.color = str(color)
    alertMesgDespacho.open = True
    body.update()


def excluir_despacho(e):
    id = txtIdExclusaoDespacho.content.value

    if (id != None):
        despachoExc = Despacho()
        despachoExc.excluirDespacho(id)
        limparFormDespacho()
        mostrarMensagemDespacho(msg="Serviço excluído!",
                                color=ft.colors.GREEN)
        atualizarGridDespacho()
        fecharModalDespacho(e)


def fecharModalDespacho(e):
    confirmaExclusaoDespacho.open = False
    despacho.update()


confirmaExclusaoDespacho = ft.AlertDialog(
    modal=True,
    title=ft.Text("Tem certeza?"),
    content=ft.Text("Essa operaçâo não poderá ser desfeita"),
    actions=[
        ft.TextButton("Sim", on_click=excluir_despacho),
        ft.TextButton("Não", on_click=fecharModalDespacho),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
    # on_dismiss=lambda e: print("Modal dialog dismissed!"),
)


def confirma_excluir_despacho(e):
    txtIdExclusaoDespacho.content.value = e.control.data
    despacho.update()

    confirmaExclusaoDespacho.open = True
    despacho.update()


def gravarDespacho(e):
    clienteId = txtIdClienteDespacho.content.value
    placa = txtPlaca.content.value
    marca = txtMarca.content.value
    ano_veiculo = txtAnoVeiculo.content.value
    cor = txtCor.content.value
    chassi = txtChassi.content.value
    combustivel = txtCombustivel.content.value
    renavam = txtRenavam.content.value
    numero_motor = txtNumeroMotor.content.value
    valor = txtValor.content.value
    data_aquisicao = txtDataAquisicao.content.value
    data_servico = txtDataServico.content.value
    valor_servico = txtValorServico.content.value
    observacao = txtObservacao.content.value
    idDespacho = txtIdDespacho.content.value

    # print(f"cleinte{cliente} placa{placa} veiculo{veiculo} marca{marca} anoVei{ano_veiculo} cor{cor} chassi{chassi} combus{combustivel} renavam{renavam} numeroMot{numero_motor} valor{valor} dataAqui{data_aquisicao} data_serv{data_servico} valorSer{valor_servico} obs{observacao}")
    if (placa == None or (placa.lstrip()) == ""):
        mostrarMensagemDespacho(msg="Informe a placa!", color=ft.colors.RED)
    elif (clienteId == None or (clienteId) == ""):
        mostrarMensagemDespacho(msg="Informe o cliente!", color=ft.colors.RED)
    else:
        if (idDespacho != None and idDespacho != ""):
            despachoEdit = Despacho()
            despachoEdit.placa = placa
            despachoEdit.marca = marca
            despachoEdit.ano_veiculo = ano_veiculo
            despachoEdit.cor = cor
            despachoEdit.chassi = chassi
            despachoEdit.combustivel = combustivel
            despachoEdit.renavam = renavam
            despachoEdit.numero_motor = numero_motor
            despachoEdit.valor = valor
            despachoEdit.data_aquisicao = data_aquisicao
            despachoEdit.data_servico = data_servico
            despachoEdit.valor_servico = valor_servico
            despachoEdit.observacao = observacao
            despachoEdit.cliente_id = clienteId

            despachoEdit.atualizarDespacho(idDespacho)
            limparFormDespacho()
            mostrarMensagemDespacho(msg="Serviço atualizado!",
                                    color=ft.colors.GREEN)
            atualizarGridDespacho()
        else:
            despacho = Despacho()
            despacho.placa = placa
            despacho.marca = marca
            despacho.ano_veiculo = ano_veiculo
            despacho.cor = cor
            despacho.chassi = chassi
            despacho.combustivel = combustivel
            despacho.renavam = renavam
            despacho.numero_motor = numero_motor
            despacho.valor = valor
            despacho.data_aquisicao = data_aquisicao
            despacho.data_servico = data_servico
            despacho.valor_servico = valor_servico
            despacho.observacao = observacao
            despacho.cliente_id = clienteId

            despacho.gravarDespacho()
            limparFormDespacho()
            mostrarMensagemDespacho(
                msg="Serviço cadastrado!", color=ft.colors.GREEN)
            atualizarGridDespacho()


def editar_despacho(e):
    txtIdClienteDespacho.content.value = e.control.data[15]
    txtClienteDespacho.content.value = e.control.data[0]
    txtPlaca.content.value = e.control.data[1]
    txtMarca.content.value = e.control.data[2]
    txtAnoVeiculo.content.value = e.control.data[3]
    txtCor.content.value = e.control.data[4]
    txtChassi.content.value = e.control.data[5]
    txtCombustivel.content.value = e.control.data[6]
    txtRenavam.content.value = e.control.data[7]
    txtNumeroMotor.content.value = e.control.data[8]
    txtValor.content.value = str(e.control.data[9]).replace(".", ",")
    txtDataAquisicao.content.value = e.control.data[10]
    txtDataServico.content.value = e.control.data[11]
    txtValorServico.content.value = str(e.control.data[12]).replace(".", ",")
    txtObservacao.content.value = e.control.data[13]
    txtIdDespacho.content.value = e.control.data[14]

    despacho.update()


def clienteEscolhido(e):
   # print(e.control.data)
    text = f"{e.control.data[1]}"
    searchCliente.data = f"{e.control.data[0]}"
    # print(f"closing view from {text}")
    searchCliente.close_view(text)
    # print(f"{e.control.data[1]}")
    # print(txtClienteDespacho.content.value)
    txtClienteDespacho.content.value = f"{e.control.data[1]}"
    # print(txtClienteDespacho.content.value)
    txtIdClienteDespacho.content.value = f"{e.control.data[0]}"
    txtClienteDespacho.update()
    txtIdClienteDespacho.update()


def pesquisarClientes(e):

    nome = searchCliente.value.upper()
    cliente = Cliente(nome="oi", cpf="oi", rg="oi",
                      endereco="oi", telefone="oi")
    clientes = cliente.pesquisaCliente(nome)
    # searchCliente.close_view()
    searchCliente.controls = []

    for cl in clientes:
        searchCliente.controls.append(ft.ListTile(title=ft.Text(
            value=str(cl[1])), on_click=clienteEscolhido, data=cl)
        )

    searchCliente.open_view()


def fecharView(e):
    # searchCliente.close_view()
    pass


def pesquisaTap(e):
    searchCliente.close_view()


def adiciona_cliente(e):
    txtIdClienteDespacho.content.value = e.control.data[15]
    txtClienteDespacho.content.value = e.control.data[0]
    despacho.update()


def atualizarGridDespacho():
    despachos = Despacho.ultimosDespachos()

    tabelaDespacho.rows = []

    for desp in despachos:
        tabelaDespacho.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(icon=ft.icons.ADD, icon_color="red",
                                      data=desp, tooltip="Incluir", on_click=adiciona_cliente, icon_size=40, width=60, height=60),
                        ft.IconButton("edit", icon_color="blue",
                                      data=desp, tooltip="Editar", on_click=editar_despacho),
                        ft.IconButton("delete", icon_color="red",
                                      data=desp[14], tooltip="Excluir", on_click=confirma_excluir_despacho),
                    ])),
                ft.DataCell(ft.Text(str(desp[0]))),
                ft.DataCell(ft.Text(str(desp[1]))),
                ft.DataCell(ft.Text(str(desp[2]))),
                ft.DataCell(ft.Text(str(desp[3]))),
                ft.DataCell(ft.Text(str(desp[4]))),
                ft.DataCell(ft.Text(str(desp[5]))),
                ft.DataCell(ft.Text(str(desp[6]))),
                ft.DataCell(ft.Text(str(desp[7]))),
                ft.DataCell(ft.Text(str(desp[8]))),
                ft.DataCell(ft.Text(str(desp[9]))),
                ft.DataCell(ft.Text(str(desp[10]))),
                ft.DataCell(ft.Text(str(desp[11]))),
                ft.DataCell(ft.Text(str(desp[12]))),
                ft.DataCell(ft.Text(str(desp[13]))),


            ],
        ))

    tabelaDespacho.update()


searchCliente = ft.SearchBar(
    autofocus=True,
    view_elevation=4,
    divider_color=ft.colors.AMBER,
    bar_hint_text="Pesquisar cliente...",
    # view_hint_text="Suggestions...",
    data=None,
    # view_hint_text="Choose a color from the suggestions...",
    # on_change=fecharView,
    on_submit=pesquisarClientes,
    on_tap=pesquisaTap,
    controls=[
        # ft.ListTile(title=ft.Text(
        #     f"Color {i}"), on_click=clienteEscolhido, data=i)
        # for i in range(10)
    ],
)

btnGravarDespacho = ft.ElevatedButton(
    text="Gravar", icon=ft.icons.ADD_ROUNDED, style=btnStyle, on_click=gravarDespacho)

alertMesgDespacho = ft.SnackBar(
    content=ft.Text("Serviço cadastrado!", color=ft.colors.GREEN, size=25),
    open=False,
    bgcolor=ft.colors.WHITE,
    show_close_icon=True,
    padding=20,
    close_icon_color=ft.colors.RED
)


txtClienteDespacho = ft.Container(content=ft.TextField(
    label='Cliente',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,


), expand=True)
txtIdClienteDespacho = ft.Container(content=ft.TextField(
    label='idCliente',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    visible=False


), expand=True)

txtPlaca = ft.Container(content=ft.TextField(
    label='Placa',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,


), expand=True)


txtMarca = ft.Container(content=ft.TextField(
    label='Marca/Modelo',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtAnoVeiculo = ft.Container(content=ft.TextField(
    label='Ano',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtCor = ft.Container(content=ft.TextField(
    label='Cor',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtChassi = ft.Container(content=ft.TextField(
    label='Chassi',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtCombustivel = ft.Container(content=ft.TextField(
    label='Combustível',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtRenavam = ft.Container(content=ft.TextField(
    label='Renavam',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtNumeroMotor = ft.Container(content=ft.TextField(
    label='Número motor',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtValor = ft.Container(content=ft.TextField(
    label='Valor',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    input_filter=ft.InputFilter(
        allow=True, regex_string=r"\d+,?\d{0,2}", replacement_string="")
), expand=True)

txtDataAquisicao = ft.Container(content=ft.TextField(
    label='Data aquisição',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    # read_only=True
), expand=True)

txtDataServico = ft.Container(content=ft.TextField(
    label='Data serviço',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    # read_only=True
), expand=True)

txtValorServico = ft.Container(content=ft.TextField(
    label='Valor serviço',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    input_filter=ft.InputFilter(
        allow=True, regex_string=r"\d+,?\d{0,2}", replacement_string="")
), expand=True)

txtObservacao = ft.Container(content=ft.TextField(
    label='Observação',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
), expand=True)

txtIdDespacho = ft.Container(content=ft.TextField(
    label='ID',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    visible=False

), expand=True)
txtIdExclusaoDespacho = ft.Container(content=ft.TextField(
    label='ID exlusao',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    visible=False
), expand=True)


tabelaDespacho = ft.DataTable(
    expand_loose=False,
    bgcolor=ft.colors.WHITE,
    border=ft.border.all(2, ft.colors.BLUE_100),
    border_radius=10,
    vertical_lines=ft.border.BorderSide(3, ft.colors.BLUE_100),
    horizontal_lines=ft.border.BorderSide(1, ft.colors.BLUE_100),
    heading_row_color=ft.colors.BLUE_100,
    data_row_color={"hovered": "0x30FF0000"},
    columns=[
        ft.DataColumn(ft.Text("")),
        ft.DataColumn(ft.Text("Cliente")),
        ft.DataColumn(ft.Text("Placa")),
        ft.DataColumn(ft.Text("Marca/Modelo")),
        ft.DataColumn(ft.Text("ano_veiculo")),
        ft.DataColumn(ft.Text("cor")),
        ft.DataColumn(ft.Text("chassi")),
        ft.DataColumn(ft.Text("combustivel")),
        ft.DataColumn(ft.Text("renavam")),
        ft.DataColumn(ft.Text("numero_motor")),
        ft.DataColumn(ft.Text("valor")),
        ft.DataColumn(ft.Text("data_aquisicao")),
        ft.DataColumn(ft.Text("data_servico")),
        ft.DataColumn(ft.Text("valor_servico")),
        ft.DataColumn(ft.Text("observacao")),

    ],
    rows=linhasTabela
)


despacho = Despacho()
despachos = Despacho.ultimosDespachos()


tabelaDespacho.rows = []

for desp in despachos:
    tabelaDespacho.rows.append(ft.DataRow(
        cells=[
            ft.DataCell(
                ft.Row([
                    ft.IconButton(icon=ft.icons.ADD, icon_color="red",
                                  data=desp, tooltip="Incluir", on_click=adiciona_cliente, icon_size=40, width=60, height=60),
                    ft.IconButton("edit", icon_color="blue",
                                  data=desp, tooltip="Editar", on_click=editar_despacho),
                    ft.IconButton("delete", icon_color="red",
                                  data=desp[14], tooltip="Excluir", on_click=confirma_excluir_despacho),
                ])),
            ft.DataCell(ft.Text(str(desp[0]))),
            ft.DataCell(ft.Text(str(desp[1]))),
            ft.DataCell(ft.Text(str(desp[2]))),
            ft.DataCell(ft.Text(str(desp[3]))),
            ft.DataCell(ft.Text(str(desp[4]))),
            ft.DataCell(ft.Text(str(desp[5]))),
            ft.DataCell(ft.Text(str(desp[6]))),
            ft.DataCell(ft.Text(str(desp[7]))),
            ft.DataCell(ft.Text(str(desp[8]))),
            ft.DataCell(ft.Text(str(desp[9]))),
            ft.DataCell(ft.Text(str(desp[10]))),
            ft.DataCell(ft.Text(str(desp[11]))),
            ft.DataCell(ft.Text(str(desp[12]))),
            ft.DataCell(ft.Text(str(desp[13]))),


        ],
    ))


def limparPesquisaDespacho(e):
    pesquisaDespacho.value = ""
    pesquisandoDespacho(e)


def pesquisandoDespacho(e):
    valor = pesquisaDespacho.value.upper()
    despachoPesqu = Despacho()
    despachos = despachoPesqu.pesquisaDespacho(valor)

    tabelaDespacho.rows = []

    for desp in despachos:
        tabelaDespacho.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(icon=ft.icons.ADD, icon_color="red",
                                      data=desp, tooltip="Incluir", on_click=adiciona_cliente, icon_size=40, width=60, height=60),
                        ft.IconButton("edit", icon_color="blue",
                                      data=desp, tooltip="Editar", on_click=editar_despacho),
                        ft.IconButton("delete", icon_color="red",
                                      data=desp[14], tooltip="Excluir", on_click=confirma_excluir_despacho),
                    ])),
                ft.DataCell(ft.Text(str(desp[0]))),
                ft.DataCell(ft.Text(str(desp[1]))),
                ft.DataCell(ft.Text(str(desp[2]))),
                ft.DataCell(ft.Text(str(desp[3]))),
                ft.DataCell(ft.Text(str(desp[4]))),
                ft.DataCell(ft.Text(str(desp[5]))),
                ft.DataCell(ft.Text(str(desp[6]))),
                ft.DataCell(ft.Text(str(desp[7]))),
                ft.DataCell(ft.Text(str(desp[8]))),
                ft.DataCell(ft.Text(str(desp[9]))),
                ft.DataCell(ft.Text(str(desp[10]))),
                ft.DataCell(ft.Text(str(desp[11]))),
                ft.DataCell(ft.Text(str(desp[12]))),
                ft.DataCell(ft.Text(str(desp[13]))),

            ],
        ))
    despacho.update()


pesquisaDespacho = ft.TextField(
    prefix_icon=ft.icons.SEARCH,
    hint_text='Digite o nome, cpf ou placa para buscar...',
    on_submit=pesquisandoDespacho
)


searchDespacho = ft.Container(
    content=ft.Column(controls=[pesquisaDespacho],
                      horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
    expand=True)

gridDespacho = ft.Container(
    expand=True,
    content=ft.Row(controls=[tabelaDespacho], scroll=ft.ScrollMode.ALWAYS,
                   ),
)

despacho = ft.Column(scroll=ft.ScrollMode.ALWAYS, controls=[
    ft.Container(
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        searchCliente,
                    ],


                ),
                ft.Row(
                    controls=[
                        txtClienteDespacho,
                        txtIdClienteDespacho,

                    ],
                ),
                ft.Row(
                    controls=[
                        txtPlaca,
                        txtMarca,

                    ],
                ),
                ft.Row(
                    controls=[
                        txtAnoVeiculo,
                        txtCor,
                        txtChassi,
                    ],
                ),

                ft.Row(
                    controls=[
                        txtCombustivel,
                        txtRenavam,
                        txtNumeroMotor,
                    ],
                ),
                ft.Row(
                    controls=[
                        txtDataAquisicao,
                        txtDataServico,
                    ],
                ),
                ft.Row(
                    controls=[
                        txtValor,
                        txtValorServico,
                    ],
                ),
                ft.Row(
                    controls=[
                        txtObservacao,
                    ],
                ),
                ft.Row(
                    controls=[
                        txtIdDespacho,
                        txtIdExclusaoDespacho,
                    ],

                ),

                ft.Row(
                    controls=[
                        btnGravarDespacho,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                alertMesgDespacho,
                confirmaExclusaoDespacho
            ],
        ),

        margin=ft.margin.all(50),
        padding=10,
    ),
    ft.Container(

        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        searchDespacho,
                        ft.ElevatedButton(
                            text="Limpar pesquisa", icon=ft.icons.CLEAR_SHARP, style=btnStyle, on_click=limparPesquisaDespacho)
                    ],
                ),
                ft.Row(
                    controls=[
                        gridDespacho,
                    ],



                ),
            ],
        ),
        margin=ft.margin.all(50),
        padding=10,

    )
])


def data_inicio(e):

    dataConverter = date_picker_inicio.value
    data2 = datetime.strptime(str(dataConverter), "%Y-%m-%d 00:00:00")

    txtDataInicio.content.value = data2.strftime("%d/%m/%Y")
    txtDataInicio.update()


date_picker_inicio = ft.DatePicker(
    on_change=data_inicio,
    # on_dismiss=date_picker_dismissed,
    first_date=datetime(2024, 1, 1),
    # last_date=datetime.datetime(2024, 10, 1),
)


date_button_inicio = ft.Container(content=ft.ElevatedButton(
    "Data Inicial",
    icon=ft.icons.CALENDAR_MONTH,
    on_click=lambda _: date_picker_inicio.pick_date(),
), expand=True)


txtDataInicio = ft.Container(content=ft.TextField(
    label='Data Inicial',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    read_only=True
), expand=True)


def data_fim(e):

    dataConverter = date_picker_fim.value
    data2 = datetime.strptime(str(dataConverter), "%Y-%m-%d 00:00:00")

    txtDataFim.content.value = data2.strftime("%d/%m/%Y")
    txtDataFim.update()


date_picker_fim = ft.DatePicker(
    on_change=data_fim,
    # on_dismiss=date_picker_dismissed,
    first_date=datetime(2024, 1, 1),
    # last_date=datetime.datetime(2024, 10, 1),
)


date_button_fim = ft.Container(content=ft.ElevatedButton(
    "Data Final",
    icon=ft.icons.CALENDAR_MONTH,
    on_click=lambda _: date_picker_fim.pick_date(),
), expand=True)


txtDataFim = ft.Container(content=ft.TextField(
    label='Data Final',
    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    bgcolor=ft.colors.BLUE_100,
    border_color=ft.colors.BLACK12,
    focused_bgcolor=ft.colors.BLUE_GREY_200,
    read_only=True
), expand=True)


def mostrarMensagemExpo(msg: str, color: str):
    alertMesgExp.content.value = str(msg)
    alertMesgExp.content.color = str(color)
    alertMesgExp.open = True
    body.update()


alertMesgExp = ft.SnackBar(
    content=ft.Text("Serviço cadastrado!", color=ft.colors.GREEN, size=25),
    open=False,
    bgcolor=ft.colors.WHITE,
    show_close_icon=True,
    padding=20,
    close_icon_color=ft.colors.RED
)


def exportarDespacho(e):
    dataInicio = txtDataInicio.content.value
    dataFim = txtDataFim.content.value
    if (dataInicio == None or (dataInicio.lstrip()) == "" or dataFim == None or (dataFim.lstrip()) == ""):
        mostrarMensagemExpo(
            msg="Informe as datas de Início e Fim!", color=ft.colors.RED)
    else:
        dataConverter = date_picker_fim.value
        dataFinal = datetime.strptime(str(dataConverter), "%Y-%m-%d 00:00:00")

        final = dataFinal.strftime("%Y-%m-%d")

        dataConverter2 = date_picker_inicio.value
        dataInicial = datetime.strptime(
            str(dataConverter2), "%Y-%m-%d 00:00:00")

        inicial = dataInicial.strftime("%Y-%m-%d")

        despachoPesqu = Despacho()
        despachos = despachoPesqu.pesquisaDespachoExportar(inicial, final)
        despachos = pd.DataFrame(despachos, columns=['nome', 'cpf', 'rg', 'endereco', 'telefone', 'Placa', 'Marca/Modleo', 'ano_veiculo',
                                 'cor', 'chassi', 'combustivel', 'renavam', 'numero_motor', 'valor', 'data_aquisicao', 'data_servico', 'valor_servico', 'observacao'])
        despachos.to_excel('servicos.xlsx')
        mostrarMensagemExpo(
            msg="Serviço exportado!", color=ft.colors.GREEN)

        # pesquisaDespachoExportar


btnExportarDespacho = ft.ElevatedButton(
    text="Exportar", icon=ft.icons.ADD_ROUNDED, style=btnStyle, on_click=exportarDespacho)
exportacao = ft.Column(controls=[
    ft.Container(
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                       date_picker_inicio,
                       date_button_inicio,
                       txtDataInicio,
                       date_picker_fim,
                       date_button_fim,
                       txtDataFim

                       ],


                ),
                ft.Row(
                    controls=[
                        btnExportarDespacho,
                    ],


                ),
                alertMesgExp
            ],
        ),
        margin=ft.margin.all(50),
        padding=10,
    ),

])


body = ft.Row(
    expand=True,
    controls=[

        ft.Column(
            expand=True,

            controls=[
                ft.Container(bgcolor=ft.colors.BLUE,
                             expand=True,
                             content=despacho,
                             ),


            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH)
    ],
)

vermelho = ft.Column(
    controls=[
        ft.Container(bgcolor=ft.colors.RED,
                     width=5,
                     height=40,
                     margin=ft.margin.only(top=100),

                     ),
    ],

)


# def irParaClienteDespacho():
#     body.controls[0].controls[0].content = pessoa
#     body.update()
#     body.controls[0].controls[0].content = despacho
#     vermelho.controls[0].margin = ft.margin.only(top=100)
#     vermelho.update()
#     body.update()


def irParaDespacho():
    body.controls[0].controls[0].content = despacho
    vermelho.controls[0].margin = ft.margin.only(top=100)
    vermelho.update()
    body.update()


def irParaCliente():
    body.controls[0].controls[0].content = pessoa
    vermelho.controls[0].margin = ft.margin.only(top=40)
    vermelho.update()
    body.update()


def changeBody(e):
    if (e.control.selected_index == 1):
        body.controls[0].controls[0].content = despacho
        vermelho.controls[0].margin = ft.margin.only(top=100)
    elif (e.control.selected_index == 0):
        body.controls[0].controls[0].content = pessoa
        vermelho.controls[0].margin = ft.margin.only(top=40)
    else:
        body.controls[0].controls[0].content = exportacao
        vermelho.controls[0].margin = ft.margin.only(top=160)

    vermelho.update()
    body.update()


def main(page: ft.Page):
    page.title = "Rasput"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[
            ft.Locale("pt", "BR"),
        ],
        current_locale=ft.Locale("pt", "BR"),
    )

    rail = ft.NavigationRail(
        selected_index=1,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=80,
        indicator_color=ft.colors.BLUE_100,
        elevation=1,
        min_extended_width=400,
        group_alignment=-0.9,
        on_change=changeBody,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.PEOPLE_ALT_OUTLINED,
                selected_icon=ft.icons.PEOPLE,
                label="Clientes"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.FOLDER_SHARED_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.FOLDER_SHARED_ROUNDED),
                label="Serviço",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.DOWNLOAD_FOR_OFFLINE_OUTLINED),
                selected_icon_content=ft.Icon(
                    ft.icons.DOWNLOAD_FOR_OFFLINE_ROUNDED),
                label="Exportar",
            ),
        ],
    )

    page.add(

        ft.Row(
            [
                rail,
                vermelho,
                body,


            ],
            expand=True,
            spacing=0
        ),
    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
