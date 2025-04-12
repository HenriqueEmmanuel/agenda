from datetime import datetime, timedelta

def data_atual():
    return datetime.now().strftime("%Y-%m-%d")

def formatar_eventos(eventos):
    if eventos:
        return "<br>".join([f"{hora} - {nome}" for nome, hora in eventos])
    else:
        return "Nenhum evento para hoje."

def eventos_com_lembrete(eventos):
    lembretes = []
    agora = datetime.now()

    for nome, hora in eventos:
        try:
            evento_dt = datetime.strptime(f"{agora.strftime('%Y-%m-%d')} {hora}", "%Y-%m-%d %H:%M")
            diferenca = evento_dt - agora
            if timedelta(minutes=59) < diferenca <= timedelta(hours=1):
                lembretes.append(f"Lembrete: {nome} às {hora}")
        except Exception:
            continue

    return lembretes
