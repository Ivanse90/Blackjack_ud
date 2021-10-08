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
<ol>
<li><b>Prueba de clase <i>Card()</i></b></li>
<br>
<p>La clase Card recibe como input dos parámetros string los cuales son una un valor de carta y un palo al recibir estos dos parámetros de entrada el output es un string que resulta ser la concatenación de ambos parámetros conectados con "de".</p>
<p>Al realizar las pruebas unitarias con pytest se encuentra lo siguiente:</p>

test_blakjack.py::test_card[Dos-Corazones-Dos de Corazones] PASSED [ 25%]<br>
test_blakjack.py::test_card[Tres-Diamantes-Tres de Diamantes] PASSED [ 50%]<br>
test_blakjack.py::test_card[Queen-Picas-Queen de Picas] PASSED [ 75%]<br>
test_blakjack.py::test_card[As-Treboles-As de Treboles] PASSED [100%]<br>
<br>
================================== <b>4 passed in 0.05s</b> ==================================
<li><b>Prueba de clase <i>Deck()</i></b></li>
<br>
<p>La clase Deck se encarga de mezclar la baraja que contiene todas las cartas y una vez solicite una carta esta se elimine de la baraja, con el fin de determinar si esta esta creando la baraja correctamente se comprueba si la posición de la carta de la baraja creada con la clase deck en el index n es igual  a la posición index n en la baraja creada manualmente, obteniendo los siguientes resultados:</p>

test_blakjack.py::test_deck[2-2] PASSED [ 25%]<br>
test_blakjack.py::test_deck[7-7] PASSED [ 50%]<br>
test_blakjack.py::test_deck[8-8] PASSED [ 75%]<br>
test_blakjack.py::test_deck[12-12] PASSED [100%]<br>
<br>
================================== <b>4 passed in 0.16s</b> ==================================
<li><b>Prueba de clase <i>Deck()</i> función shuffle</b></li>
<br>
<p>La función shuffle se encarga de mezclar la baraja cambiando la posición inicial de cada carta perteneciente a la baraja, para esto se creo la baraja y se mezclo para luego comparar la posición inicial con la posición después de mezclar con lo cual tanto la posición inicial como la posición después de mezclar debe ser diferente:</p>

test_blakjack.py::test_deck_sh[0-0] PASSED [ 25%]<br>
test_blakjack.py::test_deck_sh[15-15] PASSED [ 50%]<br>
test_blakjack.py::test_deck_sh[32-32] PASSED [ 75%]<br>
test_blakjack.py::test_deck_sh[51-51] PASSED [100%]<br>
<br>
================================== <b>4 passed in 0.05s</b> ==================================
<li><b>Prueba de clase <i>Deck()</i> función deal</b></li>
<br>
<p>La función deal se encarga eliminar  las cartas de la baraja que se asignan al jugador, para esta prueba se comprobara que luego de hacer n llamados a la función la baraja tendrá 52 elementos menos los n llamados de la función:</p>

test_blakjack.py::test_deck_dl[0-52] PASSED [ 16%]<br>
test_blakjack.py::test_deck_dl[1-51] PASSED [ 33%]<br>
test_blakjack.py::test_deck_dl[52-0] PASSED [ 50%]<br>
test_blakjack.py::test_deck_dl[51-1] PASSED [ 66%]<br>
test_blakjack.py::test_deck_dl[11-41] PASSED [ 83%]<br>
test_blakjack.py::test_deck_dl[37-15] PASSED [100%]<br>
<br>
================================== <b>6 passed in 0.07s</b> ==================================
<li><b>Prueba de clase <i>Hand()</i> función add_card</b></li>
<br>
<p>La función add_card se encarga de agregar a la mano del jugador una carta seleccionada, con esto si se asignan tres cartas se espera que la longitud del arreglo que hacer referencia a la mano del jugador será igual a tres:</p>

test_blakjack.py::test_hand_add[0-0] PASSED [ 25%]<br>
test_blakjack.py::test_hand_add[1-1] PASSED [ 50%]<br>
test_blakjack.py::test_hand_add[2-2] PASSED [ 75%]<br>
test_blakjack.py::test_hand_add[3-3] PASSED [100%]<br>
<br>
================================== <b>4 passed in 0.05s</b> ==================================
<li><b>Prueba de clase <i>Hand()</i> función adjust_for_ace</b></li>
<br>
<p>La función adjust_for_ace hace un ajuste en la puntuación de As, la cual cuando se escoge un As el primero puntuara por 11 puntos los As adicional que salgan para la baraja del jugador tendrán una puntuación de 1 punto:</p>

