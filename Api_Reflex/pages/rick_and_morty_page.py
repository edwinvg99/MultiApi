import reflex as rx
from rxconfig import config
from Api_Reflex.components.R_and_M import cardR_and_M,RickAndMortyState
from Api_Reflex.components.navbar import navbar_buttons
from Api_Reflex.components.footer import footer


@rx.page(route='/rick_and_morty', title='Rick and Morty', on_load=RickAndMortyState.get_characters)
def rickAndMorty() -> rx.Component:

    rx.button("Volver", href="/",position="top-right"), 

    return rx.box(
        navbar_buttons(),
        rx.flex(
            cardR_and_M(),

        direction='row',

        ),
        footer(),
        
        class_name=" bg-stone-950 w-full h-full"
    )
