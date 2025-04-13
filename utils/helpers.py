from datetime import datetime, timedelta

def data_atual():
    return datetime.now().strftime("%Y-%m-%d")

def formatar_eventos(eventos):
    if eventos:
        formatted = []
        for event in eventos:
            if len(event) == 4:
                _, nome, data, hora = event
                formatted.append(f"{data} {hora} - {nome}")
            elif len(event) == 2:
                nome, hora = event
                formatted.append(f"{hora} - {nome}")
        return "<br>".join(formatted)
    else:
        return "Nenhum evento hoje."


def eventos_com_lembrete(eventos):
    lembretes = []
    agora = datetime.now()

    for evento in eventos:
        try:
            if len(evento) == 4:
                _, nome, data, hora = evento
            elif len(evento) == 2:
                nome, hora = evento
                data = agora.strftime('%Y-%m-%d')
            else:
                continue

            evento_dt = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")
            diferenca = evento_dt - agora
            if timedelta(minutes=59) < diferenca <= timedelta(hours=1):
                lembretes.append(f"Lembrete: {nome} às {hora}")
        except Exception:
            continue

    return lembretes

