from rich.traceback import install

install(show_locals=True)

def dividir(a, b):
    return a / b

dividir(10, 0)
