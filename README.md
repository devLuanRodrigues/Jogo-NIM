# Jogo-NIM
Tarefa proposta no curso de Introdução à Ciência da Computação com Python - Parte 1, oferecido pela USP na plataforma Coursera.

<!-- Descrição da atividade -->
# Objetivo
<p>Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.</p>
<p>Sejam <b>n</b> o número de peças inicial e <b>m</b> o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:</p>
  
  * Se <b>n</b> é múltiplo de <b>(m+1)</b>, o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
  
  * Caso contrário, o computador toma a iniciativa de começar o jogo, declarando "Computador começa!"

<p>Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.</p>
<p>Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.</p>

# Seu Programa
<p>Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.</p>
<p>Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho funcione corretamente.</p>
<p>O programa deve implementar:</p>

* Uma função <b>computador_escolhe_jogada</b> que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.

* Uma função <b>usuario_escolhe_jogada</b> que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

* Uma função <b>partida</b> que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de <b>n</b> e <b>m</b> e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

<p>Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.</p>
<p><b>Cuidado:</b> o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função). Se seu programa usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.</p>

### Campeonatos
<p>Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função <b>partida</b> esteja funcionando, você deverá criar uma outra função chamada <b>campeonato</b>. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma</p>
<br>
<p><b>Placar: Você ??? X ??? Computador</b></p>

# Execução
<p>Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar apenas uma partida (opção <b>1</b>) ou um campeonato (opção <b>2</b>).</p>
<p><b>Atenção:</b> o corretor automático vai verificar se você está utilizando exatamente as mensagens pedidas, como "Você começa!", "O computador ganhou!" etc. Deixe para usar a sua criatividade em outros lugares!</p>
<p>Veja um exemplo de como deve funcionar o jogo:</p>
