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
R = "\033[1;31m"
B = "\033[1;34m"
C = "\033[1;37m"
Y = "\033[1;33m"
G = "\033[1;32m"
RT = "\033[;1m"

system("clear")

print(G + "Checando por atualizacoes..." + C)

run(["git", "pull"])
Banner()
sleep(3)
system("clear")

print(
    G + f"""*By PoisonBR
{B} █████╗██████╗ ██████╗{C}████████╗ █████╗  █████╗ ██╗    ██████╗
{B}██╔═══╝██╔══██╗██╔═══╝{C}╚══██╔══╝██╔══██╗██╔══██╗██║    ██╔═══╝
{B}██║    ██████╔╝█████╗ {C}   ██║   ██║  ██║██║  ██║██║    ██████╗
{B}██║    ██╔═══╝ ██╔══╝ {C}   ██║   ██║  ██║██║  ██║██║    ╚═══██║
{B}╚█████╗██║     ██║    {C}   ██║   ╚█████╔╝╚█████╔╝██████╗██████║
{B} ╚════╝╚═╝     ╚═╝    {C}   ╚═╝    ╚════╝  ╚════╝ ╚═════╝╚═════╝{G}v1.2
{G}Trending {C}mundial geral no github!"""
)


def tipos():
    print(
        f"""
{C}[{G}i{C}] Formas de operação: 
[{G}1{C}] Consultar CPF.
[{G}2{C}] Gerar CPF e consultar.
        """
    )

    tool = input(
        C + f"[{G}+{C}] Selecione a forma de operação ({G}1 {C}ou {G}2{C}): " + B
    )

    if tool == "1":
        cpf = input(C + f"[{G}*{C}] Informe o CPF a ser consultado: " + B)
        cpf = re.sub("[^0-9]+", "", cpf)
        consulta(cpf)

    elif tool == "2":
        gerarcpf()

    else:
        print(C + f"[{R}-{C}] Seleção inválida.")

        sleep(1)
        tipos()


def gerarcpf():
    print(C + f"[{G}*{C}] Gerando CPF...")

    sleep(1)

    cpf = requests.get(
        "http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2\
        ac208dd141"
    ).json()

    cpf2 = cpf["data"]["number_formatted"]
    cpf = cpf["data"]["number"]

    print(C + f"[{Y}i{C}] O CPF gerado foi: " + B + cpf2)

    sleep(1)
    
    print(C + f"[{G}*{C}] Consultando CPF gerado...")
    consulta(cpf)


def consulta(cpf):
    try:
        r = json.loads(
            requests.get(
                "https://sherlockconsulta.herokuapp.com/cpf/" + cpf
            ).content.decode()
        )

        for k, v in r["result"].items():
            print(B + k.replace("_", " ").title() + ": " + C + v.title())

        nova = input(
            C + f"[{G}+{C}]Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: "
        ).lower()

        if nova == "s" or nova == "sim":
            tipos()

        else:
            print(
                C + f"Me acompanhe no Github: {G}https://github.com/p0isonBR" + C
            )
            exit()

    except Exception:
        print(R + "CPF consultado/gerado nao existe" + C)
        tipos()


if __name__ == '__main__':
    try:
        tipos()

    except Exception as e:
        print(C + f"Erro: {R}{e}" + RT)
