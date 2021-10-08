<img src="https://www.udistrital.edu.co/themes/custom/versh/images/default/preloader.png" width="200">
<h1>JUEGO 21 -PYTHON</h1>
<h2>Integrantes</h2>
<ul>
<li>Iván Andrés Serna cod: 20211395007</li>
<li>Omar Pedraza Romero cod: 20211495007</li>
<li>Wilmer Jair Contreras Leguizamón cod: 20211495002</li>
<li>Juan Camilo Castañeda cod: 20211495001</li>
<li>Leidy Johanna Rodriguez cod: 20211495011</li>
<li>Estefania Rubio cod: 20211495012</li>
</ul>

<h2>Introducción</h2>
<img src="https://images-na.ssl-images-amazon.com/images/I/71364SGPKEL.png" width="100">
<p>El objetivo en cualquier mano de 21 es derrotar al repartidor. Para lograrlo, se debe tener una mano que puntúe más que la mano del repartidor, pero que no supere los 21 en su valor total. También se puede ganar con menos de 21, siempre que el repartidor supere esta misma cantidad. Si el valor total de la mano es de 22 o más, se dice que se ha "pasado" y automáticamente se pierde. Y en caso de empate, ganará el repartidor</p>

<h2>Historias de usuario</h2>
<ol> 
  <li><b>Como</b> <i>repartidor</i> <b>quiero</b> entregar dos cartas al <i>jugador</i>, una de esas oculta para mi <b>para</b> dar inicio a la partida.</li>
<li><b>Como</b> <i>repartidor</i> <b>quiero</b> tomar dos cartas, una de ellas oculta para el <i>jugador</i> <b>para</b> dar inicio a la partida.</li>
<li><b>Como</b> <i>jugador</i> <b>quiero</b> recibir dos cartas del <i>repartidor</i>, que sean visibles solo para mi <b>para</b> que él no vea mi juego completo.</li>
<li><b>Como</b> <i>jugador</i> <b>quiero</b> solicitar una carta visible para todos <b>para</b> sumar a mi puntaje.</li>
<li><b>Como</b> <i>jugador</i> <b>quiero</b> obtener la suma de los valores de una mano <b>para</b> saber el valor total.</li>
<li><b>Como</b> <i>jugador</i> <b>quiero</b> plantar el juego <b>para</b> no exceder el valor de 21 con la sumatoria de cartas.</li>
<li><b>Como</b> <i>repartidor</i> <b>quiero</b> definir quién ganó por mayoría de puntaje <b>para</b> finalizar el juego.</li>
<li><b>Como</b> <i>repartidor</i> <b>quiero</b> definir quién ganó en caso de empate <b>para</b> finalizar el juego.</li>
</ol>

<h2>Criterios de aceptación</h2>
<ol>
<li><b><i>Al suministrar dos cartas validar el valor de la carta oculta</i></b></li>
<br>
<b>Dado</b> que el jugador desea iniciar una partida<br>
<b>Cuando</b> el jugador y el repartidor obtengan dos cartas  cada uno<br>
<b>Entonces</b> una de las cartas del repartidor debe ser visible para el jugador<br>
<br>

<b>Given</b> the player wish to start a game<br>
<b>When</b> the player  and the dealer get 2 cards for each one<br>
<b>Then</b> one of the cards of the dealer it is visible<br>


<li><b><i>Definir quién gana el juego</i></b></li>
<br>
<b>Dado</b> que la suma de las cartas del jugador es menor a 21 <br>
<b>Cuando</b> lo considere el jugador, solicite una carta adicional al repartidor <br>
<b>Entonces</b> si se pasa, el jugador pierde la partida<br>
<br>

<b>Given</b> the sum of the players cards is less or more 22<br>
<b>When</b> the player requested the last card <br>
<b>Then</b> if it is passed, the player lose the game<br>

</ol>

<h2>Pruebas unitarias</h2>

<h2>Pruebas de aceptación</h2>
<p>Para Verificar cada uno de los criterios de aceptacion mencionados anteriormente, se ejecuta <i>behave</i> donde indica el resultado de cada una de estas pruebas:</p>
<p><b>Feature:</b> BlackJack # decktoplayer.feature:1<p>

<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD> Scenario Outline: Supply two cards and validate the value of the hidden card -- @1.1 values</TD> <TD># decktoplayer.feature:10</TD>
	</TR>
	<TR>
		<TD>Given the player wants to begin a game, the dealer and the player will take 2,2 cards</TD> <TD># steps/decktoplayer.py:5</TD>
	</TR>
  <TR>
		<TD>When the dealer gets two cards</TD> <TD>steps/decktoplayer.py:12</TD>
	</TR>
  <TR>
		<TD>Then a of these deck should visible to the player </TD> <TD># steps/decktoplayer.py:22</TD>
	</TR>
</TABLE>

<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD>Scenario Outline: Supply two cards and validate the value of the hidden card -- @1.2 values</TD> <TD># decktoplayer.feature:11</TD>
	</TR>
	<TR>
		<TD>Given the player wants to begin a game, the dealer and the player will take 0,2 cards</TD> <TD># steps/decktoplayer.py:5</TD>
	</TR>
  <TR>
		<TD>When the dealer gets two cards</TD> <TD># steps/decktoplayer.py:12</TD>
	</TR>
  <TR>
		<TD>Then a of these deck should visible to the player</TD> <TD># steps/decktoplayer.py:22</TD>
	</TR>
</TABLE>
  
