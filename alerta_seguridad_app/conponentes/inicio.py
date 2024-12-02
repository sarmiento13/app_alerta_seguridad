import reflex as rx

def inicio() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                # Encabezado Principal
                rx.heading(
                    "Acerca de Secure Paht",
                    size="8",  # Tamaño del texto
                    weight="bold",
                    color="white",
                ),
                # Breve Descripción
                rx.text(
                    "Protegiendo tus caminos, asegurando tus destinos.",
                    size="4",
                    color="lightgray",
                    margin="1em 0",
                ),
                # Secciones Informativas
                rx.box(
                    rx.heading(
                        "Funciones Clave",
                        size="6",
                        weight="bold",
                        color="white",
                        margin="1em 0",
                    ),
                    rx.text(
                        "Alertas en Tiempo Real: Recibe notificaciones instantáneas sobre incidentes de seguridad cerca de ti.",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    rx.text(
                        "Mapas de Seguridad: Visualiza las zonas más seguras para transitar.",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    rx.text(
                        "Reportes de Usuarios: Envía y recibe reportes de seguridad de otros usuarios.",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    rx.text(
                        "Historial de Alertas: Consulta el historial de incidentes en tu área.",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    spacing="4",
                    align="start",
                ),
                spacing="6",
                align="center",  # Alinear el contenido del vstack en el centro
            ),
            padding="2em",
            background="linear-gradient(135deg, #ff6b6b 0%, #f06595 100%)",  # Fondo con gradiente en tonos cálidos
            border_radius="1em",  # Bordes redondeados
            box_shadow="0 8px 16px rgba(0, 0, 0, 0.2)",  # Sombra pronunciada
            align_items="center",  # Centrar el contenido dentro del box
            max_width="800px",  # Ancho máximo del cuadro
        ),
        height="100vh",
        background="linear-gradient(135deg, #3b82f6 0%, #9333ea 100%)",  # Fondo de la página con gradiente
        justify="center",
        align_items="center",
    )

