
from multiprocessing.pool import CLOSE
import os
import PySimpleGUI as sg
from pasta_ext import criar_pastas,verificar_extensao


layout = [
    [sg.Text("Bem vindo ao meu programa, organizador de arquivos dentro de pastas")],
    [sg.FolderBrowse('Escolha o local'),
    sg.Input('', key='diretorio')],
    [sg.Button('Clique para organizar', key='organizar')],
]


window = sg.Window('Organizador 9000', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    if events == 'organizar' and values['diretorio'] != '':
        criar_pastas(values['diretorio'])
    if values['diretorio'] == '':
        sg.popup('Por gentileza adicione o local que deseja organizar')

    sg.popup('Seus arquivos foram organizado BIP BOP :) ')




