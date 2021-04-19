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
import json
from banner import Banner

# Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;1m'

system('clear')

print(f'{G}Checando por atualizacoes... {C}')

run(["git", "pull"])
Banner()
sleep(3)
system('clear')

print(f'''{G}*By PoisonBR
{B} █████╗██████╗ ██████╗{C}████████╗ █████╗  █████╗ ██╗    ██████╗
{B}██╔═══╝██╔══██╗██╔═══╝{C}╚══██╔══╝██╔══██╗██╔══██╗██║    ██╔═══╝
{B}██║    ██████╔╝█████╗ {C}   ██║   ██║  ██║██║  ██║██║    ██████╗
{B}██║    ██╔═══╝ ██╔══╝ {C}   ██║   ██║  ██║██║  ██║██║    ╚═══██║
{B}╚█████╗██║     ██║    {C}   ██║   ╚█████╔╝╚█████╔╝██████╗██████║
{B} ╚════╝╚═╝     ╚═╝    {C}   ╚═╝    ╚════╝  ╚════╝ ╚═════╝╚═════╝{G}v1.2
{G}Trending {C}mundial geral no github!''')


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
    try:
        r = json.loads(requests.get('http://poisonbr.sytes.net:12344/ConsultaCPF/' + cpf).content.decode('utf-8'))
        print(f'''
{C}CPF: {B}{r["cpf"]}
{C}Nome: {B}{r["nome"].title()}
{C}Nascimento: {B}{r["dataNascimento"]}
{C}Nome da Mae: {B}{r["nomeMae"].title()}
{C}Nome do Pai: {B}{r["nomePai"].title()}
{C}Endereco: {B}{r["enderecoTipoLogradouro"].title()} {r["enderecoLogradouro"].title()}, {r["enderecoNumero"]}
{C}Complemento: {B}{r["enderecoComplemento"].title()}
{C}Bairro: {B}{r["enderecoBairro"].title()}
{C}Cidade: {B}{r["enderecoMunicipio"].title()}
{C}CEP: {B}{r["enderecoCep"]}
''')
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
        tipos()

    except Exception as e:
        print(f'{C}Erro: {R}{e}{RT}')
