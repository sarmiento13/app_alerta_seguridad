import reflex as rx
from .home01 import home01

def home() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/image.png",  # Ruta de la imagen del logo
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Camino Seguro", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    home01(
                        "Inicio", 
                        "/",  # Redirigir a /login_page
                    ),
                    home01("Rutas seguras", "/#"),
                    home01("Precios", "/#"),
                    home01("Contacto", "/#"),
                    home01("Acerca de", "/inicio"),
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Configuración"),
                        rx.menu.item("Marketing y Promociones"),
                        rx.menu.separator(),
                        rx.menu.item("Perfil"),
                        rx.menu.item("Cerrar Sesión"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.image(
                        src="/path_to_your_image.jpg",  # Nueva imagen junto al texto
                        width="3em",  # Ajusta el tamaño según lo necesites
                        height="auto",
                        border_radius="10%",
                    ),
                    rx.heading(
                        "Camino Seguro", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Configuración"),
                        rx.menu.item("Ganancias"),
                        rx.menu.separator(),
                        rx.menu.item("Cerrar Sesión"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )


