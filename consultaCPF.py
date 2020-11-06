import requests, os, time, base64

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
os.system('git pull && clear')
a='aHR0cHM6Ly93cy5odWJkb2Rlc2Vudm9sdmVkb3IuY29tLmJyL3YyL2NwZi8/Y3BmPQ==';b='JnRva2VuPTk5NzYzNjI1R1lucG10anVndjE4MDEyMDIwMA=='
a=a.encode('ascii');b=b.encode('ascii')
a=a.base64.b64decode(a);b=b.base64.b64decode(a)
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
{B} ╚═════╝╚═╝     ╚═╝     {C}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {C}v1.0{C}
Consulta de CPF gratis!''')

def consulta():
  cpf=input('{C}[{G}+{C}]Informe o CPF a ser consultado (sem pontos ou traços): {B}')
 
  result=requests.requets('GET', a+cpf+b).json()
  if result['status']=='false':
    print('{C}[{R}-{C}]Numero nao encontrado na base da Receita Federal, tente outro.')
    consulta()
  else:
    nome=result['result']['nome_da_pf']
    nascimento=result['result']['data_nascimento']
    situacao=result['result']['situacao_cadastral']
    inscricao=result['result']['data_inscricao']

    print(f'''
{C}Nome: {nome}
{C}Data de nascimento: {nascimento.replace('\','')}
{C}Data de inscrição: {inscricao}
{C}Situação Cadastral: {situacao}
...)
    nova=input(f'{C}Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ').lower()
    if nova=='s' or nova=='sim':
      consulta()
    else:
      print(f'{C}Me acompanhe no Github: {G}https://github.com/p0isonBR'{C})
