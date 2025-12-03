import time
from datetime import datetime

# VARIÁVEIS GLOBAIS ABSOLUTAS

INICIO = 0
FIM = 0
FRASE = ""
TEMPO_GASTO = 0

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