<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD>Scenario Outline: Supply two cards and validate the value of the hidden card -- @1.3 values</TD> <TD># decktoplayer.feature:12</TD>
	</TR>
	<TR>
		<TD>Given the player wants to begin a game, the dealer and the player will take 1,2 cards</TD> <TD># steps/decktoplayer.py:5</TD>
	</TR>
  <TR>
		<TD>When the dealer gets two cards</TD> <TD># steps/decktoplayer.py:12</TD>
	</TR>
  <TR>
		<TD>Then a of these deck should visible to the player</TD> <TD># steps/decktoplayer.py:22</TD>
	</TR>
</TABLE>
    
<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD>Scenario Outline: Supply two cards and validate the value of the hidden card -- @1.4 values</TD> <TD># decktoplayer.feature:13</TD>
	</TR>
	<TR>
		<TD>Given the player wants to begin a game, the dealer and the player will take 2,1 cards</TD> <TD># steps/decktoplayer.py:5</TD>
	</TR>
  <TR>
		<TD>When the dealer gets two cards</TD> <TD># steps/decktoplayer.py:12</TD>
	</TR>
  <TR>
		<TD>Then a of these deck should Not visible to the player</TD> <TD># steps/decktoplayer.py:22</TD>
	</TR>
</TABLE>
  
<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD>Scenario Outline: Supply two cards and validate the value of the hidden card -- @1.5 values</TD> <TD># decktoplayer.feature:14</TD>
	</TR>
	<TR>
		<TD>Given the player wants to begin a game, the dealer and the player will take 1,0 cards</TD> <TD># steps/decktoplayer.py:5</TD>
	</TR>
  <TR>
		<TD>When the dealer gets two cards</TD> <TD># steps/decktoplayer.py:12</TD>
	</TR>
  <TR>
		<TD>Then a of these deck should Not visible to the player</TD> <TD># steps/decktoplayer.py:22</TD>
	</TR>
</TABLE>
    
<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD></TD> <TD></TD>
	</TR>
	<TR>
		<TD></TD> <TD></TD>
	</TR>
  <TR>
		<TD></TD> <TD></TD>
	</TR>
  <TR>
		<TD></TD> <TD></TD>
	</TR>
</TABLE>
    
<TABLE FRAME="hsides" RULES="none">
	<TR>
		<TD>Scenario Outline: Supply two cards and validate the value of the hidden card -- @1.6 values</TD> <TD># decktoplayer.feature:15</TD>
	</TR>
	<TR>
		<TD>Given the player wants to begin a game, the dealer and the player will take 0,0 cards</TD> <TD># steps/decktoplayer.py:5</TD>
	</TR>
  <TR>
		<TD>When the dealer gets two cards</TD> <TD># steps/decktoplayer.py:12</TD>
	</TR>
  <TR>
		<TD>Then a of these deck should Not visible to the player</TD> <TD># steps/decktoplayer.py:22</TD>
	</TR>
</TABLE>
<p> 
                         

Feature: BlackJack # giveCard.feature:1

  Scenario Outline: As a dealer I want to define who won the game -- @1.1 values  # giveCard.feature:9
    Given the sum of the players cards is less or more 22                         # steps/giveCard.py:5
    When the player requested the last card                                       # steps/giveCard.py:13
    Then the player lose                                                          # steps/giveCard.py:24

  Scenario Outline: As a dealer I want to define who won the game -- @1.2 values  # giveCard.feature:10
    Given the sum of the players cards is less or more 23                         # steps/giveCard.py:5
    When the player requested the last card                                       # steps/giveCard.py:13
    Then the player lose                                                          # steps/giveCard.py:24

  Scenario Outline: As a dealer I want to define who won the game -- @1.3 values  # giveCard.feature:11
    Given the sum of the players cards is less or more 19                         # steps/giveCard.py:5
    When the player requested the last card                                       # steps/giveCard.py:13
    Then the player next step                                                     # steps/giveCard.py:24

  Scenario Outline: As a dealer I want to define who won the game -- @1.4 values  # giveCard.feature:12
    Given the sum of the players cards is less or more 21                         # steps/giveCard.py:5
    When the player requested the last card                                       # steps/giveCard.py:13
    Then the player win                                                           # steps/giveCard.py:24

2 features passed, 0 failed, 0 skipped
10 scenarios passed, 0 failed, 0 skipped
30 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.012s
PS D:\BlackJack\Blackjack_ud\features> 
</p>


<h2>Actividades Planeadas</h2>
<ol> 
 <li>Generación de inventario de cartas mediante un arreglo con la cantidad de cartas participantes con sus diferentes pintas.</li>
 <li>Crear arreglo para el participante</li>
<li>Seleccionar dos (2) elementos aleatorios del arreglo inventario.</li>
<li>Agregar al arreglo los dos (2) elementos aleatorios del  participante y eliminarlo del arreglo inventario.</li>
<li>Seleccionar un (1) elemento aleatorio del arreglo inventario, agregarlo al arreglo del participante y eliminarlo del arreglo inventario</li>
<li>Agregar al arreglo un (1) elemento aleatorio del  particpante y eliminarlo del arreglo inventario.</li>
<li>Sumar los valores de los elementos del arreglo</li>
<li>Verificar que la puntuación del participante sea menor  o igual que 21</li>
<li>Imprimir la puntuación actual del participante del modo “You have A,B,C for a total of XXX”</li>
<li>Verificar que la puntuación del participante cumpla con las condiciones del juego</li>
<li>Comparar la sumatoria de los arreglos de los participantes</li>
<li>Imprimir quien es el ganador de la partida </li>
</ol> 

