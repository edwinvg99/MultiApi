import reflex as rx
from rxconfig import config

from Api_Reflex.components.navbar import navbar_buttons
from Api_Reflex.components.footer import footer
from Api_Reflex.pages.rick_and_morty_page import rickAndMorty

class State(rx.State):
    """The app state."""
    ...

rx.theme_panel(default_open=True)

def index() -> rx.Component:

    return rx.box(
        navbar_buttons(),
        rx.hstack(

            rx.button("Api Rick and Morty",
                      class_name=' max-lg:w-full  ease-in-out duration-30  ', 
                      on_click=rx.redirect("/rick_and_morty"),
                    ), 
            rx.button("Proxima Api ",
                      class_name=' max-lg:w-full  ease-in-out duration-30  ', 
                      on_click=rx.redirect("/https://th.bing.com/th/id/OIP.VYGMBP5CLBX7XxJIWqaypQHaFj?rs=1&pid=ImgDetMain"),
                    ), 
            rx.button("Proxima Api ",
                      class_name=' max-lg:w-full  ease-in-out duration-30  ', 
                      on_click=rx.redirect("/https://th.bing.com/th/id/OIP.VYGMBP5CLBX7XxJIWqaypQHaFj?rs=1&pid=ImgDetMain"),
                    ), 
                
                min_height="80vh",
                class_name=" flex place-content-center justify-center bg-gradient-to-t from-sky-700 from-0% via-slate-900 via-90% to-slate-900 to-20% max-lg:flex-col max-lg:p-5",  
    ), 
         footer(),
)


app = rx.App()
app.add_page(index)
app.add_page(rickAndMorty)