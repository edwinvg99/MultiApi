import reflex as rx
import os


config = rx.Config(
    app_name="Api_Reflex",
    tailwind={},
    port=int(os.getenv("PORT", 3000)),  # Puerto asignado por Railway
    host="0.0.0.0",  # Permitir conexiones externas

)