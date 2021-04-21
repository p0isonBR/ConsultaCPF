#!/usr/bin/ python
# -*- coding: utf-8 -*-
#
# Autor:    p0isonBR
# GitHub:   https://github.com/p0isonBR
# Email:    poisonbr@pm.me
# Contato:  https://t.me/p0isonBR
# 
# Apoie meu trabalho: pix 04a06b5f-9036-47aa-9611-445b7c5e1246
# 
# -There is no knowledge that is not power-

from os import system
from time import sleep
from subprocess import run
import requests
import re
import base64
import banner as b

# Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;1m'


def tipos():
    print(f'''
{C}[{G}i{C}] Formas de operação: 
[{G}1{C}] Consultar CPF.
[{G}2{C}] Gerar CPF e consultar.
''')
    tool = input(f'{C}[{G}+{C}] Selecione a forma de operação ({G}1 {C}ou {G}2{C}): ' + B)

    if tool == '1':
        cpf = input(f'{C}[{G}*{C}] Informe o CPF a ser consultado: {B}')
        cpf = re.sub('[^0-9]+', '', cpf)
        consulta(cpf)

    elif tool == '2':
        gerarcpf()

    else:
        print(f'{C}[{R}-{C}] Seleção inválida.')

        sleep(1)
        tipos()


def gerarcpf():
    print(f'{C}[{G}*{C}] Gerando CPF...')

    sleep(1)
    cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
    cpf2 = cpf['data']['number_formatted']
    cpf = cpf['data']['number']
    print(f'{C}[{Y}i{C}] O CPF gerado foi: {B} {cpf2}')

    sleep(1)
    print(f'{C}[{G}*{C}] Consultando CPF gerado...')
    consulta(cpf)


def consulta(cpf):
    a = [x + 76 for x in range(5)]
    
    ab = chr(a[0])
    c = chr(a[1])
    d = chr(a[2])
    e = chr(a[3])
    a = chr(a[4])

    a = bytes.fromhex(b.a + b.b + b.c + b.d + b.e).decode()
    
    try:
        ab = requests.get(base64.b64decode(re.search("\'(.*?)\'", a).group(1)).decode() + cpf).json()
        
        print(f"""
{C}CPF: {B}{ab["cpf"]}
{C}Nome: {B}{ab["nome"].title()}
{C}Nascimento: {B}{ab["dataNascimento"]}
{C}Nome da Mae: {B}{ab["nomeMae"].title()}
{C}Nome do Pai: {B}{ab["nomePai"].title()}
{C}Endereco: {B}{ab["enderecoTipoLogradouro"].title()} {ab["enderecoLogradouro"].title()}, {ab["enderecoNumero"]}
{C}Complemento: {B}{ab["enderecoComplemento"].title()}
{C}Bairro: {B}{ab["enderecoBairro"].title()}
{C}Cidade: {B}{ab["enderecoMunicipio"].title()}
{C}CEP: {B}{ab["enderecoCep"]}
""")
        nova = input(f'{C}[{G}+{C}]Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()

        if nova == 's' or nova == 'sim':
            tipos()

        else:
            print(f'\n{C}Me acompanhe no Github: {G}https://github.com/p0isonBR{C}')
            exit()

    except Exception:
        print(f'{R}CPF consultado/gerado nao existe{C}')
        tipos()


if __name__ == '__main__':
    try:
        system('clear')
        print(f'{G}Checando por atualizacoes... {C}')
        run(["git", "pull"])
        system('clear')
        print(b.banner)
        sleep(3)
        system('clear')
        print(b.banner2)
        tipos()

    except Exception as e:
        print(f'{C}Erro: {R}{e}{RT}')
