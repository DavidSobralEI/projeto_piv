import requests
from bs4 import BeautifulSoup
import csv
import unicodedata



def continente():
    urls=['https://www.continente.pt/produto/cebola-roxa-continente-5394157.html',
          'https://www.continente.pt/produto/batata-vermelha-continente-5454736.html',
          'https://www.continente.pt/produto/banana-continente-2597619.html',
          'https://www.continente.pt/produto/leite-uht-meio-gordo-mimosa-2210946.html',
          'https://www.continente.pt/produto/maca-gala-continente-7174689.html',
          'https://www.continente.pt/produto/pera-packhams-continente-2373500.html',
          'https://www.continente.pt/produto/laranja-igp-algarve-2507240.html',
          'https://www.continente.pt/produto/queijo-flamengo-fatiado-continente-6184775.html',
          'https://www.continente.pt/produto/cenoura-continente-5063155.html',
          'https://www.continente.pt/produto/brocolos-bonduelle-5383902.html',
          'https://www.continente.pt/produto/broa-de-milho-doce-continente-7680684.html',
          'https://www.continente.pt/produto/bifes-de-frango-continente-7068833.html',
          'https://www.continente.pt/produto/agua-sem-gas-garrafao-caldas-de-penacova-4028645.html',
          'https://www.continente.pt/produto/chourico-de--carne-portugal-de-sabores-7435436.html',
          'https://www.continente.pt/produto/fiambre-da-pa-fatiado-continente-7102478.html',
          'https://www.continente.pt/produto/curgete-verde-continente-2076759.html',
          'https://www.continente.pt/produto/atum-em-oleo-vegetal-e-continente-7301722.html',
          'https://www.continente.pt/produto/ovos-de-solo-classe-m-continente-7284496.html',
          'https://www.continente.pt/produto/papel-higienico-2-folhas-continente-4507682.html',
          'https://www.continente.pt/produto/batata-frita-lisa-sabor-camponesa-continente-4462848.html'
          ]

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        nome = soup.find('h1',class_='pwc-h3 col-h3 product-name pwc-font--primary-extrabold mb-0').get_text(strip=True)
        print('nome:',nome)
        categoria = soup.find('span',class_='breadcrumb-fill',itemprop='name').get_text(strip=True)
        print('categoria',categoria)
        preco = soup.find('span',class_='ct-price-formatted').get_text(strip=True)
        print('preço:',preco)
        loja = soup.find('a',class_='ct-pdp--brand col-pdp--brand').get_text(strip=True)
        print('loja:',loja,'\n ------------------------')
        

#def auchan():
    #urls = ['https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/batata-vermelha-auchan-3-kg/3483188.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/cebola-kg/21946.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/fruta/banana-e-frutos-tropicais/banana-importada-kg/234229.html',
           # 'https://www.auchan.pt/pt/alimentacao/produtos-lacteos/leites/leite-uht/leite-mimosa-uht-meio-gordo-1l/11885.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/maca-gala-auchan-kg/3356631.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/pera-rocha-auchan-kg/3356405.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/fruta/laranjas-clementinas-e-limoes/laranja-algarve-igp-auchan-cultivamos-o-bom-kg/547063.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/queijaria/queijo-fatiado-e-barra/queijo-flamengo-auchan-a-mesa-em-portugal-acores-fatias-500g/3352009.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/legumes/abobora-cenoura-e-alho-frances/cenoura-auchan-kg/3374234.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/legumes/couves-brocolos-e-espinafres/brocolos-kg/20649.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/padaria/pao-fresco-e-broa/broa-de-milho-amarelo-producao-propria-kg/2643802.html',
           # 'https://www.auchan.pt/pt/biologicos-e-alternativas/biologicos/biologicos-produtos-frescos/talho-e-peixaria/talho/bife-peito-de-frango-biologic-bio-300-g/3499575.html',
           # 'https://www.auchan.pt/pt/bebidas-e-garrafeira/aguas/aguas-sem-gas/agua-caldas-de-penacova-garrafao-5l/333590.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/charcutaria/chourico-bacon-e-outros/chourico-de-carne-auchan-corrente-800-g/2975441.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/charcutaria/fiambre-de-porco/fiambre-da-pa-auchan-fatias-200-g/2975436.html',
           # 'https://www.auchan.pt/pt/produtos-locais/produtos-locais-frescos/frutas-e-legumes-produtos-locais/curgete-kg-produto-local/68695.html',
           # 'https://www.auchan.pt/pt/alimentacao/mercearia/conservas/atum/atum-posta-auchan-em-oleo-120%2878%29g/686901.html',
           # 'https://www.auchan.pt/pt/produtos-frescos/ovos/ovos-de-galinhas-criadas-no-solo/ovos-auchan-galinhas-solo-classe-m-uma-duzia/2945539.html',
           # 'https://www.auchan.pt/pt/beleza-e-higiene/papel-higienico-e-lencos-papel/papel-higienico-eco-e-premium/papel-higienico-auchan-ecologico-2-folhas-100-pasta-reciclada-12-rolos-%3D-24-rolos/3347366.html',
           # 'https://www.auchan.pt/pt/alimentacao/mercearia/batatas-fritas-e-aperitivos-snacks/batatas-com-sabores/batatas-auchan-fritas-girassol-camponesas-150g/1182735.html']

    #for url in urls:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html-parser')

        # loja = soup.find() 
        # nome = soup.find('h1')
        # preco =
        # categoria =
        # rating = 
        # reviews =
        # reviews_nr = 


