import flet as ft


def main(page: ft.Page):

    page.fonts = {
        'Kanit': ''
    }
    page.window_height = 900
    page.window_width = 400
    page.window_top = 20
    page.window_always_on_top = True

    containers = [
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.CYAN, ft.colors.BLUE, ft.colors.PURPLE],
                stops=[0, 0.5, 1]
            ),
        ),
        ft.Container(
            expand=True,
            gradient=ft.RadialGradient(
                colors=[ft.colors.AMBER,
                        ft.colors.DEEP_ORANGE,
                        ft.colors.PINK
                        ],
                stops=[0, 0.5, 1],
                radius=1
            ),
        ),
        ft.Container(
            expand=True,
            gradient=ft.SweepGradient(
                colors=[ft.colors.RED,
                        ft.colors.BLACK,
                        ft.colors.PINK
                        ],
                stops=[0, 0.5, 1],
            ),
        )
    ]

    page.add(*containers)


ft.app(target=main, assets_dir='assets')
