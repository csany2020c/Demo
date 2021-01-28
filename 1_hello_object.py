#A HelloWorld egy objektum osztály, amely egybezárja az egy feladathoz tartozó mezőket (a mezőkben adatokat tárolunk)
# és a metódusaokat (a metódusok pedig az adatokon végeznek műveletet).
#Az alábbi osztály annyira egyszerű, hogy nem is tartalmaz tárolt értékeket, mezőket, hanem csak 2 db metódust,
# műveletet, amit a def kulcsszóval kell kezdeni.
#Az osztályban megírt programkód a futtatás során nem fut le automatikusan.
class HelloWorld:
    #Az __init__ metódus az osztály konstruktora. Ez akkor fut le, amikor egy példányt létrehozunk belőle.
    #Minden példány létrehozásakor lefut.
    def __init__(self):
        #A szövegeket idézőjelbe kell tenni. A kijratás a konzolba a print("") függvvény hívásával történik.
        print("Hello world")
        #A függvények más függvényektől is kaphatnak bemeneti értéket.
        # A self-el saját magára hivatkozik egy objektum példány.
        # A self.__hash__() metódus egy számot ad eredményként, amely egyedi azonosítója a példánynak.
        # A print ezt a számot írja ki.
        #Nagyon fontos a műveleti sorrend értelmezése. Előszösr a self, majd a __hash__() függvény értékelődik ki.
        #Az így kapott számot kapja meg a print függvény, amely kiértékelése során a konzolba ír.
        print(self.__hash__())

    #Egy másik metódus. Ez nem hajtódik végre automatikusan, meg kell hívni, ha akarjuk, hogy fusson.
    def programozo_leszek(self):
        print("Programozó leszek, ha nagy leszek!")
        print(self.__hash__())


#3 példány létrehozása a fent deklarált objektum osztályból. A példányora a, b és c betűvel hivatkozunk a továbbiakban.
#A hivatkozást referenciának is szoktuk nevezni.
#A műveleti sorrend szintén fontos. Az értékadás egyike a "jobbról balra" műveleteknek, azaz először a Helloworld()
# hajtódik végre, majd utána az = művelet, azaz az értéke, referenciája a változóba kerül.
#Itt megfigyelhető még a konstruktor lefutása is.
a = HelloWorld()
b = HelloWorld()
c = HelloWorld()

#Mivel a, b és c példányok a programunkban létrejöttek, így meghívhatók a benne lévő metódusok, és ha lennének
#benne mezők, akkor azoknak az adatai is módosíthatók lennének. Majd később lesznek is:)
#Itt figyeljük meg a kiírt hash értékeket is.
a.programozo_leszek()
a.programozo_leszek()

b.programozo_leszek()
b.programozo_leszek()
b.programozo_leszek()

c.programozo_leszek()

#Órai analógiával: az objektum osztály olyan, mint amikor készítünk egy nyomóformát, amivel sokszor tudjuk
#ugyanazt kinyomtatni. Az objektum példány pedig a nyomat, amit kedvünkre színezhetünk, persze csak a megadott
#vonalakon belül. Minden nyomatot máshogy színezhetünk.