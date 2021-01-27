class HelloWorld:
    def __init__(self):
        print("Hello world")
        print(self.__hash__())

    def programozo_leszek(self):
        print("Programozó leszek, ha nagy leszek!")
        print(self.__hash__())


a = HelloWorld()
b = HelloWorld()
c = HelloWorld()

a.programozo_leszek()
a.programozo_leszek()

b.programozo_leszek()
b.programozo_leszek()
b.programozo_leszek()

c.programozo_leszek()