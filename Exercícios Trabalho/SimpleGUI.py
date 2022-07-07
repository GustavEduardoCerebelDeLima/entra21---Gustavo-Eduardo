import PySimpleGUI as sg
#
# sg.theme_previewer()

theme_name_list = sg.theme_list()
# sg.theme('HotDogStand')

# print("Olá mundo")


# sg.popup("Olá mundo")

# sg.popup_ok_cancel("Olá mundo")

# sg.popup_notify("Enviado!")

# layout = [
#     [sg.Text('janela')]
# ]

# layout = [
#     [sg.Text('GUguziS')],
#     [sg.Button('OK')]
# ]

# janela = sg.Window("Titulo", layout)

# janela = sg.Window("Aula", layout)

# janela.read()
#
# janela = [
    # [sg.Text('Olá Mundo!', justification='u')],
#     [sg.Input()],            #caixinha pra escrever
#     [sg.Multiline()],        #caixinha pra escrever mais pika
#     [sg.Combo(['Paulo', 'Rodrigo'])],
#     [sg.Checkbox('Deficiente?')],
#     [sg.Radio('sim','opc'),sg.Radio('nao','opc'), sg.Radio('talves', 'opc')],
#     [sg.Spin(list(range(1,100)))],
#     [sg.Slider((1,100))],
#     [sg.Button('OK')],
#     [sg.Image('dois.PNG')],
#     [sg.Text("OLa muNDO")],
# ]
#
# bola = sg.Window("Titulo", janela)
#
# bola.read()

# layout = [
    # [sg.Input(key="nome", default_text="Digite aqui", background_color="cyan")],
    # [sg.Button('salvar')],
    # [sg.Slider((1.0,11.0), orientation='h', size=(30, 20), key='slider')],
#     [sg.Text('Ola mundo', size=(30, 1), font=30, justification='r')],
#     [sg.Slider((1,100),enable_events=False, key="slider", orientation='h')],
#     [sg.Button("salvar")]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela.close()
#
# txtBotao = 'Salvar'
# layout = []

# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     print(type(janela))
#     if eventos == 'Salvar':
#         janela['nome'].update(range=(1,10))
#         janela['txt'].update('PAULAO')
#         janela['btn'].update('PAULAO')

    #     print('nome salvo')
    #     print(valores['nome'])
    # elif eventos == sg.WINDOW_CLOSED:
    #     break


layout = [
    [sg.Text('ALUNO', size=(25, 1), font=30, justification='r')],
    [sg.Text("Nome: "), (sg.Input(key="Nome"))],
    [sg.Text("Idade:  "), (sg.Input(key="Idade"))],
    [sg.Button("OK"),(sg.Text("Temas: ")),sg.Combo([Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga'])]
]
sg.theme()

janela = sg.Window('Exercício', layout)

janela.read()

