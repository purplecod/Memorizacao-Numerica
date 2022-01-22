# Memorizacao-Numerica
Jogo desenvolvido em Python

A ideia desse jogo foi inspirada em um brinquedo de decorar sequencias de cores.

Como jogar:
A cada rodada, seu computador irá gerar um numero de uma 1 á 5 e adicioná-lo em uma lista de números, depois o jogador terá que responder o primeiro número até o último da lista na ordem.
a cada rodada a lista de números vai ficando maior e mais difícil de decorar  

Como o programa funciona:
O programa começa verificando se a máquina possui um arquivo chamando “Records.txt”, se não tiver, será criado um.

Logo após, aparecera um menu com as seguintes opções:
	1 - SOLO
	2 - MULTIPLAYER
	3 - RECORDS
	4 - COMO JOGAR
	5 - SAIR DO JOGO
Digite o numero da opção para escolher o que deseja fazer

SOLO:
O jogo começara imediatamente gerando números e o jogador respondendo até perder, quando a jogatina acabar, se a lista de records ter menos que cinco nomes ou o jogador ter perdido em um número de rodadas maior que o do quinto colocado da lista de records, aparecera essa mensagem: “você pode entrar na lista de records, deseja entrar? [1/sim] [2/não]:”, pressionando “1” o script perguntara seu nome, inserindo o seu nome, você entrar na lista de records

MULTIPLAYER:
Selecionando essa opção, a tela irar exibir outro menu:
1  –  voltar
2  –  2 players
3  –  3 players
4  –  4 players

Aqui o usuário especificará quantos jogadores vai participar do jogo
O jogo no modo multiplayer:
O multiplayer tem uma experiencia semelhante ao modo solo.
primeiramente, os jogadores vão inserir seus nomes, depois disso, o jogo começara a gerar números e cada participante respondera em suas devidas rodadas, com passar do tempo os jogadores serão eliminados e o jogo terá um fim quando sobrar só um jogador, assim, definindo o vencedor e mostrando o ranking da partida.

RECORD:
Essa opção exibira os cinco jogadores com as maiores pontuações feitas no modo solo.

OPÇÃO: COMO JOGAR:
Exibira um manual de como se joga o jogo.

SAIR DO JOGO:
Encerra o jogo.
