from bs4 import BeautifulSoup
import requests
from operator import itemgetter
#
# produtos = []
# valores = []
# geral = []
#
# for i in range(100):
#
#     link = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html?p={i+1}'
#     resposta = requests.get(link)
#     html = BeautifulSoup(resposta.text, 'html.parser')
#
#     for produto in html.select('.product-item-link'):
#         produtos.append(produto.text.replace(" ",'').replace('\n',''))
#     for valor in html.select('.price-wrapper .price'):
#         valores.append(float(valor.text.replace('.','').replace(',','.').replace('R$', '')))
#
# for i in range(len(produtos)):
#     novo_registro = {'Produto':produtos[i], 'Valor':valores[i]}
#     geral.append(novo_registro)
#
# lista_final = sorted(geral, key=itemgetter('Valor'), reverse=True)
#
# for i in lista_final:
#     print(i)

from bs4 import BeautifulSoup
import requests
from operator import itemgetter

produtos = []
valores = []
geral = []

for i in range(2):

    link = f'https://br.ebay.com/b/Action-Figures/246/bn_1648288?_trkparms=%2526clkid%253D2319920863668778290{i+1}'
    resposta = requests.get(link)
    html = BeautifulSoup(resposta.text, 'html.parser')

    for produto in html.select('.b-info__title'):
        produtos.append(produto.text)
    for valor in html.select('.default'):
        valores.append(valor.text)

for i in range(len(produtos)):
    novo_registro = {'Produto':produtos[i], 'Valor':
