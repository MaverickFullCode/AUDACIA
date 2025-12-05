import time
import pytesseract
import pyautogui
import speech_recognition as sr
import pyautogui as pg
import pyperclip
import pygame
import os
from tkinter import *
from PIL import Image
from datetime import datetime

# VARIÁVEIS GLOBAIS ABSOLUTAS

INICIO = 0
FIM = 0
FRASE = ""
TEMPO_GASTO = 0
TAMANHO_DA_TELA = [0, 0]

# *** FUNÇÕES GERAIS ***

# FUNÇÕES RELATIVAS A TEMPO OU PARADA DO MESMO


def inicio():
    global INICIO
    INICIO = time.time()


def fim():
    global FIM
    FIM = time.time()


def tempo_gasto():
    global INICIO
    global FIM
    global TEMPO_GASTO
    if INICIO != 0 and FIM != 0:
        TEMPO_GASTO = FIM - INICIO
        return TEMPO_GASTO
    else:
        return 0


def data_atual():
    return (datetime.today().strftime('%d-%m-%Y')).replace("-", "/")


def pare(segundos):
    time.sleep(segundos)


# FUNÇÃO DE CONVERTER VOZ EM TEXTO


def ouvir_microfone():
    global FRASE

    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

    try:
        FRASE = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + FRASE)

    except sr.UnknownValueError:
        print("Não entendi")
        FRASE = ""


# FUNÇÕES DO TKINTER


def tela():
    return Tk()


def definir_titulo(nome_tela, titulo):
    return nome_tela.title(f"{titulo}")


def tamanho_de_tela(nome_tela, tamanho_x, tamanho_y, distancia_de_x, distancia_de_y):
    return nome_tela.geometry(f"{tamanho_x}x{tamanho_y}+{distancia_de_x}+{distancia_de_y}")


def texto(tela_text, texto_text, font_text, position_text="center"):
    return Label(master=tela_text, text=texto_text, anchor=position_text, font=font_text)


def entrada_de_texto(tela_entry, font_entry, justificar="center"):
    return Entry(master=tela_entry, font=font_entry, justify=justificar)


def botao(tela_button, texto_button, font_button, comando, position_button="center"):
    return Button(master=tela_button, text=texto_button, font=font_button, command=comando, anchor=position_button)


def posicionar(nome, largura, altura, x, y):
    nome.place(width=largura, height=altura, x=x, y=y)


# FUNÇÃO DO PYAUTOGUI


def rolar_para_baixo(numero_de_rolagens):
    pg.scroll(-1 * (int(numero_de_rolagens)))


def rolar_para_cima(numero_de_rolagens):
    pg.scroll(int(numero_de_rolagens))


def escreva(text_):
    for x in text_:
        time.sleep(0.01)
        pg.write(str(x))


def segurar_tecla(tecla_):
    pg.keyDown(str(tecla_))


def soltar_tecla(tecla_):
    pg.keyUp(str(tecla_))


def aperte(tecla_):
    pg.press(str(tecla_))


def clique_duplo(x, y):
    pg.doubleClick(x=x, y=y)


def clique_direito(x, y):
    pg.rightClick(x=x, y=y)


def clique_duplo_imagem(nome_da_imagem):
    pg.doubleClick(str(nome_da_imagem))


def clique_direito_imagem(nome_da_imagem):
    pg.rightClick(str(nome_da_imagem))


def clique_simples_imagem(nome_da_imagem):
    pg.click(str(nome_da_imagem))


def clique_simples(x, y):
    pg.click(x=x, y=y)


def comando_duplo(tecla_a, tecla_b):
    pg.hotkey(str(tecla_a), str(tecla_b))


def comando_triplo(tecla_a, tecla_b, tecla_c):
    pg.hotkey(str(tecla_a), str(tecla_b), str(tecla_c))


def mover_mouse(x, y, tempo_=0.01):
    pg.moveTo(x, y, tempo_)


def clique_com_arraste(x, y, tempo_):
    pg.drag(xOffset=x, yOffset=y, duration=tempo_)


def localizar_mouse():
    crdx, crdy = (pg.position())[0], (pg.position())[1]
    return crdx, crdy


def segurar_mouse():
    pg.mouseDown()


def soltar_mouse():
    pg.mouseUp()


def ver_lista_de_teclas():
    print(pg.KEYBOARD_KEYS)


def descobrir_tamanho_de_tela():
    global TAMANHO_DA_TELA
    TAMANHO_DA_TELA[0] = pg.size()[0]
    TAMANHO_DA_TELA[1] = pg.size()[1]
    return TAMANHO_DA_TELA


def alerta(mensagem_de_alerta):
    pg.alert(mensagem_de_alerta)


def printar_tela(nome_do_print="teste", nome_da_pasta=""):
    printado = pg.screenshot()
    txt_ext = ".png"
    if nome_da_pasta != "":
        newpath = f"{os.getcwd()}".replace(r"/", "/") + r"/" + f"{nome_da_pasta}"
        if not os.path.isdir(newpath):
            os.makedirs(newpath)
    printado.save(f"{os.getcwd()}".replace(r"/", "/") + r"/" + f"{nome_da_pasta}" + r"/" + f"{nome_do_print}" + txt_ext)


def solicitar_dados(texto_, title="", default=""):
    return pyautogui.prompt(text=texto_, title=title, default=default)


def colar(texto_):
    pg.write(texto_)


def copiar_valor(valor_ou_texto):
    pyperclip.copy(valor_ou_texto)


def colar_valor():
    pyperclip.paste()


def maximizar_tela():
    pyautogui.hotkey("win", "up")


def desktop():
    pyautogui.hotkey("win", "d")


def converter_imagem_em_texto(nome_da_imagem="teste.png"):
    return pytesseract.image_to_string(Image.open(f"{os.getcwd()}".replace(r"/", "/") + r"/" + nome_da_imagem))


def adicionar_posicao(variavel):
    variavel.extend((localizar_mouse(),))


# Pygame


def tocar_musica(nome_da_musica):
    pygame.mixer.init()
    pygame.mixer.music.load(nome_da_musica)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
