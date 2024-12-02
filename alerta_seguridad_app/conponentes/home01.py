import reflex as rx

def home01(label: str, href: str, **kwargs) -> rx.Component:
    # Combinar kwargs con on_click si es necesario
    if 'on_click' not in kwargs:
        kwargs['on_click'] = lambda: rx.redirect(href)
    return rx.button(
        label,
        **kwargs  # Pasar otros argumentos directamente
    )