def aldi():
    urls = ['https://www.aldi.pt/oportunidades-da-semana/a-partir-de-4-f-26-6/cebola-7005581-2-0.article.html',
            'https://www.aldi.pt/oportunidades-da-semana/a-partir-de-4-f-26-6/batata-roxa-nacional-7005571-2-0.article.html',
            'https://www.aldi.pt/produto/snack-crocante-de-cenoura-banana-biologico-7006070-1-0.article.html#/produtos/bem-estar-beleza-e-bebe/bebe',
            'https://www.aldi.pt/produto/leite-meio-gordo-605-1-0.article.html#/produtos/laticinios/leite-natas-e-ovos',
            'https://www.aldi.pt/produto/chips-de-maca-desidratada-7000549-1-0.article.html#/produtos/vegan-e-vegetariano',
            'https://www.aldi.pt/produto/nectar-de-pera-161-1-0.article.html#/produtos/bebidas-nao-alcoolicas/sumos-e-refrigerantes',
            'https://www.aldi.pt/produto/nectar-de-laranja-417-1-0.article.html#/produtos/bebidas-nao-alcoolicas/sumos-e-refrigerantes',
            'https://www.aldi.pt/oportunidades-da-semana/a-partir-de-4-f-26-6/queijo-flamengo-em-fatias-3514-2-0.article.html',
            'https://www.aldi.pt/produto/cenoura-ralada-7008480-1-0.article.html#/produtos/frescos-e-prontos/pronto-a-comer',
            'https://www.aldi.pt/produto/brocolos-6671-1-0.article.html#/produtos/congelados/frutas-e-legumes',
            'https://www.aldi.pt/produto/broa-de-milho-4143-1-0.article.html#/produtos/pao-e-pastelaria/nosso-forno',
            'https://www.aldi.pt/produto/bifes-de-frango-nacionais-5078-1-0.article.html#/produtos/carne-e-peixe/carne',
            'https://www.aldi.pt/oportunidades-da-semana/a-partir-de-4-f-26-6/agua-mineral-7000599-2-0.article.html',
            'https://www.aldi.pt/produto/chourico-alentejano-9905-1-0.article.html#/produtos/frescos-e-prontos/charcutaria',
            'https://www.aldi.pt/produto/fiambre-da-pa-7006855-1-0.article.html#/produtos/frescos-e-prontos/charcutaria',
            'https://www.aldi.pt/produto/pepinos-em-vinagre-4420-1-0.article.html#/produtos/mercearia/conservas',
            'https://www.aldi.pt/produto/atum-posta-em-oleo-vegetal-9692-1-0.article.html#/produtos/mercearia/conservas',
            'https://www.aldi.pt/produto/ovos-do-solo-classe-m-nacionais-6273-1-0.article.html#/produtos/laticinios/leite-natas-e-ovos',
            'https://www.aldi.pt/produto/papel-higienico-3-folhas-5254-1-0.article.html#/produtos/casa-e-lar/papel',
            'https://www.aldi.pt/oportunidades-da-semana/a-partir-de-4-f-26-6/batatas-fritas-classicas-8531-2-0.article.html']

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        nome = soup.find('h1').get_text(strip=True)
        print('nome:',nome)
        categoria = soup.find_all('li', class_='mod-breadcrumb__item')
        subcat = categoria[2].text
        print('categoria:', subcat)
        preco = soup.find('span',class_='price__wrapper').get_text(strip=True)
        print('preço:',preco)
        loja = soup.find('span',class_='mod-article-intro__header-headline-small').get_text(strip=True)
        print('loja:',loja,'\n ------------------------')


if __name__=='__main__':
    #continente()
    aldi()