import flet as ft
from db import cursor, banco
from cliente import Cliente


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
    id = txtId.content.value
    if (nome == None or (nome.lstrip()) == ""):
        mostrarMensagem(msg="Informe o nome do cliente!", color=ft.colors.RED)
    else:
        if (id != None and id != ""):
            cliente = Cliente(nome=nome, cpf=cpf, rg=rg,
                              endereco=endereco)
            cliente.atualizarCliente(id)
            limparFormCliente()
            mostrarMensagem(msg="Cliente atualizado!",
                            color=ft.colors.GREEN)
            atualizarGridPessoas()
        else:
            cliente = Cliente(nome=nome, cpf=cpf, rg=rg, endereco=endereco)
            cliente.gravarCliente()
            limparFormCliente()
            mostrarMensagem(msg="Cliente cadastrado!", color=ft.colors.GREEN)
            atualizarGridPessoas()


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
    print(txtIdExclusao.content.value)
    id = txtIdExclusao.content.value

    if (id != None):
        cliente = Cliente(nome="oi", cpf="oi", rg="oi", endereco="oi")
        cliente.excluirCliente(id)
        limparFormCliente()
        mostrarMensagem(msg="Cliente excluído!",
                        color=ft.colors.GREEN)
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
    txtId.content.value = e.control.data[0]
    pessoa.update()


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
        ft.DataColumn(ft.Text("Nome")),
        ft.DataColumn(ft.Text("Cpf")),
        ft.DataColumn(ft.Text("Rg")),
        ft.DataColumn(ft.Text("Endereço")),
        ft.DataColumn(ft.Text("")),
    ],
    rows=linhasTabela
)


cliente = Cliente(nome="oi", cpf="oi", rg="oi", endereco="oi")
clientes = cliente.ulimosCliente()

tabelaPessoas.rows = []

for cl in clientes:
    tabelaPessoas.rows.append(ft.DataRow(
        cells=[
            ft.DataCell(ft.Text(str(cl[1]))),
            ft.DataCell(ft.Text(str(cl[2]))),
            ft.DataCell(ft.Text(str(cl[3]))),
            ft.DataCell(ft.Text(str(cl[4]))),
            ft.DataCell(
                ft.Row([
                    ft.IconButton("edit", icon_color="blue",
                                  data=cl, tooltip="Editar", on_click=editar_cliente),
                    ft.IconButton("delete", icon_color="red",
                                  data=cl[0], tooltip="Excluir", on_click=confirma_excluir_cliente),
                ])),
        ],
    ))


def limparPesquisa(e):
    print(pesquisaPessoa.value)
    pesquisaPessoa.value = ""
    search(e)


def search(e):
    nome = pesquisaPessoa.value.upper()
    cliente = Cliente(nome="oi", cpf="oi", rg="oi", endereco="oi")
   # cliente.pesquisaCliente(nome)
    clientes = cliente.pesquisaCliente(nome)

    tabelaPessoas.rows = []

    for cl in clientes:
        tabelaPessoas.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(cl[1]))),
                ft.DataCell(ft.Text(str(cl[2]))),
                ft.DataCell(ft.Text(str(cl[3]))),
                ft.DataCell(ft.Text(str(cl[4]))),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton("edit", icon_color="blue",
                                      data=cl, tooltip="Editar", on_click=editar_cliente),
                        ft.IconButton("delete", icon_color="red",
                                      data=cl[0], tooltip="Excluir", on_click=confirma_excluir_cliente),
                    ])),
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
    cliente = Cliente(nome="oi", cpf="oi", rg="oi", endereco="oi")
    clientes = cliente.ulimosCliente()

    tabelaPessoas.rows = []

    for cl in clientes:
        tabelaPessoas.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(cl[1]))),
                ft.DataCell(ft.Text(str(cl[2]))),
                ft.DataCell(ft.Text(str(cl[3]))),
                ft.DataCell(ft.Text(str(cl[4]))),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton("edit", icon_color="blue",
                                      data=cl, tooltip="Editar", on_click=editar_cliente),
                        ft.IconButton("delete", icon_color="red",
                                      data=cl[0], tooltip="Excluir",  on_click=confirma_excluir_cliente),
                    ])),
            ],
        ))

    # tabelaPessoas.rows.insert(0,ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("Deigo tomaz")),
    #                     ft.DataCell(ft.Text("Wong")),
    #                     ft.DataCell(ft.Text("324")),
    #                     ft.DataCell(ft.Text("43")),
    #                 ],
    #             ))

    tabelaPessoas.update()


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
                        txtEndereco
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


def gravarDespacho():
    pass


def clienteEscolhido(e):
   # print(e.control.data)
    text = f"{e.control.data[1]}"
    # print(f"closing view from {text}")
    searchCliente.close_view(text)


def pesquisarClientes(e):

    nome = searchCliente.value.upper()
    cliente = Cliente(nome="oi", cpf="oi", rg="oi", endereco="oi")
    clientes = cliente.pesquisaCliente(nome)
    searchCliente.close_view()
    searchCliente.controls = []

    for cl in clientes:
        searchCliente.controls.append(ft.ListTile(title=ft.Text(
            value=str(cl[1])), on_click=clienteEscolhido, data=cl)
        )
    print(searchCliente.controls)

    searchCliente.open_view()


def fecharView(e):
    searchCliente.close_view()


searchCliente = ft.SearchBar(
    autofocus=True,
    view_elevation=4,
    divider_color=ft.colors.AMBER,
    bar_hint_text="Pesquisar cliente...",
    # view_hint_text="Choose a color from the suggestions...",
    on_change=fecharView,
    on_submit=pesquisarClientes,
    # on_tap=fecharView,
    controls=[
        # ft.ListTile(title=ft.Text(
        #     f"Color {i}"), on_click=clienteEscolhido, data=i)
        # for i in range(10)
    ],
)

btnGravarDespacho = ft.ElevatedButton(
    text="Gravar", icon=ft.icons.ADD_ROUNDED, style=btnStyle, on_click=gravarDespacho)

alertMesgDespacho = ft.SnackBar(
    content=ft.Text("Despacho cadastrado!", color=ft.colors.GREEN, size=25),
    open=False,
    bgcolor=ft.colors.WHITE,
    show_close_icon=True,
    padding=20,
    close_icon_color=ft.colors.RED
)

confirmaExclusaoDespacho = ft.AlertDialog(
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


def changeBody(e):
    if (e.control.selected_index == 1):
        body.controls[0].controls[0].content = despacho
        vermelho.controls[0].margin = ft.margin.only(top=100)
    else:
        body.controls[0].controls[0].content = pessoa
        vermelho.controls[0].margin = ft.margin.only(top=40)

    vermelho.update()
    body.update()


def main(page: ft.Page):
    page.title = "Rasput"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

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
                label="Despacho",
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
