import requests
import pyfiglet

# Використовуємо requests
print(f"Поточна версія requests у цьому оточенні: {requests.__version__}")

# Використовуємо pyfiglet
ascii_art = pyfiglet.figlet_format("VS Code VENV!")
print(ascii_art)
