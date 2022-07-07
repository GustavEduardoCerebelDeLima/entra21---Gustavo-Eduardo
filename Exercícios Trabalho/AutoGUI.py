import pyautogui
from time import sleep

# while True:
#     print(pyautogui.position())
#     sleep(2)

"Move o mouse para *tal* posição"

# pyautogui.moveTo(100, 100)

"Move o mouse *tantas* posições para cima e/ou lado"

# pyautogui.moveRel(100,100,3)

"positivo direita"
"negativo esquerda"
"primeiro valor x e segundo valor y"

# pyautogui.click()
# pyautogui.rightClick()
# pyautogui.leftClick()
# pyautogui.doubleClick()
# pyautogui.tripleClick()

"Atalhos"

# pyautogui.hotkey("ctrl","shift","esc")
# pyautogui.hotkey("win","r")

# pyautogui.keyDown('win')
# pyautogui.keyDown('r')
# pyautogui.keyUp('r')
# pyautogui.keyUp('win')

# "Abrir calculadora"
#
# pyautogui.press("win")
# pyautogui.write("calculadora", interval=0.5)
# pyautogui.press("Enter")

# print(pyautogui.KEYBOARD_KEYS())

# sleep(3)
# with pyautogui.hold("alt"):
#     pyautogui.press("tab", presses=2, interval=1)


# pyautogui.dragTo(50, 50, button="right")

# sleep(3)
# pyautogui.dragRel(-600, -200, duration=4)

# pyautogui.alert(text="EVACUEM A INTERNET POIS CALVOS ESTÃO ONLINE NESTE MOMENTO!!!!!", title="ALERTA", button="OK")

# alou = pyautogui.prompt(text="Cauan", title="Alert", default="")
# print(alou)

# pyautogui.confirm(text="Cauan", title="Alert", buttons=("OK", "CANCEL"))

# pyautogui.password(text="Cauan", title="Alert", default="", mask="*")

# sleep(3)
# x = pyautogui.locateOnScreen("dois.PNG")
# pyautogui.click(x)

#ATIVIDADE1

# pyautogui.press("win")
# pyautogui.write("notas", interval=0.2)
# pyautogui.press("Enter")
# sleep(1)
# pyautogui.write("Eu quero um gol", interval=0.2)

#ATIVIDADE2

# num = input("Digite seu cálculo: ")
#
# pyautogui.press("win")
# pyautogui.write("calculadora", interval=0.2)
# pyautogui.press("Enter")
#
# sleep(2)
#
# pyautogui.write(num)
# pyautogui.press("=")

#ATIVIDADE3

pyautogui.moveTo(185, 1061)
sleep(2)

pyautogui.typewrite("paint")
pyautogui.click()
sleep(2)

pyautogui.press("Enter")

sleep(2)
distancia = 300
pyautogui.moveTo(363, 249)

while distancia > 0:
   pyautogui.drag(distancia, 0, duration=0.2)
   distancia = distancia - 20
   pyautogui.drag(0, distancia, duration=0.2)
   pyautogui.drag(-distancia, 0, duration=0.2)
   distancia = distancia - 20
   pyautogui.drag(0, -distancia, duration=0.2)
sleep(2)

#PROVA

# pyautogui.click(50, 10)
#
# sleep(1)
#
# pyautogui.click(200,300)
#
# sleep(1)
#
# pyautogui.write("Bondia", interval=0.2)
#
# pyautogui.click("enter")

#BGLH PIKA DO GUSTAVO

from pyautogui import typewrite, click, press, moveTo
from time import sleep
from webbrowser import open
from getpass import getpass
from re import fullmatch
from email_validator import validate_email, EmailNotValidError

# Expressão regular
regex = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Função para verificar se o e-mail está dentro da expressão regular
def check(variavel):
    if fullmatch(regex, variavel):
        return 1
    else:
        return 2


e_mail = input('Insira seu e-mail\n>>> ')
senha = getpass(prompt="Insira sua senha\n>>> ", stream=None)

while True:  # Verificar se o e-mail está válido.
    if check(e_mail) == 1:
        try:
            e_mail = validate_email(e_mail).email
            break
        except EmailNotValidError as e:
            e_mail = input("Insira um e-mail válido!\n>>> ")
            continue
    else:
        e_mail = input("Insira um e-mail válido!\n>>> ")

selecionar_aula = input("Qual é a sua aula hoje?\n[1] Python\n[2] Empreendedorismo e Inovação\n[3] Inglês"
                        "\n[4] Desenvolvimento Humano\n[5] Contabilidade e Finanças\n>>> ")
selecionar_avaliacao = input("Gostaria de fazer a avaliação automática ou selecionar os critérios da sua avaliação?\n[1] Automática\n[2] Selecionar critérios\n>>> ")

# Coordenada para cada cada aula.
if selecionar_aula == "2":
    selecionar_aula = 1775, 425
elif selecionar_aula == "3":
    selecionar_aula = 1775, 555
elif selecionar_aula == "4":
    selecionar_aula = 1775, 672
elif selecionar_aula == "5":
    selecionar_aula = 1775, 794
elif selecionar_aula != "5":
    selecionar_aula = 1775, 296

