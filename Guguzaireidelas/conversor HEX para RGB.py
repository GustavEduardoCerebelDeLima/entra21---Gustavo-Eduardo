r = int(input('Digite o valor de Red: '))
g = int(input('Digite o valor de Green: '))
b = int(input('Digite o valor de Blue: '))

if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
    print('Revise os números')
else:
    print(f'#{r:02X}{g:02X}{b:02X}')

# if True:
#     print("café com leite")
# else:
#     print("café com açucar")