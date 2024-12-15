import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "MultiAPI", size="7", weight="bold"
                        ),
                        href='/',
                        align_items="center",
                        class_name='text-gray-50'

                    ),

                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button(
                        "Log In", 
                        size="3",
                        
                    ),

                    rx.color_mode.button(),

                    spacing="4",
                    justify="end",
                ),
                
                justify="between",
                align_items="center",
                min_width="100vh",
            

            ),
            rx.divider(),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(

                    rx.link(
                        rx.heading(
                            "Reflex", size="7", weight="bold"
                        ),
                        href='/',
                        align_items="center",
                    ),
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
                class_name='text-gray-50'
            ),
        ),

        class_name="bg-slate-900 min-w-full p-5 ",

    )