# Opção da avaliação não ser 100% automatizada
if selecionar_avaliacao != "1":
    print("""Critérios de avaliação.
1- Péssimo
2- Ruim
3- Razoável
4- Bom
5- Excelente""")
    try:
        print("\nAvaliação geral sobre seu dia!")
        hoje = int(input("Hoje\n>>> "))
        while hoje < 1 or hoje > 5:
            hoje = int(input("Por favor, número valido!\n>>> "))

        print("\nQuanto ao instrutor.")
        metodologia = int(input("Metodologia\n>>> "))
        while metodologia < 1 or metodologia > 5:
            metodologia = int(input("Por favor, número valido!\n>>> "))

        postura = int(input("Postura\n>>> "))
        while postura < 1 or postura > 5:
            postura = int(input("Por favor, número valido!\n>>> "))

        dominio = int(input("Domínio\n>>> "))
        while dominio < 1 or dominio > 5:
            dominio = int(input("Por favor, número valido!\n>>> "))

        print("\nQuanto a empresa.")
        ambiente = int(input("Ambiente\n>>> "))
        while ambiente < 1 or ambiente > 5:
            ambiente = int(input("Por favor, número valido!\n>>> "))

        micros = int(input("Micros\n>>> "))
        while micros < 1 or micros > 5:
            micros = int(input("Por favor, número valido!\n>>> "))

        recepcao = int(input("Recepção\n>>> "))
        while recepcao < 1 or recepcao > 5:
            recepcao = int(input("Por favor, número valido!\n>>> "))

    except ValueError:
        print("Digite apenas números válidos!")
        exit()

    open("https://externo.proway.com.br/login-aluno")
    sleep(5)

    click(893, 525, interval=0.10)
    typewrite(e_mail, interval=0.0)
    sleep(0.5)
    click(880, 639, interval=0.10)
    typewrite(senha, interval=0.0)
    sleep(0.3)
    click(935, 738, interval=0.10)
    sleep(0.3)

    click(selecionar_aula, interval=0.5)

    if hoje == 1:
        click(845, 330, interval=0.5)
    elif hoje == 2:
        click(902, 330, interval=0.5)
    elif hoje == 3:
        click(950, 330, interval=0.5)
    elif hoje == 4:
        click(1000, 330, interval=0.5)
    elif hoje == 5:
        click(1060, 330, interval=0.5)

    if metodologia == 1:
        click(845, 480, interval=0.5)
    elif metodologia == 2:
        click(902, 480, interval=0.5)
    elif metodologia == 3:
        click(950, 480, interval=0.5)
    elif metodologia == 4:
        click(1000, 480, interval=0.5)
    elif metodologia == 5:
        click(1060, 480, interval=0.5)

    if postura == 1:
        click(845, 590, interval=0.5)
    elif postura == 2:
        click(902, 590, interval=0.5)
    elif postura == 3:
        click(950, 590, interval=0.5)
    elif postura == 4:
        click(1000, 590, interval=0.5)
    elif postura == 5:
        click(1060, 590, interval=0.5)

    if dominio == 1:
        click(845, 706, interval=0.5)
    elif dominio == 2:
        click(902, 706, interval=0.5)
    elif dominio == 3:
        click(950, 706, interval=0.5)
    elif dominio == 4:
        click(1000, 706, interval=0.5)
    elif dominio == 5:
        click(1060, 706, interval=0.5)

    if ambiente == 1:
        click(845, 860, interval=0.5)
    elif ambiente == 2:
        click(902, 860, interval=0.5)
    elif ambiente == 3:
        click(950, 860, interval=0.5)
    elif ambiente == 4:
        click(1000, 860, interval=0.5)
    elif ambiente == 5:
        click(1060, 860, interval=0.5)

    if micros == 1:
        click(845, 970, interval=0.5)
    elif micros == 2:
        click(902, 970, interval=0.5)
    elif micros == 3:
        click(950, 970, interval=0.5)
    elif micros == 4:
        click(1000, 970, interval=0.5)
    elif micros == 5:
        click(1060, 970, interval=0.5)

    press("end", interval=0.1)
    sleep(0.3)

    if recepcao == 1:
        click(845, 726, interval=0.5)
    elif recepcao == 2:
        click(902, 726, interval=0.5)
    elif recepcao == 3:
        click(950, 726, interval=0.5)
    elif recepcao == 4:
        click(1000, 726, interval=0.5)
    elif recepcao == 5:
        click(1060, 726, interval=0.5)

    sleep(0.3)
    moveTo(1122, 983)

elif selecionar_avaliacao == "1":
    open("https://externo.proway.com.br/login-aluno")  # Parte de abrir e fazer login!
    sleep(4)
    click(893, 525, interval=0.10)
    typewrite(e_mail, interval=0.0)
    sleep(0.5)
    click(880, 639, interval=0.10)
    typewrite(senha, interval=0.0)
    sleep(0.3)
    click(935, 738, interval=0.10)
    sleep(0.3)

    # Clickar no botao para começar a avaliar
    click(selecionar_aula, interval=0.5)

    # Avaliar
    click(1060, 330, interval=0.5)
    click(1060, 480, interval=0.5)
    click(1060, 590, interval=0.5)
    click(1060, 706, interval=0.5)
    click(1060, 860, interval=0.5)
    click(1060, 970, interval=0.5)
    press("end", interval=0.1)
    sleep(0.3)
    click(1060, 726, interval=0.5)
    sleep(0.3)

    # Finalizar!
    moveTo(1122, 983)
    sleep(7)
















