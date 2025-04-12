import pygame
import pygame_gui
from database import db_manager
from ui.components import criar_interface
from utils.helpers import data_atual, formatar_eventos

pygame.init()
pygame.display.set_caption("Agenda")
window_size = (600, 400)
window_surface = pygame.display.set_mode(window_size)
manager = pygame_gui.UIManager(window_size)

elementos = criar_interface(manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(30) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == elementos["adicionar_btn"]:
                nome = elementos["nome_input"].get_text()
                data = elementos["data_input"].get_text()
                hora = elementos["hora_input"].get_text()
                if nome and data and hora:
                    db_manager.adicionar_evento(nome, data, hora)
                    elementos["nome_input"].set_text("")
                    elementos["eventos_list"].set_text("Evento adicionado!")

            elif event.ui_element == elementos["ver_btn"]:
                eventos = db_manager.buscar_eventos_do_dia(data_atual())
                texto = formatar_eventos(eventos)
                elementos["eventos_list"].set_text(texto)

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.fill((30, 30, 30))
    manager.draw_ui(window_surface)
    pygame.display.update()

db_manager.fechar_conexao()
pygame.quit()
