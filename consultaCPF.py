import requests, os, time, base64, json

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
os.system('git pull && clear')
a='aHR0cHM6Ly93cy5odWJkb2Rlc2Vudm9sdmVkb3IuY29tLmJyL3YyL2NwZi8/Y3BmPQ==';b='JnRva2VuPTk5NzYzNjI1R1lucG10anVndjE4MDEyMDIwMA=='
a=a.encode('ascii');b=b.encode('ascii')
a=base64.b64decode(a);b=base64.b64decode(b)
a=a.decode('ascii');b=b.decode('ascii')
print(f'''{C}
                            /+osyhhhhhhyys++/
                         +oydddhhhhyyhhhhdddhy+/
                      /+yddhyyyys.josue.syyhddhs/
                     +hddyyssssssssssssssssssyyhdds/
                   /sddhyyyyyyssssssssssssssyyyyyhmh+
                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo
                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo
                /hmmmy{B}.           `````          `{C}smddd+
                smddm/{B}     `````          `````   {C}mdhmh/
               +ddydm+{B}  -/osyyyys+.    ./syyyyso/-{C}mdydms
               ymhyhmh{B}.yyo/ -- +hdo  /dho -- /oyh.{C}ymdyymd/
              /dmyyymd{B}.  ``.-   ./   -/.-   .``  `{C}dmhsydmo
              smdysymd{B}   shdhyydy      sdyyhddy   {C}dmyyshmy
              dmysshmy{B}                            {C}smhssymd/
             /dmyssymd{B}                            {C}hmhsyymm/
             /dmyssyhms{B}                          /{C}mdysyymm/
             /dmyssyydm/{B}  sh       hh/     -hy  .{C}dmyssyymm/
              dmhssssydd/{B} -hdhysshdysdhssyhdd  -{C}hmhyssyymd/
              ymhssssyyddo{B}``. //+/.` ./+// -` /{C}ddhysssyhmh
              +mdysssssyhdh{B} `     `/+`      -{C}sddysssssydmo
               ymhysssssyyddh/{B}`   `dm.   ` {C}sddhysssssyhmh/
               /hmhysssssyyyhdds{B} ..dm . {C}ohddhyyssssyyhmd+
                /yddhyssssssyyhhddhddddddhyyssssssyydmh+
               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/
           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/
         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+
        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo
        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms
         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/
           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///
                       ///////+++++++++++++//////
     ██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗██████╗ ██████╗
     ██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
     ██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██████╔╝██████╔╝
     ██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██╔══██╗██╔══██╗
     ██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║
     ╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
     {RT}{B}*t.me/p0isonBR*{RT}'''); time.sleep(3)

os.system('clear')

print(f'''{G}*By PoisonBR
{B} ██████╗██████╗ ███████╗{C}████████╗ ██████╗  ██████╗ ██╗     ███████╗
{B}██╔════╝██╔══██╗██╔════╝{C}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{B}██║     ██████╔╝█████╗  {C}   ██║   ██║   ██║██║   ██║██║     ███████╗
{B}██║     ██╔═══╝ ██╔══╝  {C}   ██║   ██║   ██║██║   ██║██║     ╚════██║
{B}╚██████╗██║     ██║     {C}   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{B} ╚═════╝╚═╝     ╚═╝     {C}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {G}v1.0
Consulta de CPF gratis!''')
def tipos():
  print(f'''
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar CPF.
[{G}2{C}] Gerar CPF e consultar.
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação ({G}1 {C}ou {G}2{C}): ')
  if tool=='1':
    cpf=input(f'{C}[{G}*{C}] Informe o CPF a ser consultado (sem pontos ou traços): {B}')
    consulta(cpf)
  elif tool=='2':
    gerarcpf()
  else:
    print(f'{C}[{R}-{C}] Seleção inválida.')
    time.sleep(1)
    tipos()
    
def gerarcpf():
  print(f'{C}[{G}*{C}] Gerando CPF...')
  time.sleep(1)
  cpf=requests.request('GET','http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
  cpf2=cpf['data']['number_formatted']
  cpf=cpf['data']['number']
  print(f'{C}[{Y}i{C}] O CPF gerado foi: {B}'+cpf2)
  time.sleep(1)
  print(f'{C}[{G}*{C}] Consultando CPF gerado...')
  consulta(cpf)
  
def consulta(cpf):
  results=requests.request('GET', a+cpf+b).json()
  if results['status']==False:
    rf=results['message']
    print(f'{C}[{R}-{C}] Erro, resposta do servidor: '+rf)
    tipos()
  nome=results['result']['nome_da_pf'].capitalize()
  nascimento=results['result']['data_nascimento']
  situacao=results['result']['situacao_cadastral'].capitalize()
  inscricao=results['result']['data_inscricao']

  print(f'''
{C}[{G}!{C}] Resultado da consulta:
{C}Nome: {B}{nome}
{C}Data de nascimento: {B}{nascimento}
{C}Data de inscrição: {B}{inscricao}
{C}Situação Cadastral: {B}{situacao}
''')
  nova=input(f'{C}[{G}+{C}]Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
  if nova=='s' or nova=='sim':
    tipos()
  else:
    print()
    print(f'{C}Me acompanhe no Github: {G}https://github.com/p0isonBR{C}')
    exit()
tipos()
