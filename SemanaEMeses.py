import flet as ft

def main(page: ft.Page):
    page.title = "Mi presentación"
    page.padding = 20
    page.scroll = "adaptive"
    page.bgcolor = "black"

    # Dados da semana e meses
    profile_data = {
        'Lunes': ["Tener un momento de lectura", "Tener un momento viendo series con mi esposo", "Ir al gimnasio", "Tener un buen día de trabajo", "Clase de inglés", "Cumplir la meta de leer 2 capítulos de la Biblia al día", "Estudiar programación", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\lua-cheia.png"],
        'Martes': ["Tener un momento de lectura", "Tener un momento viendo series con mi esposo", "Ir al gimnasio", "Tener un buen día de trabajo", "Estudiar español", "Estudiar programación", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\marte.png"],
        'Miércoles': ["Tener un momento de lectura", "Tener un momento viendo series con mi esposo", "Ir jugar baloncesto", "Tener un buen día de trabajo", "Estudiar español", "Estudiar programación", "Aprender una nueva canción para tocar la kalimba", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\hermes.png"],
        'Jueves': ["Tener un momento de lectura", "Tener un momento viendo series con mi esposo", "Ir al gimnasio", "Tener un buen día de trabajo", "Estudiar español", "Estudiar programación", "Practicar la canción aprendida en la kalimba", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\zeus.png"],
        'Viernes': ["Tener un momento de lectura", "Tener un momento viendo series con mi esposo", "Ir al gimnasio", "Ir jugar baloncesto", "Tener un buen día de trabalho", "Estudiar español", "Estudiar programación", "Practicar la canción aprendida en la kalimba", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\afrodite.png"],
        'Sábado': ["Jugar juegos de mesa con mis amigos", "Hacer un almuerzo muy sabroso", "Ir al gimnasio o ir jugar baloncesto por la mañana", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\saturno.png"],
        'Domingo': ["Estudiar programación", "Descansar y organizar las cosas para la próxima semana", "Clase de español", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\sol.png"]
    }

    profile_data_meses = {
        "Enero": ["Continuar cumpliendo la meta de leer la Biblia (estoy en el capítulo 37 de Génesis)", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\biblia.png"],
        "Febrero": ["Comprar una kalimba para aprender hasta que puedas comprar la cítara", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\kalimba.png"],
        "Marzo": ["Empezar a leer La montaña mágica", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\lendo-um-livro.png"],
        "Abril": ["Tal vez viajar con una pareja de amigos a la playa", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\de-praia.png"],
        "Mayo": ["Tener una barriguita más plana y no comer ramen instantáneo", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\cintura.png", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\macarrao.png"],
        "Junio": ["Tal vez hacer una escapada de un día con mi esposo", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\viagem-romantica.png"],
        "Julio": ["Comprar la lavadora", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\lavanderia.png"],
        "Agosto": ["Si no he encontrado un mejor empleo, intensificar la búsqueda", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\job-promotion.png"],
        "Septiembre": ["Celebrar el cumpleaños de mi amiga", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\bolo-de-aniversario.png"],
        "Octubre": ["Una cena especial para celebrar un año de matrimonio", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\aliancas-de-casamento.png"],
        "Noviembre": ["Es el mes de las vacaciones de mi esposo, tal vez un viaje o comprar cosas importantes para nuestra casita", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\familia.png"],
        "Diciembre": ["Comenzar a preparar la Navidad", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\papai-noel.png", r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\presente-de-natal.png"]
    }

    current_screen = 0

    def change_screen(e):
        nonlocal current_screen
        current_screen += e
        current_screen = max(0, min(current_screen, len(profile_data) + len(profile_data_meses) + 1))

        page.clean()
        build_screen()
        page.update()

    def build_screen():
        if current_screen == 0:
            page.add(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("La semana perfecta y metas para los meses", color="white", size=20),
                            ft.Image(src=r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\corre.png"),
                            ft.ElevatedButton("Siguiente", on_click=lambda e: change_screen(1)),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            )
        elif current_screen <= len(profile_data):
            dia = list(profile_data.keys())[current_screen - 1]
            metas = profile_data[dia]
            page.add(
                ft.Column(
                    [
                        ft.Text(f"{dia}:", color="white", size=18, weight="bold"),
                        ft.Column([ft.Text(f"- {meta}", color="white") for meta in metas[:-1]], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Image(src=metas[-1]),
                        ft.Row(
                            [
                                ft.ElevatedButton("Anterior", on_click=lambda e: change_screen(-1)),
                                ft.ElevatedButton("Siguiente", on_click=lambda e: change_screen(1)),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        elif current_screen == len(profile_data) + 1:
            page.add(
                ft.Column(
                    [
                        ft.Text("Metas para los meses del año", color="white", size=22, weight="bold"),
                        ft.Image(src=r"C:\Users\Ingrid\OneDrive\Documentos\Teste\Espanhol\Apresentacíon\Imagens pro slide\calendario-desktop.png"),
                        ft.Row(
                            [
                                ft.ElevatedButton("Anterior", on_click=lambda e: change_screen(-1)),
                                ft.ElevatedButton("Siguiente", on_click=lambda e: change_screen(1)),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        else:
            mes = list(profile_data_meses.keys())[current_screen - len(profile_data) - 2]
            metas = profile_data_meses[mes]
            page.add(
                ft.Column(
                    [
                        ft.Text(f"{mes}: {metas[0]}", color="white", size=18),
                        ft.Row([ft.Image(src=imagem) for imagem in metas[1:]], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(
                            [
                                ft.ElevatedButton("Anterior", on_click=lambda e: change_screen(-1)),
                                ft.ElevatedButton("Siguiente", on_click=lambda e: change_screen(1)),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

    build_screen()

if __name__ == "__main__":
    ft.app(target=main)
