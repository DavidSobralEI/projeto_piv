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
        

if __name__=='__main__':
    continente()