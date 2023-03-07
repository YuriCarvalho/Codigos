import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Quantidade de Tupla:'), sg.Input(key='tuplas', size=(20,1))],
    [sg.Text('Quantidade de Páginas:'), sg.Input(key='páginas', size=(20,1))],
    [sg.Text('Tamanho da Página:'), sg.Input(key='tamanhop', size=(20,1))],
    [sg.Text('Table Scan:'), sg.Input(key='scan', size=(20,1))],
    [sg.Button('Search'), sg.Button('Cancel')]
]

#Janela 
janela = sg.Window('Tela do Usuário', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos in (None, 'Cancel'):
        break
            
    if eventos == 'Search':
        print('ok')
