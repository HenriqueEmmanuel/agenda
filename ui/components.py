import pygame
import pygame_gui

def criar_interface(manager):
    elementos = {}

    elementos["nome_input"] = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50, 50), (200, 30)), manager=manager)

    elementos["data_input"] = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50, 100), (200, 30)), manager=manager)
    elementos["data_input"].set_text("AAAA-MM-DD")

    elementos["hora_input"] = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50, 150), (200, 30)), manager=manager)
    elementos["hora_input"].set_text("HH:MM")

    elementos["adicionar_btn"] = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((270, 150), (100, 30)), text="Adicionar", manager=manager)

    elementos["ver_btn"] = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((400, 150), (100, 30)), text="Ver Hoje", manager=manager)

    elementos["eventos_list"] = pygame_gui.elements.UITextBox(
        html_text="", relative_rect=pygame.Rect((50, 200), (500, 150)), manager=manager)

    return elementos
