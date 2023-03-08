import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Tamanho da Página:'), sg.Input(key='tamanhop', size=(20,1))],
    [sg.Text('Busca por Tupla:'), sg.Input(key='páginas', size=(19,1))],
    [sg.Button('Search'), sg.Button('Cancel')],
    [sg.Text('Quantidade Table Scan:'), sg.Input(key='qtdtable', size=(20,1))],
    [sg.Text('Table Scan:'), sg.Input(key='scan', size=(20,1))],
    [sg.Button('Scan'), sg.Button('Cancel2')]
]

#Janela 
janela = sg.Window('Tela do Usuário', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos in (None, 'Cancel', 'Cancel2'):
        break
            
    if eventos == 'Search':
        print('Search')
    if eventos == 'Scan':
        print('Scan')
