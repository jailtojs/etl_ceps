import requests 
import pandas as pd
import pprint
import json


# consumindo api ceps. 
# criei uma variavel cep que será alimentada atraves de um input 
# consumindo a api atraves do metodo GET 
# criei uma estrutura de repetição para usar cada item da retorno da api
# coloquei dentro de uma função e usei a função no final 


def consulta_cep():
    dados_json = ['cep','logradouro','complemento','bairro','localidade','uf','ibge','gia','ddd','siafi'] 
    cep = input('Insira o CEP')
    for item in dados_json:
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        data = request.json() 
        print(item,': {}'.format(data[item]))
    


def contador():
    lista = list()
    inicio = 0
    while (inicio < 999):
        inicio = inicio + 1
        lista.append(str(inicio))
    return lista


def concat_numeros():
    sufixo_cep = list()
    for numero in contador():
        qtd = len(numero)
        if qtd == 1:
            result = '00' + str(numero)
            sufixo_cep.append(result)
        elif qtd == 2:
            result = '0' + str(numero)
            sufixo_cep.append(result)
        elif qtd == 3:
            result = str(numero)
            sufixo_cep.append(result)
    print(sufixo_cep)  