test_blakjack.py::test_hand_adj[1-11] PASSED [ 16%]<br>
test_blakjack.py::test_hand_adj[2-12] PASSED [ 33%]<br>
test_blakjack.py::test_hand_adj[3-13] PASSED [ 50%]<br>
test_blakjack.py::test_hand_adj[4-14] PASSED [ 66%]<br>
test_blakjack.py::test_hand_adj[5-15] PASSED [ 83%]<br>
test_blakjack.py::test_hand_adj[0-0] PASSED [100%]<br>
<br>
================================== <b>6 passed in 0.06s</b> ==================================
<li><b>Prueba para la función <i>show_some()</i></b></li>
<br>
<p>Teniendo en cuenta que esta función imprime textos, se comprueba retornando el string  "Jugando!", se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_show_some PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.05s</b> ==================================
<li><b>Prueba para la función <i>show_all()</i></b></li>
<br>
<p>Teniendo en cuenta que esta función imprime textos, se comprueba retornando el string  "****", se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_show_some PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.02s</b> ==================================
<li><b>Prueba para la función <i>player_busts()</i></b></li>
<br>
<p>La función payer_busts se encarga de retornar el string “Lo siento. Te pasaste. Perdiste”, se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_player_busts PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.04s</b> ==================================	
<li><b>Prueba para la función <i>player_wins()</i></b></li>
<br>
<p>La función payer_wins se encarga de retornar el string “Felicitaciones. Ganaste”, se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_player_wins PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.04s</b> ==================================
<li><b>Prueba para la función <i>dealer_busts()</i></b></li>
<br>
<p>La función dealer_busts se encarga de retornar el string “El repartidor se paso. Tu ganas!”, se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_dealer_busts PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.03s</b> ==================================
<li><b>Prueba para la función <i>dealer_wins()</i></b></li>
<br>
<p>La función dealer_wins se encarga de retornar el string “Lo siento, ¡perdiste el repartido gano!”, se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_dealer_wins PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.04s</b> ==================================
<li><b>Prueba para la función <i>push()</i></b></li>
<br>
<p>La función push se encarga de retornar el string “Lo siento, empataron. El repartdos gano!”, se comprueba evidenciando el mismo texto:</p>

test_blakjack.py::test_push PASSED [100%]<br>
<br>
================================== <b>1 passed in 0.04s</b> ==================================
<li><b>Pruebas unitarias completas</b></li>
<br>collected 35 items<br>
<br>
test_blakjack.py::test_card[Dos-Corazones-Dos de Corazones] PASSED [  2%]<br>
test_blakjack.py::test_card[Tres-Diamantes-Tres de Diamantes] PASSED [  5%]<br>
test_blakjack.py::test_card[Queen-Picas-Queen de Picas] PASSED [  8%]<br>
test_blakjack.py::test_card[As-Treboles-As de Treboles] PASSED [ 11%]<br>
test_blakjack.py::test_deck[2-2] PASSED [ 14%]<br>
test_blakjack.py::test_deck[7-7] PASSED [ 17%] <br>
test_blakjack.py::test_deck[8-8] PASSED [ 20%] <br>
test_blakjack.py::test_deck[12-12] PASSED [ 22%] <br>
test_blakjack.py::test_deck_sh[0-0] PASSED [ 25%] <br>
test_blakjack.py::test_deck_sh[15-15] PASSED [ 28%]<br>
test_blakjack.py::test_deck_sh[32-32] PASSED [ 31%] <br>
test_blakjack.py::test_deck_sh[51-51] PASSED [ 34%] <br>
test_blakjack.py::test_deck_dl[0-52] PASSED [ 37%] <br>
test_blakjack.py::test_deck_dl[1-51] PASSED [ 40%]<br>
test_blakjack.py::test_deck_dl[52-0] PASSED [ 42%] <br>
test_blakjack.py::test_deck_dl[51-1] PASSED [ 45%] <br>
test_blakjack.py::test_deck_dl[11-41] PASSED [ 48%] <br>
test_blakjack.py::test_deck_dl[37-15] PASSED [ 51%]<br>
test_blakjack.py::test_hand_add[0-0] PASSED [ 54%] <br>
test_blakjack.py::test_hand_add[1-1] PASSED [ 57%] <br>
test_blakjack.py::test_hand_add[2-2] PASSED [ 60%]<br>
test_blakjack.py::test_hand_add[3-3] PASSED [ 62%] <br>
test_blakjack.py::test_hand_adj[1-11] PASSED [ 65%] <br>
test_blakjack.py::test_hand_adj[2-12] PASSED [ 68%]<br>
test_blakjack.py::test_hand_adj[3-13] PASSED [ 71%] <br>
test_blakjack.py::test_hand_adj[4-14] PASSED [ 74%] <br>
test_blakjack.py::test_hand_adj[5-15] PASSED [ 77%] <br>
test_blakjack.py::test_hand_adj[0-0] PASSED [ 80%] <br>
test_blakjack.py::test_show_some PASSED [ 82%] <br>
test_blakjack.py::test_show_all PASSED [ 85%] <br>
test_blakjack.py::test_player_busts PASSED [ 88%] <br>
test_blakjack.py::test_player_wins PASSED [ 91%] <br>
test_blakjack.py::test_dealer_busts PASSED [ 94%] <br>
test_blakjack.py::test_dealer_wins PASSED [ 97%] <br>
test_blakjack.py::test_push PASSED [100%]<br>
<br>	
================================= <b>35 passed in 0.23s</b> ==================================
</ol>

