def vermelho(txt):
  return f'\033[31m{txt}\033[m'
def verde (txt):
  return f'\033[32m{txt}\033[m'
def amarelo (txt):
  return f'\033[33m{txt}\033[m'
def azul (txt):
  return f'\033[34m{txt}\033[m'
def roxo (txt):
  return f'\033[35m{txt}\033[m'
def ciano (txt):
  return f'\033[36m{txt}\033[m'
def cinza (txt):
  return f'\033[37m{txt}\033[m' 
  

def titulo(txt):
  print('==='*15)
  print(txt.center(44))
  print('==='*15)


def cadasmenu(lista,txt='MENU PRINCIPAL'):
  c=1
  titulo(txt)
  for items in lista:
    print(f'{c} - {roxo(items)}')
    c+=1
  print('==='*15)


def rank(lista):
  c=1
  titulo('RANKING DA PARTIDA')
  for a in range(len(lista)-1,-1,-1):
    print(f'{c}° - {lista[a]}')
    c+=1
  print('==='*15)