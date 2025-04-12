from datetime import datetime

def data_atual():
    return datetime.now().strftime("%Y-%m-%d")

def formatar_eventos(eventos):
    if eventos:
        return "<br>".join([f"{hora} - {nome}" for nome, hora in eventos])
    else:
        return "Nenhum evento para hoje."
