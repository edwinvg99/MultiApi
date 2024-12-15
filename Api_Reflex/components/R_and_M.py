import reflex as rx
import requests
from rxconfig import config


class RickAndMortyState(rx.State):
    characters: list[dict] = []  # La lista contiene diccionarios con claves y valores tipo str

    @rx.event
    async def get_characters(self):
        try:
            response = requests.get("https://rickandmortyapi.com/api/character")
            if response.status_code == 200:
                self.characters = response.json()["results"]



        except Exception as e:
            print(f"Error fetching characters: {e}")

def cardR_and_M()-> rx.Component:

    return rx.box( 
        # rx.button("Log", on_click=rx.console_log(RickAndMortyState.characters)),
        rx.heading("Rick and Morty Personajes", class_name='text-[40px] text-center m-10 underline  decoration-sky-500'),
            rx.flex( 


                rx.cond(
                    RickAndMortyState.characters,
                    rx.foreach( 
                        RickAndMortyState.characters,
                        lambda character: rx.flex(
                            rx.card(
                                rx.vstack(
                                    rx.image(src=character["image"], class_name='w-full h-auto rounded-md'),
                                    rx.divider(size="4", color_scheme='jade', orientation='horizontal'),
                                    rx.text(f'Nombre: {character["name"]}', class_name='color-red'),
                                    rx.text(f'Estado : {character["status"]}', class_name=''),
                                    rx.text(f'Genero : {character["gender"]}', class_name=''),


                                ),
                                class_name='bg-blue-950 ease-in-out duration-300 shadow-lg hover:scale-90 hover:shadow-fuchsia-500/40 translate-x-1 skew-y-1 transform-none font-bold ' #estilos de la card
                            ),
                            class_name="flex flex-row  shadow-md shadow-cyan-500/100 rounded-md place-content-center ease-in-out duration-300 hover:scale-90 translate-x-1 skew-y-2 transform-none hover:shadow-none max-sm:mt-10", #estilos de contenedor de la card
                        ),   
                ), 
                        rx.button(rx.spinner(loading=True), "Cargando", class_name='w-full bg-gray-900 ')                               
            ),

            class_name='flex flex-row flex-wrap size-full bg-gradient-to-t from-sky-700 from-0% via-slate-900 via-90% to-slate-900 to-20% p-1 place-content-center gap-5 max-sm:bg-yellow-400  '
            #estilo de contenedor de las cords
    ),
    class_name='flex flex-col size-full bg-gradient-to-t from-sky-700 from-0% via-slate-900 via-90% to-slate-900 to-20%  text-base content-center'
)