<h2>Pruebas de aceptación</h2>
<p>Para Verificar cada uno de los criterios de aceptacion mencionados anteriormente, se ejecuta <i>behave</i> donde indica el resultado de cada una de estas pruebas:</p>

<b>Scenario Outline:</b> Supply two cards and validate the value of the hidden card<br>
<br>
<b>Given</b> the player wants to begin a game, the dealer and the player will take <values> cards<br>
<b>When</b> the dealer gets two cards<br>
<b>Then</b> a of these deck should <visible> to the player<br>
	
<b>Examples:</b> values<br>
<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>values</TD> <TD>visible</TD>
</TR>
<TR>
	<TD>2,2</TD> <TD>visible</TD>
</TR>
<TR>
	<TD>0,2 </TD> <TD>visible</TD>
</TR>
<TR>
	<TD>1,2</TD> <TD>visible</TD>
</TR>
<TR>
	<TD>2,1</TD> <TD>Not visible></TD>
</TR>
<TR>
	<TD>1,0</TD> <TD>Not visible</TD>
</TR>
<TR>
	<TD>0,0</TD> <TD>Not visible</TD>
</TR>
</TABLE>

	
<b>Feature:</b> BlackJack # decktoplayer.feature:1

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
	
<b>Scenario Outline:</b> As a dealer I want to define who won the game<br>
<br>
<b>Given</b> the sum of the players cards is less or more <value><br>
<b>When</b> the player requested the last card<br>
<b>Then</b> the player <statusplayer><br>
	
<b>Examples:</b> values<br>
<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>values</TD> <TD>statusplayer</TD>
</TR>
<TR>
	<TD>22</TD> <TD>lose</TD>
</TR>
<TR>
	<TD>23</TD> <TD>lose</TD>
</TR>
<TR>
	<TD>19</TD> <TD>next step</TD>
</TR>
<TR>
	<TD>21</TD> <TD>win</TD>
</TR>
</TABLE>

                         
<b>Feature:</b> BlackJack # giveCard.feature:1

<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>Scenario Outline: As a dealer I want to define who won the game -- @1.1 values</TD> <TD># giveCard.feature:9</TD>
</TR>
<TR>
	<TD>Given the sum of the players cards is less or more 22</TD> <TD># steps/giveCard.py:5</TD>
</TR>
<TR>
	<TD>When the player requested the last card</TD> <TD># steps/giveCard.py:13</TD>
</TR>
<TR>
	<TD>Then the player lose</TD> <TD># steps/giveCard.py:24</TD>
</TR>
</TABLE>                                      

<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>Scenario Outline: As a dealer I want to define who won the game -- @1.2 values</TD> <TD># giveCard.feature:10</TD>
</TR>
<TR>
	<TD>Given the sum of the players cards is less or more 23</TD> <TD># steps/giveCard.py:5</TD>
</TR>
<TR>
	<TD>When the player requested the last card</TD> <TD># steps/giveCard.py:13</TD>
</TR>
<TR>
	<TD>Then the player lose</TD> <TD># steps/giveCard.py:24</TD>
</TR>
</TABLE>                                      
                                                              
<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>Scenario Outline: As a dealer I want to define who won the game -- @1.3 values</TD> <TD># giveCard.feature:11</TD>
</TR>
<TR>
	<TD>Given the sum of the players cards is less or more 19</TD> <TD># steps/giveCard.py:5</TD>
</TR>
<TR>
	<TD>When the player requested the last card</TD> <TD># steps/giveCard.py:13</TD>
</TR>
<TR>
	<TD>Then the player next step</TD> <TD># steps/giveCard.py:24</TD>
</TR>
</TABLE>                                    
                                                         
<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>Scenario Outline: As a dealer I want to define who won the game -- @1.4 values</TD> <TD># giveCard.feature:12</TD>
</TR>
<TR>
	<TD>Given the sum of the players cards is less or more 21</TD> <TD># steps/giveCard.py:5</TD>
</TR>
<TR>
	<TD>When the player requested the last card</TD> <TD># steps/giveCard.py:13</TD>
</TR>
<TR>
	<TD>Then the player win</TD> <TD># steps/giveCard.py:24</TD>
</TR>
</TABLE>

<b>Results:</b>
                             
<TABLE FRAME="hsides" RULES="none">
<TR>
	<TD>2 features passed, 0 failed, 0 skipped</TD> 
</TR>
<TR>
	<TD>10 scenarios passed, 0 failed, 0 skipped</TD>
</TR>
<TR>
	<TD>30 steps passed, 0 failed, 0 skipped, 0 undefined</TD>
</TR>
<TR>
	<TD>Took 0m0.012s</TD>
</TR>
</TABLE>                                          
                                                               

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

