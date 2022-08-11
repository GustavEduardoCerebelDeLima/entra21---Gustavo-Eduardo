from PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Nome'), sg.Input(key='nome')],
    [sg.Text('Telefone'), sg.Input(key='telefone')],
    [sg.Text('Email'), sg.Input(key='email')],
    [sg.Button('Salvar')],
    [sg.Button('Parar')],
    [sg.Button('Continuar')]
]
resp = []
#janela
janela = sg.Window('Tela de Cadastro', layout)
#ler os eventos

location = (layout[0][1])
while True:
    eventos, valores = janela.read()
    if eventos == 'Parar':
        eventos = sg.WINDOW_CLOSED
        print('Programa encerrado')
        break
    if eventos == 'Salvar':
        resp.append(valores)
        print(valores)
        print(resp)
        resp.append(layout[0][1])
        resp.append(layout[1][1])
        resp.append(layout[2][1])

        print('Dados salvos')
    if eventos == 'Continuar':
        eventos = janela
        print('Digite seus dados')

# import PySimpleGUI as sg
# sg.theme('Dark Blue 3')  # please make your windows colorful
# event, values = sg.Window('SHA-1 & 256 Hash', [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
#                         [sg.InputText(), sg.FileBrowse()],
#                         [sg.Submit(), sg.Cancel()]]).read(close=True)
# source_filename = values[0]
# print(source_filename)
