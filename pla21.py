import random

class Juego():

    def __init__(self,variable = []):
        self.variable = variable
        self.mano = []
        self.carta1 = []
        self.carta2 = []
        self.asig = []
        self.total = 0

    def cartas(self):
        
        cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        pintas = ["Picas","Diamantes","Trebol","Corazon"]
        self.baraja = []
        for i in range(0,len(cartas)):
            for j in range(0,len(pintas)):
                self.baraja.append(cartas[i]+ " " +pintas[j])
        return self.baraja

    
    def iniciar_partida(self):
        self.carta1 = random.choice(self.cartas())
        return self.carta1 
    
    def asignar_cartas(self, asignar):
        self.asig.append(asignar)
        self.baraja.remove(asignar)
        return self.asig
    
    def puntuacion(self,card):
        # self.variable = [x for x in range(1,14)]
        p1 = card[0:2]
        
        if p1 == "A " and self.total <= 11:
            self.total = 10
        elif p1 == "A " and self.total > 11:
            self.total = 1
        elif p1 == "2 ":
            self.total = 2
        elif p1 == "3 ":
            self.total = 3
        elif p1 == "4 ":
            self.total = 4
        elif p1 == "5 ":
            self.total = 5
        elif p1 == "6 ":
            self.total = 6
        elif p1 == "7 ":
            self.total = 7
        elif p1 == "8 ":
            self.total = 8
        elif p1 == "9 ":
            self.total = 9
        elif p1 == "10":
            self.total = 10
        elif p1 == "J ":
            self.total = 11
        elif p1 == "Q ":
            self.total = 11
        elif p1 == "K ":
            self.total = 11
        return self.total 
    
    def usuario(self):
        card = self.iniciar_partida()
        ca = self.asignar_cartas(card)
        return ca

    def total_mano(self, mano):
        sumacard = mano
        subt = 0
        for i in range(0,len(sumacard)):
            subt += self.puntuacion(sumacard[i])
        return subt 
    
    def game(self):
        initcard = self.iniciar_partida()
        initcard2 = self.iniciar_partida()
        asg1 = self.asignar_cartas(initcard)
        asg1 = self.asignar_cartas(initcard2)
        print("Tu mano es:", asg1, prueba.total_mano(asg1))
        choice = input("Desea [S]olicitar, [P]lantar, or [R]etirarse: ").lower()

        while choice != "r":
            
            if choice == "s":
                
                adicional = self.usuario()
                if  self.total_mano(adicional) > 51:
                    break

                print(adicional, "puntuacion:", self.total_mano(adicional))
                choice = input("Desea [S]olicitar, [P]lantar, or [R]etirarse: ").lower()  
                
        return "ok"




prueba = Juego(4)
# print(len(prueba.cartas()))
# card = prueba.iniciar_partida()
# print(card)
# print("puntuacion igual:",prueba.puntuacion(card))
# card2 = prueba.iniciar_partida()
# print(card2)
# print(card,card2)
# print("puntuacion igual:",prueba.puntuacion(card2))

# print(prueba.cartas())
# print(len(prueba.cartas()))
# mano_usr  = prueba.usuario()

# print(mano_usr, "puntuacion:", prueba.total_mano(mano_usr))
print(prueba.game())
