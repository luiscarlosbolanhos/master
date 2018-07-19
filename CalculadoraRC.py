# -*- coding: utf-8 -*-
from Tkinter import*
import math
import random

def dec2any(numero,base):
        converstr = "0123456789abcdefghijklmnopqrstuvwxyz"
        if numero<base:
            return converstr[numero]
        else:
            return dec2any(numero//base,base) + converstr[numero%base]
            
class Marcado():
    def __init__(self, calc):
        
        calc.title("Triple-C ( Chicken Colorful Calculator ) v1")
        self. a = "0" 
        self.suma = Calcula()
        
        caja_texto = Texto(calc, self.a)
    
        self.boton1 = Boton(calc, "1", 3, 2, lambda : self.Numero(1))
        self.boton2 = Boton(calc, "2", 3, 3, lambda : self.Numero(2))
        self.boton3 = Boton(calc, "3", 3, 4, lambda : self.Numero(3))
        self.boton4 = Boton(calc, "4", 4, 2, lambda : self.Numero(4))
        self.boton5 = Boton(calc, "5", 4, 3, lambda : self.Numero(5))
        self.boton6 = Boton(calc, "6", 4, 4, lambda : self.Numero(6))
        self.boton7 = Boton(calc, "7", 5, 2, lambda : self.Numero(7))
        self.boton8 = Boton(calc, "8", 5, 3, lambda : self.Numero(8))
        self.boton8 = Boton(calc, "9", 5, 4, lambda : self.Numero(9))
        self.boton8 = Boton(calc, "0", 5, 5, lambda : self.Numero(0))

        self.boton_suma = Boton(calc, "+", 3, 5, self.Suma )
        self.boton_resta = Boton(calc, "-", 4, 5, self.Resta)
        self.boton_resta = Boton(calc, "*", 3, 6, self.Multiplica)
        self.boton_resta = Boton(calc, "/", 4, 6, self.Divide)
        self.boton_igual = Boton(calc, "=", 5, 6, self.Igual)
        
        self.boton_calc_panel = Boton(calc, "Sqr()", 2, 5, self.Raiz_Quadrada)
        self.boton_calc_panel = Boton(calc, "CA", 2, 6, self.C)
        self.boton_calc_panel = Boton(calc, "OCT", 3, 1, self.Octal)
        self.boton_calc_panel = Boton(calc, "HEX", 4, 1, self.Hex)
        self.boton_calc_panel = Boton(calc, "DEC", 5, 1, self.Decimal)
        self.boton_calc_panel = Boton(calc, "BIN", 2, 1, self.Bin)
        self.boton_calc_panel = Boton(calc, "x²", 2, 2, self.Pow)
        self.boton_calc_panel = Boton(calc, "log10()", 2, 3, self.Log10)
        self.boton_calc_panel = Boton(calc, "%", 2, 4, self.Percent)
        

    def C(self):
        m = Marcado(calc)
        
    def Raiz_Quadrada(self):
        temporal = math.sqrt(float(self.a))
        self.a = str(temporal)
        caja_texto = Texto(calc, self.a)

    def Octal(self):
        temporal = dec2any(int(float(self.a)),8)
        calc.title("Conversion (OCT): "+temporal)
        
    def Hex(self):
        temporal = dec2any(int(float(self.a)),16)
        calc.title("Conversion (HEX): "+temporal)

    def Decimal(self):
        temporal = dec2any(int(float(self.a)),10)
        calc.title("Conversion (DEC): "+temporal)

    def Log10(self):
        temporal = math.log10(int(self.a))
        self.a = temporal
        caja_texto = Texto(calc, self.a)

    def Bin(self):
        temporal = dec2any(int(float(self.a)),2)
        calc.title("Conversion (BIN): "+temporal)
        
    def Pow(self):
        self.a = math.pow(float(self.a), 2)
        caja_texto = Texto(calc, self.a)

    def Percent(self):
        self.a = (float(self.a)/100)
        caja_texto = Texto(calc, self.a)

    def Igual(self):
        self.suma._numero_B = self.a
        if (self.suma._sinal == "suma"):
            v = self.suma.suma()
        elif (self.suma._sinal == "resta"):
            v = self.suma.resta()
        elif (self.suma._sinal == "multiplica"):
            v = self.suma.multiplica()
        elif (self.suma._sinal == "divide"):
            v = self.suma.divide()
        caja_texto = Texto(calc, v)
        self.a = str(int(v))

    def Suma(self):
        self.suma._numero_A = self.a
        self.suma._sinal = "suma"
        self.a = "0"
        
    def Multiplica(self):
        self.suma._numero_A = self.a
        self.suma._sinal = "multiplica"
        self.a = "0"

    def Divide(self):
        self.suma._numero_A = self.a
        self.suma._sinal = "divide"
        self.a = "0"

    def Resta(self):
        self.suma._numero_A = self.a
        self.suma._sinal = "resta"
        self.a = "0"

    def Numero(self, numero):
        self.a += str(int(numero))
        caja_texto = Texto(calc, self.a)

class Boton():
    def __init__(self, frame, text_boton, linea, coluna, comando):
        color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
        #self.button = Button(frame, text = text_boton, fg="black", bg="grey", command = comando, font = ("Arial", "20", "bold"))
        self.button = Button(frame, text = text_boton, fg="black", bg=color, command = comando, font = ("Arial", "20", "bold"))
        self.button["width"] = 5
        self.button["height"] = 1
        self.button.grid(row = linea, column = coluna)

class Calcula():
    def __init__(self):
        self._numero_A = None
        self._numero_B = None
        #self._sinal = None

    def suma(self):
        return float(self._numero_A) + float(self._numero_B)

    def resta(self):
        return float(self._numero_A) - float(self._numero_B)

    def multiplica(self):
        return float(self._numero_A) * float(self._numero_B)
    
    def divide(self):
        return float(self._numero_A) / float(self._numero_B)

class Texto():
    def __init__(self, calc, texto):
        self.texto = Label(calc, text =round (float(texto), 2), font = ("Arial", "40", "bold"))
        self.texto["height"] = 2 
        self.texto["width"] = 2
        self.texto.grid(row=1, column=1, columnspan=6,sticky=W+E+N+S)

        

calc = Tk()

# calc.geometry("570x354")
# Centrado de la Pantalla

# Tamanho de la pantalla
w = 570
h = 354

# Calculo del centro de la pantalla en base al tamanho de la ventana

ws = calc.winfo_screenwidth()
hs = calc.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

calc.geometry('%dx%d+%d+%d' % (w, h, x, y))
# calc.title("Calculadora: Chicken++ v1")
calc.resizable(width=False, height=False)

m = Marcado(calc)
calc.mainloop()
