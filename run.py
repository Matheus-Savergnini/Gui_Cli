import os
import pyautogui as pg
from time import sleep
import tkinter as tk
import keyboard


# cli
def handle_focus(event):
    if event.widget == window:
        window.focus_force()
        window.focus_set()
        entrada.focus_set()


# fecha a gui
# com input escape{ESC} é preciso parametro E -> de event
def gui_destroy_from_escape(e):
    window.destroy()


# quanod no script esse parametro é inexistente
def gui_destroy_from_script():
    window.destroy()

def steam_login(resultado):
    # mata a steam se já estiver aberta para evitar bugs
    os.system('taskkill /f /im steam.exe')
    # abre a steam
    os.startfile('C:\\Program Files (x86)\\Steam\\steam.exe')

    # espera a steam abrir
    sleep(5)

    # clica na barra da steam
    pg.click(x=1100, y=473)
    sleep(0.1)

    # limpa a barra da steam
    pg.keyDown('ctrl')
    pg.keyDown('a')
    pg.keyUp('a')
    pg.keyUp('ctrl')
    sleep(0.5)
    pg.press('backspace')
    sleep(0.5)

    # digita o login
    if resultado == '1':
        login = 'login1'
    elif resultado == '2':
        login = 'login2'

    pg.write(login)
    sleep(0.2)

    # aperta tab
    pg.press('tab')
    sleep(0.1)

    # digita a senha
    if resultado == '1':
        senha = 'senha1'
    elif resultado == '2':
        senha = 'senha2'
    pg.write(senha)
    sleep(0.2)

    # aperta enter
    pg.press('return')


## cria função login
def basic(e):
    # verifica o input e valida os logins
    resultado = entrada.get()
    gui_destroy_from_script()

    if resultado == '1':
        steam_login('1')
    elif resultado == '2':
        steam_login('2')
    elif resultado == 'd':
        os.startfile('C:\\Users\\mathe\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe')


# cria janela
while True:
    keyboard.wait('Ctrl+f11')

    window = tk.Tk()
    window.title("Steam Login")

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    # cria a entrada (input)
    entrada = tk.Entry(master=frm_form, width=50)
    entrada.grid(row=0, column=0)
    entrada.focus_force()

    # enter executa a função basic
    window.bind('<Return>', basic)
    window.bind('<Escape>', gui_destroy_from_escape)

    window.mainloop()
