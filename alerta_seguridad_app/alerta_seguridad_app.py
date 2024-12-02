import reflex as rx
from .conponentes.login_page import login_page
from .conponentes.home import home
from .conponentes.inicio import inicio

class ExampleState(rx.State):
    colors: list[str] = [
        "black",
        "red",
        "green",
        "blue",
        "purple",
    ]
    index: int = 0

    @rx.event
    def next_color(self):
        self.index = (self.index + 1) % len(self.colors)

    @rx.var
    def color(self) -> str:
        return self.colors[self.index]

def index():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Bienvenido a Secure Path!",
                    size="8",  # Aumentar tamaño del texto
                    on_click=ExampleState.next_color,
                    color=ExampleState.color,
                    _hover={"cursor": "pointer"},
                ),
                rx.text(
                    "Protegiendo tus caminos, asegurando tus destinos.",  # Breve descripción
                    size="4",
                    color="gray",
                    margin="1em 0",
                ),
                rx.vstack(
                    rx.button(
                        "INICIAR SESIÓN",
                        size="4",
                        padding="1em",
                        on_click=lambda: rx.redirect("/login_page"),
                        margin="1em",
                    ),
                    rx.button(
                        "REGISTRARTE",
                        size="4",
                        padding="1em",
                        on_click=lambda: rx.redirect("/register"),
                        margin="1em",
                    ),
                    spacing="2",
                    align="center",  # Alinear los botones en el centro
                ),
                spacing="6",
                align="center",  # Alinear el contenido del vstack en el centro
            ),
            padding="2em",
            background="linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%)",  # Fondo con gradiente en tonos pastel
            border_radius="1em",  # Bordes más redondeados
            box_shadow="0 8px 16px rgba(0, 0, 0, 0.2)",  # Sombra más pronunciada
            border="2px solid #96e6a1",  # Borde con color llamativo
            align_items="center",  # Centrar el contenido dentro del box
        ),
        height="100vh",
        background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",  # Fondo de la página con gradiente
        justify="center",
    )

app = rx.App()
app.add_page(index, route="/")
app.add_page(login_page, route="/login_page")
app.add_page(home, route="/home")
app.add_page(inicio, route="/inicio")

