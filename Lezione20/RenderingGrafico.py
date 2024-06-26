#  EDOARDO DI LISIO
#  12.06.24

'''
2. RENDERING GRAFICO
Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della 
forma e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() 
per disegnare su schermo la forma.

Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. Il quadrato 
da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome 
della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del trinagolo 
(per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stamapre su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati 
nel costruttore. Il traingolo da stampare deve essere un traingolo vuoto (" "), avente degli asterischi ("*") 
lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina 
ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa 
riga, separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
'''

from abc import ABC, abstractmethod  # Importa la classe ABC e il decoratore abstractmethod dal modulo abc
# Definizione della classe astratta Forma che eredita dalla classe ABC
class Forma(ABC):
    # Costruttore della classe con un parametro 'nome'
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod  # Metodo astratto che deve essere implementato nelle classi figlie
    def getArea(self):
        pass

    @abstractmethod  # Metodo astratto che deve essere implementato nelle classi figlie
    def render(self):
        pass

# Definizione della classe figlia Quadrato che eredita dalla classe Forma
class Quadrato(Forma):
    # Costruttore della classe con un parametro 'lato'
    def __init__(self, lato):
        super().__init__("Quadrato")  # Chiama il costruttore della classe madre
        self.lato = lato

    # Implementazione del metodo per calcolare l'area del quadrato
    def getArea(self):
        return self.lato * self.lato

    # Implementazione del metodo per renderizzare il quadrato
    def render(self):
        print(f"Ecco un {self.nome} di lato {self.lato}!")
        for i in range(self.lato):
            if i == 0 or i == self.lato - 1:
                print("* " * self.lato)
            else:
                print("* " + "  " * (self.lato - 2) + "*")
        print(f"L'area di questo {self.nome} vale: {self.getArea()}\n")

# Definizione della classe figlia Rettangolo che eredita dalla classe Forma
class Rettangolo(Forma):
    # Costruttore della classe con due parametri 'base' e 'altezza'
    def __init__(self, base, altezza):
        super().__init__("Rettangolo")  # Chiama il costruttore della classe madre
        self.base = base
        self.altezza = altezza

    # Implementazione del metodo per calcolare l'area del rettangolo
    def getArea(self):
        return self.base * self.altezza

    # Implementazione del metodo per renderizzare il rettangolo
    def render(self):
        print(f"Ecco un {self.nome} avente base {self.base} ed altezza {self.altezza}!")
        print("* " * self.base)
        for i in range(self.altezza - 2):
            print("*" + " " * (self.base * 2 - 3) + "*")
        print("* " * self.base)
        print(f"L'area di questo {self.nome} vale: {self.getArea()}\n")

# Definizione della classe figlia Triangolo che eredita dalla classe Forma
class Triangolo(Forma):
    # Costruttore della classe con un parametro 'lato'
    def __init__(self, lato):
        super().__init__("Triangolo")  # Chiama il costruttore della classe madre
        self.lato = lato

    # Implementazione del metodo per calcolare l'area del triangolo
    def getArea(self):
        return (self.lato * self.lato) / 2

    # Implementazione del metodo per renderizzare il triangolo
    def render(self):
        print(f"Ecco un {self.nome} avente base {self.lato} ed altezza {self.lato}!")
        for i in range(self.lato):
            if i == 0:
                print("* ")
            elif i == self.lato - 1:
                print("* " * self.lato)
            else:
                print("* " + "  " * (i - 1) + "* ")
        print(f"L'area di questo {self.nome} vale: {self.getArea()}\n")

# Test delle classi
quadrato = Quadrato(4)  # Crea un'istanza di Quadrato con lato 4
quadrato.render()  # Chiama il metodo render di Quadrato

rettangolo = Rettangolo(8, 4)  # Crea un'istanza di Rettangolo con base 8 e altezza 4
rettangolo.render()  # Chiama il metodo render di Rettangolo

triangolo = Triangolo(4)  # Crea un'istanza di Triangolo con lato 4
triangolo.render()  # Chiama il metodo render di Triangolo
