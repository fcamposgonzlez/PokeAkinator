import tkinter as tk
import sys
import os
from random import randint

global ListaPoke
global Selec
global PreguntaAct
PreguntaAct = 0
ListaPoke = []

def LeerArchivo ():
    global ListaPoke
    with open('pokedex.txt') as f:
        for line in f:
            listaAux = []
            for u in (line.split(',')):
                listaAux.append(u.rstrip())
            ListaPoke.append(listaAux)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        global ListaPoke
        global Selec
        global PreguntaAct
        self.Pregunta = tk.StringVar()
        self.Pregunta.set("¿Posee MegaEvolución?")
        self.grid()
        self.create_widgets()
        PreguntaAct = 0
    def create_widgets(self):
        global Selec
        #Genio del Akinator
        avatar = tk.PhotoImage(file="src/PokeTrainer.gif")
        Avatar = tk.Label(self,image = avatar)
        Avatar.image = avatar
        Avatar.grid(row=0, column=4,rowspan = 3,columnspan = 2)
        #
        L_Pregunta = tk.Label(self,textvariable = self.Pregunta).grid(row=0, column=2)
        B_Si= tk.Button(self,text = 'Si',command=self.F_Si).grid(row=1,column = 1)
        B_No=tk.Button(self,text = 'No',command=self.F_No).grid(row=1,column = 2)
        B_NoSe=tk.Button(self,text = 'No sé',command=self.F_NoSe).grid(row=1,column = 3)
        B_Reset=tk.Button(self,text = 'Resetear',command=self.resete).grid(row=2,column = 3)
    def resete(self):
        self.master.destroy()
    def F_Si(self):
        global Selec
        Selec = 0
        self.Akinator()
    def F_No(self):
        global Selec
        Selec = 1
        self.Akinator()
    def F_NoSe(self):
        global Selec
        Selec = 2
        self.Akinator()
    def Akinator(self):
        try:
            global PreguntaAct
            global ListaPoke
            global Selec
            ListaAux = []
            #MegaEvolucion
            if (PreguntaAct == 0):
                if (Selec == 0):
                    for x in ListaPoke:
                        if (x[15] == 'Si'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 1
                    self.Pregunta.set("¿Evoluciona Con Piedra?")
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[15] == 'No'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 1
                    self.Pregunta.set("¿Evoluciona Con Piedra?")
                elif (Selec == 2):
                    PreguntaAct = 1
                    self.Pregunta.set("¿Evoluciona Con Piedra?")
            #Evolucion con piedra
            elif (PreguntaAct == 1):
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[14] == 'Si'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 2
                    self.Pregunta.set("¿Evoluciona Con Nivel?")
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[14] == 'No'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 2
                    self.Pregunta.set("¿Evoluciona Con Nivel?")
                elif (Selec == 2):
                    PreguntaAct = 2
                    self.Pregunta.set("¿Evoluciona Con Nivel?")
            #Evolucion con nivel
            elif (PreguntaAct == 2):
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[13] != 'N/A'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 3
                    self.Pregunta.set("¿Posee Tipo Secundario?")
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[13] == 'N/A'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 3
                    self.Pregunta.set("¿Posee Tipo Secundario?")
                elif (Selec == 2):
                    PreguntaAct = 3
                    self.Pregunta.set("¿Posee Tipo Secundario?")
            #Posee Tipo secundario
            elif (PreguntaAct == 3):
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[4] != 'N/A'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 4
                    self.Pregunta.set("¿Es de color (Oficial) "+ListaPoke[0][12]+'?')
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[4] == 'N/A'):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 4
                    self.Pregunta.set("¿Es de color (Oficial) "+ListaPoke[0][12]+'?')
                elif (Selec == 2):
                    PreguntaAct = 4
                    self.Pregunta.set("¿Es de color (Oficial) "+ListaPoke[0][12]+'?')
            #COLORES
            elif (PreguntaAct == 4):
                ele = ListaPoke[0][12]
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[12] == ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 5
                    self.Pregunta.set("¿Vive en el "+ListaPoke[0][11]+'?')
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[12] != ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 4
                    self.Pregunta.set("¿Es de color (Oficial) "+ListaPoke[0][12]+'?')
                elif (Selec == 2):
                    PreguntaAct = 5
                    self.Pregunta.set("¿Vive en el "+ListaPoke[0][11]+'?')
            #Locacion
            elif (PreguntaAct == 5):
                ele = ListaPoke[0][11]
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (len(ListaPoke)== 2):
                    PreguntaAct = 100
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[11] == ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 6
                    self.Pregunta.set("¿El tipo principal es "+ListaPoke[0][3])
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[11] != ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 5
                    self.Pregunta.set("¿Vive en el "+ListaPoke[0][11]+'?')
                elif (Selec == 2):
                    PreguntaAct = 6
                    self.Pregunta.set("¿El tipo principal es "+ListaPoke[0][3])
            #Tipo
            elif (PreguntaAct == 6):
                ele = ListaPoke[0][3]
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[3] == ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 7
                    self.Pregunta.set("¿Es conocido como el Pokemon "+ListaPoke[0][2]+'?')
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[3] != ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 6
                    self.Pregunta.set("¿El tipo principal es "+ListaPoke[0][3]+'?')
                elif (Selec == 2):
                    PreguntaAct = 7
                    self.Pregunta.set("¿Es conocido como el Pokemon "+ListaPoke[0][2]+'?')
            #Conocido como
            elif (PreguntaAct == 7):
                ele = ListaPoke[0][2]
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[2] == ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 8
                    self.Pregunta.set("¿Es de crecimiento "+ListaPoke[0][16]+'?')
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[2] != ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 7
                    self.Pregunta.set("¿Es conocido como el Pokemon "+ListaPoke[0][2]+'?')
                elif (Selec == 2):
                    PreguntaAct = 8
                    self.Pregunta.set("¿Es de crecimiento "+ListaPoke[0][16]+'?')
            #Crecimiento
            elif (PreguntaAct == 8):
                ele = ListaPoke[0][16]
                if (len(ListaPoke)== 1):
                    self.ChoosenOne()
                elif (Selec == 0):
                    for x in ListaPoke:
                        if (x[16] == ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 100
                    self.Pregunta.set("¿Es una evolucion?")
                elif (Selec == 1):
                    for x in ListaPoke:
                        if (x[16] != ele):
                            ListaAux.append(x)
                    ListaPoke = ListaAux
                    PreguntaAct = 8
                    self.Pregunta.set("¿Es conocido como el Pokemon "+ListaPoke[0][16]+'?')
                elif (Selec == 2):
                    PreguntaAct = 100
                    self.Pregunta.set("¿Es una evolucion?")
            elif (PreguntaAct == 100):
                if (Selec == 0):
                    ListaAux.append(ListaPoke[1])
                    ListaPoke = ListaAux
                    self.ChoosenOne()
                elif (Selec == 1):
                    ListaAux.append(ListaPoke[0])
                    ListaPoke = ListaAux
                    self.ChoosenOne()
                elif (Selec == 2):
                    ListaAux.append(ListaPoke[randint(0,1)])
                    ListaPoke = ListaAux
                    self.ChoosenOne()
        except:
            self.Pregunta.set("No sé de que me habla u.u")
        print(ListaPoke)
    def ChoosenOne(self):
        Pokedex = tk.Toplevel(root)
        tk.Label(Pokedex, text="Nombre:").grid(row = 0,column = 1)
        tk.Label(Pokedex, text="Numero:").grid(row = 1,column = 1)
        tk.Label(Pokedex, text="El Pokemon:").grid(row = 2,column = 1)
        tk.Label(Pokedex, text="Tipo1:").grid(row = 3,column = 1)
        tk.Label(Pokedex, text="Tipo2:").grid(row = 4,column = 1)
        tk.Label(Pokedex, text="Habilidad:").grid(row = 5,column = 1)
        tk.Label(Pokedex, text="Habilidad Oculta:").grid(row = 6,column = 1)
        tk.Label(Pokedex, text="Peso(Kg):").grid(row = 7,column = 1)
        tk.Label(Pokedex, text="Altura(m):").grid(row = 8,column = 1)
        tk.Label(Pokedex, text="Macho:").grid(row = 9,column = 1)
        tk.Label(Pokedex, text="Hembra:").grid(row = 10,column = 1)
        tk.Label(Pokedex, text="Locacion:").grid(row = 1,column = 3)
        tk.Label(Pokedex, text="Color:").grid(row = 2,column = 3)
        tk.Label(Pokedex, text="Nivel de Evolucion:").grid(row = 3,column = 3)
        tk.Label(Pokedex, text="Roca Evolutiva:").grid(row = 4,column = 3)
        tk.Label(Pokedex, text="Mega Evolucion:").grid(row = 5,column = 3)
        tk.Label(Pokedex, text="Tipo de Crecimiento:").grid(row = 6,column = 3)
        tk.Label(Pokedex, text="Ratio de captura:").grid(row = 7,column = 3)
        tk.Label(Pokedex, text="Ciclos de Eclosion:").grid(row = 8,column = 3)
        tk.Label(Pokedex, text="PS:").grid(row = 9,column = 3)
        tk.Label(Pokedex, text="Ataque:").grid(row = 10,column = 3)
        tk.Label(Pokedex, text="Defensa:").grid(row = 1,column = 5)
        tk.Label(Pokedex, text="Ataque Especial:").grid(row = 2,column = 5)
        tk.Label(Pokedex, text="Defensa Especial:").grid(row = 3,column = 5)
        tk.Label(Pokedex, text="Velocidad:").grid(row = 4,column = 5)

        tk.Label(Pokedex, text=ListaPoke[0][0]).grid(row = 0,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][1]).grid(row = 1,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][2]).grid(row = 2,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][3]).grid(row = 3,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][4]).grid(row = 4,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][5]).grid(row = 5,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][6]).grid(row = 6,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][7]).grid(row = 7,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][8]).grid(row = 8,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][9]).grid(row = 9,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][10]).grid(row = 10,column = 2)
        tk.Label(Pokedex, text=ListaPoke[0][11]).grid(row = 1,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][12]).grid(row = 2,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][13]).grid(row = 3,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][14]).grid(row = 4,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][15]).grid(row = 5,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][16]).grid(row = 6,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][17]).grid(row = 7,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][18]).grid(row = 8,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][19]).grid(row = 9,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][20]).grid(row = 10,column = 4)
        tk.Label(Pokedex, text=ListaPoke[0][21]).grid(row = 1,column = 6)
        tk.Label(Pokedex, text=ListaPoke[0][22]).grid(row = 2,column = 6)
        tk.Label(Pokedex, text=ListaPoke[0][23]).grid(row = 3,column = 6)
        tk.Label(Pokedex, text=ListaPoke[0][24]).grid(row = 4,column = 6)
        poki = tk.PhotoImage(file="src/"+ListaPoke[0][0]+".gif")
        Poki= tk.Label(Pokedex,image = poki)
        Poki.image = poki
        Poki.grid(row=0, column=7,rowspan = 10)
        

LeerArchivo()
root = tk.Tk()
app = Application(master=root)
app.mainloop()



