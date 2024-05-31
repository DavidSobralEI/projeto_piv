import requests
from bs4 import BeautifulSoup
import csv



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
        

def auchan():
    urls = ['https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/batata-vermelha-auchan-3-kg/3483188.html',
            'https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/cebola-kg/21946.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/banana-e-frutos-tropicais/banana-importada-kg/234229.html',
            'https://www.auchan.pt/pt/alimentacao/produtos-lacteos/leites/leite-uht/leite-mimosa-uht-meio-gordo-1l/11885.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/maca-gala-auchan-kg/3356631.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/pera-rocha-auchan-kg/3356405.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/laranjas-clementinas-e-limoes/laranja-algarve-igp-auchan-cultivamos-o-bom-kg/547063.html',
            'https://www.auchan.pt/pt/produtos-frescos/queijaria/queijo-fatiado-e-barra/queijo-flamengo-auchan-a-mesa-em-portugal-acores-fatias-500g/3352009.html',
            'https://www.auchan.pt/pt/produtos-frescos/legumes/abobora-cenoura-e-alho-frances/cenoura-auchan-kg/3374234.html',
            'https://www.auchan.pt/pt/produtos-frescos/legumes/couves-brocolos-e-espinafres/brocolos-kg/20649.html',
            'https://www.auchan.pt/pt/produtos-frescos/padaria/pao-fresco-e-broa/broa-de-milho-amarelo-producao-propria-kg/2643802.html',
            'https://www.auchan.pt/pt/biologicos-e-alternativas/biologicos/biologicos-produtos-frescos/talho-e-peixaria/talho/bife-peito-de-frango-biologic-bio-300-g/3499575.html',
            'https://www.auchan.pt/pt/bebidas-e-garrafeira/aguas/aguas-sem-gas/agua-caldas-de-penacova-garrafao-5l/333590.html',
            'https://www.auchan.pt/pt/produtos-frescos/charcutaria/chourico-bacon-e-outros/chourico-de-carne-auchan-corrente-800-g/2975441.html',
            'https://www.auchan.pt/pt/produtos-frescos/charcutaria/fiambre-de-porco/fiambre-da-pa-auchan-fatias-200-g/2975436.html',
            'https://www.auchan.pt/pt/produtos-locais/produtos-locais-frescos/frutas-e-legumes-produtos-locais/curgete-kg-produto-local/68695.html',
            'https://www.auchan.pt/pt/alimentacao/mercearia/conservas/atum/atum-posta-auchan-em-oleo-120%2878%29g/686901.html',
            'https://www.auchan.pt/pt/produtos-frescos/ovos/ovos-de-galinhas-criadas-no-solo/ovos-auchan-galinhas-solo-classe-m-uma-duzia/2945539.html',
            'https://www.auchan.pt/pt/beleza-e-higiene/papel-higienico-e-lencos-papel/papel-higienico-eco-e-premium/papel-higienico-auchan-ecologico-2-folhas-100-pasta-reciclada-12-rolos-%3D-24-rolos/3347366.html',
            'https://www.auchan.pt/pt/alimentacao/mercearia/batatas-fritas-e-aperitivos-snacks/batatas-com-sabores/batatas-auchan-fritas-girassol-camponesas-150g/1182735.html']

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html-parser')

        loja = soup.find() 
        nome = soup.find('h1')
        # preco =
        # categoria =
        # rating = 
        # reviews =
        # reviews_nr = 


def Lidl():
    urls = ['https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/batata-vermelha-auchan-3-kg/3483188.html',
            'https://www.auchan.pt/pt/produtos-frescos/legumes/batatas-alho-e-cebola/cebola-kg/21946.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/banana-e-frutos-tropicais/banana-importada-kg/234229.html',
            'https://www.auchan.pt/pt/alimentacao/produtos-lacteos/leites/leite-uht/leite-mimosa-uht-meio-gordo-1l/11885.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/maca-gala-auchan-kg/3356631.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/macas-peras-e-uvas/pera-rocha-auchan-kg/3356405.html',
            'https://www.auchan.pt/pt/produtos-frescos/fruta/laranjas-clementinas-e-limoes/laranja-algarve-igp-auchan-cultivamos-o-bom-kg/547063.html',
            'https://www.auchan.pt/pt/produtos-frescos/queijaria/queijo-fatiado-e-barra/queijo-flamengo-auchan-a-mesa-em-portugal-acores-fatias-500g/3352009.html',
            'https://www.auchan.pt/pt/produtos-frescos/legumes/abobora-cenoura-e-alho-frances/cenoura-auchan-kg/3374234.html',
            'https://www.auchan.pt/pt/produtos-frescos/legumes/couves-brocolos-e-espinafres/brocolos-kg/20649.html',
            'https://www.auchan.pt/pt/produtos-frescos/padaria/pao-fresco-e-broa/broa-de-milho-amarelo-producao-propria-kg/2643802.html',
            'https://www.auchan.pt/pt/biologicos-e-alternativas/biologicos/biologicos-produtos-frescos/talho-e-peixaria/talho/bife-peito-de-frango-biologic-bio-300-g/3499575.html',
            'https://www.auchan.pt/pt/bebidas-e-garrafeira/aguas/aguas-sem-gas/agua-caldas-de-penacova-garrafao-5l/333590.html',
            'https://www.auchan.pt/pt/produtos-frescos/charcutaria/chourico-bacon-e-outros/chourico-de-carne-auchan-corrente-800-g/2975441.html',
            'https://www.auchan.pt/pt/produtos-frescos/charcutaria/fiambre-de-porco/fiambre-da-pa-auchan-fatias-200-g/2975436.html',
            'https://www.auchan.pt/pt/produtos-locais/produtos-locais-frescos/frutas-e-legumes-produtos-locais/curgete-kg-produto-local/68695.html',
            'https://www.auchan.pt/pt/alimentacao/mercearia/conservas/atum/atum-posta-auchan-em-oleo-120%2878%29g/686901.html',
            'https://www.auchan.pt/pt/produtos-frescos/ovos/ovos-de-galinhas-criadas-no-solo/ovos-auchan-galinhas-solo-classe-m-uma-duzia/2945539.html',
            'https://www.auchan.pt/pt/beleza-e-higiene/papel-higienico-e-lencos-papel/papel-higienico-eco-e-premium/papel-higienico-auchan-ecologico-2-folhas-100-pasta-reciclada-12-rolos-%3D-24-rolos/3347366.html',
            'https://www.auchan.pt/pt/alimentacao/mercearia/batatas-fritas-e-aperitivos-snacks/batatas-com-sabores/batatas-auchan-fritas-girassol-camponesas-150g/1182735.html']

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
        

if __name__=='__main__':
    continente()