import reflex as rx

from rxconfig import config

class EstadoContador(rx.State):
    conteo: int = 0
    
    def incrementar(self):
        self.conteo += 1

    def disminuir(self):
        self.conteo -= 1

    def reload(self):
        self.conteo = 0


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://archive.org",
                is_external=True,
            ),
            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def contador() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Disminuir",
                on_click=EstadoContador.disminuir,
            ),
            rx.heading(EstadoContador.conteo, font_size="2em"),
            rx.button(
                "Incrementar",
                on_click=EstadoContador.incrementar,
            ),
            rx.button(
                "Reiniciar",
                on_click=EstadoContador.reload,
            ),
        ),
    )

app = rx.App()
app.add_page(index, route="/")  #Ruta para la página de inicio
app.add_page(contador, route="/exp1")  #Ruta para el componente con botones